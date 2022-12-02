def main():
    for x in lines:
        print(x, sep="", end="")
    # code here


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    main()
