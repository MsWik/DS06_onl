from typing import Dict
from torch import save

class Callback:
    def __init__(self, name: str = "callback") -> None:
        self.name = name

    def __call__(self, metrics: Dict) -> None:
        pass

class ModelCheckPoint(Callback):
    def __init__(
            self, 
            name: str = "modelcp",
            filepath: str = "mymodel",
            initial_threshold: float = 0.,
            monitor: str = "loss",
            mode: str = 'max',
            use_postfix: bool = False,
            ) -> None:
        super().__init__(name)
        self.__filepath: str = filepath
        self.__initial_threshold: float = initial_threshold
        self.__mode: str = mode
        self.__monitor: str = monitor
        self.__use_postfix: bool = use_postfix
    
    def __call__(self, metrics: Dict, model) -> None:
        if self.__monitor not in metrics.keys():
            print(f"There is no {self.__monitor} in metrics. {self.name} skipping")
            return
        if self.__mode == 'max':
            if metrics[self.__monitor] > self.__initial_threshold:
                self.__initial_threshold = metrics[self.__monitor]
                save(model, self.__filepath+f"{metrics[self.__monitor]:.4f}") if self.__use_postfix else save(model, self.__filepath)
        elif self.__mode == 'min':
            if metrics[self.__monitor] < self.__initial_threshold:
                self.__initial_threshold = metrics[self.__monitor]
                save(model, self.__filepath+f"{metrics[self.__monitor]:.4f}") if self.__use_postfix else save(model, self.__filepath)



class EarlyStopping(Callback):
    def __init__(
            self,
            name: str = "earlystopping",
            min_delta: float = 0.01,
            patience: int = 5,
            monitor: str = "loss",
            initial_epoch: int = 5,
            ) -> None:
        super().__init__(name)
        self.__min_delta: float = min_delta
        self.__patience: int = patience
        self.__monitor: str = monitor
        self.__initial_epoch: int = initial_epoch
        self.__current_epochs: int = 0
        self.__current_patience: int = 0
        self.__old_metric_value: float = 0.

    def __call__(self, metrics: Dict) -> bool:
        if self.__current_epochs < self.__initial_epoch: return True
        if self.__monitor not in metrics.keys(): 
            print(f"There is no {self.__monitor} in metrics. {self.name} skipping")
            return True
        self.__current_patience+=1
        if self.__current_patience != self.__patience: return True
        if abs(self.__old_metric_value-metrics[self.__monitor])<self.__min_delta:
            return False
        self.__current_patience=0
        self.__old_metric_value = metrics[self.__monitor]
        


class Logger(Callback):
    def __init__(
            self,
            name: str = "logger",
            filepath: str = "logs"
            ) -> None:
        super().__init__(name)
        self.__filepath: str = filepath
        self.__first_time: bool = True

    def __call__(self, metrics: Dict) -> None:
        with open(self.__filepath, 'a') as file:
            if self.__first_time: file.write(",".join(metrics.keys())) 
            file.write("\n"+",".join(map(str,metrics.values())))
        self.__first_time = False
