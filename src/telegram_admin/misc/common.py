class BaseEditCallback:
    pass

class TeacherEditCallback(BaseEditCallback):
    PREV = "teacher_prev"
    NEXT = "teacher_next"
    EDIT_NAME = "teacher_edit_name"
    EDIT_DESC = "teacher_edit_description"
    EDIT_PHOTO = "teacher_edit_photo"
    DELETE = "teacher_delete"