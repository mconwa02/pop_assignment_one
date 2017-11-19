import LunarLander
import unittest

def test_lundarLander_for20a20f():
        answer = LunarLander.my_game(20.0, 0.0 , 20.0)
        print(answer)

def test_lundarLander_for1000a1000f():
        answer = LunarLander.my_game(1000.0, 0.0 , 1000.0)
        print(answer)

def test_lundarLander_for100a100f():
        answer = LunarLander.my_game(100.0, 0.0 , 100.0)
        print(answer)

def test_lundarLander_for1000a10f():
        answer = LunarLander.my_game(1000.0, 0.0 , 10.0)
        print(answer)
				
#run tests
if __name__ == '__main__':
    unittest.main()
