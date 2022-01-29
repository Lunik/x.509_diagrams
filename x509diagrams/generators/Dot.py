import logging
import graphviz

from .Generic import GenericGenerator
from x509diagrams.utils.certificates import human_readable_fingerprint, common_name

class DotGenerator(GenericGenerator):
  logger = logging.getLogger(__name__)

  DEFAULT_NAME = "result"

  def generate(self, output):
    if output is None:
      output = self.DEFAULT_NAME

    dot = graphviz.Digraph("Certificate tree")

    temp_certs = []

    for cert in self.certificates:
      subject = cert.subject.rfc4514_string()
      if subject not in temp_certs:
        temp_certs.append(subject)
        dot.node(subject, subject)

    temp_links = []

    for cert in self.certificates:
      subject = cert.subject.rfc4514_string()
      issuer = cert.issuer.rfc4514_string()
      if (issuer, subject) not in temp_links and issuer != subject:
        temp_links.append((issuer, subject))
        dot.edge(issuer, subject)

    with open(f"{output}.dot", 'w') as f:
      f.write(dot.source)

    dot.render(filename=output, format="svg")