# Hist Painting Python

## Description
The Hist Painting program creates a visually appealing dot art design using the Python Turtle module. It generates a grid of dots in various colors, creating a vibrant and dynamic pattern.

## Features
- Random selection of colors from a predefined list.
- Customizable dot size and spacing.
- Automatically exits when the screen is clicked.

## Usage
1. Ensure you have Python installed on your system.
2. Run the program using a Python interpreter.
3. Click anywhere on the Turtle graphics window to exit the program.

## Requirements
- Python 3.x
- Turtle module (standard library in Python)

## Instructions
1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the Python script.
3. Run the script using the command `python turtle_dot_art.py`.
4. Follow the on-screen instructions, and enjoy the visual display.
5. Click anywhere on the screen to exit the program.

## Customization
- You can adjust the dot size by changing the first argument of the `dot()` function.
- Modify the `colors_list` variable to include your preferred color palette.
- Alter the loop parameters to change the number of dots and their arrangement.

## Example
```python
# Increase dot size
tim.dot(20, random.choice(colors_list))

# Add more colors to the palette
colors_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Change the number of dots
for dot_count in range(1, 50):
    # Your code here
```

## Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to fork the repository and submit a pull request.

## Credits
Developed by Philip Matthew.
Inspired by Python Turtle module and Angela yu's App brewery.

## Acknowledgments
Special thanks to the Python Turtle module developers and the open-source community for providing such a fun and educational tool.
Inspiration drawn from various Turtle graphics projects and artistic endeavors.

Enjoy creating beautiful art with Python Turtle Dot Art! 🐢🎨
