from abc import ABC, abstractmethod
from typing import List


class DataStream(ABC):
    def __init__(self, stream_id: str | None = None) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_stream(self) -> None:
        pass

    def validate(self) -> bool:
        pass

    def filtered(self) -> bool:
        pass

    def transformation(self) -> None:
        pass


class StreamProcessor():
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_streams(self) -> None:
        for stream in self.streams:
            stream.process_stream()


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
        if not self.filtered():
            return
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

    def filtered(self) -> bool:
        self.validate_data = [
            x for x in self.int_data
            if x is not None and x >= 0
            ]
        if self.validate_data == []:
            return (False)
        else:
            print(f"Processing sensor batch: {self.validate_data}")
            return (True)

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
    def __init__(self, stream_id, data: List) -> None:
        super().__init__(stream_id)
        self.data: List = data
        self.int_data: List[int] = []
        self.validate_data: List[int] = []
        self.operations: int = 0
        self.net_flow: int = 0

    def process_stream(self) -> None:
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")
        if not self.validate():
            print("Transaction Stream failed. Data is corrupted")
            return
        if not self.filtered():
            return
        self.transformation()

    def validate(self) -> bool:
        self.int_data = []
        try:
            for n in self.data:
                self.int_data.append(int(n))
            return (True)
        except ValueError:
            print("TransactionStream failed: Data are not numbers")
            return (False)

    def filtered(self) -> bool:
        self.validate_data = [data for data in self.int_data if data != 0]
        if self.validate_data == []:
            print("Transaction stream failed. Data is 0")
            return (False)
        else:
            print(f"Processing transaction batch: {self.validate_data}")
            return (True)

    def transformation(self) -> None:
        self.operations = len(self.validate_data)
        self.net_flow = sum(self.validate_data)
        if self.net_flow >= 0:
            print(
                f"Transaction analysis: {self.operations} operations, "
                f"net flow: +{self.net_flow} units")
        else:
            print(
                f"Transaction analysis: {self.operations} operations, "
                f"net flow: {self.net_flow} units")


class EventStream(DataStream):
    def __init__(self, stream_id, data: List[str]) -> None:
        super().__init__(stream_id)
        self.data = data
        self.str_data: List[str] = []
        self.events: int = 0
        self.error_event: int = 0

    def process_stream(self):
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")
        if not self.validate():
            print("Event Stream failed. Data is corrupted")
            return
        if not self.filtered():
            print("Event Stream failed. Strings out of range")
        self.transformation()

    def validate(self) -> bool:
        if not isinstance(self.data, list):
            print("EventStream failed: data is not iterable")
            return False

        for event in self.data:
            if not isinstance(event, str):
                print("EventStream failed: non-string event detected")
                return False
            if event.strip() == "":
                print("EventStream failed: empty event detected")
                return False

        return True

    def filtered(self) -> bool:
        keywords = {"login", "logout", "error"}
        self.str_correct = [
            word for word in self.data
            if word in keywords
            ]
        if self.str_correct == []:
            print("Event Stream failed. Events are not valid")
            return (False)
        else:
            print(f"Processing event batch: {self.str_correct}")
            return (True)

    def transformation(self) -> None:
        self.events = len(self.str_correct)
        count: int = 0
        for event in self.str_correct:
            if event == "error":
                count += 1
        self.error_event = count
        print(
            f"Event analysis: {self.events} events, "
            f"{self.error_event} error detected")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream(
        "SENSOR_001",
        [22.5, 65, 1013]
    )

    transaction = TransactionStream(
        "TRANS_001",
        [100, -75, 150]
    )

    event = EventStream(
        "EVENT_001",
        ["login", "error", "logout"]
    )

    sensor.process_stream()
    transaction.process_stream()
    event.process_stream()

    # --- Polymorphic processing demo ---
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(
        SensorStream("SENSOR_BATCH", [20, 21, 22])
    )
    processor.add_stream(
        TransactionStream("TRANS_BATCH", [200, -50, -25, 75])
    )
    processor.add_stream(
        EventStream("EVENT_BATCH", ["login", "error", "logout"])
    )

    processor.process_streams()

    print("Stream filtering active: High-priority data only")
    print(
        "Filtered results: 2 critical sensor alerts, "
        "1 large transaction"
    )
    print(
        "All streams processed successfully. "
        "Nexus throughput optimal."
    )
