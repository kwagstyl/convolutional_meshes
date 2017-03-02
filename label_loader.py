import io_mesh as io
import numpy as np

## Load limiting mask i.e. vertices to include
mask = np.loadtxt('mask/vlpfc_nodes.1D', dtype=int)

## Load subject IDs      
IDs = np.loadtxt('convolutional_meshes_data/Labels/subject_ids.txt', dtype=str)

label_matrix = np.zeros([len(IDs), len(mask)])

s=-1
for subject in IDs:
  s+=1
  fulldata=np.loadtxt('convolutional_meshes_data/Labels/BA45_' + subject + '.1D')
  label_matrix[s,:] = fulldata[mask]

