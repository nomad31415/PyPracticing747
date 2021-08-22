if __name__ == '__main__':
    for h in range(10):
        for p in range(50):
            for r in range(100):
                if (10*h + 3*p + 0.5 * r == 100) and (h + p + r == 100):
                    print(h,p,r)
    print("end............")                

