import io_mesh as io
import numpy as np

## Load limiting mask i.e. vertices to include
mask = np.loadtxt('vlpfc_nodes.1D', dtype=int)-1

## Load subject IDs      
IDs = np.loadtxt('Labels/subject_ids.txt', dtype=str)

label_matrix44 = np.zeros([len(IDs), len(mask)])
label_matrix45 = np.zeros([len(IDs), len(mask)])


s=-1
for subject in IDs:
  s+=1
  fulldata=np.loadtxt('Labels/BA45_' + subject + '.1D')
  label_matrix45[s,:] = fulldata[mask]
  fulldata=np.loadtxt('Labels/BA44_' + subject + '.1D')
  label_matrix44[s,:] = fulldata[mask]

np.savetxt('Label44_data_in_mask.txt', label_matrix44, fmt='%i')
np.savetxt('Label45_data_in_mask.txt', label_matrix45, fmt='%i')

