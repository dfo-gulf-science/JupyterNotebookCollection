#!/bin/bash

#git fetch origin
#git reset --hard origin/main

#jupyter notebook --ip='*' --NotebookApp.token='' --NotebookApp.password='' -p 80:80


jupyter notebook --port=80 --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.notebook_dir='/opt/JupyterNotebookCollection/'
