"""
`behave_odoo` is a Python package that provides a collection of helper functions designed to simplify the process of writing behave tests for Odoo 14. 

The package includes functions for navigating the Odoo interface, interacting with form fields, and performing common actions within the Odoo environment.


```python
import behave_odoo as bodoo

@given('the user log in on the Odoo Instance')
def step_impl(context):
    bodoo.login(context)
```

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


# Login to Odoo

def login(context, **kwargs):
    """
    Login to Odoo.

    ```python
    bodoo.login(context)
    ```

    By default, it uses the following context variables from behave.ini:
    - odoo_url
    - odoo_username
    - odoo_password
    :param context: behave context
    """
    odoo_url = kwargs.get("odoo_url", context.odoo_url)
    odoo_username = kwargs.get("odoo_username", context.odoo_username)
    odoo_password = kwargs.get("odoo_password", context.odoo_password)

    context.browser.get(odoo_url + "/web")
    username_input = context.browser.find_element(By.NAME, "login")
    username_input.send_keys(odoo_username)
    password_input = context.browser.find_element(By.NAME, "password")
    password_input.send_keys(odoo_password)
    password_input.submit()


# Menu navigation

def click_menu_item(context, menu_text):
    """
    Clicks on the main menu item that contains the given text

    ```python
    bodoo.click_menu_item(context, "Sales")
    ```

    :param context: behave context
    :param menu_text: text to search for in the menu item
    """
    menu_item_xpath = \
        f"//a[contains(@class, 'dropdown-toggle') and contains(normalize-space(), '{menu_text}')]"

    menu_item = WebDriverWait(context.browser, 3).until(
        EC.element_to_be_clickable((By.XPATH, menu_item_xpath)))
    menu_item.click()


def navigate_menu(context, menu_text, submenu_text):
    """
    Navigates to the given submenu item

    ```python
    bodoo.navigate_menu(context, "Sales", "Orders")
    ```

    :param context: behave context
    :param menu_text: text of the menu item
    :param submenu_text: text of the submenu item
    """
    click_menu_item(context, menu_text)
    _click_submenu_item(context, submenu_text)


def _click_submenu_item(context, submenu_text):
    """
    Clicks on the submenu item with the given text

    :param context: behave context
    :param submenu_text: text to search for in the submenu item
    """
    submenu_item_xpath = \
        f"//a[contains(@class, 'dropdown-item')]/span[contains(normalize-space(), '{submenu_text}')]"
    submenu_item = WebDriverWait(context.browser, 3).until(
        EC.element_to_be_clickable((By.XPATH, submenu_item_xpath)))
    submenu_item.click()


# Form helpers
def set_text_field(context, field_name, value):
    """
    Sets the value of the text field with the given name
    
    ```python
    bodoo.set_text_field(context, "name", "John Doe")
    ```       

    :param context: behave
    :param field_name: label of the text field
    :param value: value to set
    """
    element = WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//input[contains(@name,'{field_name}')]"))
    )

    element.send_keys(value)


def set_select_field(context, select_item, option):
    """
    Set an option in a select field with the given name
    
    ```python
    bodoo.set_select_field(context, "country_id", "United States")
    ```       
        
    :param context: behave
    :param select_item: name of the select field
    :param option: (visible) value to set
    """
    select_element = WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//select[contains(@name, '{select_item}')]"))
    )
    select = Select(select_element)
    select.select_by_visible_text(option)


def set_autocomplete_field(context, field_name, chars):
    """
    Set an autocomplete (one2many, many2one, many2many) field.

    Introduce the characters and press tab to select the first highlighted option.
    
    ```python
    bodoo.set_autocomplete_field(context, "partner_id", "John Do")
    ```       
        
    :param context: behave
    :param field_name: name of the select field
    :param chars: string to enter prior to tab
    """

    autocomplete_input = WebDriverWait(context.browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//div[@name='{field_name}']//input[contains(@class, 'o_input')]"))
    )
    autocomplete_input.click()
    autocomplete_input.send_keys(chars)
    autocomplete_input.send_keys(Keys.TAB)


def select_dropdown_item(context, option_text):
    """
    Selects the dropdown item with the given text
    
    ```python
    bodoo.select_dropdown_item(context, "Delete")
    ```       
        
    :param context: behave context
    :param option_text: text of the dropdown item
    """
    option_element = WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//ul[@class='o_dropdown_menu dropdown-menu show']//a[contains(text(), '{option_text}')]"))
    )
    option_element.click()


def click_button(context, button_text):
    """
    Clicks on the button with the given text

    
    ```python
    bodoo.click_button(context, "Create")
    ```       
    
    :param context: behave context
    :param button_text: text of the button
    """
    # Buscar el elemento del botón por su texto
    button_element = WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located(
            (By.XPATH,
             f"//button[contains(text(), '{button_text}')] | //button//span[contains(text(), '{button_text}')]"))

    )

    # Hacer clic en el botón
    button_element.click()



def switch_form_tab(context, tab_name):
    """
    Switches to an Odoo tab in form view
    ```python
        bodoo.switch_form_tab(context, "Sales")
    ```    
    :param context: behave context
    :param tab_name: name of the tab to switch to
    """
    tab_xpath = f"//a[contains(normalize-space(), '{tab_name}') and @data-toggle='tab' and @role='tab']"
    WebDriverWait(context.browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, tab_xpath))
    ).click()


def ensure_readonly_mode(context):
    """
    Ensure that the current view is in readonly mode

    ```python
    bodoo.ensure_readonly_mode(context)
    ```    
    :param context: behave context
    """
    WebDriverWait(context.browser, 1).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(@class, 'o_form_button_edit')]"))
    )
    WebDriverWait(context.browser, 1).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'o_form_readonly')]"))
    )


# Tree view helpers

def get_first_fields_from_tree_view(context):
    """
    Returns the second td content (the first is the checkbox) of each row in the tree view

    ```python
    bodoo.get_first_fields_from_tree_view(context)
    ```    
    :param context: behave context
    :return: list of strings
    """
    elements = context.browser.find_elements(By.XPATH,
                                             "//div[contains(@class, 'o_list_view')]//table[contains(@class, 'o_list_table')]/tbody[contains(@class, 'ui-sortable')]/tr/td[2]")
    return [x.text for x in elements]


def is_tree_view_by_column_name(context, column_name):
    """
    Checks if the current view is a tree view and the second column has a given name.

    (The first column is the checkbox)

    ```python
    bodoo.is_tree_view_by_column_name(context, "Name")
    ```    
    :param context: behave context
    :param column_name: The name to check for in the second column
    :return: True if the conditions are met, False otherwise
    """
    try:
        WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//th[2][contains(text(), '{column_name}')]"))
        )
        return True
    except NoSuchElementException:
        return False

# Module helpers


def switch_module(context, module_name):
    """
    Switches to the given Odoo module (snake_case)

    ```python
    bodoo.switch_module(context, "sale_management")
    ```
    
    :param context: behave context
    :param module_name: name of the module
    """
    app_icon_found = _find_and_click_app_icon(context, module_name)

    if not app_icon_found:
        _open_drawer_if_exists(context)
        app_icon_found = _find_and_click_app_icon(context, module_name)
        if not app_icon_found:
            _find_and_click_module_in_dropdown(context, module_name)


def _find_and_click_app_icon(context, module_name):
    """
    Finds and clicks on the app icon with the given name
    :param context: behave context
    :param module_name: name of the module
    """
    try:
        app_icon = WebDriverWait(context.browser, 1).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[@class='oe_menu_text' and contains(text(), '{module_name}')]"))
        )
        app_icon.click()
        return True
    except Exception as e:
        pass


def _open_drawer_if_exists(context):
    """
    Opens the drawer if it exists
    :param context: behave context
    """
    try:
        WebDriverWait(context.browser, 1).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@data-toggle='dropdown']"))
        ).click()
        return True
    except Exception as e:
        return False


def _find_and_click_module_in_dropdown(context, module_name):
    """
    Finds and clicks on the module in the dropdown
    :param context: behave context
    :param module_name: name of the module (pascal_case)
    """
    xpath = "//a[contains(@class, 'dropdown-item o_app') and contains(text(), '{module_name}')]"

    WebDriverWait(context.browser, 3).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@data-menu-xmlid, '" + module_name + "')]")
        )).click()


# Untested functions


def click_smart_button(context, button_css_selector):
    """
    Clicks on the smart button with the given css selector
    :param context: behave context
    :param button_css_selector: css selector of the smart button
    (ALPHA: Untested)
    """
    button = WebDriverWait(context.browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, button_css_selector)))
    button.click()
