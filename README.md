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

laminar python

It's got some awesome functions so please do download the whole package. but we're only using io_mesh.py so you could just download that module.

git clone https://github.com/kwagstyl/laminar_python


git clone https://github.com/kwagstyl/convolutional_meshes

add path:

export PYTHONPATH=$PYTHONPATH:/path/to/convolutional_meshes



