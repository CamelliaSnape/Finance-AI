import sys
from predictor import FinancePredictor

def main():
    try:
        predictor = FinancePredictor()
        print("AI Predictor Engine initialized successfully.")
    except Exception as e:
        print(f"Initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()