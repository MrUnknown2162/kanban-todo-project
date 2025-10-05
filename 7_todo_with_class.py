from enum import Enum
from datetime import datetime
from typing import List, Optional

class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"

#================================================================================
#============================== Base Entity Class ============================
#================================================================================
class BaseEntity:
    """Base class cho tất cả entities"""
    def __init__(self):
        self.id = self._generate_id()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def _generate_id(self):
        import uuid
        return str(uuid.uuid4())[:8]
    
    def update_timestamp(self):
        self.updated_at = datetime.now()

#================================================================================
#============================== User Class =================================
#================================================================================
class User(BaseEntity):
    def __init__(self, username: str, email: str, full_name: str = None):
        super().__init__()
        self.username = username
        self.email = email
        self.full_name = full_name or username
        self.role = UserRole.USER
        self.is_active = True
        self._password_hash = None
    
    def set_password(self, password: str):
        """Set password (sẽ hash trong thực tế)"""
        # Trong thực tế sẽ dùng bcrypt
        self._password_hash = hash(password)
        self.update_timestamp()
    
    def verify_password(self, password: str) -> bool:
        """Verify password"""
        return self._password_hash == hash(password)
    
    def promote_to_admin(self):
        """Promote user to admin"""
        self.role = UserRole.ADMIN
        self.update_timestamp()
    
    def deactivate(self):
        """Deactivate user"""
        self.is_active = False
        self.update_timestamp()
    
    def __str__(self):
        return f"User({self.username}, {self.role.value})"
    
    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, role={self.role.value})"

#================================================================================
#============================== Board Class =================================
#================================================================================
class Board(BaseEntity):
    def __init__(self, name: str, description: str = None, owner: User = None):
        super().__init__()
        self.name = name
        self.description = description or ""
        self.owner = owner
        self.is_public = False
        self.tasks: List['Task'] = []
    
    def add_task(self, task: 'Task'):
        """Add task to board"""
        if task not in self.tasks:
            self.tasks.append(task)
            task.board = self
            self.update_timestamp()
    
    def remove_task(self, task: 'Task'):
        """Remove task from board"""
        if task in self.tasks:
            self.tasks.remove(task)
            task.board = None
            self.update_timestamp()
    
    def get_tasks_by_status(self, status: TaskStatus) -> List['Task']:
        """Get all tasks with specific status"""
        return [task for task in self.tasks if task.status == status]
    
    def get_tasks_by_priority(self, priority: Priority) -> List['Task']:
        """Get all tasks with specific priority"""
        return [task for task in self.tasks if task.priority == priority]
    
    def get_task_count(self) -> dict:
        """Get count of tasks by status"""
        return {
            "todo": len(self.get_tasks_by_status(TaskStatus.TODO)),
            "in_progress": len(self.get_tasks_by_status(TaskStatus.IN_PROGRESS)),
            "done": len(self.get_tasks_by_status(TaskStatus.DONE)),
            "total": len(self.tasks)
        }
    
    def set_public(self, is_public: bool):
        """Set board visibility"""
        self.is_public = is_public
        self.update_timestamp()
    
    def __str__(self):
        return f"Board({self.name}, {len(self.tasks)} tasks)"

#================================================================================
#============================== Task Class =================================
#================================================================================
class Task(BaseEntity):
    def __init__(self, title: str, description: str = None):
        super().__init__()
        self.title = title
        self.description = description or ""
        self.status = TaskStatus.TODO
        self.priority = Priority.MEDIUM
        self.assigned_to: Optional[User] = None
        self.board: Optional[Board] = None
        self.position = 0
        self.due_date: Optional[datetime] = None
    
    def assign_to(self, user: User):
        """Assign task to user"""
        self.assigned_to = user
        self.update_timestamp()
    
    def unassign(self):
        """Unassign task"""
        self.assigned_to = None
        self.update_timestamp()
    
    def set_priority(self, priority: Priority):
        """Set task priority"""
        self.priority = priority
        self.update_timestamp()
    
    def move_to_status(self, new_status: TaskStatus):
        """Move task to different status"""
        old_status = self.status
        self.status = new_status
        self.update_timestamp()
        print(f"Task '{self.title}' moved from {old_status.value} to {new_status.value}")
    
    def set_due_date(self, due_date: datetime):
        """Set due date for task"""
        self.due_date = due_date
        self.update_timestamp()
    
    def is_overdue(self) -> bool:
        """Check if task is overdue"""
        if self.due_date and self.status != TaskStatus.DONE:
            return datetime.now() > self.due_date
        return False
    
    def update_content(self, title: str = None, description: str = None):
        """Update task content"""
        if title:
            self.title = title
        if description:
            self.description = description
        self.update_timestamp()
    
    def __str__(self):
        assigned = f" -> {self.assigned_to.username}" if self.assigned_to else ""
        return f"Task({self.title}, {self.status.value}, {self.priority.value}{assigned})"

# Demo usage