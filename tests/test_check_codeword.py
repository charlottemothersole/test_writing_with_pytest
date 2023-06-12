from lib.check_codeword import * 

def test_check_codeword_with_horse() :
    result = check_codeword('horse')
    assert "Correct! Come in."

def test_check_codeword_with_nonsense() :
    result = check_codeword('nonsense')
    assert "WRONG!"

def test_check_codeword_with_house() :
    result = check_codeword('house')
    assert "Close, but nope."