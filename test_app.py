from app import greeting

def test_greeting():
    assert greeting('AWS') == 'Hello, AWS!'
