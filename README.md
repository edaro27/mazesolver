# mazesolver
Boot.dev maze solver project

We use Tkinter, a Python 3 library, to open a graphical window with a blank canvas that the program will draw on.

Run python -m tkinter from command line to open a window demonstrating the interface.

Install pyenv with webi: curl -sS https://webi.sh/pyenv | sh

Add these to the bottom of the bash file:
    export PYENV_ROOT="$HOME/.pyenv"
    command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

pyenv install -v 3.10.7 - to install that Python version

pyenv global 3.10.7 - to set it as your default

check python and python3 --version

brew list - to see modules installed with homebrew
brew install python-tk@3.9 - to install tkinter