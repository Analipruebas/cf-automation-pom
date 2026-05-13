import os

def main():
    name = os.getenv("USERNAME")
    print(f"Hola {name}! Estoy en Github Actions")


if __name__ == "__main__":
    main()