# IS218 Fall 2024 Midterm Calculator App
## Table of Contents
1. [Design Patterns](/README.md#design-patterns)
2. [Environment Variables](/README.md#environemnt-variables)
3. [Logging](/README.md#logging)
4. [LBYL/EAFP Implementation](/README.md#lbyleafp-implementation)
5. [Demo](/README.md#demo)
## Design Patterns
### Strategy
```python
 def set_operation(self, operation: Operation) -> None:
        """Set current operation strategy."""
        self.operation_strategy = operation
        logging.info(f"Set operation: {operation}")
```
### Observer
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
    }
```
### Memento
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
        }
```
## Environment Variables
```env
CALCULATOR_BASE_DIR=/path/to/base/dir
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=10
CALCULATOR_MAX_INPUT_VALUE=1e100
CALCULATOR_DEFAULT_ENCODING=utf-8
```
## Logging

## LBYL/EAFP Implementation

## Demo
