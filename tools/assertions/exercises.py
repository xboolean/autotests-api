from clients.exercises.exercises_schema import (
    CreateExerciseResponseSchema, 
    CreateExerciseRequestSchema, 
    ExerciseSchema,
    UpdateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
)
from clients.errors_schema import InternalErrorResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_internal_error_response


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


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "courseId")
    assert_equal(actual.max_score, expected.max_score, "maxScore")
    assert_equal(actual.min_score, expected.min_score, "minScore")
    assert_equal(actual.order_index, expected.order_index, "orderIndex")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimatedTime")


def assert_get_exercise_response(
        get_exercise_response: CreateExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если данные упражнения не совпадают.
    """

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExerciseResponseSchema):
    """
    Проверяет, что ответ на обновление упражнения соответствует данным из запроса.

    :param request: Исходный запрос на обновление упражнения.
    :param response: Ответ API с обновленными данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "maxScore")
    assert_equal(response.exercise.min_score, request.min_score, "minScore")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimatedTime")
    assert_equal(response.exercise.order_index, request.order_index, "orderIndex")


def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Проверяет, что ответ на запрос несуществующего упражнения соответствует ожидаемому ответу об ошибке 404.

    :param actual: Ответ от API с ошибкой, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """

    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)