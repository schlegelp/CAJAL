from .. import util as util
from ..geometry import triangulate_quads as triangulate_quads

def load_off(file_obj, **kwargs): ...
def export_off(mesh, digits: int = ...): ...
