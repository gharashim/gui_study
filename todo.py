import flet as ft

class Task(ft.UserControl):
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete

    def build(self):
        self.display_task = ft.Checkbox(label = self.task_name, value = False)
        self.edit_name = ft.TextField(value = self.task_name, expand = True)

        self.display_view = ft.Row(
            controls = [
                self.display_task,
                ft.Row(
                  controls = [
                      ft.IconButton(icon = ft.icons.CREATE_OUTLINED,
                                    tooltip = "수정",
                                    on_click = self.edit_clicked),
                      ft.IconButton(icon = ft.icons.DELETE_OUTLINED,
                                    tooltip = "삭제",
                                    on_click = self.delete_clicked)]
                )
            ]
        )

        self.edit_view = ft.Row(
            visible = False,
            controls = [
                self.edit_name,
                ft.IconButton(icon = ft.icons.DONE_OUTLINE_OUTLINED,
                              tooltip = "완료",
                              icon_color = ft.colors.GREEN,
                              on_click = self.done_clicked),
            ]
        )

        return ft.Column(controls = [self.display_view, self.edit_view])
    
    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def done_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
    
    def delete_clicked(self, e):
        self.task_delete(self)


class TodoApp(ft.UserControl):
    
    def build(self):
        self.new_task = ft.TextField(hint_text = "새로운 할일", expand = True)
        self.tasks = ft.Column()

        return ft.Column(controls = [
            ft.Row(controls = [
                self.new_task,
                ft.FloatingActionButton(icon = ft.icons.ADD, on_click = self.add_clicked)
            ]),
            self.tasks    
        ])
    
    def add_clicked(self, e):
        # self.tasks.controls.append(ft.Checkbox(label = self.new_task.value))

        task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()
    
    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()
    

def main(page: ft.Page):
    page.title = "To Do" 
    page.update()
    todo = TodoApp()
    page.add(todo)
    # def add_clicked(e):
    #     tasks_view.controls.append(ft.Checkbox(label = new_task.value))
    #     new_task.value = ""
    #     page.update()

    # new_task = ft.TextField(hint_text = "새로운 할일", expand = True)
    # btn = ft.FloatingActionButton(icon = ft.icons.ADD, on_click = add_clicked)
    # tasks_view = ft.Column(controls = [
        
    # ])
    # row = ft.Row(controls = [
    #     new_task,
    #     btn
    # ])
    # col = ft.Column(controls = [
    #     row,
    #     tasks_view
    # ])
    # page.add(row)
    # page.add(col)

    # page.add(ft.FloatingActionButton(icon = ft.icons.ADD, on_click = add_clicked))

ft.app(target = main)