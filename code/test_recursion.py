from recursion import is_palindrome


def test_is_palindrome():
    assert is_palindrome('') is True
    assert is_palindrome('a') is True
    assert is_palindrome('abba') is True
    assert is_palindrome('abbab') is False
    assert is_palindrome('kanak') is True
    assert is_palindrome('123123') is False
