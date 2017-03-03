import io_mesh as io
import numpy as np
import scipy.misc
from scipy.sparse import csr_matrix

def mesh_to_graph(faces):
    n=faces.max()+1
    adj = np.zeros([n,n], dtype=bool)
    for v0, v1, v2 in faces:
        #adj[v0][v0]=adj[v1][v1]=adj[v2][v2]=1
        adj[v0][v1] = adj[v1][v0] = 1
        adj[v0][v2] = adj[v2][v0] = 1
        adj[v1][v2] = adj[v2][v1] = 1

    return adj

def mask_faces(mask, faces):

    masked_faces=[]
    for i in range(len(faces)):
        f=faces[i]
        if f[0] in mask and f[1] in mask and f[2] in mask:
            masked_faces.append(f)
    return masked_faces

def reindexing(masked_faces):
    all_masked_vertices = np.unique( np.array(masked_faces).flatten() )
    reindex = dict([ (all_masked_vertices[i], i) for i in range(len(all_masked_vertices)) ])
    return reindex


def reindex_faces(masked_faces):
    all_masked_vertices = np.unique( np.array(masked_faces).flatten() )
    reindex = dict([ (all_masked_vertices[i], i) for i in range(len(all_masked_vertices)) ])
    masked_faces_ridx = np.array( [ map(lambda x : reindex[x], f) for f in masked_faces ], dtype=int)
    return masked_faces_ridx


def surface_to_graph(mesh_fn, mask_fn, adj_fn):
    #mesh_fn='data/Structure/average/S900.L.pial_MSMAll.32k_fs_LR.surf.gii'
    #mask_fn='data/vlpfc_nodes.1D'
    #import template mesh. has fields mesh['coords'] for xyz coordinates
    # and mesh['faces'] for face indices
    mesh = io.load_mesh_geometry(mesh_fn)
    faces = mesh['faces']

    #load in mask of vertices being considered (BA44 and 45)
    mask = np.loadtxt(mask_fn, dtype=int)
    mask = mask - 1

    #Mask the faces
    masked_faces=mask_faces(mask, faces)
    #Create indices for masked vertices
    reindex = reindexing(masked_faces)
    masked_faces_ridx = np.array( [ map(lambda x : reindex[x], f) for f in masked_faces ], dtype=int)  
    #restrict mesh using the mask
    adj = mesh_to_graph(masked_faces_ridx)

    #convert to sparse matrix
    #sparse_adj = csr_matrix(adj)
#    scipy.misc.imsave('data/adjacency_matrix.png', adj, format='png')
    np.save(adj_fn, adj)
    return adj


def main():
    return surface_to_graph()


if __name__ == '__main__':
    main()

