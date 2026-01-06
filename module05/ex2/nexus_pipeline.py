from collections import deque


class ProcessingPipeline():
    def __init__(self, pipeline_id: str | None = None) -> None:
        self.pipeline_id = pipeline_id
        self.stages = deque()

    def add_stage(self, stage) -> None:
        self.stages.append(stage)

    def execute_pipeline(self, data):
        new_data = data
        for stage in self.stages:
            new_data = stage.execute(new_data)
        return new_data


class InputStage():
    def execute(self, data: dict) -> dict:
        return data


class TransformStage():
    def execute(self, data: dict) -> dict:
        return data


class OutputStage():
    def execute(self, data: dict) -> dict:
        return data


class NexusManager():
    def __init__(self):
        self.pipelines_collection = {}

    def register_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines_collection[pipeline.pipeline_id] = pipeline

    def main_execution(self, data_adapted_dict):
        pipeline_id = data_adapted_dict["pipeline_id"]
        try:
            pipeline = self.pipelines_collection[pipeline_id]
            return (pipeline.execute_pipeline(data_adapted_dict))
        except KeyError:
            print("Pipeline not exist")
            return


class JSONAdapter():
    def __init__(self, pipeline_id: int):
        self.pipeline_id = pipeline_id

    def adapt(self, raw_data) -> dict:
        data_adapted = {
            "pipeline_id": self.pipeline_id,
            "payload": raw_data
            }
        return data_adapted


class CSVAdapter():
    def __init__(self, pipeline_id: int):
        self.pipeline_id = pipeline_id

    def adapt(self, raw_data) -> dict:
        data_adapted = {
            "pipeline_id": self.pipeline_id,
            "payload": raw_data
        }
        return data_adapted


class StreamAdapter():
    def __init__(self, pipeline_id: int):
        self.pipeline_id = pipeline_id

    def adapt(self, raw_data) -> dict:
        data_adapted = {
            "pipeline_id": self.pipeline_id,
            "payload": raw_data
        }
        return data_adapted


if __name__ == "__main__":
    pass
