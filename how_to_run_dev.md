## How to debug source code of installed Python packages (e.g. scikit-learn)

Problem: I want to debug/step through scikit-learn code. But scikit-learn is already installed by conda:
```python
>>> import sklearn
>>> sklearn.__version__
'0.18.1'
>>> sklearn.__file__
'/Users/yangzhang/anaconda/lib/python3.6/site-packages/sklearn/__init__.py'
```

Fork the repo `https://github.com/scikit-learn/scikit-learn` to `https://github.com/yang-zhang/scikit-learn`.

```bash
$ pwd /Users/yangzhang/git
$ git clone https://github.com/yang-zhang/scikit-learn.git 
```

Install the package:
```
$ python setup.py build_ext --inplace
```

Add to `~/.bash_profile`:
```bash
export PYTHONPATH="/Users/yangzhang/git/scikit-learn:$PYTHONPATH"
```

and do:
```bash
$ source ~/.bash_profile
```

Now scikit-learn is using the development version:
```python
>>> import sklearn
>>> sklearn.__version__
'0.19.dev0'
>>> sklearn.__file__
'/Users/yangzhang/git/scikit-learn/sklearn/__init__.py'
```

Now you can use `pdb` to debug the source code (for example in examples in `examples` folder):
```python
import pdb; pdb.set_trace()
```
References:
- http://scikit-learn.org/stable/developers/contributing.html
- http://scikit-learn.org/stable/developers/advanced_installation.html
- https://stackoverflow.com/questions/6570635/installing-multiple-versions-of-a-package-with-pip

[Back](./)
