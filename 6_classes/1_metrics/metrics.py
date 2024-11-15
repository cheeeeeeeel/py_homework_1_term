
import csv
from typing import Protocol
from datetime import datetime, timezone


class TypeFile(Protocol):

    def __init__(self, path: str):
        self.path = path
        self._create_file()

    def writing_to_file(self, data: list[list[str]]) -> None:
        """Записывает data (данные хранящиеся в буфере) в файл"""

    def _create_file(self) -> None:
        """Создаёт файл"""


class TxtFile(TypeFile):

    def writing_to_file(self, data: list[list[str]]) -> None:
        with open(self.path, "a", newline="") as file:
            for date_metric_value in data:
                date, metric, value = date_metric_value
                file.write(f"{date} {metric} {value}\n")

    def _create_file(self) -> None:
        with open(self.path, "w", newline="") as _:
            pass


class CsvFile(TypeFile):

    def writing_to_file(self, data: list[list[str]]) -> None:
        with open(self.path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
            writer.writerows(data)

    def _create_file(self) -> None:
        with open(self.path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerow(["date", "metric", "value"])


class Statsd:

    def __init__(self, buffer_limit: int, storage_type: TypeFile):
        self.buffer_limit = buffer_limit
        self.storage = storage_type
        self.buffer = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._from_buffer_to_file()

    def _metric_writing(self, metric: str, value: int) -> None:
        """Записывает метрики в буфер. При полном заполнении буфера эвакуирует данные в хранилище"""
        self.buffer.append([date_utc_now(), metric, value])
        if len(self.buffer) == self.buffer_limit:
            self._from_buffer_to_file()

    def _from_buffer_to_file(self) -> None:
        """Переносит данные из буфера в файл. Теперь буфер пуст"""
        self.storage.writing_to_file(self.buffer)
        self.buffer = []

    def incr(self, metric_name: str) -> None:
        """Прирост метрики"""
        self._metric_writing(metric_name, 1)

    def decr(self, metric_name: str)  -> None:
        """Уменьшение метрики"""
        self._metric_writing(metric_name, -1)

def date_utc_now() -> str:
    """Дата и время прямо сейчас в UTC тайм зоне"""
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")

def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Инициализацию метрик для текстового файла"""
    if not path.endswith(".txt"):
        raise ValueError("Файл должен иметь расширение '.txt'")
    return Statsd(buffer_limit, TxtFile(path))

def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Инициализацию метрик для csv файла"""
    if not path.endswith(".csv"):
        raise ValueError("Файл должен иметь расширение '.csv'")
    return Statsd(buffer_limit, CsvFile(path))