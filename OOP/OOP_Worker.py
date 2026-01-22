class Worker:
  def __init__(self, worker_id, name, position, salary):
    self.worker_id = worker_id
    self.name = name
    self.position = position
    self.salary = float(salary)
    self.hours_worked = 0.0

  def work(self, hours):
    self.hours_worked += hours
    return f"{self.name} hat {hours} Stunden gearbeitet."

  def give_raise(self, amount=None, percent=None):
    if amount is not None:
      self.salary += amount
    elif percent is not None:
      self.salary *= 1 + percent / 100

  def info(self):
    return f"ID {self.worker_id} — {self.name} ({self.position}), Gehalt: {self.salary:.2f}, gearbeitete Stunden: {self.hours_worked:.1f}"

  def to_dict(self):
    return {
      "worker_id": self.worker_id,
      "name": self.name,
      "position": self.position,
      "salary": self.salary,
      "hours_worked": self.hours_worked,
    }


class FullTimeWorker(Worker):
  def __init__(self, worker_id, name, position, salary, benefits=None, vacation_days=20):
    super().__init__(worker_id, name, position, salary)
    self.benefits = benefits or []
    self.vacation_days = vacation_days

  def take_vacation(self, days):
    if days <= 0:
      return "Ungültige Urlaubstage."
    if days > self.vacation_days:
      return f"Nicht genug Urlaubstage. Verfügbar: {self.vacation_days}"
    self.vacation_days -= days
    return f"{self.name} nimmt {days} Urlaubstag/e. Verbleibend: {self.vacation_days}"

  def info(self):
    base = super().info()
    benefits_str = ', '.join(self.benefits) if self.benefits else 'keine'
    return f"{base}, Benefits: {benefits_str}, Urlaubstage: {self.vacation_days}"


class Manager(Worker):
  def __init__(self, worker_id, name, position, salary, team=None):
    super().__init__(worker_id, name, position, salary)
    self.team = team or []

  def add_member(self, worker):
    if worker not in self.team:
      self.team.append(worker)

  def remove_member(self, worker):
    if worker in self.team:
      self.team.remove(worker)

  def list_team(self):
    return [f"{w.worker_id}: {w.name} ({w.position})" for w in self.team]

  def assign_task(self, worker, task):
    if worker not in self.team:
      return f"{worker.name} ist nicht im Team von {self.name}."
    return f"{self.name} weist {worker.name} die Aufgabe zu: {task}"


if __name__ == "__main__":
  w1 = Worker(1, "Anna Müller", "Technikerin", 3500.0)
  w2 = FullTimeWorker(2, "Ben Schmidt", "Entwickler", 4800.0, benefits=["Krankenversicherung", "Fahrkostenzuschuss"],
                      vacation_days=25)
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