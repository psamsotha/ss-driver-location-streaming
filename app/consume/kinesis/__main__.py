import sys

from app.consume.kinesis.main import main


if __name__ == '__main__':
    main(sys.argv[1:])
