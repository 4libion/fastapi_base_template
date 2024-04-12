from sqlalchemy import select
from database import TaskOrm, new_session
from schemas import SchemeTask, SchemeTaskAdd

class TaskRepository:
    @classmethod
    async def add_task(cls, data: SchemeTaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)

            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_tasks(cls) -> list[SchemeTask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [SchemeTask.model_validate(task_models) for task_model in task_models]
            return task_models
