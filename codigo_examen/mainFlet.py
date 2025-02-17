import flet as ft
def main(page: ft.Page):
    page.title = "Gestió d'Usuaris"
    
    menu = ft.MenuBar(
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Usuaris"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Afegir"),
                        on_click=lambda e: page.open(dlg_modal)

                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Modificar"),
                        on_click=lambda e: page.open(dlg_modal2)

                    ),

                ]
            )
        ]
    )
    dlg_modal = ft.AlertDialog(
        modal=True,
        content=ft.Text("Vols afegir?"),
        actions=[
            ft.TextButton("Yes", on_click=page.close),
            ft.TextButton("No", on_click=page.close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    dlg_modal2 = ft.AlertDialog(
        modal=True,
        content=ft.Text("Vols afegir?"),
        actions=[
            ft.TextButton("Yes", on_click=page.close),
            ft.TextButton("No", on_click=page.close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    user_table = ft.DataTable(
        
        columns=[
            ft.DataColumn(label=ft.Text("Nom")),
            ft.DataColumn(label=ft.Text("Contrasenya")),
            ft.DataColumn(label=ft.Text("Rol"))
        ],
        rows=[]
    )
    eliminar = ft.TextButton("Eliminar")
    page.add(menu, eliminar, user_table)

ft.app(target=main)




# import flet as ft


# def main(page: ft.Page):
#     page.title = "Gestió d'Usuaris"
    
#     menu = ft.MenuBar(
#         controls=[
#             ft.SubmenuButton(
#                 content=ft.Text("Usuaris"),
#                 controls=[
#                     ft.MenuItemButton(
#                         content=ft.Text("Afegir"),

#                     ),
#                     ft.MenuItemButton(
#                         content=ft.Text("Modificar"),

#                     ),

#                 ]
#             )
#         ]
#     )
    
#     user_table = ft.DataTable(
        
#         columns=[
#             ft.DataColumn(label=ft.Text("Nom")),
#             ft.DataColumn(label=ft.Text("Contrasenya")),
#             ft.DataColumn(label=ft.Text("Rol"))
#         ],
#         rows=[]
#     )
    
#     page.add(menu, user_table)

# ft.app(target=main)
