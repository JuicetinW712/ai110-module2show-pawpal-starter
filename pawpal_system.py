from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class Owner:
    id: str
    name: str
    email: str


@dataclass
class Pet:
    id: str
    name: str
    species: str
    breed: str
    weight: float


@dataclass
class Task:
    id: str
    name: str
    description: str
    duration: int
    priority: str
    start_date: date
    end_date: Optional[date]
    recurring_days: List[str] = field(default_factory=list)


@dataclass
class Scheduler:
    def create_task(self, pet_id: str, task: Task) -> None:
        """Create a new task for a pet."""
        pass

    def update_task(self, pet_id: str, task_id: str, task: Task) -> None:
        """Update an existing task for a pet."""
        pass

    def delete_task(self, pet_id: str, task_id: str) -> None:
        """Delete a task for a pet."""
        pass

    def get_tasks_for_date(self, pet_id: str, target_date: date) -> List[Task]:
        """Retrieve all tasks scheduled for a pet on a specific date."""
        pass

    def get_all_tasks(self, pet_id: str) -> List[Task]:
        """Retrieve all tasks for a pet."""
        pass


@dataclass
class Recommendation:
    id: str
    pet_id: str
    category: str
    text: str
    explanation: str

    @staticmethod
    def generate(pet: Pet, tasks: List[Task]) -> List["Recommendation"]:
        """Generate recommendations based on pet profile and scheduled tasks."""
        pass
