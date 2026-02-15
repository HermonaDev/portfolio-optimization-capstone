import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from typing import Tuple, Optional
import joblib
import os

class LSTMForecaster:
    """Refactored Week 9 LSTM logic into a production-ready class."""
    
    def __init__(self, window_size: int = 60):
        self.window_size = window_size
        self.model: Optional[Sequential] = None
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def create_sequences(self, data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        X, y = [], []
        for i in range(self.window_size, len(data)):
            X.append(data[i-self.window_size:i, 0])
            y.append(data[i, 0])
        return np.array(X), np.array(y)

    def build_model(self, input_shape: Tuple[int, int]):
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

    def train(self, data: pd.Series, epochs: int = 5, batch_size: int = 32):
        scaled_data = self.scaler.fit_transform(data.values.reshape(-1, 1))
        X, y = self.create_sequences(scaled_data)
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))
        
        if self.model is None:
            self.build_model((X.shape[1], 1))
            
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=0)
        return self.model
