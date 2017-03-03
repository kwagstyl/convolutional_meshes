import numpy as np
from scipy import sparse
from scipy import io


def main():
    print 'Hello World!'
    mesh_fn='data/Structure/average/S900.L.pial_MSMAll.32k_fs_LR.surf.gii'
    IDs_fn='Labels/subject_ids.txt'
    label1_fn='data/vlpfc_nodes.1D'
    adj_fn='data/adjacency_matrix.npy'

    IDs = np.loadtxt(IDs_fn,dtype=str)
    label = np.loadtxt(label1_fn)
    length = len(label)
    if os.path.exists(adj_fn):
        adj = np.load().astype(bool)
    else:
        adj = surface_to_graph(mesh_fn, label1_fn , adj_fn)

    block_adj = np.zeros([len(IDs)*length,len(IDs)*length],dtype=bool)
    s=-1
    for sub in IDs:
        s+=1
        print (s+1)*length
        block_adj[s*length:(s+1)*length,s*length:(s+1)*length]=adj

    sparse_mat = sparse.coo_matrix(block_adj, dtype=int)
    #plt.plot(sparse_mat.col, sparse_mat.row, 's')

    sparse_csr = sparse.csr_matrix(sparse_mat)

    io.mmwrite('data/all_subjects_adjacency.mtx', sparse_csr) 
    #np.save('data/all_subjects_adjacency.npy',sparse_csr)

if __name__ == '__main__':
    main()


