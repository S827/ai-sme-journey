# Progress Log – Linear Regression Basics

## 1.1 – Create project folder
- **Task**: Created project folder `01_linear_regression_basic`.
- **Command**:
  mkdir 01_linear_regression_basic
  cd 01_linear_regression_basic
- **Notes**: Done inside ai-sme-journey repo.

## 1.2 – Initialize virtual environment
- **Task**: Created isolated Python environment `.venv`.
- **Command**:
  python -m venv .venv
- **Notes**: Keeps dependencies separate.

## 1.3 – Activate venv
- **Task**: Activated `.venv`.
- **Command**:
  .venv\Scripts\Activate.ps1
- **Fix**: Had to run:
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  because PowerShell blocked scripts.

## 1.4 – Upgrade pip
- **Task**: Ensure latest pip.
- **Command**:
  python -m pip install --upgrade pip

## 1.5 – Create requirements.txt
- **Task**: Added dependencies list.
- **Command**:
  ni requirements.txt
- **Content**:
  numpy
  matplotlib
  scikit-learn
  jupyter

## 1.6 – Install dependencies
- **Command**:
  pip install -r requirements.txt

## 1.7 – Freeze dependencies
- **Task**: Pinned exact versions.
- **Command**:
  pip freeze > requirements.txt

## 1.8 – Create notebooks folder
- **Task**: Organize experiments in Jupyter notebooks.
- **Command**:
  mkdir notebooks

## 1.9 – Start Jupyter Notebook
- **Command**:
  jupyter notebook

## 1.10 – Generate synthetic dataset
- **Code**:
  import numpy as np
  X = 2 * np.random.rand(100, 1)
  y = 4 + 3 * X + np.random.randn(100, 1)
- **Notes**: Created 100 samples with noise.

## 1.11 – Visualize dataset
- **Code**:
  import matplotlib.pyplot as plt
  plt.scatter(X, y)
  plt.xlabel("X")
  plt.ylabel("y")
  plt.show()

## 1.12 – Explore dataset (print samples)
- **Code**:
  for i in range(5):
      print(f"Sample {i+1}: X={X[i,0]:.3f}, y={y[i,0]:.3f}")

## 1.13 – Manual Linear Regression (Gradient Descent)
- **Math**:
  Hypothesis: y = wX + b  
  Loss: MSE  
  Gradient Descent updates:
    w := w - η * ∂J/∂w  
    b := b - η * ∂J/∂b
- **Code**:
  w, b = 0, 0
  lr = 0.1
  n = len(X)
  for _ in range(1000):
      y_pred = w*X + b
      dw = -(2/n) * np.sum(X * (y - y_pred))
      db = -(2/n) * np.sum(y - y_pred)
      w -= lr * dw
      b -= lr * db

## 1.14 – Train using Scikit-Learn
- **Code**:
  from sklearn.linear_model import LinearRegression
  lin_reg = LinearRegression()
  lin_reg.fit(X, y)
  print("Intercept:", lin_reg.intercept_[0])
  print("Coefficient:", lin_reg.coef_[0][0])

## 1.15 – Predict with trained model
- **Code**:
  X_new = np.array([[0], [2]])
  y_pred = lin_reg.predict(X_new)
  print(y_pred)
- **Notes**: Predicted outputs for X=0 and X=2.

## 1.16 – Visualize predictions
- **Code**:
  plt.scatter(X, y)
  plt.plot(X_new, y_pred, color="red", linewidth=2)
  plt.show()

## 1.17 – Model evaluation (MSE, RMSE, R²)
- **Code**:
  from sklearn.metrics import mean_squared_error, r2_score
  y_pred_all = lin_reg.predict(X)
  mse = mean_squared_error(y, y_pred_all)
  rmse = np.sqrt(mse)
  r2 = r2_score(y, y_pred_all)
  print("MSE:", mse, "RMSE:", rmse, "R2:", r2)
- **Result**:
  MSE ≈ 0.085  
  RMSE ≈ 0.291  
  R² ≈ 0.973

## 1.18 – Save trained model
- **Task**: Persist trained linear regression model for reuse.
- **Code**:
  ```python
  import joblib
  joblib.dump(lin_reg, "../models/linear_regression_model.pkl")

---

## Git Workflow
After every meaningful microstep:
  git add .
  git commit -m "step 1.xx: description"
  git push origin main
