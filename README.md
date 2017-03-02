# convolutional_meshes
framework to apply convolutional neural networks to neuroimaging surfaces


#Dependencies:

standard python packages:
pip install numpy argparse nibabel tensorflow networkx

python package for gcn implementation:

git clone https://github.com/tkipf/gcn

Make sure you can run:

python train.py

If you have trouble, open up utils.py

For us, sp.diags(r_inv) needed to be changed to sp.diags(r_inv, offsets=0)
(2 instances of sp.diags to change in total)


For reading in neuroimaging data we're going to be using io_mesh.py

It comes from laminar_python, which has some awesome functions so please do download the whole package (package: https://github.com/juhuntenburg/laminar_python  paper: https://doi.org/10.3897/rio.3.e12346). but we're currently only using io_mesh.py so I've copied it to this package. 


git clone https://github.com/kwagstyl/convolutional_meshes

add paths:

export PYTHONPATH=$PYTHONPATH:/path/to/convolutional_meshes



