import torch
class Metric:
    def __init__(self, name: str = "metric") -> None:
        self.name: str = name

    def __call__(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> float:
        pass

class Accuracy(Metric):
    def __init__(self, name: str = "accuracy") -> None:
        super().__init__(name)

    def __call__(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> float:
        pred_classes = torch.argmax(y_pred, dim=1)
        correct = torch.eq(pred_classes, y_true).sum().item()
        return correct/len(y_pred) 
    
class F1Score(Metric):
    def __init__(self,  num_classes: int = 2, name: str = 'f1score') -> None:
        super().__init__(name)
        self.__num_classes: int = num_classes

    def __call__(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> float:
        f1_scores = []
        y_pred = torch.argmax(y_pred, dim=1)
        for i in range(self.__num_classes):
            tp = ((y_pred == i) & (y_true == i)).sum().item()
            fp = ((y_pred == i) & (y_true != i)).sum().item()
            fn = ((y_pred != i) & (y_true == i)).sum().item()
            
            precision = tp / (tp + fp + 1e-8)
            recall = tp / (tp + fn + 1e-8)
            
            f1 = 2 * (precision * recall) / (precision + recall + 1e-8)
            f1_scores.append(f1)
        
        f1_score = sum(f1_scores) / len(f1_scores)
        return f1_score