# cli.py
import argparse
#from my_cli_tool.core import add

def main():
    parser = argparse.ArgumentParser(description="File forensics tools.")
    parser.add_argument("x", type=int, help="The first number")
    parser.add_argument("y", type=int, help="The second number")
    parser.add_argument("--add", action="store_true", help="Add the numbers")

    args = parser.parse_args()

    if args.add:
        result = add(args.x, args.y)
        print(f"The result is: {result}")

if __name__ == "__main__":
    main()
