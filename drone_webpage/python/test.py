def main():
    import random, time, sys
    for x in range(10):
        sys.stdout.write(str(random.randint(23,28)) + " C")
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    main()