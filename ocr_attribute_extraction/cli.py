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
        metavar='PATH',
        type=str,
        nargs='+',
    )
    parser.add_argument(
        '--language',
        type=str,
        choices=['en', 'de'],
        default='en',
        help="the language of the input data. default: en",
    )
    parser.add_argument(
        '--skip-download-models',
        dest='download_models',
        action='store_false',
        default=True,
        help="don't download models on start",
    )
    parser.add_argument(
        '--extraction-method',
        type=str,
        choices=['complex', 'simple'],
        default='complex',
        help="choose the extraction method. default: complex",
    )
    parser.add_argument(
        '--json',
        type=str,
        default=None,
        metavar="PATH",
        help="output the extracted attributes at the specified path",
    )
    args = parser.parse_args()

    stages = [
        DirIteratorStage(allowed_extensions=[
            ".jpg", ".jpeg", ".png"
        ]),
        OCRStage(),
        TextSpellCorrectionStage(),
    ]
    if args.extraction_method == "simple":
        stages.append(SimpleAttributeExtractionStage(language=args.language))
    else:
        stages.append(AdvancedAttributeExtractionStage(
            language=args.language,
            download_models=args.download_models
        ))
    if args.json is not None:
        stages.append(JsonOutputStage(path=args.json))
    stages.append(PrintStage())
    pipeline = Pipeline(stages)

    pipeline.run(args.input_paths)
