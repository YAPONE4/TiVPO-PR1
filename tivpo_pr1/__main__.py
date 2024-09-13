from pathlib import Path
from tivpo_pr1.parser import Parser

path_to_input_file: Path = Path(Path.cwd(), "examples/input_example.txt")

with open(path_to_input_file) as f:
    a = Parser().parse(f)

