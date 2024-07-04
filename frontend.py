from fastapi import FastAPI

from nicegui import app, ui

current_items = []

app_version = '1.0.0'

def init(fastapi_app: FastAPI) -> None:
    @ui.page('/')
    def show():
        app.add_static_files('/static', 'static')

        ui.colors(primary='#16CFB1')

        with ui.header(elevated=True).style('background-image: linear-gradient(to right, rgba(22,207,177,1) , rgba(8,116,110,1);').classes('items-center justify-between'):
            ui.image("static/intel-tiber-dark.svg").props('width=100px')
            ui.label('Automated Self-Checkout')
            # NOTE dark mode will be persistent for each user across tabs and server restarts
            ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
            ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')

        columns = [
            {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
            #{'name': 'quantity', 'label': 'Quantity', 'field': 'quantity', 'sortable': True},
            {'name': 'price', 'label': 'Price', 'field': 'price', 'sortable': True},
        ]
        rows = current_items
        table = ui.table(columns=columns, rows=rows, row_key='name')
        total_price_label = ui.label(f'Total price: {sum(item["price"] for item in current_items)} $')
        total_price_label.style(add='font-size: 4vw;')
        ui.button('Pay with Credit Card').props('size=lg')

        with ui.footer().style('background-image: linear-gradient(to right, rgba(22,207,177,1) , rgba(8,116,110,1);'):
            ui.label(f"App version: {app_version}")
        

        def update_table():
            print(current_items)
            # if not current_items[-1]['name'] == 'Total':
            #     current_items.append({'name': 'Total', 'price': sum(item["price"] for item in current_items), 'quantity': sum(item["quantity"] for item in current_items)})
            #ui.label(f'Total price: {sum(item["price"] for item in current_items)}')
            table.rows = current_items
            total_price_label.text = f'Total price: {sum(item["price"] for item in current_items)} $'
            table.update()
            total_price_label.update()


        ui.timer(1.0, update_table)

    @ui.page('/defect-alarm')
    def show():
        app.add_static_files('/static', 'static')

        ui.colors(primary='#16CFB1')

        with ui.header(elevated=True).style('background-image: linear-gradient(to right, rgba(22,207,177,1) , rgba(8,116,110,1);').classes('items-center justify-between'):
            ui.image("static/intel-tiber-dark.svg").props('width=100px')
            ui.label('Automated Self-Checkout')
            # NOTE dark mode will be persistent for each user across tabs and server restarts
            ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
            ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')

        

        ui.footer().style('background-image: linear-gradient(to right, rgba(22,207,177,1) , rgba(8,116,110,1);')
        

        def update_state():
            print(current_items)
            table.rows = current_items
            total_price_label.text = f'Total price: {sum(item["price"] for item in current_items)} $'
            table.update()
            total_price_label.update()


        ui.timer(1.0, update_table)

    ui.run_with(
        fastapi_app,
        mount_path='/gui',  # NOTE this can be omitted if you want the paths passed to @ui.page to be at the root
        storage_secret='pick your private secret here',  # NOTE setting a secret is optional but allows for persistent storage per user
    )
