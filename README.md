# `behave_odoo`

behave_odoo is a Python package that provides a collection of helper functions designed to simplify the process of writing [behave](https://github.com/behave) tests for Odoo applications. The package includes functions for navigating the Odoo interface, interacting with form fields, and performing common actions within the Odoo environment.

## Installation

To install behave_odoo, use pip:

```shell
pip install behave_odoo
```

## Usage

To use the behave_odoo in your project, simply import the functions you need:

```python
from behave_odoo import (
    is_tree_view_by_column_name,
    login,
    navigate_menu,
    switch_module,
    click_button,
    set_text_field,
    set_select_field,
    set_autocomplete_field,
    ensure_readonly_mode,
    select_dropdown_item,
    switch_form_tab,
    get_first_fields_from_tree_view,
)
```

Or use it with prefix:

```python
import behave_odoo as bodoo

@given('the user log in on the Odoo Instance')
def step_impl(context):
    bodoo.login(context)
```

Refer to the package's [documentation](https://coopdevs.github.io/behave_odoo/) for detailed information on each function and how to use them in your tests.

## Contributing

We welcome contributions to the behave_odoo project. If you find a bug or would like to request a new feature, please open an issue on the [project's issue tracker](https://github.com/coopdevs/behave_odoo/issues). If you would like to contribute code, please fork the repository and submit a pull request.

## License

behave_odoo is released under the AGPL-3.0 License. See the `LICENSE` file for more information.

## Support

If you encounter any issues while using behave_odoo, please report them on the project's issue tracker.
