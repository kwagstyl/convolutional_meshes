import io_mesh as io
import numpy as np

## Load limiting mask i.e. vertices to include
mask = np.loadtxt('vlpfc_nodes.1D', dtype=int)-1

## Load subject IDs      
IDs = np.loadtxt('Labels/subject_ids.txt', dtype=str)

label_matrix = np.zeros([len(IDs), len(mask)])

s=-1
for subject in IDs:
  s+=1
  fulldata=np.loadtxt('Labels/BA45_' + subject + '.1D')
  label_matrix[s,:] = fulldata[mask]

np.savetxt('Label_data_in_mask.txt', label_matrix, fmt='%i')
