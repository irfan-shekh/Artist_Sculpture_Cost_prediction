#!/usr/bin/env python
"""
Test script for Artist Sculpture Cost Prediction ML model.
Run directly via: python test_models.py
"""
import os
import sys
import pickle
import pandas as pd
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def test_artist_model():
    print("🎨 Testing Artist Sculpture Cost Prediction ML Model")
    print("=" * 55)

    base_dir = Path(__file__).resolve().parent
    model_path = base_dir / 'mysite' / 'polls' / 'Artist.pickle'

    if not model_path.exists():
        print(f"❌ Model file not found at: {model_path}")
        return False

    print(f"✅ Model file located: {model_path}")

    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print("✅ Model successfully loaded into memory")

        # Sample test sculpture
        sample = {
            'Artist Reputation': 0.75,
            'Height': 18.0,
            'Width': 8.0,
            'Weight': 1200.0,
            'Material': 1,              # Brass
            'Price Of Sculpture': 350.0,
            'Base Shipping Price': 45.0,
            'International': 1,
            'Express Shipment': 1,
            'Installation Included': 0,
            'Transport': 0,             # Airways
            'Fragile': 0,
            'Customer Information': 1,
            'Remote Location': 0,
            'Waiting time': 3.0
        }

        df = pd.DataFrame([sample])
        pred = model.predict(df)[0]
        predicted_cost = round(float(pred), 2)

        print(f"\n🧪 Input Features Shape: {df.shape}")
        print(f"💰 Predicted Sculpture Total Cost: ${predicted_cost:,.2f} USD")
        print("\n✅ All model tests completed successfully!")
        return True

    except Exception as e:
        print(f"❌ Error testing model: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_artist_model()
    sys.exit(0 if success else 1)
