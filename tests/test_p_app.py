import pytest
from p_app.p_app import P_app
import sys

class Test_P_app:
    @pytest.mark.parametrize("log_file, result", [(True, True), (False, False)])
    def test_init_p_app(self, log_file, result):
        if '-v' in sys.argv:
            sys.argv.remove('-v')
        #sys.argv.append('-d')
        app = P_app(log_file)
        assert app.log_file == result

    def test_debug_mode_true(self):
        if '-v' in sys.argv:
            sys.argv.remove('-v')
        sys.argv.append('-d')
        app = P_app()
        assert app.args.debug == True
                
    def test_debug_mode_false(self):
        if '-v' in sys.argv:
            sys.argv.remove('-v')
        if '-d' in sys.argv:
            sys.argv.remove('-d')
        app = P_app()
        assert app.args.debug == False

    def test_without_load_config_file(self):
        if '-v' in sys.argv:
            sys.argv.remove('-v')
        #sys.argv.append('-cf "test_config.json"')
        app = P_app()
        assert app.load_config_file() == None
    
    def test_with_load_config_file(self):
        if '-v' in sys.argv:
            sys.argv.remove('-v')
        sys.argv.append('-cf')
        sys.argv.append('tests/test_config.json')
        app = P_app()
        assert app.load_config_file() == {'hello': 'world'}

    def test_load_args(self):
        app = P_app()
        assert app.load_args() == {'config_file': 'tests/test_config.json', 'debug': False}


