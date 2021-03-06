# GF Live2D Decrypter
> C# to Python 3

## Install
```
python setup.py install
```

## Usage
```python
import gflive2d

with open('model.moc.txt', 'rb') as f:
    data = gflive2d.decrypt(f.read())
with open('model.moc', 'wb') as f:
    f.write(data)
```

**Extension Change Guide**
* .moc.txt → .moc
* .mtn.txt → .mtn
* .txt → .json

```python
# This code is an example and is not included within the module.
def extensionChanger(ext):
    return {
        'moc.txt': 'moc',
        'mtn.txt': 'mtn',
        'txt': 'json'
    }.get(ext, ext)

filename = 'model.moc.txt'
filename, extension = filename.split('.', 1)
extension = extensionChanger(extension)
# filename='model', extension='moc'
```

## Source
版权属于: Perfare's Blog
原文地址: https://www.perfare.net/1162.html

## License
[MIT](https://github.com/KOZ39/GF-Live2D-Decrypter/blob/master/LICENSE)