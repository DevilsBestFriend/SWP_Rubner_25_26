# python
from __future__ import annotations
from typing import List, Optional

class Worker:
    def __init__(self, worker_id: int, name: str, position: str, salary: float):
        self.worker_id = worker_id
        self.name = name
        self.position = position
        self.salary = float(salary)
        self.hours_worked = 0.0

    def work(self, hours: float) -> str:
        self.hours_worked += hours
        return f"{self.name} hat {hours} Stunden gearbeitet."

    def give_raise(self, amount: Optional[float] = None, percent: Optional[float] = None) -> None:
        if amount is not None:
            self.salary += amount
        elif percent is not None:
            self.salary *= 1 + percent / 100

    def info(self) -> str:
        return f"ID {self.worker_id} — {self.name} ({self.position}), Gehalt: {self.salary:.2f}, gearbeitete Stunden: {self.hours_worked:.1f}"

    def to_dict(self) -> dict:
        return {
            "worker_id": self.worker_id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary,
            "hours_worked": self.hours_worked,
        }
# python
class FullTimeWorker(Worker):
    def __init__(self, worker_id: int, name: str, position: str, salary: float,
                 benefits: Optional[List[str]] = None, vacation_days: int = 20):
        super().__init__(worker_id, name, position, salary)
        self.benefits = benefits or []
        self.vacation_days = vacation_days

    def take_vacation(self, days: int) -> str:
        if days <= 0:
            return "Ungültige Urlaubstage."
        if days > self.vacation_days:
            return f"Nicht genug Urlaubstage. Verfügbar: {self.vacation_days}"
        self.vacation_days -= days
        return f"{self.name} nimmt {days} Urlaubstag/e. Verbleibend: {self.vacation_days}"

    def info(self) -> str:
        base = super().info()
        return f"{base}, Benefits: {', '.join(self.benefits) if self.benefits else 'keine'}, Urlaubstage: {self.vacation_days}"
# python
class Manager(Worker):
    def __init__(self, worker_id: int, name: str, position: str, salary: float,
                 team: Optional[List[Worker]] = None):
        super().__init__(worker_id, name, position, salary)
        self.team: List[Worker] = team or []

    def add_member(self, worker: Worker) -> None:
        if worker not in self.team:
            self.team.append(worker)

    def remove_member(self, worker: Worker) -> None:
        if worker in self.team:
            self.team.remove(worker)

    def list_team(self) -> List[str]:
        return [f"{w.worker_id}: {w.name} ({w.position})" for w in self.team]

    def assign_task(self, worker: Worker, task: str) -> str:
        if worker not in self.team:
            return f"{worker.name} ist nicht im Team von {self.name}."
        return f"{self.name} weist {worker.name} die Aufgabe zu: {task}"
# python
if __name__ == "__main__":
    w1 = Worker(1, "Anna Müller", "Technikerin", 3500.0)
    w2 = FullTimeWorker(2, "Ben Schmidt", "Entwickler", 4800.0, benefits=["Krankenversicherung", "Fahrkostenzuschuss"], vacation_days=25)
    m = Manager(0, "Clara Leitung", "Teamleiterin", 6500.0)

    m.add_member(w1)
    m.add_member(w2)

    print(w1.info())
    print(w2.info())
    print(m.info())

    print(w2.take_vacation(5))
    w1.work(8)
    print(w1.info())

    print(m.assign_task(w2, "Implementiere Feature X"))
    print("Team von", m.name, ":", m.list_team())
    m.give_raise(percent=5)
    print("Nach Gehaltserhöhung:", m.info())