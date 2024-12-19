## **Paper Replications - Operations Research & Operations Management**

This repository contains replications of key studies and algorithms from **Operations Research** and **Operations Management** papers published in top-tier journals, such as those from **INFORMS**, Management Science, Operations Research, and other notable outlets. Each folder replicates a specific study, focusing on implementing the models, algorithms, and methods presented.

The aim is to provide clean, reproducible, and well-documented implementations for foundational and cutting-edge work in operations research and its applications.

---

### **Repository Structure**

Each replicated study is organized in its own directory under `src/`. The folder names follow the format:  

**`<author(s)>_<year>_<journal>`**

Each folder contains the following subdirectories:

- `code/` : Python implementations of the models and algorithms presented in the paper.  
- `results/` : Outputs and results demonstrating the implementation, including numerical experiments or visualizations.  
- `tests/` : Unit tests validating the correctness of the implemented methods.  

---

### **Included Replications**

| Study Name | Author(s), Year, Journal | Description |
|------------|--------------------------|-------------|
| **Dynamic Economic Lot Sizing** | Wagner & Whitin, 1958, Management Science | A dynamic programming approach to solving the deterministic lot-sizing problem. |
| **[Add next study here]** | [Author(s), Year, Journal] | [Brief description of the study]. |
| **[Add next study here]** | [Author(s), Year, Journal] | [Brief description of the study]. |

---

### **Example Study: Wagner & Whitin (1958)**

#### **Problem Overview**
The **deterministic economic lot-sizing problem** involves determining the optimal order quantities over a finite planning horizon such that the **total cost** is minimized. The costs include:  
1. **Fixed Ordering Costs**: Cost incurred each time an order is placed, irrespective of the order size.  
2. **Inventory Holding Costs**: Cost for carrying inventory forward across periods.  

The Wagner-Whitin algorithm employs a **recursive dynamic programming (DP) approach** to determine the exact optimal order schedule.

#### **Implementation**
- **Folder**: `src/wagner_whitin_1958_management_science/`
- **Core Code**: `code/dynamic_program.py`
- **Tests**: `tests/test_algorithm.py`
- **Output**: Cost breakdowns and optimal policies for a given demand input.

#### **How to Run**
```bash
# Run the dynamic program
cd src/wagner_whitin_1958_management_science
python code/main.py

# Run unit tests
cd tests
python -m unittest test_algorithm.py
```


### **Prerequisites**

1. Python >= 3.8  
2. Libraries:
   - `numpy`

Install dependencies using `pip`:
```bash
pip install -r requirements.txt
```



### **How to Contribute**

Contributions are welcome! Here’s how you can help:

1. Fork the repository.
2. Add a new replication under the `src/` directory.
   - Name the folder using the format: `<author(s)>_<year>_<journal>`.
   - Include the following subdirectories:
     - `code/`: Python implementations of the models and algorithms.
     - `results/`: Outputs and visualizations.
     - `tests/`: Unit tests to validate your code.
3. Ensure that your code is well-documented and adheres to Python best practices.
4. Run all tests and confirm they pass before submitting.
5. Submit a pull request.

For any issues or questions, feel free to open an issue in the repository.

---

### **References**

1. Wagner, H. M., & Whitin, T. M. (1958). "Dynamic Version of the Economic Lot Size Model". *Management Science*, 5(1), 89-96. [https://doi.org/10.1287/mnsc.5.1.89](https://doi.org/10.1287/mnsc.5.1.89)


---

### **Acknowledgments**

This repository is inspired by seminal and contemporary works in **Operations Research** and **Operations Management**. Special thanks to the original authors whose contributions laid the foundation for this field.

---

### **License**

This repository is open-source and licensed under the MIT License. See the `LICENSE` file for details.