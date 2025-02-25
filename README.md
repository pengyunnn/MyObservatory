# 🌦️ MyObservatory - Appium UI Testing

![Test Automation](https://img.shields.io/badge/Test-Automation-blue)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Appium](https://img.shields.io/badge/Appium-1.22%2B-green)

Automated UI testing for the **MyObservatory** app using **Appium** and **pytest**.

## 📌 **Project Overview**
This repository contains automated UI tests for **MyObservatory**, a weather forecasting app. The tests use **Appium** to interact with an **iOS** device or simulator and validate UI elements, including:
- 🏠 **Opening the App**
- 🌦️ **Navigating Weather Forecasts**
- 📸 **Taking Screenshots**
- 📊 **Logging Test Results**

---

## 📂 **Project Structure**
```
📆 MyObservatory
├── 📁 tests
│   ├── test_ios.py        # Main test cases
│   ├── conftest.py        # Test configurations, logging, and screenshots
├── 📁 results             # Stores test results, logs, and screenshots
│   ├── <timestamp>/ 
│   |     ├── logs/        # Test execution logs
│   |     ├── screenshots/ # Captured screenshots
├── requirements.txt       # Required dependencies
├── README.md              # Setup and instructions
```

---

## 🛠 **Setup & Installation**
### **1️⃣ Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### **2️⃣ Install Appium Server**
```sh
npm install -g appium
appium
```

### **3️⃣ Set Up WebDriverAgent for iOS**
Follow the official setup guide:  
📺 **[Appium WebDriverAgent Setup](https://appium.github.io/appium-xcuitest-driver/latest/preparation/real-device-config/)**

### **4️⃣ Connect Your iOS Device**
- Get your **UDID**:
  ```sh
  idevice_id -l
  ```
- Trust your device in **Xcode** and ensure it's **unlocked**.

---

## 🚀 **Running Tests**
### **Run All Tests**
```sh
pytest --capture=no --disable-warnings
```

### **Run a Specific Test**
```sh
pytest tests/test_ios.py::test_open_my_observatory
```

### **View Test Logs**
```sh
cat results/<timestamp>/logs/test_run_<timestamp>.log
```

---

## 📸 **Screenshots & Logs**
- **Screenshots** are saved in `results/<timestamp>/screenshots/`
- **Logs** are stored in `results/<timestamp>/logs/`

📺 **Example: Screenshot after opening "MyObservatory"**
```sh
results/<timestamp>/screenshots/after_click.png
```

---


## 🛠 **Troubleshooting**
### ❌ **Issue: Appium Not Found**
```sh
zsh: command not found: appium
```
✅ **Solution:** Ensure Appium is installed globally.
```sh
npm install -g appium
```

### ❌ **Issue: WebDriverAgent Signing Error**
```sh
Failed Registering Bundle Identifier: The app identifier cannot be registered to your development team.
```
✅ **Solution:** Open `WebDriverAgent.xcodeproj` in Xcode, set your Apple **Development Team**, and enable **Automatically Manage Signing**.

---

## 🎯 **Contributing**
📺 **Pull Requests Welcome!** If you have improvements, feel free to open a PR.

---

## 📝 **License**
This project is open-source under the **MIT License**.

---

✅ **Happy Testing!** 🚀

