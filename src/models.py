import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import joblib

class LSTMForecaster:
    def __init__(self, config):
        self.config = config
        self.model = None
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def prepare_data(self, prices_df):
        """Logic to create windows (X, y) from Week 9."""
        # We will insert your specific Week 9 window logic here
        pass

    def build_model(self, input_shape):
        """Refactored Week 9 Model Architecture."""
        model = Sequential([
            LSTM(units=50, return_sequences=True, input_shape=input_shape),
            Dropout(0.2),
            LSTM(units=50, return_sequences=False),
            Dropout(0.2),
            Dense(units=25),
            Dense(units=1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        self.model = model
        return model
