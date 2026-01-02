from abc import ABC, abstractmethod
from typing import List


class StreamProcessor():
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_streams(self) -> None:
        for stream in self.streams:
            stream.process_stream()


class DataStream(ABC):
    def __init__(self, stream_id: str | None = None) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_stream(self) -> None:
        pass

    def validate(self) -> bool:
        pass

    def filtered(self) -> None:
        pass

    def transformation(self) -> None:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id, data: List) -> None:
        super().__init__(stream_id)
        self.data: List = data
        self.int_data: List[int] = []
        self.validate_data: List[int] = []
        self.len_data: int = 0
        self.average_data: float = 0

    def process_stream(self) -> None:
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
        if not self.validate():
            print("SensorStream failed: Data is corrupted")
            return
        self.filtered()
        self.transformation()

    def validate(self) -> bool:
        self.int_data = []
        try:
            for n in self.data:
                self.int_data.append(int(n))
            return (True)
        except ValueError:
            print("SensorStream failed: Data are not numbers")
            return (False)

    def filtered(self) -> None:
        self.validate_data = [x for x in self.int_data if x is not None and x >= 0]
        print(f"Processing sensor batch: {self.validate_data}")

    def transformation(self) -> None:
        self.len_data = len(self.validate_data)
        try:
            self.average_data = sum(self.validate_data) / self.len_data
            print(
                f"Sensor analysis: {self.len_data} readings processed, "
                f"avg temp: {self.average_data}°C")
        except ZeroDivisionError:
            print("Cannot calculate average")


class TransactionStream(DataStream):
    pass


class EventStream(DataStream):
    pass
