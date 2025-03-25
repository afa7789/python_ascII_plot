# plot.py

import math

# High ASCII slope characters
SLOPE_CHARS = ["─", "╌", "╱", "╲", "│", "╴", "╶", "▲", "▼", "├", "┤"]
COLORS = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
RESET = "\033[0m"

def choose_char(slope):
    if slope == 0:
        return SLOPE_CHARS[0]
    elif slope > 0:
        if 0 < slope < 0.1:
            return SLOPE_CHARS[1]
        elif 0.1 <= slope < 0.5:
            return SLOPE_CHARS[5]
        elif 0.5 <= slope < 1:
            return SLOPE_CHARS[2]
        elif 1 <= slope < 2:
            return SLOPE_CHARS[7]
        elif slope >= 2:
            return SLOPE_CHARS[4]
    else:
        slope = abs(slope)
        if 0 < slope < 0.1:
            return SLOPE_CHARS[1]
        elif 0.1 <= slope < 0.5:
            return SLOPE_CHARS[6]
        elif 0.5 <= slope < 1:
            return SLOPE_CHARS[3]
        elif 1 <= slope < 2:
            return SLOPE_CHARS[8]
        elif slope >= 2:
            return SLOPE_CHARS[4]
    return SLOPE_CHARS[2]

def scale_data(data, width, height, max_y_val=float('inf')):
    max_x = max(x for x, y in data) if data else 1
    max_y = min(max(y for x, y in data), max_y_val) if data else 1
    if max_x == 0 or max_y == 0:
        return [(0, 0)] * len(data)
    return [(int(round((x / max_x) * (width - 1))), int(round((y / max_y) * (height - 1)))) for x, y in data]

def format_label(value, max_len=8):
    if abs(value) > 99999 or abs(value) < 0.01:
        return f"{value:.1e}"[:max_len]
    return f"{value:>8.1f}"[:max_len]

def draw_ascii_graph(datasets, width=58, height=15, mode="single", left_label="Value", right_label="Other"):
    if mode == "dual" and len(datasets) != 2:
        print("Dual-Scale Mode requires exactly two datasets.")
        return
    
    total_width = width + 20 if mode == "dual" else width + 12
    graph = [[" " for _ in range(total_width)] for _ in range(height + 2)]
    
    # Max X for all datasets
    all_x = [x for data in datasets for x, y in data]
    max_x = max(all_x) if all_x else 1
    
    # Fixed label width to ensure alignment
    label_width = 8  # Matches max_len in format_label
    
    if mode == "single":
        max_y = max(y for data in datasets for x, y in data) if datasets else 1
        for y in range(height):
            label = format_label(max_y * (height - y - 1) / (height - 1))
            for i in range(label_width):
                graph[y][i] = label[i] if i < len(label) else " "
            graph[y][label_width] = "│"
        graph[height] = ["─" for _ in range(total_width)]
        graph[height][label_width] = "┴"
        x_labels = [format_label(max_x * x / (width - 1)) for x in range(0, width, width // 5)]
        for i, label in enumerate(x_labels):
            x_pos = label_width + i * (width // 5)
            for j, char in enumerate(label):
                if x_pos + j < total_width:
                    graph[height + 1][x_pos + j] = char
    # In the dual-scale mode section (else branch):
    else:  # Dual-Scale Mode
        max_y_left = max(y for x, y in datasets[0]) if datasets[0] else 1
        max_y_right = max(y for x, y in datasets[1]) if datasets[1] else 1
        
        # Calculate right border position
        right_border_pos = width + label_width + 1
        
        for y in range(height):
            # Left label
            label = format_label(max_y_left * (height - y - 1) / (height - 1))
            for i in range(label_width):
                graph[y][i] = label[i] if i < len(label) else " "
            graph[y][label_width] = "│"
            
            # Right label
            label = format_label(max_y_right * (height - y - 1) / (height - 1))
            for i in range(label_width):
                # Position right labels starting after right border
                pos = right_border_pos + 1 + i
                if pos < total_width:
                    graph[y][pos] = label[i] if i < len(label) else " "
            graph[y][right_border_pos] = "│"  # Fixed right border

        # Draw horizontal line
        graph[height] = ["─" for _ in range(total_width)]
        graph[height][label_width] = "├"
        graph[height][right_border_pos] = "┤"
        
    # Plot datasets
    symbols = ["◆", "■", "▲", "●", "★", "◇"]
    for idx, data in enumerate(datasets):
        max_y = max_y_left if idx == 0 else max_y_right
        scaled_data = scale_data(data, width, height, max_y)
        symbol = symbols[idx % len(symbols)]
        color = COLORS[idx % len(COLORS)]
        
        for i in range(1, len(scaled_data)):
            x1, y1 = scaled_data[i - 1]
            x2, y2 = scaled_data[i]
            
            # Constrain x positions to stay within borders
            x1 = min(x1, width - 1)
            x2 = min(x2, width - 1)
            
            slope = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
            char = choose_char(slope)
            
            # Plot points ensuring they stay within borders
            for x, y in [(x1, y1), (x2, y2)]:
                col = x + label_width + 1
                if col > right_border_pos:  # Don't plot beyond right border
                    continue
                row = height - y - 1
                if 0 <= row < height and 0 <= col < total_width:
                    current = graph[row][col]
                    if current == " " or current in SLOPE_CHARS:
                        graph[row][col] = f"{color}{symbol}{RESET}"
                    elif current != f"{color}{symbol}{RESET}":
                        graph[row][col] = f"{COLORS[idx+1%len(COLORS)]}✦{RESET}"  # Bright yellow
            
            # Plot connecting lines
            dx, dy = abs(x2 - x1), abs(y2 - y1)
            steps = max(dx, dy)
            for step in range(1, steps):
                intermediate_x = x1 + (x2 - x1) * step / steps
                intermediate_y = y1 + (y2 - y1) * step / steps
                col = int(round(intermediate_x)) + label_width + 1
                if col > right_border_pos:  # Don't plot beyond right border
                    continue
                row = height - int(round(intermediate_y)) - 1
                if 0 <= row < height and 0 <= col < total_width:
                    current = graph[row][col]
                    if current == " ":
                        graph[row][col] = f"{color}{char}{RESET}"

    
    # Render
    for row in graph:
        print("".join(row[:80]))
    
    # Legend
    print("\nLegend:")
    if mode == "single":
        for idx, data in enumerate(datasets):
            symbol = symbols[idx % len(symbols)]
            color = COLORS[idx % len(COLORS)]
            print(f"{color}{symbol}{RESET} -> Dataset {idx + 1} ({left_label})")
    else:
        print(f"{COLORS[0]}{symbols[0]}{RESET} -> {left_label}")
        print(f"{COLORS[1]}{symbols[1]}{RESET} -> {right_label}")
        print(f"{COLORS[2]}✦{RESET} -> Overlap")

def tester():
    # Single-Scale Mode: Multiple USD prices
    data1 = [(1, 1), (4, 5000), (7, 8000), (10, 10000), (15, 12000)]
    data2 = [(1, 3000), (3, 4000), (5, 7000), (7, 6000), (10, 5000)]
    data3 = [(1, 10000), (3, 8000), (5, 6000), (7, 4000), (10, 2000)]
    print("Single-Scale Mode:")
    draw_ascii_graph([data1, data2, data3], mode="single", left_label="USD")

    print("\n" + "="*50 + "\n")

    # Dual-Scale Mode: USD vs EUR
    usd_prices = [(1, 100), (4, 150), (7, 200), (10, 180), (15, 220)]
    eur_prices = [(1, 10000), (3, 8000), (5, 6000), (7, 4000), (10, 2000)]
    print("Dual-Scale Mode:")
    draw_ascii_graph([usd_prices, eur_prices], mode="dual", left_label="USD", right_label="EUR")
# if __name__ == "__main__":
#     tester()