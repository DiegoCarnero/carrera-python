import typer


def main(name: str, a="AA"):
    print(f"Hello {name} {a}")


if __name__ == "__main__":
    typer.run(main)
