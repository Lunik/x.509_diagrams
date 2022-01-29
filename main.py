import argparse
import logging

from x509diagrams.logger import get_custom_logger
from x509diagrams.generators.Factory import GeneratorFactory


parser = argparse.ArgumentParser(description="Generage diagrams from x.509 certificates")

parser.add_argument("--source-directory", "-s",
  dest="src",
  required=True,
  help="The source directory containing x.509 certificates",
)

parser.add_argument("--recursive", "-r",
  action="store_true",
  dest="recursive",
  default=False,
  help="Recurse in source directory",
)

parser.add_argument("--debug",
  action="store_true",
  dest="debug",
  default=False,
  help="Debug logs",
)

parser.add_argument("--output-format", "-f",
  dest="format",
  default="dot",
  choices=GeneratorFactory.list_generators(),
  help="The output format",
)

parser.add_argument("--output-file", "-o",
  dest="output",
  help="The output file path",
)


if __name__ == "__main__":
  args = parser.parse_args()

  log_level = logging.INFO
  if args.debug:
    log_level = logging.DEBUG

  logger=get_custom_logger()
  logger.setLevel(log_level)

  generator = GeneratorFactory.get_generator(args.format)()

  generator.retreiv_certificates_from_folder(args.src, recurse=args.recursive)

  generator.generate(args.output)