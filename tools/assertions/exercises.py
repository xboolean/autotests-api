from clients.exercises.exercises_schema import (
    CreateExerciseResponseSchema, 
    CreateExerciseRequestSchema, 
)
from tools.assertions.base import assert_equal


def assert_create_exercise_response(
        response: CreateExerciseResponseSchema,
        request: CreateExerciseRequestSchema
):
    """
    Проверяет, что ответ на создание упражнения соответствует ожидаемым данным.

    :param response: Фактический ответ от API при создании упражнения.
    :param request: Исходный запрос на создание упражнения.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "courseId")
    assert_equal(response.exercise.max_score, request.max_score, "maxScore")
    assert_equal(response.exercise.min_score, request.min_score, "minScore")
    assert_equal(response.exercise.order_index, request.order_index, "orderIndex")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimatedTime")