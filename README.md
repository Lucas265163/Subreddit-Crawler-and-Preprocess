# Laptop Subreddit Scraper

This project is designed to scrape comments from the laptop subreddit for the years 2022 to 2024. It provides a structured approach to gather, process, and analyze user comments related to laptops.

## Project Structure

```
laptop-subreddit-scraper
├── src
│   ├── scraper.py          # Main logic for scraping comments
│   ├── reddit_client.py    # Handles Reddit API connection
│   ├── config.py           # Configuration settings
│   ├── utils.py            # Utility functions for data processing
│   └── notebooks
│       └── spider.ipynb    # Jupyter notebook for data analysis
├── data
│   ├── raw                 # Directory for raw scraped data
│   └── processed           # Directory for processed data
├── tests
│   └── test_scraper.py     # Unit tests for the Scraper class
├── .env.example            # Template for environment variables
├── .gitignore              # Files and directories to ignore by Git
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd laptop-subreddit-scraper
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables by copying `.env.example` to `.env` and filling in the necessary API keys.

## Usage

To run the scraper, execute the following command:
```
python src/scraper.py
```

This will initiate the scraping process and store the raw data in the `data/raw` directory. After processing, the cleaned data will be saved in the `data/processed` directory.

## Testing

To run the unit tests for the Scraper class, use:
```
python -m unittest tests/test_scraper.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.# Subreddit-Crawler-and-Preprocess
