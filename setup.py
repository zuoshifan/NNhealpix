from setuptools import setup

setup(
    name="nnhealpix",
    version="0.3.0",
    description="",
    url="",
    author="Nicoletta Krachmalnicoff, Maurizio Tomasi",
    author_email="nkrach@sissa.it, maurizio.tomasi@unimi.it",
    license="MIT",
    packages=["nnhealpix", "nnhealpix.layers", "nnhealpix.projections"],
    package_dir={"nnhealpix": "nnhealpix", "nnhealpix.layers": "nnhealpix/layers", "nnhealpix.projections": "nnhealpix/projections"},
    # package_data={"nnhealpix": ["ancillary_files/*"]},
    # include_package_data=True,
    zip_safe=False,
)
