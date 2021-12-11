import argparse

from .dir_iterator_stage import DirIteratorStage
from .json_output_stage import JsonOutputStage
from .print_stage import PrintStage
from .pipeline import Pipeline
from .ocr_stage import OCRStage
from .simple_attribute_extraction_stage import SimpleAttributeExtractionStage
from .advanced_attribute_extraction_stage import AdvancedAttributeExtractionStage
from .spell_correction_stage import TextSpellCorrectionStage


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_paths',
        metavar='DIRECTORY',
        type=str,
        nargs='+',
    )
    parser.add_argument(
        '--language',
        type=str,
        choices=['en', 'de'],
        default='en',
    )
    args = parser.parse_args()

    pipeline = Pipeline(stages=[
        DirIteratorStage(allowed_extensions=[
            ".jpg", ".jpeg", ".png"
        ]),
        OCRStage(),
        TextSpellCorrectionStage(),
        SimpleAttributeExtractionStage(language=args.language),
        AdvancedAttributeExtractionStage(language=args.language),
        JsonOutputStage(),
        PrintStage(),
    ])

    pipeline.run(args.input_paths)
