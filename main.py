import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    
    def adicionar_tarefa(e):
        if not campo_tarefa.value:
            campo_tarefa.error_text = "Por favor, insira uma tarefa"
            page.update()
            return
        
        nova_tarefa = ft.Checkbox(label=campo_tarefa.value, value=False)
        lista_tarefas.controls.append(nova_tarefa)
        
        campo_tarefa.value = ""
        campo_tarefa.error_text = None
        campo_tarefa.focus()
        page.update()
    
    campo_tarefa = ft.TextField(
        label="Nova tarefa",
        hint_text="O que você precisa fazer?",
        expand=True,
        on_submit=adicionar_tarefa  # Permite adicionar tarefa pressionando Enter
    )
    
    botao_adicionar = ft.ElevatedButton(
        text="Adicionar",
        icon="add",
        on_click=adicionar_tarefa
    )
    
    controles_entrada = ft.Row(
        controls=[
            campo_tarefa,
            botao_adicionar
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    lista_tarefas = ft.Column()
    titulo = ft.Text("Minha Lista de Tarefas", size=32, weight=ft.FontWeight.BOLD)
    subtitulo = ft.Text("Adicione suas tarefas abaixo:", size=16)
    
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    titulo,
                    subtitulo,
                    ft.Divider(),
                    controles_entrada,
                    ft.Divider(),
                    ft.Text("Tarefas:", size=20, weight=ft.FontWeight.W_500),
                    lista_tarefas
                ],
                spacing=20
            ),
            padding=20
        )
    )
    
    campo_tarefa.focus()
    page.update()

ft.app(target=main)
