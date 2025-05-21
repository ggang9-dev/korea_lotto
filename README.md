# Korean Lottery Store Crawler

This project consists of Python scripts that crawl the dhlottery.co.kr website to gather information about lottery stores. It can find stores that sold winning tickets for specific draws and list all available lottery store locations across different regions in South Korea.

## `get_lotto_winning_store.py`

This script finds and lists lottery stores that sold 1st and 2nd place winning tickets for a specific lottery draw number.

**Usage:**

```bash
python get_lotto_winning_store.py
```

By default, it fetches the latest draw results. You can modify the script to specify a particular draw number if needed.

**Output:**

The script prints the draw number, followed by a list of 1st prize winning stores (name, type of win - e.g., automatic/manual, address) and 2nd prize winning stores (name, address).

## `get_store_info.py`

This script crawls the lottery website to gather information about all registered lottery store locations across various regions in South Korea.

**Usage:**

```bash
python get_store_info.py
```

**Output:**

The script prints a list of lottery stores, including their name, phone number (if available), full address, and geographical coordinates (latitude and longitude). The output is grouped by region.

## Dependencies

This project relies on several Python libraries. The dependencies are listed in the `requirements.txt` file.

To install them, you can use pip:

```bash
pip install -r requirements.txt
```

## How to Use

1.  **Clone the repository (if you haven't already):**
    ```bash
    # If you have git installed
    git clone <repository_url>
    cd <repository_directory>
    ```
    Alternatively, download the script files (`get_lotto_winning_store.py`, `get_store_info.py`, `requirements.txt`) into a directory on your computer.

2.  **Install dependencies:**
    Open your terminal or command prompt, navigate to the project directory, and run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the scripts:**
    *   To find winning stores for the latest draw:
        ```bash
        python get_lotto_winning_store.py
        ```
    *   To get a list of all lottery stores by region:
        ```bash
        python get_store_info.py
        ```

## Data Source

The information provided by these scripts is crawled from the official Korean lottery website: [dhlottery.co.kr](https://dhlottery.co.kr).
