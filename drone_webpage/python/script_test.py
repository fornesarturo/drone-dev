def writeFlush(text):
    import sys
    sys.stdout.write(text)
    sys.stdout.flush()

def main():
    import random, time
    for x in range(15):
        writeFlush(str(random.randint(23,28)) + " C")
        time.sleep(0.5)
    writeFlush("SCRIPT ENDED")

if __name__ == '__main__':
    main()