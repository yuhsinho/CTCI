import ch1


def test1():
    print(ch1.is_unique_string('abc'))
    # output should be true

def test2():
    print(ch1.is_unique_string('aba'))
    # output should be false

def test3():
    print(ch1.is_unique_string(''))
    # output should be true



def main():
    test1()
    test2()
    test3()

if __name__== '__main__':
  main()
