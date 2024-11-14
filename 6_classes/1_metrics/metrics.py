
from datetime import datetime, timezone
from abc import ABC, abstractmethod
import csv


class Statsd(ABC):

    def __init__(self, path: str, buffer_limit: int):
        self.path = path
        self.buffer_limit = buffer_limit
        self.buffer = []

    @abstractmethod
    def _metric(self, metric: str, value: int):
        pass

    def incr(self, metric_name: str):
        self._metric(metric_name, 1)

    def decr(self, metric_name: str):
        self._metric(metric_name, -1)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._writing_to_file()

    @abstractmethod
    def _writing_to_file(self):
        pass


class TxtFile(Statsd):

    def __init__(self, path: str, buffer_limit: int):
        super().__init__(path, buffer_limit)
        with open(path, "w", newline="") as _:
            pass

    def _metric(self, metric: str, value: int):
        date = datetime.now(tz=timezone.utc)
        date = date.strftime("%Y-%m-%dT%H:%M:%S%z")
        self.buffer.append(f"{date} {metric} {value}\n")
        if len(self.buffer) == self.buffer_limit:
            self._writing_to_file()

    def _writing_to_file(self):
        with open(self.path, "a", newline="") as file:
            file.writelines(self.buffer)
        self.buffer = []


class CsvFile(Statsd):

    def __init__(self, path: str, buffer_limit: int):
        super().__init__(path, buffer_limit)
        with open(path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerow(["date", "metric", "value"])

    def _metric(self, metric: str, value: int):
        date = datetime.now(tz=timezone.utc)
        date = date.strftime("%Y-%m-%dT%H:%M:%S%z")
        self.buffer.append([date, metric, value])
        if len(self.buffer) == self.buffer_limit:
            self._writing_to_file()

    def _writing_to_file(self):
        with open(self.path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
            writer.writerows(self.buffer)
        self.buffer = []


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Инициализацию метрик для текстового файла"""
    if not path.endswith(".txt"):
        raise ValueError("Файл должен иметь расширение '.txt'")
    return TxtFile(path, buffer_limit)


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Инициализацию метрик для csv файла"""
    if not path.endswith(".csv"):
        raise ValueError("Файл должен иметь расширение '.csv'")
    return CsvFile(path, buffer_limit)