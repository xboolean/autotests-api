from tools.fakers import get_random_email
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercise_client
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.exercises.exercise_schema import CreateExerciseRequestSchema


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_http_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercise_client = get_exercise_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.jpg"
)

files_client = get_files_client(authentication_user)

create_file_response = files_client.create_file(create_file_request)

create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score="100",
    min_score="10",
    description="Python API course",
    estimated_time="2 weeks",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
create_exercise_request = CreateExerciseRequestSchema(
    title="Первое задание", 
    courseId=create_course_response.course.id,
    min_score="10",
    max_score="100",
    order_index="1",
    description="Super description",
    estimated_time="1 day"
)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)

print(f"Create file data: {create_file_response}")
print(f"Create course data: {create_course_response}")
print(f"Create exercise data: {create_exercise_response}")