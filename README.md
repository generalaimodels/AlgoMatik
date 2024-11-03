
# AlgoMatik

A command-line interface (CLI) application that uses the **GPT-4o-mini** model (via `g4f.client` API) to process complex mathematical questions into step-by-step pseudo-algorithms. This tool is designed to help users breakdown intricate math problems into structured, easy-to-understand steps.

## Features
- Converts complex math questions into pseudo-algorithms.
- Implements "chain of thoughts" methodology for clearer breakdown.
- Logs errors for troubleshooting.

# Using below 
"gpt4free" serves as a PoC (proof of concept), demonstrating the development of an API package with multi-provider requests, with features like timeouts, load balance and flow control.
more  info [g4f.client](https://github.com/g4f-client) library

## Installation
Clone the repository and install the necessary dependencies:
```bash
git clone https://github.com/generalaimodels/AlgoMatik.git
cd AlgoMatik
pip install -r requirements.txt
```

## Usage
Run the application from the command line with your mathematical question as an argument:
```bash
python app.py "Your complex mathematical question here"
```

### Example
```bash
python app.py "What are the steps to solve a quadratic equation?"
```

The application will process the question and print a step-by-step pseudo-algorithm.

## Logging
Error logs are displayed in the console for easier debugging.


