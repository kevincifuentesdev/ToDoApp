class Todo:

    def __init__(self, code_id: int, title: str, description: str) -> None:
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []
    
    def mark_completed(self):
        self.completed = True
    
    def add_tag(self, tag: str):
        if tag not in self.tags: 
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"


class TodoBook:

    def __init__(self) -> None:
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:

        id = len(self.todos) + 1
        new_todo = Todo(id, title, description)
        self.todos[id] = new_todo
        
        return id
    
    def pending_todos(self) -> list[Todo]:

        pendings: list[Todo] = [pending_todo for pending_todo in self.todos.values() if not pending_todo.completed]

        return pendings
    
    def completed_todos(self) -> list[Todo]:

        completed_todos: list[Todo] = [pending_todo for pending_todo in self.todos.values() if pending_todo.completed]

        return completed_todos
    
    
    def tags_todo_count(self) -> dict[str, int]:
        tags_count: dict[str, int] = {}

        for todo in self.todos.values():
            for tag in todo.tags:
                if tag not in tags_count.keys():
                    tags_count[tag] = 1
                else:
                    tags_count[tag] += 1

        return tags_count