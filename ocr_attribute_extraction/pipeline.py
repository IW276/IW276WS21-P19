class Pipeline:
    def __init__(self, stages):
        self.stages = stages

    def run(self, input_items):
        items = input_items

        for stage in self.stages:
            items = [
                processed_item
                for item in items
                for processed_item in stage.process(item)
            ]
