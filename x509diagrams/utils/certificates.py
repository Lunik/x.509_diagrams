import binascii

from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID

def human_readable_fingerprint(certificate):
  return binascii.hexlify(
    certificate.fingerprint(
      hashes.SHA256()
    ), ':').decode()

def common_name(certificate):
  return certificate.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value