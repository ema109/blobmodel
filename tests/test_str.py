import pytest
from blobmodel import Model, BlobShapeImpl
from blobmodel.geometry import Geometry


def test_blob_shape_exception():
    with pytest.raises(NotImplementedError):
        bm = Model(
            Nx=2,
            Ny=2,
            Lx=10,
            Ly=10,
            dt=0.5,
            T=1,
            periodic_y=False,
            blob_shape=BlobShapeImpl("different_shape"),
            num_blobs=1,
        )
        bm.make_realization(speed_up=True, error=0.1)


def test_geometry_str():
    geo = Geometry(1, 1, 1, 1, 1, 1, False)
    assert (
        str(geo)
        == "Geometry parameters:  Nx:1,  Ny:1, Lx:1, Ly:1, dt:1, T:1, y-periodicity:False"
    )


def test_model_str():
    bm = Model(
        Nx=2,
        Ny=2,
        Lx=10,
        Ly=10,
        dt=0.5,
        T=1,
        periodic_y=False,
        blob_shape=BlobShapeImpl("exp"),
        num_blobs=1,
    )
    assert str(bm) == "2d Blob Model with num_blobs:1 and t_drain:10"


test_blob_shape_exception()
test_geometry_str()
test_model_str()
