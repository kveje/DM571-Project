# DM571 - Projekt

Authors: Tan Nhat Lee, Nikolaj Dall, Emil Czepluch, Kasper Veje Jakobsen

The report can be read in the file "rapport.pdf"

The readme-file contains information on

- How to run the test code
- How to use the implemented prototype

## How to: Test

To use the test code in the project, follow the instructions.

- Make sure, that you have python (>= 3.8) installed

In your terminal, navigate to

- ..relative-path/DM571-Project/Python

Then you have the following possibilities

| Action                      | Code                                  |
| --------------------------- | ------------------------------------- |
| Run test                    | python -m coverage run -m unittest -v |
| Get coverage report         | python -m coverage report             |
| Get coverage report in html | python -m coverage html               |

## How to: Prototype

To run the prototype, follow the instructions.

- Make sure, that you have python (>= 3.8) and pip installed

In your terminal, navigate to

- ..relative-path/DM571-Project/Python

To install dependencies, run the following code

- pip install -r requirements.txt

Then, run the following code to start the flask server

- python main.py

Now, you can interact with the server on

- http://localhost:5000

To use the implemented GUI, simply open either "GUI/basket.html" or "GUI/products.html" in a browser (only tested on Chrome).
