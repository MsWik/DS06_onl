import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
from tqdm import tqdm
from torch.utils.data import DataLoader, TensorDataset
from Metrics import Accuracy, F1Score
from Callbacks import ModelCheckPoint, EarlyStopping, Logger
from typing import Dict

class TextClassificationNN(nn.Module):
    def __init__(self) -> None:
        super(TextClassificationNN, self).__init__()
        self.embedding = nn.Embedding(5000, 128)
        self.transformer_encoder_1 = nn.TransformerEncoder(nn.TransformerEncoderLayer(128, 8, 2048, batch_first=True), num_layers=3)
        self.output = nn.Linear(128, 4)

    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer_encoder_1(x)
        x = x.mean(dim=1)
        x = self.output(x)
        return x

    def create_template(self, metrics) -> str:
        base_description: str = "epoch: {epoch} loss: {loss:.4f}"
        for metric in metrics:
            base_description += f" {metric.name}: {{{metric.name}:.4f}}"
        return base_description

    def update_metrics(self, metrics_value, metrics, args, i) -> Dict:
        self.eval()
        y_pred = self(args[0])
        self.train()
        for j, metric in zip(metrics_value.keys(), metrics):
            metrics_value[j] += metric(y_pred, args[1])
        return {key.name:value/i for key,value in zip(metrics, metrics_value.values())}

    def validate_model(self, metrics_value, metrics, args):
        self.eval()
        y_pred = self(args[0])
        self.train()
        for j, metric in zip(metrics_value.keys(), metrics):
            metrics_value[j] += metric(y_pred, args[1])

    def calc_mean(self, metrics_value, n) -> Dict:
        return {key:value/n for key,value in zip(metrics_value,metrics_value.values())}

    def fit(self, train_data, val_data = None, epochs=10, lr=0.01) -> None:
        modelcp = ModelCheckPoint(filepath='model', initial_threshold=0.5, monitor='f1score')
        early_stopping = EarlyStopping(min_delta=0.05, patience=10, monitor='f1score')
        logger = Logger()
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(self.parameters(), lr=lr, betas=(0.9,0.98), eps=1e-6, amsgrad=True)
        metrics = [Accuracy(), F1Score(num_classes=4)]
        base_description: str = self.create_template(metrics)
        for epoch in range(1, epochs+1):
            it = tqdm(zip(train_data, range(1, len(train_data)+1)), total=len(train_data), desc=base_description)
            total_loss = 0
            train_metrics_value = {key.name:0 for key in metrics}
            valid_metrics_value = {key.name:0 for key in metrics}
            i = 0
            for args, i in it: # args[0] - inputs, args[1] - outputs
                optimizer.zero_grad()
                outputs = self(args[0])
                loss = criterion(outputs, args[1])
                loss.backward()
                optimizer.step()
                total_loss += loss.item()
                it.set_description(base_description.format(epoch=epoch, loss=total_loss/i,**self.update_metrics(train_metrics_value, metrics, args, i)))  
            for args in val_data:
                self.validate_model(valid_metrics_value, metrics, args)
            final_metrics = self.calc_mean(valid_metrics_value, len(val_data))
            print(final_metrics)
            modelcp(final_metrics, self)
            logger(self.calc_mean(train_metrics_value, len(train_data)))
            if not early_stopping(final_metrics): exit(0)
            

def main():
    train_data = pd.read_csv('training_cleared.csv')
    test_data = pd.read_csv('test_cleared.csv')
    valid_data = pd.read_csv('valid_cleared.csv')

    y_train = torch.tensor(train_data.flag).to('cuda')
    y_test = torch.tensor(test_data.flag).to('cuda')
    # x_train_classes = torch.tensor(train_data.game_name)
    # x_test_classes = torch.tensor(test_data.game_name)
    x_train = torch.tensor(np.load('train.npy')).to('cuda')
    x_test = torch.tensor(np.load('test.npy')).to('cuda')
    y_valid = torch.tensor(valid_data.flag).to('cuda')
    # x_valid_classes = torch.tensor(valid_data.game_name)
    x_valid = torch.tensor(np.load('valid.npy')).to('cuda')

    # train_dataset = TensorDataset(x_train, y_train)
    # batch_size = 512
    # train_data_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    # valid_dataset = TensorDataset(x_valid, y_valid)
    # batch_size = 64
    # valid_data_loader = DataLoader(valid_dataset, batch_size=batch_size, shuffle=False)

    # model = TextClassificationNN().to('cuda')
    # model.fit(train_data_loader, valid_data_loader, epochs=25, lr=0.001)

    test_dataset = TensorDataset(x_test, y_test)
    batch_size = 64
    test_data_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    model = torch.load('model')
    model.eval()
    model.to('cuda')
    metrics = [Accuracy(), F1Score(num_classes=4)]
    metrics_values = {key.name:0 for key in metrics}
    with torch.no_grad():
        for x,y in tqdm(test_data_loader, total=len(test_data_loader)):
            output = model(x)
            metrics_values['accuracy']+=metrics[0](output, y)
            metrics_values['f1score']+=metrics[1](output, y)
    print('accuracy', metrics_values['accuracy']/len(test_data_loader))
    print('f1score', metrics_values['f1score']/len(test_data_loader))

# https://prnt.sc/cG_AxKhZXNw4
# https://prnt.sc/9YLEqWgna0cs
    
if __name__ == '__main__':
    main()