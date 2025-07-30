from http import HTTPStatus

import pytest
import allure
from allure_commons.types import Severity

from clients.exercises.exercises_client import ExercisesClient
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema, 
    CreateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema
)
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response, 
    assert_get_exercise_response, 
    assert_update_exercise_response,
    assert_exercise_not_found_response
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
class TestExercises:

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create exercise")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        """
        Проверяет создание упражнения.
        """
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())
    
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get exercise")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_exercise(self, function_exercise: ExerciseFixture, exercises_client: ExercisesClient):
        """
        Проверяет получение упражнения по ID.
        """
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())
    
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Update exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        """
        Проверяет обновление упражнения.
        """
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercises_api(function_exercise.response.exercise.id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Delete exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        """
        Проверяет удаление упражнения.
        """
        delete_response = exercises_client.delete_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())
