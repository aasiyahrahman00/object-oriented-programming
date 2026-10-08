
class PluginManager:
    # Singleton, registers plugins and receives updates
    _instance = None

    def __new__(cls):
        # Creates instace once
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialise singleton data only when instaqnce created
            cls._instance.plugins = []

        return cls._instance

    def register_plugin(self, plugin):
        # Register plugin with  manager
        if plugin not in self.plugins:
            self.plugins.append(plugin)
            plugin.attach(self)

    def unregister_plugin(self, plugin):
        # Remove plugin from manger
        if plugin in self.plugins:
            self.plugins.remove(plugin)
            plugin.detach(self)

    def update(self, plugin, status):
        # Recives status updates from plugins
        print(f"PluginManager received update: {plugin.name} is now {status}")


manager_one = PluginManager()
manager_two = PluginManager()

print(manager_one is manager_two)
            






from abc import ABC, abstractmethod

class Plugin(ABC):
    def __init__(self, name):
        self.name = name
        self.status = "Not active"
        self._observers = []

    def attach(self, observer):
        # Subscribe observer
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # Unsubscribe obsrever
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        # Notify observers about current status
        for observer in self._observers:
            observer.update(self, self.status)

    def set_status(self, new_status):
        # Change status and notify observers
        self.status = new_status
        self.notify()

    @abstractmethod
    def run(self):
        # Each plugin provides its own behavior
        pass


class SpellChecker(Plugin):
    def __init__(self):
        super().__init__("Spell Checker")

    def run(self):
        self.set_status("Running")
        print("Spell Checking Completed")
        self.set_status("Completed")


class GrammarChecker(Plugin):
    def __init__(self):
        super().__init__("Grammar Checker")

    def run(self):
        self.set_status("Running")
        print("Grammar Checking Completed")
        self.set_status("Completed")
        

manager = PluginManager()

spell_checker = SpellChecker()
grammar_checker = GrammarChecker()

manager.register_plugin(spell_checker)
manager.register_plugin(grammar_checker)

spell_checker.run()
grammar_checker.run()






class Task:
    # Represents a task in a team project.
    statuses = {
        "Pending",
        "In Progress",
        "Completed"
    }

    def __init__(
        self,
        title: str,
        description: str,
        assignee: str | None = None,
        status: str = "Pending"
    ):
        # Validate  title and description.
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty")

        if not isinstance(description, str) or not description.strip():
            raise ValueError("Task description cannot be empty")

        # Validate initial status.
        if status not in self.statuses:
            raise ValueError("Invalid task status")

        self.title = title.strip()
        self.description = description.strip()
        self.assignee = assignee
        self.status = status

    def assign_task(self, team_member: str) -> None:
        # Assign the task to a team member.
        if not isinstance(team_member, str) or not team_member.strip():
            raise ValueError("Team member name cannot be empty")

        self.assignee = team_member.strip()

    def update_status(self, new_status: str) -> None:
        # Update the tasks current status
        if new_status not in self.statuses:
            raise ValueError(
                "Status must be pending, in progress, or completed"
            )
        self.status = new_status
    
        
task = Task(
    "Create login page",
    "Design and implement user login interface"
)

task.assign_task("Aasiyah")
task.update_status("In Progress")

print(task.title)
print(task.assignee)
print(task.status)







import unittest

class TestTask(unittest.TestCase):
    def setUp(self):
        # create a task object before each test
        self.task = Task(
            "Create login page",
            "Design and implmeent login intefce"
        )

    def test_task_initial_values(self):
        self.assertEqual(self.task.title, "Create login page")
        self.assertEqual(
            self.task.description,
            "Design and implement login interface"
        )
        self.assertIsNone(self.task.assignee)
        self.assertEqual(self.task.status, "Pending")

    def test_assign_task(self):
        self.task.assign_task("Aasiyah")

        self.assertEqual(self.task.assignee, "Aasiyah")

    def test_update_status(self):
        self.task.update_status("In Progress")

        self.assertEqual(self.task.status, "In Progress")

    def test_complete_task(self):
        self.task.update_status("Completed")

        self.assertEqual(self.task.status, "Completed")

    def test_empty_assignee_is_rejected(self):
        with self.assertRaises(ValueError):
            self.task.assign_task("")

