# jupyter run
jupyter notebook

# jupyter theme
- https://code-machina.github.io/2019/02/07/Jupyter-Notebook-themes.html
- pip install jupyterthemes
- jt -l
- jt -t grade3 -f roboto -fs 12 -altp -tfs 12 -nfs 12 -cellw 80% -T -N

# add kernel
- source ./venv/bin/activate 한후 현재 venv 의 값을 venv01 로 kernel 추가시 아래처럼
- python -m ipykernel install --user --name=venv01
