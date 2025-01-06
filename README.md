# DPP Project

Authors: Przemysław Ćwięk, Julia Duch, Hubert Głąb, Magda Jaźwińska

📚 Project Overview

The DPP Project is a Python-based solution aimed at solving graph-related problems and providing efficient graph visualization and shortest path calculations. This project was developed as part of a group collaboration to explore advanced concepts in graph theory and practical implementations using Python libraries.

🚀 Features

Graph Visualization: A set of functions to visualize graphs with nodes and edges.

Shortest Path Calculation: Implementation of algorithms to find the shortest path between nodes in a graph.

Automated Testing: Includes unit tests to ensure functionality and robustness.

CI/CD Integration: Configured GitHub Actions workflow for automated testing and continuous integration.

🛠️ Installation

Clone the repository:

git clone https://github.com/juliaduch/dpp_projekt.git
cd dpp_projekt

Create a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

🧩 Usage

Functions

functions.py:

Implements the core graph algorithms and visualization utilities.

Example:

from functions import visualize_graph, calculate_shortest_path

Your graph as an adjacency list or matrix
graph = {...}

Visualize the graph
visualize_graph(graph)

Calculate shortest path
shortest_path = calculate_shortest_path(graph, start_node, end_node)
print(shortest_path)

test_functions.py:

Contains unit tests for functions in functions.py.

Run the tests:

pytest test_functions.py

🌐 Key Files

functions.py: Main Python file containing graph algorithms and utilities.

test_functions.py: Unit tests for the project.

requirements.txt: Dependencies for the project, including:

networkx

matplotlib

.github/workflows/ci.yml: GitHub Actions workflow for continuous integration.

🛆 Dependencies

The project relies on the following libraries:

networkx: For graph creation and manipulation.

matplotlib: For graph visualization.

Install all dependencies using:

pip install -r requirements.txt

🛡️ Testing

Unit tests are included in the test_functions.py file. To run the tests, use:

pytest

🌐 CI/CD

The project uses GitHub Actions for automated testing:

Workflow file: .github/workflows/ci.yml

Triggers tests for every pull request and push to the main branch.

📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.

