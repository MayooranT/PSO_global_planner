import matplotlib.pyplot as plt
import pandas as pd
import glob

def plot_csv_files(directory, file_pattern="*.csv"):
    """
    Reads multiple CSV files from a directory and plots their values in a single figure.

    Parameters:
    - directory (str): Path to the directory containing the CSV files.
    - file_pattern (str): File pattern to match (default: "*.csv").
    """
    # Use glob to find all CSV files matching the pattern in the specified directory
    files = glob.glob(f"{directory}/{file_pattern}")
    
    if not files:
        print("No CSV files found.")
        return

    plt.figure(figsize=(10, 6))  # Set figure size

    for file in files:
        # Read the single-column CSV file
        data = pd.read_csv(file, header=None)
        
        # Ensure the file has only one column
        if data.shape[1] != 1:
            print(f"Skipping {file}: file does not have a single column.")
            continue

        # Plot the data
        plt.plot(data[0], label=file.split("/")[-1])  # Use file name as label
    
    plt.xlabel("Consecutive plan updates")
    plt.ylabel("Best Particle fitness")
    plt.title("particle initialisation method")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage
plot_csv_files("/home/mayooran/Documents/ece788/src/pso_global_planner/presentation/init_pos_mode")
