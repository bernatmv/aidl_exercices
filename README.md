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

Set the environment in VS Code on `settings.json`:

```json
{
  "editor.tabSize": 4,
  "python.linting.enabled": true,
  "python.pythonPath": "/Users/YOUR_HOME/.venv/bin/python",
  "python.linting.flake8Enabled": false,
  "python.linting.pylintEnabled": false,
  "python.linting.pycodestyleEnabled": true
}
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

# How to approach models

- Problem: we need a problem to solve and a definition of it

- Dataset

  - Inspect the dataset:

    - Look at some random samples.

    - Is it big enough? how many classes it have?

    - Does it have a class imbalance? (deviation between classses...)

  - Are you, as a human, able to solve that prolem withh these samples?

  - Split the dataset into 3 _separate_ subsets (selected randomly or randomly _per class_)

    - Train (train data distribution, > ~70% of the dataset): used to train the model

    - Validation (validation data distribution, < ~20% of the dataset (just be sure there is enough data to be representative)):

      - Should not contain any traning data ecause we need to validate if the model has memorized all training data (eg: it has too many parameters and it's not generic enough)

      - Every once in a while during training we use validation data to extract preformance metrics (to choose which model is the best; which, _caution_, leads to choose the model that better adapts to the subset you have chosen for this distribution so you can skew the final solution to the data selected for validation)

    - Test (test data distribution, < ~10% of the dataset (just be sure there is enough data to be representative)): "definitive" performance metrics (pending overfitting and othher considerations)

  - Data augmentation: amplify your dataset and maybe also normalize skewed datasets (eg: change brightness/contrast of images, flipping them, cropping them, etc)

    - Disk > Load > Transformation > Feed

    - Usually all data augmentation is done with CPU, while training is done by GPU

- Train:

  - Iteration process:

    - Feed batches of X samples of the train distribution

- Feeding data:

  - `feed_dict` is not efficient when dealing with big datasets!

  - `tf.data` efficiently handles the input pipeline so it optimizes GPU processing time, it does organizes CPU/GPU work so that GPU is always processing (adding them to the path can be parallelized based on the computational path for the graph).

    - `tf.data.Dataset` represents all the dataset so that you can load, transform and manipulate _AND_ all that will be represented as operations on the graph so that TF can optimize all this process (represented as symbolic elements, but _not_ embedded)

    - `tf.data.Iterator` iterates over the dataset and provides the samples to the network

    - All `tf.data` transformation functions are implemented in `C` so those are far more efficient to use than embedding Python functions as the transformations

- Validate:

  - Performance metrics:

    - Feed batch of Y samples of the validation distribution
