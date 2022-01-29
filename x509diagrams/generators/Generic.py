import os
import logging

from colorama import Fore, Back, Style
from cryptography import x509

from x509diagrams.logger import get_custom_logger
from x509diagrams.utils.certificates import common_name


class GenericGenerator:
  logger = get_custom_logger()
  certificates = []

  def add_certificate(self, certificate):
    self.logger.info(f"Adding certificate CN={Style.BRIGHT}{certificate.subject.rfc4514_string()}{Style.RESET_ALL}")
    self.certificates.append(certificate)

  def retreiv_certificate(self, path):
    self.logger.debug(f"Trying to parse file: {Style.BRIGHT}{path}{Style.RESET_ALL}")
    res = None

    try:
      with open(path, 'rb') as f:
        try:
          res = x509.load_pem_x509_certificate(f.read())
          self.logger.debug(f"Successfully parsed file : {path}")
        except ValueError as e:
          self.logger.warning(f"Unable to parse certificate at path : {Style.BRIGHT}{path}{Style.RESET_ALL}")
          self.logger.warning(str(e))
    except PermissionError as e:
      self.logger.warning(f"Unable to read certificate at path : {Style.BRIGHT}{path}{Style.RESET_ALL}")
      self.logger.warning(str(e))

    return res

  def retreiv_certificates_from_folder(self, path, recurse=False):
    self.logger.debug(f"Searching if folder : {Style.BRIGHT}{path}{Style.RESET_ALL}")
    items = os.scandir(path)

    for item in items:
      if item.is_file():
        cert = self.retreiv_certificate(item.path)
        if cert is not None:
          self.add_certificate(cert)
      elif item.is_dir() and recurse:
        self.retreiv_certificates_from_folder(item.path, recurse=recurse)

  def generate(self, output):
    raise Exception("Method should be implemented")