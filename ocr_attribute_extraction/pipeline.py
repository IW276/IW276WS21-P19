import sys
import time


class Pipeline:
    def __init__(self, stages):
        self.stages = stages

    def run(self, input_items):
        items = input_items

        for stage in self.stages:
            start = time.time()
            items = [
                processed_item
                for item in items
                for processed_item in stage.process(item)
            ]
            stage.finalize()
            end = time.time()
            print(
                f"{type(stage).__name__:─^34} Time taken: {round(end - start, 5): >10} seconds",
                file=sys.stderr
            )
