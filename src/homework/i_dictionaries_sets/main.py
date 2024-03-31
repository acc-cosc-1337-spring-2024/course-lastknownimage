RECORD_DELETED = {'widgets': '', 'quantities': []}

def add_widget(widgets, widget_name, quantity):
    if not widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity

def remove_inventory_widget(widget_name, widgets):
    if widget_name in widgets:
        RECORD_DELETED.append(widget_name)
        widgets.pop(widget_name)
        return RECORD_DELETED
    else:
        return 'Item not found'