import argparse
from .dir_iterator_stage import DirIteratorStage
from .print_stage import PrintStage
from .pipeline import Pipeline
from .ocr_stage import OCRStage
from .simple_attribute_extraction_stage import SimpleAttributeExtractionStage


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_paths',
        type=str,
        nargs='+',
    )
    args = parser.parse_args()

    pipeline = Pipeline(stages=[
        DirIteratorStage(allowed_extensions=[
            ".jpg", ".jpeg", ".png"
        ]),
        OCRStage(),
        SimpleAttributeExtractionStage(),
        PrintStage()
    ])

    pipeline.run(args.input_paths)
