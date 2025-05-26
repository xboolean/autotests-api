from tools.fakers import get_random_email
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercise_client, ExerciseCreateRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request["email"],
    password=create_user_request["password"]
)
private_users_client = get_private_http_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercise_client = get_exercise_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.jpg"
)

files_client = get_files_client(authentication_user)

create_file_response = files_client.create_file(create_file_request)

create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response["file"]["id"],
    createdByUserId=create_user_response["user"]["id"]
)
create_course_response = courses_client.create_course(create_course_request)
create_exercise_request = ExerciseCreateRequestDict(
    title="Первое задание", 
    courseId=create_course_response["course"]["id"],
    minScore="10",
    maxScore="100",
    orderIndex="1",
    description="Super description",
    estimatedTime="1 day"
)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)

print(f"Create file data: {create_file_response}")
print(f"Create course data: {create_course_response}")
print(f"Create exercise data: {create_exercise_response}")