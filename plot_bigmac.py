import json
from typing import List, Tuple
from plot import draw_ascii_graph, scale_data  # Import only the functions you need

def load_bigmac_data(filename: str) -> tuple[List[Tuple[float, float]], List[Tuple[float, float]], int, int, int]:
    """
    Load normalized graph data and convert back to original price scales.
    Adjusts prices for ASCII rendering where lower values represent lower prices.
    Returns USD data, Satoshi data, width, height, and space_diff.
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        # Extract relevant fields
        time_array = data['X1Array']  # Unix timestamps
        normalized_usd_prices = data['Y1Array']  # Normalized USD prices
        normalized_satoshi_prices = data['Y1ArraySatoshi']  # Normalized Satoshi prices
        
        # Denormalization factors
        max_usd_price = data['MaxPrice']
        max_satoshi_price = data['MaxPriceSatoshi']
        
        # Denormalize prices 
        # Original format: 0 is highest, 300 is lowest
        # We want to convert to actual price values
        usd_prices = [
            (300 - price) / 300 * max_usd_price if max_usd_price is not None else (300 - price)
            for price in normalized_usd_prices
        ]
        
        satoshi_prices = [
            (300 - price) / 300 * max_satoshi_price if max_satoshi_price is not None else (300 - price)
            for price in normalized_satoshi_prices
        ]
        
        # Extract chart dimensions and space difference
        size_width = data.get('SizeWidth', 700)
        size_height = data.get('SizeHeight', 400)
        space_diff = data.get('SpaceDiff', 50)
        
        # Create paired datasets with original prices
        usd_data = list(zip(time_array, usd_prices))
        satoshi_data = list(zip(time_array, satoshi_prices))
        
        return usd_data, satoshi_data, size_width, size_height, space_diff
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return [], [], 700, 400, 50
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'")
        return [], [], 700, 400, 50
    except KeyError as e:
        print(f"Error: Missing expected key in JSON: {e}")
        return [], [], 700, 400, 50

def adjust_dimensions(width: int, height: int, space_diff: int) -> tuple[int, int]:
    """
    Adjust JSON width and height to fit ASCII graph, considering SpaceDiff and bounds (50-650, 50-350).
    """
    # Target ASCII dimensions (to match expected output)
    max_ascii_width = 58  # Matches the expected output width
    max_ascii_height = 15  # Matches the expected output height
    
    # Scale based on actual graph bounds (650-50=600, 350-50=300 effective range)
    width_scale = (650 - 50) / width  # Effective width range / JSON width
    height_scale = (350 - 50) / height  # Effective height range / JSON height
    
    # Apply scaling without dividing by space_diff, as it's not needed for ASCII scaling
    adjusted_width = int(width * width_scale)
    adjusted_height = int(height * height_scale)
    
    # Ensure the dimensions are within bounds
    adjusted_width = max(20, min(max_ascii_width, adjusted_width))
    adjusted_height = max(10, min(max_ascii_height, adjusted_height))
    
    return adjusted_width, adjusted_height

def main():
    # Load data from JSON
    usd_data, satoshi_data, size_width, size_height, space_diff = load_bigmac_data('data_btc_bigmac.json')
    
    if not usd_data or not satoshi_data:
        print("Failed to load data. Please check the JSON file.")
        return
    
    # Adjust dimensions for ASCII graph
    width, height = adjust_dimensions(size_width, size_height, space_diff)
    
    # Draw the graph in dual mode
    print(f"Dual-Scale Mode: Big Mac Prices (USD vs Satoshis)\nWidth: {width}, Height: {height}")
    draw_ascii_graph(
        datasets=[usd_data, satoshi_data],
        width=width,
        height=height,
        mode="dual",
        left_label="USD",
        right_label="Satoshis"
    )

if __name__ == "__main__":
    main()