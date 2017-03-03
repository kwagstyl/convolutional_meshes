import numpy as np
from scipy import sparse

IDs = np.loadtxt('../convolutional_meshes_data/Labels/subject_ids.txt',dtype=str)
label = np.loadtxt('data/vlpfc_nodes.1D')
length = len(label)
adj = np.load('data/sparse_adjacency_matrix.npy')
adj = np.load('data/adjacency_matrix.npy').astype(bool)

block_adj = np.zeros([len(IDs)*length,len(IDs)*length],dtype=bool)
s=-1
for sub in IDs:
    s+=1
    print (s+1)*length
    block_adj[s*length:(s+1)*length,s*length:(s+1)*length]=adj

sparse_mat = sparse.coo_matrix(block_adj, dtype=int)
#plt.plot(sparse_mat.col, sparse_mat.row, 's')

sparse_csr = sparse.csr_matrix(sparse_mat)

np.save('data/all_subjects_adjacency.npy',sparse_csr)

