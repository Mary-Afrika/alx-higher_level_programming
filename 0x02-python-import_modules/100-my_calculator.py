if __name__ == "__main__":
    ac = len(sys.argv) - 1
    if ac != 3:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
