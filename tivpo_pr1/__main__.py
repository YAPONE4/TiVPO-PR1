from pathlib import Path
from tivpo_pr1.grid_objects.objects import GridObject
from tivpo_pr1.parser import Parser
from turtle import *
from tivpo_pr1.Printer import * 

path_to_input_file: Path = Path(Path.cwd(), "examples/input_example.txt")

symbols: list[GridObject]
with open(path_to_input_file) as f:
    symbols = Parser().parse(f)

for symbol in symbols:
    print(f"{symbol.symbol} at line {symbol.line_num} at index {symbol.index}")


printer:Printer = Printer()
'''printer.drawArrowLeft(1, 1)
printer.drawArrowRight(0, 1)
printer.drawArrowLeftRight(0, 2)
printer.drawArrowLeftRight(1, 2)
printer.drawCircle(2, 2)
printer.drawSquare(0, 3)
printer.drawArrowLeft(1, 3)
printer.drawCircle(2, 1)
printer.drawArrowLeftRight(3, 1)
printer.drawArrowLeft(3, 2)'''
printer.drawWholePicture(symbols)
printer.showScreen()
