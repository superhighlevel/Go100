def filterHmm():
    l = [1,2,3,4,5,6,7,8,9,10]
    test_filter= list(filter(lambda x: x%2==0, l))
    print(test_filter)
filterHmm()