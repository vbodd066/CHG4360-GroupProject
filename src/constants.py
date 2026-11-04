# =======================================================================
# CONSTANTS
# Define constant values that do not change throughout your program.
# =======================================================================

# Path to Dataset
DATASET = "datasets/dataset_cell_growth_7factor.csv"

# Features and target column names in raw dataset
FEATURES = ["Temperature [C]","pH","Glucose [mM]","Glutamine [mM]","Lactate [mM]","Ammonia [mM]","Viable Cell Density [cells/mL]"]
TARGET = ["Specific Growth Rate [d^-1]","Specific Death Rate [d^-1]","Specific Production Rate [pg cell^-1 d^-1]"]

# Train-Test split
TEST_SIZE = 0.2
RANDOM_STATE = 41








