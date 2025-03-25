# BigMac Price ASCII Plotter

## Overview

This Python script plots BigMac price data in ASCII format, providing a simple terminal-based visualization of price trends.

## Requirements

- Python 3.x
- JSON data file with price information ( gotted it from my other project: https://afa7789.github.io/satsukashii/ )

## Usage

```bash
python3 plot_bigmac.py
```

## Dependencies

- `plot.py` (custom plotting module)
- Standard Python libraries

## Data Format

The script expects a JSON file containing:
- `X1Array`: Unix timestamps
- `Y1Array`: Normalized USD prices
- `Y1ArraySatoshi`: Normalized Satoshi prices
- `MaxPrice`: Maximum USD price
- `MaxPriceSatoshi`: Maximum Satoshi price

## How It Works

1. Loads price data from a JSON file
2. Converts normalized prices to actual price values
3. Renders an ASCII graph of price trends

## Example Output


<img width="545" alt="image" src="https://github.com/user-attachments/assets/ab7c458c-c787-4534-9acb-07fdcbf11acf" />


## Note

Prices are plotted using an inverted scale where 0 represents the highest price and 300 represents the lowest price.
