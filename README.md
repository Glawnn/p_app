# p_app

## Install
```bash
sudo apt install make
make install
```

## Use
Create your python class (me in test.py)
```python
from p_app.p_app import P_app


class my_class(P_app):
    def __init__(self, ) -> None:
        super().__init__(True) # True if you want output log

        self.argsparser.add_argument("-i", "--input", help="Input file.")
        self.args_cmd = self.load_args()
        self.args_file = self.load_config_file()

        self.logger.info(self.args_cmd)
        self.logger.debug(self.args_file)


mc = my_class()

```
```bash
> python test.py
> 2022-07-30 17:32:21,633 - INFO - {'debug': False, 'config_file': None, 'input': None}
```
```bash
> python test.py -d
> 2022-07-30 17:32:28,173 - INFO - {'debug': True, 'config_file': None, 'input': None}
> 2022-07-30 17:32:28,173 - DEBUG - None
```

