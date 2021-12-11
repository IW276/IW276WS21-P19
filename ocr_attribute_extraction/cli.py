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
    download_models_parser = parser.add_mutually_exclusive_group(
        required=False)
    download_models_parser.add_argument(
        '--download-models',
        dest='download_models',
        action='store_true'
    )
    download_models_parser.add_argument(
        '--skip-download-models',
        dest='download_models',
        action='store_false'
    )
    parser.set_defaults(download_models=True)
    args = parser.parse_args()

    pipeline = Pipeline(stages=[
        DirIteratorStage(allowed_extensions=[
            ".jpg", ".jpeg", ".png"
        ]),
        OCRStage(),
        TextSpellCorrectionStage(),
        SimpleAttributeExtractionStage(language=args.language),
        AdvancedAttributeExtractionStage(
            language=args.language,
            download_models=args.download_models
        ),
        JsonOutputStage(),
        PrintStage(),
    ])

    pipeline.run(args.input_paths)
