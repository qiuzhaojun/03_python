def test_gen():
    for i in range(5):
        yield
        print("---")

gen = test_gen()
iter = gen.__iter__()
