from src.repository.store import Store
from .production import (
    ChecklistItemServiceImpl,
    ChecklistServiceImpl,
    CommentServiceImpl,
    ProjectMemberServiceImpl,
    ProjectServiceImpl,
    StatusServiceImpl,
    TagServiceImpl,
    TaskServiceImpl,
    TaskSequenceServiceImpl,
    TaskTagServiceImpl,
    UserServiceImpl,
)


class ServiceImpl:
    def __init__(self, store: Store):
        self.checklist_items = ChecklistItemServiceImpl(store)
        self.checklists = ChecklistServiceImpl(store)
        self.comments = CommentServiceImpl(store)
        self.project_members = ProjectMemberServiceImpl(store)
        self.projects = ProjectServiceImpl(store)
        self.statuses = StatusServiceImpl(store)
        self.tags = TagServiceImpl(store)
        self.tasks = TaskServiceImpl(store)
        self.task_sequences = TaskSequenceServiceImpl(store)
        self.task_tags = TaskTagServiceImpl(store)
        self.users = UserServiceImpl(store)
