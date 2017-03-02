import io_mesh as io
import numpy as np

#import template mesh. has fields mesh['coords'] for xyz coordinates
# and mesh['faces'] for face indices
mesh = io.load_mesh_geometry('Structure/average/S900.L.pial_MSMAll.32k_fs_LR.surf.gii')

#load in mask of vertices being considered (BA44 and 45)
mask = np.loadtxt('vlpfc_nodes.1D', dtype=int)

#restrict mesh using the mask

