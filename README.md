# BigMac Price ASCII Plotter

## Overview

This Python script plots BigMac price data in ASCII format, providing a simple terminal-based visualization of price trends.

## Requirements

- Python 3.x
- JSON data file with price information

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


```bash
Dual-Scale Mode: Big Mac Prices (USD vs Satoshis)
Width: 58, Height: 15
     3.9│    [92m■[0m[92m■[0m                                               [91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m│4.7e+09   
     3.6│    [92m■[0m[92m■[0m[92m■[0m                                            [91m◆[0m[91m◆[0m[91m◆[0m    │4.4e+09   
     3.3│     [92m■[0m[92m■[0m                                          [91m◆[0m[91m◆[0m[91m◆[0m      │4.0e+09   
     3.0│      [92m■[0m[92m■[0m                                     [91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m        │3.7e+09   
     2.8│       [92m■[0m [92m■[0m                            [91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m            │3.4e+09   
     2.5│       [92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m             [91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m                   │3.0e+09   
     2.2│       [92m■[0m[92m■[0m  [92m■[0m[92m■[0m[92m■[0m    [91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m                               │2.7e+09   
     1.9│       [92m■[0m     [93m✦[0m[93m✦[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m                                       │2.4e+09   
     1.7│         [91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[92m■[0m[92m■[0m[92m■[0m                                         │2.0e+09   
     1.4│        [91m◆[0m[91m◆[0m    [92m■[0m [92m■[0m [92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m                                 │1.7e+09   
     1.1│    [91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m[91m◆[0m       [92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m  [92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m                             │1.3e+09   
     0.8│                [92m■[0m          [92m■[0m[92m■[0m[92m■[0m                            │1.0e+09   
     0.6│                             [92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m [92m■[0m[92m■[0m                  │6.7e+08   
     0.3│                              [92m■[0m[92m■[0m[92m■[0m[92m■[0m  [92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m    [92m■[0m[92m■[0m[92m■[0m[92m■[0m       │3.4e+08   
0.0e+00 │                               [92m■[0m         [92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m[92m■[0m [92m■[0m  │0.0e+00   
────────├──────────────────────────────────────────────────────────┤──────────
                                                                              

Legend:
[91m◆[0m -> USD
[92m■[0m -> Satoshis
[93m✦[0m -> Overlap

```

## Note

Prices are plotted using an inverted scale where 0 represents the highest price and 300 represents the lowest price.