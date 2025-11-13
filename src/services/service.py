from src.repository.store import Store

from .production import (
    ChecklistItemServiceImpl,
    ChecklistServiceImpl,
    CommentServiceImpl,
    ProjectMemberServiceImpl,
    ProjectServiceImpl,
    StatusServiceImpl,
    TagServiceImpl,
    TaskSequenceServiceImpl,
    TaskServiceImpl,
    TaskTagServiceImpl,
    UserServiceImpl,
)
from .interfaces import Service

# noinspection DuplicatedCode
class ServiceImpl(Service):
    def __init__(self, store: Store):
        self.checklist_items: ChecklistItemServiceImpl = ChecklistItemServiceImpl(store)
        self.checklists: ChecklistServiceImpl = ChecklistServiceImpl(store)
        self.comments: CommentServiceImpl = CommentServiceImpl(store)
        self.project_members: ProjectMemberServiceImpl = ProjectMemberServiceImpl(store)
        self.projects: ProjectServiceImpl = ProjectServiceImpl(store)
        self.statuses: StatusServiceImpl = StatusServiceImpl(store)
        self.tags: TagServiceImpl = TagServiceImpl(store)
        self.tasks: TaskServiceImpl = TaskServiceImpl(store)
        self.task_sequences: TaskSequenceServiceImpl = TaskSequenceServiceImpl(store)
        self.task_tags: TaskTagServiceImpl = TaskTagServiceImpl(store)
        self.users: UserServiceImpl = UserServiceImpl(store)

    def checklist_item_service(self) -> ChecklistItemServiceImpl:
        return self.checklist_items

    def checklist_service(self) -> ChecklistServiceImpl:
        return self.checklists

    def comment_service(self) -> CommentServiceImpl:
        return self.comments

    def project_member_service(self) -> ProjectMemberServiceImpl:
        return self.project_members

    def project_service(self) -> ProjectServiceImpl:
        return self.projects

    def status_service(self) -> StatusServiceImpl:
        return self.statuses

    def tag_service(self) -> TagServiceImpl:
        return self.tags

    def task_service(self) -> TaskServiceImpl:
        return self.tasks

    def task_sequence_service(self) -> TaskSequenceServiceImpl:
        return self.task_sequences

    def task_tag_service(self) -> TaskTagServiceImpl:
        return self.task_tags

    def user_service(self) -> UserServiceImpl:
        return self.users
