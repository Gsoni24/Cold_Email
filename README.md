# Cold Mail Generator

## Installation

To use the Cold Mail Generator, you'll need to have the following dependencies installed:

- Python 3.7 or later
- Streamlit
- langchain-community

You can install the required dependencies using pip:

```
pip install streamlit langchain-community
```

## Usage

To run the Cold Mail Generator, execute the `main.py` file:

```
python main.py
```

This will start the Streamlit application. You can then enter a URL in the input field and click the "Submit" button to generate cold emails based on the content of the webpage.

## API

The Cold Mail Generator uses the following functions:

`create_streamlit_app(llm, clean_text)`:
- This function sets up the Streamlit application and handles the user input and email generation.
- `llm` is an instance of the `Chain` class, which is responsible for extracting job information and generating the cold emails.
- `clean_text` is a function from the `utils.py` file that cleans the text content of the webpage.

`clean_text(text)`:
- This function takes the raw text content of a webpage and performs the following cleaning operations:
  - Removes HTML tags
  - Removes URLs
  - Removes special characters
  - Replaces multiple spaces with a single space
  - Trims leading and trailing whitespace
  - Removes extra whitespace

## Contributing

If you would like to contribute to the Cold Mail Generator, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Submit a pull request to the main repository

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

To run the tests for the Cold Mail Generator, you can use the following command:

```
python -m unittest discover tests
```

This will run all the tests located in the `tests` directory.
