
from datetime import datetime, timezone
import csv
from typing import Protocol


class TypeFile(Protocol):

    def metric_writing(self, metric: str, value: int) -> None:
        """Записывает данные в буфер. При полном заполнении буфера сохраняет данные в файл"""

    def writing_to_file(self) -> None:
        """Запись данных из буфера в файл"""


class TxtFile:

    def __init__(self, path: str, buffer_limit: int):
        self.path = path
        self.buffer_limit = buffer_limit
        self.buffer = []
        self.create_file(path)

    def metric_writing(self, metric: str, value: int) -> None:
        self.buffer.append(f"{Statsd.date_utc_now()} {metric} {value}\n")
        if len(self.buffer) == self.buffer_limit:
            self.writing_to_file()

    def writing_to_file(self) -> None:
        with open(self.path, "a", newline="") as file:
            file.writelines(self.buffer)
        self.buffer = []

    @staticmethod
    def create_file(file_path):
        with open(file_path, "w", newline="") as _:
            pass


class CsvFile:

    def __init__(self, path: str, buffer_limit: int):
        self.path = path
        self.buffer_limit = buffer_limit
        self.buffer = []
        self.create_file_with_header(path)

    def metric_writing(self, metric: str, value: int) -> None:
        self.buffer.append([Statsd.date_utc_now(), metric, value])
        if len(self.buffer) == self.buffer_limit:
            self.writing_to_file()

    def writing_to_file(self) -> None:
        with open(self.path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
            writer.writerows(self.buffer)
        self.buffer = []

    @staticmethod
    def create_file_with_header(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerow(["date", "metric", "value"])


class Statsd:

    def __init__(self, storage_type: TypeFile):
        self.storage = storage_type

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.storage.writing_to_file()

    def incr(self, metric_name: str) -> None:
        """Прирост метрики"""
        self.storage.metric_writing(metric_name, 1)

    def decr(self, metric_name: str)  -> None:
        """Уменьшение метрики"""
        self.storage.metric_writing(metric_name, -1)

    @staticmethod
    def date_utc_now() -> str:
        """Дата и время прямо сейчас в UTC тайм зоне"""
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Инициализацию метрик для текстового файла"""
    if not path.endswith(".txt"):
        raise ValueError("Файл должен иметь расширение '.txt'")
    return Statsd(TxtFile(path, buffer_limit))


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Инициализацию метрик для csv файла"""
    if not path.endswith(".csv"):
        raise ValueError("Файл должен иметь расширение '.csv'")
    return Statsd(CsvFile(path, buffer_limit))