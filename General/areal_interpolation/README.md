# Instruction for setting up Areal Interpolation
 
Before you begin, I assume that you have `python3` installed on your machine and you are using a Unix based shell (like Terminal on Mac OS).
 
A bit about virtual environments... certain packages and programs, like `areal_interpolation.py` rely on other packages with a specific version. This can get a bit messy when different programs require different versions of the same package.
 
We want to be able to use programs with different dependencies without needing a different computer for each program. For each program that is picky about which versions of packages it wants, we can create a *virtual environment* to keep that program's dependencies separate from all the rest.
 
1) In terminal, navigate to the directory you will be working in.
2) Ensure you don't have any virtual environments activated
    * Use command `deactivate` or `conda deactivate` if you are using a conda environment
3) Make a new virtual environment with `python3 -m venv areal_ve`
    * Use command `ls` and you should see a directory named `areal_ve`, which is the top level folder for the virtual environment you just created.
4) Activate the virtual environment you just created with `source areal_ve/bin/activate'`
    * Conda users may be used to activating their virtual environment from any directory, but note that you must be in the directory with `areal_ve` for this command to work.
    * You can deactivate this virtual environment at any time with `deactivate` (don't deactivate now if you wish to continue following this tutorial)
5) Run `pip install -r requirements.txt`
    * This installs all the dependencies listed in the `requirements.txt` file, but just inside our virtual environment.


If step 5 fails, run the following commands and try step 5 again.
```
pip install --upgrade setuptools
pip install ez_setup
brew install spatialindex
```

Additional debugging ideas:
If you see [GDAL](https://gdal.org/download.html) errors in your stack trace, consider trying to install it. 
```
brew install GDAL
pip3 install gdal
```
