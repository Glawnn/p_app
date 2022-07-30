from p_app.p_app import P_app

def test_init_p_app():
    app = P_app()
    assert app.debug == False
    assert app.log_file == True