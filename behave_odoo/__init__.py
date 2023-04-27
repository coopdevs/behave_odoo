"""
`behave_odoo` is a Python package that provides a collection of helper functions designed to simplify the process of writing behave tests for Odoo applications. 

The package includes functions for navigating the Odoo interface, interacting with form fields, and performing common actions within the Odoo environment.


```python
import behave_odoo as bodoo

@given('the user log in on the Odoo Instance')
def step_impl(context):
    bodoo.login(context)
```

"""
from .behave_odoo import (
    login,
    click_menu_item,
    navigate_menu,
    set_text_field,
    set_select_field,
    set_autocomplete_field,
    select_dropdown_item,
    click_button,
    switch_form_tab,
    ensure_readonly_mode,
    get_first_fields_from_tree_view,
    is_tree_view_by_column_name,
    switch_module,
    click_smart_button,
)

__all__ = [
    "login",
    "click_menu_item",
    "navigate_menu",
    "set_text_field",
    "set_select_field",
    "set_autocomplete_field",
    "select_dropdown_item",
    "click_button",
    "switch_form_tab",
    "ensure_readonly_mode",
    "get_first_fields_from_tree_view",
    "is_tree_view_by_column_name",
    "switch_module",
    "click_smart_button",
]
