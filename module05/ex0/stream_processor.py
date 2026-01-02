from abc import ABC, abstractmethod
from typing import List


class DataProcessor(ABC):
    def __init__(self, data: str | None = None) -> None:
        self.data = data

    @abstractmethod
    def process(self) -> None:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def format_output(self) -> None:
        pass


class NumericProcessor(DataProcessor):
    def __init__(self, data: List | None = None) -> None:
        super().__init__(data)
        if self.data is None:
            self.data: List = []
        self.proces_nbr: List[int] = []

    def process(self) -> None:
        print("Initializing Numeric Processor...")
        print(f"Processing data: {self.data}")
        if self.validate():
            self.format_output()

    def validate(self) -> bool:
        try:
            self.proces_nbr = []
            for n in self.data:
                self.proces_nbr.append(int(n))
            print("Validation: Numeric data verified")
            return (True)
        except ValueError:
            print("Error processing data")
            return (False)

    def format_output(self) -> None:
        sume = 0
        count = 0
        for n in self.proces_nbr:
            sume += n
            count += 1
        avg = sume / count
        print(f"Processed {count} numeric values, sum={sume}, avg={avg:.1f}")


class TextProcessor(DataProcessor):
    def __init__(self, data: str | None = None) -> None:
        super().__init__(data)
        if self.data is None:
            self.data: str = ""
        self.words: int = 0
        self.phrase: str = ""

    def process(self) -> None:
        print("Initializing Text Processor...")
        print(f"Processing data: {self.data}")
        if self.validate():
            self.format_output()

    def validate(self) -> bool:
        if type(self.data) is str and self.data.strip():
            self.phrase = self.data.strip()
            self.words = len(self.phrase.split())
            print("Validation: Text data verified")
            return True
        return False

    def format_output(self) -> None:
        count = 0
        for p in self.phrase:
            count += 1
        print(
            f"Output: Processed text: {count} characters, {self.words} words"
            )


class LogProcessor(DataProcessor):
    def __init__(self, data: str | None = None) -> None:
        super().__init__(data)
        if self.data is None:
            self.data: str = ""
        self.normal: str = ""
        self.level: str = ""
        self.message: str = ""

    def process(self) -> None:
        print("Initializing Log Processor...")
        print(f'Processing data: "{self.data}"')
        if self.validate():
            self.format_output()

    def validate(self) -> bool:
        if type(self.data) is str:
            self.normal = self.data.strip()
            if self.normal.startswith(("ERROR:", "INFO:")):
                self.normal_splited: List = self.normal.split(":", maxsplit=1)
                self.level = self.normal_splited[0]
                self.message = self.normal_splited[1].strip()
                print("Validation: Log entry verified")
                return (True)
            else:
                print("Cannot validate log")
                return (False)
        else:
            print("Cannot validate log")
            return (False)

    def format_output(self) -> None:
        if self.level == "ERROR":
            print(
                f"Output: [ALERT] {self.level} level detected: "
                f"{self.message}")
        else:
            print(
                f"[INFO] {self.level} level detected: "
                f"{self.message}")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    processors = [
        NumericProcessor([1, 2, 3, 4, 5]),
        TextProcessor("Hello Nexus World"),
        LogProcessor("ERROR: Connection timeout"),
        LogProcessor("INFO: System ready"),
    ]

    for processor in processors:
        processor.process()
        print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    demo_processors = [
        NumericProcessor([1, 2, 3]),
        TextProcessor("Hello World"),
        LogProcessor("INFO: System ready"),
    ]

    index = 1
    for processor in demo_processors:
        print(f"Result {index}: ", end="")
        processor.process()
        index += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
