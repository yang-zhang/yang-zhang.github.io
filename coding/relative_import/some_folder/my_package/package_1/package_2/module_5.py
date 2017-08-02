from . import module_4
from .. import module_3
from ... import module_1

from .module_4 import func_4
from ..module_3 import func_3
from ...module_1 import func_1 

print('module_5!')

func_4()
func_3()
func_1()

module_4.func_4()
module_3.func_3()
module_1.func_1()