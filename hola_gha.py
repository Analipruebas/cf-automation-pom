import os

def main():
    name = os.getenv("USERNAME")
    print(f"Hola {name}! Estoy en Github Actions!git add")


if __name__ == "__main__":
    main()