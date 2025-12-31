from typing import


class DataProcessor():
    def __init__(self, data: str) -> None:
        self.data = data

    def process(self) -> None:
        print("Generic message")
        self.validate()
        self.format_output()

    def validate(self) -> None:
        print("Generic message")

    def format_output(self) -> None:
        print("Generic message")


class NumericProcessor(DataProcessor):
    def __init__(self, data):
        super().__init__(data)
        self.flag = True
        self.proces_nbr = []

    def process(self) -> None:
        print(f"Processing data: {self.data}")
        self.validate()

    def validate(self) -> None:
        try:
            for n in self.data:
                self.proces_nbr.append(int(n))
            print("Validation: Numeric data verified")
        except ValueError:
            self.flag = False
            print("Error processing data")
        if self.flag:
            self.format_output()

    def format_output(self) -> None:
        sume = 0
        count = 0
        for n in self.proces_nbr:
            sume += n
            count += 1
        avg = sume / count
        print(f"Processed {count} numeric values, sum={sume}, avg={avg:.1f}")


class TextProcessor(DataProcessor):
    def __init__(self, data):
        super().__init__(data)
        self.words = 0
        self.phrase = ""

    def process(self) -> None:
        print(f"Processing data: {self.data}")
        if self.validate():
            self.format_output()

    def validate(self) -> bool:
        if type(self.data) == str and self.data != "" and len(self.data.split()):
            self.phrase = self.data.strip()
            self.words = len(self.phrase.split(" "))
            print("Validation: Text data verified")
            return (True)
        else:
            print("Invalid text")
            return (False)

    def format_output(self) -> None:
        count = 0
        for p in self.phrase:
            count += 1
        print(
            f"Output: Processed text: {count} characters, {self.words} words"
            )


class LogProcessor(DataProcessor):
    def process(self):
        print("Processing data: ")

    def validate(self):
        pass

    def format_output(self):
        pass
