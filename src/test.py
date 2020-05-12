import metodosComunes

def test_verificadorNumero():
    assert metodosComunes.verificadorNumero("5") == True
    assert metodosComunes.verificadorNumero("4") == True
    assert metodosComunes.verificadorNumero("3") == True
    assert metodosComunes.verificadorNumero("2") == True
    assert metodosComunes.verificadorNumero("1") == True
    assert metodosComunes.verificadorNumero("0") == True


