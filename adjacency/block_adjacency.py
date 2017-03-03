import numpy as np
from scipy import sparse
from scipy import io
import os
import sys

def blocked_adjacency(nSubjects=10, mesh_fn='data/Structure/average/S900.L.pial_MSMAll.32k_fs_LR.surf.gii',  label1_fn='data/vlpfc_nodes.1D', aggr_adj_fn='data/all_subjects_adjacency.mtx' ):
    adj_fn='data/adjacency_matrix.npy'
    
    label = np.loadtxt(label1_fn)
    length = len(label)

    
    if os.path.exists(adj_fn):
        print 'Loading standard adjacency matrix'
        adj = np.load(adj_fn).astype(bool)
    else:
        print 'Creating standard adjacency matrix'
        adj = surface_to_graph(mesh_fn, label1_fn , adj_fn)

    block_adj = np.zeros([nSubjects*length,nSubjects*length],dtype=bool)
    s=-1
    
    print 'Creating blocked adjacency matrix for ', str(nSubjects), 'subjects'
    for sub in range(nSubjects):
        s+=1
        #print (s+1)*length
        block_adj[s*length:(s+1)*length,s*length:(s+1)*length]=adj

    print 'Converting blocked matrix to sparse matrix'
    sparse_mat = sparse.coo_matrix(block_adj, dtype=int)
    #plt.plot(sparse_mat.col, sparse_mat.row, 's')
    sparse_csr = sparse.csr_matrix(sparse_mat)

    print 'Writing sparse blocked matrix to', aggr_adj_fn
    io.mmwrite(aggr_adj_fn, sparse_csr) 
    #np.save('data/all_subjects_adjacency.npy',sparse_csr)
    return sparse_csr

def main():
    if sys.argv[1] != None:
        nSubjects=int(sys.argv[1])


    return blocked_adjacency(nSubjects=nSubjects)


if __name__ == '__main__':
    main()


