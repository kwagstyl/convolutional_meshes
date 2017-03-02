import io_mesh as io
import numpy as np
##loading data
#load limiting mask i.e. vertices to include
#-1 for matlab python indexing
mask = np.loadtxt('vlpfc_nodes.1D', dtype=int)-1


#load subject ids
IDs = np.loadtxt('Labels/subject_ids.txt',dtype=str)

#load subject overlays

files = ['curvature.32k_fs_LR.shape.gii', 'thickness.32k_fs_LR.shape.gii', 
       'sulc.32k_fs_LR.shape.gii', 'MyelinMap.32k_fs_LR.func.gii',
       'MyelinMap_BC.32k_fs_LR.func.gii', 'corrThickness.32k_fs_LR.shape.gii']


feature_matrix = np.zeros([len(IDs), len(mask), len(files)])
#mask out all vertices not of interest

s=-1
for subject in IDs:
    s+=1
    f=-1
    for file in files:
        f+=1
        fulldata = io.load_mesh_data('Structure/' + subject + '/' + subject + '.L.' + file)
        feature_matrix[s,:,f] = fulldata[mask]


       
np.save('feature_matrix.npy', feature_matrix)
