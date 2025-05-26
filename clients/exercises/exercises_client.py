from typing import TypedDict

from httpx import Response

from ..api_client import APIClient


class ExerciseQueryDict(TypedDict):
    courseId: str


class ExerciseCreateRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: str
    minScore: str
    orderIndex: str
    description: str
    estimatedTime: str
    

class ExerciseUpdateRequestDict(TypedDict):
    title: str | None
    courseId: str | None
    maxScore: str | None
    minScore: str | None
    orderIndex: str | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, request: ExerciseQueryDict) -> Response:
        """
        Метод получения списка заданий по идентификатору курса.

        :param request: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/", params=request)
    
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения деталей задания по идентификатору задания.

        :param course_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request: ExerciseCreateRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises/", json=request)

    def update_exercises_api(self, request: ExerciseUpdateRequestDict) -> Response:
        """
        Метод обновления задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch("/api/v1/exercises/", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
    