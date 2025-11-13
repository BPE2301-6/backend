# noinspection DuplicatedCode
from sqlalchemy.ext.asyncio import AsyncSession

from .interfaces import Store
from .sql import (
    ChecklistItemRepositoryImpl,
    ChecklistRepositoryImpl,
    CommentRepositoryImpl,
    ProjectMemberRepositoryImpl,
    ProjectRepositoryImpl,
    StatusRepositoryImpl,
    TagRepositoryImpl,
    TaskRepositoryImpl,
    TaskSequenceRepositoryImpl,
    TaskTagRepositoryImpl,
    UserRepositoryImpl,
)


# noinspection DuplicatedCode
class StoreImpl(Store):
    def __init__(self, session: AsyncSession):
        self.checklist_items: ChecklistItemRepositoryImpl = ChecklistItemRepositoryImpl(session)
        self.checklists: ChecklistRepositoryImpl = ChecklistRepositoryImpl(session)
        self.comments: CommentRepositoryImpl = CommentRepositoryImpl(session)
        self.project_members: ProjectMemberRepositoryImpl = ProjectMemberRepositoryImpl(session)
        self.projects: ProjectRepositoryImpl = ProjectRepositoryImpl(session)
        self.statuses: StatusRepositoryImpl = StatusRepositoryImpl(session)
        self.tags: TagRepositoryImpl = TagRepositoryImpl(session)
        self.tasks: TaskRepositoryImpl = TaskRepositoryImpl(session)
        self.task_sequences: TaskSequenceRepositoryImpl = TaskSequenceRepositoryImpl(session)
        self.task_tags: TaskTagRepositoryImpl = TaskTagRepositoryImpl(session)
        self.users: UserRepositoryImpl = UserRepositoryImpl(session)

    def checklist_item_repo(self) -> ChecklistItemRepositoryImpl:
        return self.checklist_items

    def checklist_repo(self) -> ChecklistRepositoryImpl:
        return self.checklists

    def comment_repo(self) -> CommentRepositoryImpl:
        return self.comments

    def project_member_repo(self) -> ProjectMemberRepositoryImpl:
        return self.project_members

    def project_repo(self) -> ProjectRepositoryImpl:
        return self.projects

    def status_repo(self) -> StatusRepositoryImpl:
        return self.statuses

    def tag_repo(self) -> TagRepositoryImpl:
        return self.tags

    def task_repo(self) -> TaskRepositoryImpl:
        return self.tasks

    def task_sequence_repo(self) -> TaskSequenceRepositoryImpl:
        return self.task_sequences

    def task_tag_repo(self) -> TaskTagRepositoryImpl:
        return self.task_tags

    def user_repo(self) -> UserRepositoryImpl:
        return self.users
