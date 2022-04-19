from isograms import *

def test_IsItEmpty():
    assert IsItEmpty("") == True

def test_IsItEmpty1():
    assert IsItEmpty("apple") == False

def test_IsItAlphabetStr():
    assert IsItAlphabetStr("apple") == True

def test_IsItAlphabetStr1():
    assert IsItAlphabetStr("appl0") == False

def test_IsItAlphabetStr2():
    assert IsItAlphabetStr("carot") == True

def test_IsItAlphabetStr3():
    assert IsItAlphabetStr("c3r0t") == False

def test_UniqueChars():
    assert UniqueChars("melon") == True

def test_UniqueChars1():
    assert UniqueChars("apPle") == False

def test_IsItIsogram():
    assert IsItIsogram("melon") == True

def test_IsItIsogram1():
    assert IsItIsogram("kiwI") == False

def test_IsItIsogram2():
    assert IsItIsogram("") == True

def test_IsItIsogram3():
    assert IsItIsogram("ap4le") == False
