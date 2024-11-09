# IS218 Fall 2024 Midterm Calculator App
## Table of Contents
1. [Design Patterns](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#design-patterns)
2. [Environment Variables](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#environment-variables)
3. [Logging](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#logging)
4. [LBYL/EAFP Implementation](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#lbyleafp-implementation)
5. [Demo](https://github.com/heatherrabanes/calculator_is218_f24?tab=readme-ov-file#demo)
## Design Patterns
### Strategy
The Strategy design pattern is used for
```python
 def set_operation(self, operation: Operation) -> None:
        """Set current operation strategy."""
        self.operation_strategy = operation
        logging.info(f"Set operation: {operation}")
```
### Observer
Observer design patterns are used for management of calculator history. This includes the HistoryObserver class, LoggingObserver class, and AutoSaveObserver class. Sample code for HistoryObserver is shown below:
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
The Factory design pattern is used to manage individual operations in the calculator. The code for the creation of the Factory class is shown below:
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
The Memento design pattern is used for 
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
Environmental variables are used to control calculator behavior. The base `.env` file is shown as below:
```env
CALCULATOR_BASE_DIR=/path/to/base/dir
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=10
CALCULATOR_MAX_INPUT_VALUE=1e100
CALCULATOR_DEFAULT_ENCODING=utf-8
```
## Logging
Logging configuration is stored in `logging.conf`. The `log_file` method is associated with the `CalculatorConfig` class, as shown below:
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

## Demo
