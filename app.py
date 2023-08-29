import flet as ft

def main(page:ft.Page):
    page.title = "헬로 유아이"
  
    def on_click_handler(e):
        print("버튼이 눌렸습니다.", text_field.value)
        row.controls.append(ft.Text(text_field.value))
        col.controls.append(ft.Text(text_field.value))
        text_field.value = ""
        page.update()


    page.add(ft.Text("안녕하세요"))
    row = ft.Row()
    col = ft.Column()
    page.add(row)
    page.add(col)

    text_field = ft.TextField(hint_text = "이름을 입력하세요.", on_submit = on_click_handler)

    page.add(text_field)

    page.add(ft.ElevatedButton("눌러봐", on_click = on_click_handler))

    page.update()


ft.app(target = main)