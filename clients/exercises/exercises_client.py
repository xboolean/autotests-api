from httpx import Response

from ..api_client import APIClient
from .exercise_schema import (
    CreateExerciseResponseSchema,
    CreateExerciseRequestSchema,
    UpdateExerciseRequestSchema,
    GetExercisesQuerySchema,
    GetExercisesResponseSchema
)
from clients.private_http_builder import get_private_http_client
from clients.private_http_builder import AuthenticationUserSchema


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, request: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий по идентификатору курса.

        :param request: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises", params=request)
    
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения деталей задания по идентификатору задания.

        :param course_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercises_api(self, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
    
    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)
    
    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercises_api(request)
        print(response.text)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
