# AI:DL Exercices

Exercices for the post-grad of AI with Deep Learning

# Setup

Create a virtual environment

```sh
virtualenv --system-site-packages -p python3 ~/.venv
```

Activate to starting bash (.zshrc) script:

```sh
source ~/.venv/bin/activate
```

# Auto-Formatting

I'm using (VS Code)[https://code.visualstudio.com/docs/python/python-tutorial] with the (Python extension)[https://marketplace.visualstudio.com/items?itemName=ms-python.python] and autoformatting with `autopep8`.

```
"python.formatting.provider": "autopep8"
```

Make sure that the dependency is installed

```sh
pip install pep8
pip install --upgrade autopep8
```

If using VS Code made sure that

```
"editor.formatOnSave": true
```

# Linting

# Test
