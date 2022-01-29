
from .Dot import DotGenerator
from .Diagram import DiagramGenerator

class GeneratorFactory:

  generators = {
    'dot': DotGenerator,
    'diagram': DiagramGenerator
  }

  @classmethod
  def list_generators(cls):
    return cls.generators.keys()

  @classmethod
  def get_generator(cls, name):
    if name not in cls.generators:
      raise Exception(f"Generator not found : {name}. Valid values or {','.join(self.list_generators())}")

    return cls.generators[name]