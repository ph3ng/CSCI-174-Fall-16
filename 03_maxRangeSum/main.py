import sys

def main(input_file):
    with open(input_file, 'r') as fh:
        for line in fh:
            ln = line.strip()
            d = int(line.split(';')[0])
            arr = [int(x) for x in line.split(';')[1].split(' ')]
            max_sum = 0
            for i in range(0, len(arr)-d+1):
                max_sum = max(sum(arr[i:i+d]), max_sum)
            print(max_sum)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
