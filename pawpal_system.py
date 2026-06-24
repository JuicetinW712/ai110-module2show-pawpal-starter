from dataclasses import dataclass, field
from typing import List


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    weight: float

    def updateWeight(self, w: float) -> None:
        """Update the weight of the pet."""
        pass


@dataclass
class Task:
    id: str
    name: str
    duration: int
    priority: str
    scheduledDate: str
    recurringDays: List[str] = field(default_factory=list)

    def isRecurring(self) -> bool:
        """Check if the task is recurring."""
        pass


@dataclass
class DietEntry:
    date: str
    mealName: str
    calories: int


@dataclass
class Scheduler:
    petId: str
    date: str
    availableMinutes: int
    tasks: List[Task] = field(default_factory=list)

    def createTask(self, task: Task) -> None:
        """Create a new task in the scheduler."""
        pass

    def deleteTask(self, id: str) -> None:
        """Delete a task by its ID."""
        pass

    def getTasksForDate(self, date: str) -> List[Task]:
        """Retrieve all tasks scheduled for a specific date."""
        pass


@dataclass
class DietTracker:
    petId: str
    dailyCalGoal: int
    entries: List[DietEntry] = field(default_factory=list)

    def getCalories(self, date: str) -> int:
        """Get total calories consumed on a specific date."""
        pass

    def getNutritionLog(self) -> List[DietEntry]:
        """Retrieve the nutrition log."""
        pass


@dataclass
class Recommendations:
    pet: Pet
    scheduler: Scheduler
    dietTracker: DietTracker

    def generateRecs(self) -> List[str]:
        """Generate recommendations based on scheduling and diet information."""
        pass

    def explainRec(self, id: str) -> str:
        """Explain the rationale behind a recommendation by its ID."""
        pass
