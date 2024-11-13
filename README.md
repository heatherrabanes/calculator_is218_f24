# IS218 Fall 2024 Midterm Calculator App
## Table of Contents
1. [Features and Usage](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#features-and-usage)
2. [Design Patterns](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#design-patterns)
3. [Environment Variables](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#environment-variables)
4. [Logging](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#logging)
5. [LBYL/EAFP Implementation](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#lbyleafp-implementation)
6. [Installation and Testing](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#installation-and-testing)
7. [Demo](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#demo)
## Features and Usage
### Features
- **Operations Supported**:
  - Addition, Subtraction, Multiplication, Division
  - Power, Root operations with error handling
- **Advanced Configuration**:
  - Customizable settings including precision, history size, and max input values, configured through environment variables or fallback defaults.
- **Persistence**:
  - Calculation history can be saved and loaded, with directories and file paths configured dynamically.
- **Validation & Error Handling**:
  - Input validation and descriptive error messages for invalid configurations and operations.
### Usage
The calculator supports the following commands in its REPL interface:
- **Basic Operations**:
  - `add`, `subtract`, `multiply`, `divide`
- **Advanced Operations**:
  - `power`, `root`
- **History Commands**:
  - `history` - Shows all past calculations
  - `clear` - Clears the calculation history
  - `undo`, `redo` - Undo/redo last operation
- **File Operations**:
  - `save`, `load` - Save/load calculation history to/from file
  - `exit` - Exit the calculator
 
 The `help` command can be entered to view a list of available commands.
## Design Patterns
### Observer
Observer design patterns are used for management of calculator history. This includes the `HistoryObserver` class, `LoggingObserver` class, and `AutoSaveObserver` class. Sample code for `HistoryObserver`, found in `app.history`, is shown below:
```python
class HistoryObserver(ABC):
    """Abstract base class for calculator observers."""
    
    @abstractmethod
    def update(self, calculation: Calculation) -> None:
        """
        Handle new calculation event.
        
        Args:
            calculation: The calculation that was performed
        """
        pass

```
### Factory
The Factory design pattern is used to manage individual mathematical operations in the calculator. This pattern is used in the `OperationFactory` class. The code for the creation of `OperationFactory`, found in `app.operations`, is shown below:
```python
class OperationFactory:
    """Factory class for creating operation instances."""
    
    _operations: Dict[str, type] = {
        'add': Addition,
        'subtract': Subtraction,
        'multiply': Multiplication,
        'divide': Division,
        'power': Power,
        'root': Root
```
### Memento
The Memento design pattern is used in order to implement reversal and/or reptition of commands. This pattern is used in the `CalculatorMemento` class. The code for the creation of `CalculatorMemento`, found in `app.calculator`, is shown below: 
```python
@dataclass
class CalculatorMemento:
    """Stores calculator state for undo/redo functionality."""
    history: List[Calculation]
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)

    def to_dict(self) -> Dict[str, Any]:
        """Convert memento to dictionary."""
        return {
            'history': [calc.to_dict() for calc in self.history],
            'timestamp': self.timestamp.isoformat()
```
## Environment Variables
Environmental variables are used to customize calculator behavior. The base `.env` file is shown under the [Installation and Testing](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#installation-and-testing) section.
## Logging
Logging is implemented using Python's built-in `logging` module in order to record events during the excecution of the calculator program. This is crucial for debugging and monitoring purposes. Logging configuration is stored in `logging.conf`. The `log_file` method is defined in `app.calculator_config` and is associated with the `CalculatorConfig` class, as shown below in the sample code:
```python
 @property
    def log_file(self) -> Path:
        """Get log file path."""
        return Path(os.getenv(
            'CALCULATOR_LOG_FILE',
            str(self.log_dir / "calculator.log")
        )).resolve()
```
The `log_file` method is called by the `Calculator` class with the `setup_logging` method. Sample code shown below:
```python
def _setup_logging(self) -> None:
        """Configure logging system."""
        try:
            os.makedirs(self.config.log_dir, exist_ok=True)
            log_file = self.config.log_file.resolve()
            logging.basicConfig(
                filename=str(log_file),
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                force=True
```
## LBYL/EAFP Implementation
The 'Easier to Ask for Forgiveness Than Permission' methodology is used to handle exceptions in this program. A hierarchy of exception classes is stored in `app.exceptions` and includes `CalculatorError`, `ValidationError`, `OperationError`, and `ConfigurationError`.

## Installation and Testing
### Installation
1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/calculator.git
   cd calculator
   ```

2. Set up the virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. To set up the environment variables, create a `.env` file in the project root:

   ```env
   CALCULATOR_BASE_DIR=/path/to/base/dir
   CALCULATOR_MAX_HISTORY_SIZE=100
   CALCULATOR_AUTO_SAVE=true
   CALCULATOR_PRECISION=10
   CALCULATOR_MAX_INPUT_VALUE=1e100
   CALCULATOR_DEFAULT_ENCODING=utf-8
   ```

4. Run the program:

   ```bash
   python3 main.py
   ```
### Testing
To run the unit tests for this calculator:

```bash
pytest
```

Code coverage reports are generated and stored in the `htmlcov` directory.

## Demo
[Link to demo on YouTube]()
