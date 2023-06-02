import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError) as errorMessage:
        encrypt_message(None, 5)
    assert str(errorMessage.value) == "tipo inválido para message"

    with pytest.raises(TypeError) as erroKey:
        encrypt_message("testes", None)
    assert str(erroKey.value) == "tipo inválido para key"

    assert encrypt_message("Stariel", 7) == "leiratS"
    assert encrypt_message("Stariel", 2) == "leira_tS"
    assert encrypt_message("Stariel", 4) == "lei_ratS"
    assert encrypt_message("Stariel", 9) == "leiratS"
