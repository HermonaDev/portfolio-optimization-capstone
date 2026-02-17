import shap
import numpy as np
import matplotlib.pyplot as plt
import os

class ModelExplainer:
    def __init__(self, model, background_data):
        self.model = model
        # Use a subset of data for faster SHAP calculation
        self.explainer = shap.GradientExplainer(self.model, background_data[:50])

    def explain(self, test_data):
        shap_values = self.explainer.shap_values(test_data)
        
        plt.figure(figsize=(10, 6))
        # Plotting the SHAP values for the most recent window
        shap.summary_plot(shap_values[0][:,:,0], plot_type="bar", show=False)
        plt.title("Feature Importance (Lags) explaining the Portfolio rebalance")
        plt.tight_layout()
        os.makedirs("reports", exist_ok=True)
        plt.savefig("reports/shap_summary.png")
        return shap_values
