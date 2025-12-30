from typing import List


class DataProcessor():
    def process(self):
        pass

    def validate(self):
        pass

    def format_output(self):
        pass


class NumericProcessor(DataProcessor):
    def process(self, numbers: List) -> None:
        print(f"Processing data: {numbers}")

    def validate(self, numbers: List) -> None:
        try:
            for n in numbers:
                n = int(n)
        except ValueError:
            print("Error processing data")
        print("Validation: Numeric data verified")

    def format_output(self, numbers: List) -> None:
        sum = 0
        count = 0
        for n in numbers:
            sum += n
            count += 1
        avg = sum / count
        print(f"Processed {count} numeric values, sum={sum}, avg={avg:.1f}")


class TextProcessor(DataProcessor):
    def process(self, phrase: str) -> None:
        print(f"Processing data: {phrase}")

    def validate(self, phrase: str) -> None:
        try:
            "Hello" + phrase
        except TypeError:
            print("Cannot do that")
        print("Validation: Text data verified")

    def format_output(self, phrase: str) -> None:
        count = 0
        for p in phrase:
            count += 1
        number_words = len(phrase.split(" "))
        print(f"Output: Processed text: {count} characters, {number_words} words")


class LogProcessor(DataProcessor):
    def process(self):
        print("Processing data: ")

    def validate(self):
        pass

    def format_output(self):
        pass
