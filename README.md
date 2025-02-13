# Math Prof show - Class HS23 Course Project
![python badge](https://img.shields.io/badge/python-3.8-orange?logo=python&logoColor=white)
![Manim badge](https://img.shields.io/badge/Manim-0.18.0-blue")
![MiKTeX badge](https://img.shields.io/badge/MiKTeX-23.10.12-red?logo=latex&logoColor=white)

## Description
Python for Engineers course project to generate a mathematical video with the Manim Python library. We chose to prove TODO in an intuitive graphical way by dividing a unit square into triangles with known size due to geometry. Summing up these triangles represents the elements of the sum to be proven. Run the code and watch the generated video to see for yourself!

## Installation
### Python and Libraries
We've tested this project with Python 3.8
The only required python dependency is the manim package which you can install using pip
```
pip install manim
```
Optionally we also provide an environment.yml file for a conda environment. Create the environment with:
```
conda env create -f environment.yml
``` 

### LaTeX
To render the formulas a working version of LaTeX is required. For Windows, the recommended LaTeX distribution for Manim is MiKTeX. You will be prompted to install the required LaTeX packages when running the Python script for the first time. More detailed instructions to install Manim and a LaTeX distribution are given in the [Manim documentation](https://docs.manim.community/en/stable/index.html)

## Usage
The code will generate a mp4 file in the media/videos project subdirectory. To run this code enter:
```
manim -ql scene.py MyScene
```
The -ql flag will make manim render a low quality video for faster execution.

## Authors
Florian Wiederkehr & Dimitri Eilinger