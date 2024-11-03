#!/usr/bin/env python3
"""
Command-Line Interface Application for Processing Complex Mathematical Questions
Using GPT-4o-mini  Model via g4f.client API
"""

import sys
import argparse
import asyncio
from typing import Optional
from g4f.client import Client
import logging

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr)
    ]
)


if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
class MathQuestionProcessor:
    """
    A processor that interacts with GPT-4o-mini model to convert
    complex mathematical questions into pseudo-algorithms.
    """

    def __init__(self, model: str = "gpt-4o-mini") -> None:
        """
        Initializes the MathQuestionProcessor with the specified model.

        Args:
            model (str): The model name to use for completions.
        """
        self.client = Client()
        self.model = model

    def generate_pseudo_algorithm(self, question: str) -> Optional[str]:
        """
        Generates a pseudo-algorithm from a complex mathematical question.

        Args:
            question (str): The complex mathematical question.

        Returns:
            Optional[str]: The generated pseudo-algorithm or None if failed.
        """
        try:
            messages = [
                {"role": "user", "content": f"Please provide a step-by-step pseudo-algorithm using chain of thoughts for the following mathematical problem:\n\n{question}"}
            ]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=15000,
                temperature=0.9,
                n=1,
                stop=None
            )
            if response and response.choices:
                return response.choices[0].message.content.strip()
            else:
                logging.error("No response received from the API.")
                return None
        except Exception as e:
            logging.error(f"An error occurred while generating pseudo-algorithm: {e}")
            return None

def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Process complex mathematical questions into pseudo-algorithms."
    )
    parser.add_argument(
        'question',
        type=str,
        help='A complex mathematical question to process.'
    )
    return parser.parse_args()

def main() -> None:
    """
    The main function that orchestrates the CLI application.
    """
    args = parse_arguments()
    processor = MathQuestionProcessor()

    print("Processing your mathematical question. Please wait...\n")
    pseudo_algorithm = processor.generate_pseudo_algorithm(args.question)

    if pseudo_algorithm:
        print("Generated Pseudo-Algorithm:\n")
        print(pseudo_algorithm)
    else:
        print("Failed to generate pseudo-algorithm. Please check the logs for more details.")

if __name__ == "__main__":
    main()