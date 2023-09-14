class TestUI:

    def test_ui_upper(self):
        assert 'foo'.upper() == 'FOO'

    def test_ui_isupper(self):
        assert 'FOO'.isupper()
