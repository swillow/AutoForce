# +
import os

from ase.io import read

import theforce.distributed as dist
from theforce.cl import ARGS
from theforce.cl.mlmd import mlmd, read_md
from theforce.util.parallel import mpi_init

group = ARGS["process_group"]
os.environ["CORES_FOR_ML"] = str(dist.get_world_size())
try:
    from theforce.calculator import vasp

    calc_script = vasp.__file__
except:
    raise

atoms = read("POSCAR")
mlmd(atoms, calc_script=calc_script, **read_md("MD"), group=group)
