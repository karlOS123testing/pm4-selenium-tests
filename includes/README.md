# Files 

## Classes

[`/includes/test_classes.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/test_classes.py "test_classes.py")
Class | Extends | Changes
--- | --- | ---
`CustomTestSuite` | `unittest.TestSuite` | Add custom attributes
`CustomTestLoader` | `unittest.TestLoader` | Set custom `suiteClass`
`CustomTextTestResult` | `unittest.TextTestResult` | Add custom attributes to instantiation
`CustomTextTestRunner` | `unittest.TextTestRunner` | Set custom `resultclass`, add custom attributes, and set custom `_makeResult()`

[`/includes/test_parent.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/test_parent.py "test_parent.py")
Class | Function | Extends | Methods | Attributes
--- | --- | --- | --- | ---
`BaseTest` | Defines base test class | `unittest.TestCase` | <ul><li>`setUpClass()`: instantiates webdriver instance</li><li>`tearDownClass()`: closes webdriver instance</li></ul> | <ul><li>`log`: a list initialized with one item</li></ul>

[`/includes/element.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/element.py "element.py")
Class | Function | Methods | Attributes
--- | --- | --- | ---
`BasePageElement` | Defines base page element class | <ul><li>`__init__()`: instantiates class</li><li>`__set__()`: assigns value to a page element</li><li>`__get__()`: retrieves value of a page element</li></ul> | <ul><li>`element_type`: string that defines element type as `ID`, `NAME`, or `XPATH`</li></ul>

[`/includes/locators.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/locators.py "locators.py")
Class | Function | Attributes
--- | --- | ---
`BasePageLocators` | Defines page element locators | <ul><li>Global page elements:</li><li>`REQUESTS_LINK`: Request link element</li><li>`TASKS_LINK`: Tasks link element</li><li>`DESIGNER_LINK`: Designer link element</li><li>...</li></ul>
`LoginPageLocators` | Defines page element locators | <ul><li>Login page elements</li><li>`USERNAME`: Username field element</li><li>`PASSWORD`: Password field element</li><li>`LOGIN_BUTTON`: Login button element</li></ul>
`[...]PageLocators` | Defines page element locators | <ul><li>[...] page elements</li></ul>

[`/includes/page.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/page.py "page.py")
Class | Function | Extends | Methods | Attributes
--- | --- | --- | --- | ---
`BasePageShell` | Defines base page shell | ----- | <ul><li>`__init__()`: instantiates class with attributes</li><li>`go_to_page()`: navigates to `page_url`</li></ul> | <ul>instance attributes:<li>`driver`: webdriver instance created in `BaseTest`</li><li>`data`: configuration defined in Trogdor request or in local `__init__.py`</li><li>`page_url`: server url extracted from `data`</li></ul>
`BasePage` | Defines base page | `BasePageShell` | <ul><li>`click_requests_link()`: clicks on Requests link</li><li>`click_tasks_link()`: click on Tasks link</li><li>`click_designer_link()`: click on Designer link</li><li>`click_admin_link()`: click on Admin link</li><li>`click_avatar()`: click on avatar</li></ul> | -----
`UsernameFieldElement` | Defines username field element | `BasePageElement` | ----- | <ul><li>`locator`: element identifier</li></ul>
`PasswordFieldElement` | Defines password field element | `BasePageElement` | ----- | <ul><li>`locator`: element identifier</li></ul>
`LoginPage` | Defines login page | `BasePageShell` | <ul><li>`__init__()`: redefines `page_url`</li><li>`login()`: logs in to server</ul> | <ul>class attributes:<li>`username_field_element`: instance of `UsernameFieldElement`</li><li>`password_field_element`: instance of `PasswordFieldElement`</li></ul><ul>instance attributes:<li>`page_url`: extended from `BasePageShell` and redefined</li>
`RequestsPage` | Defines requests page | `BasePage` | <ul><li>`__init__()`: redefines `page_url`</li></ul> | <ul><li>`page_url`: extended from `BasePageShell` and redefined</li></ul>
`AdminPage` | Defines admin page | `BasePage` | <ul><li>`__init__()`: redefines `page_url`</li></ul> | <ul><li>`page_url`: extended from `BasePageShell` and redefined</li></ul>
`DesignerPage` | Defines designer page | `BasePage` | <ul><li>`__init__()`: redefines `page_url`</li></ul> | <ul><li>`page_url`: extended from `BasePageShell` and redefined</li></ul>

## Methods

[`/includes/util.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/util.py "util.py")
Method | Function | Parameters | Uses
--- | --- | --- | ---
`run_test` | <ul><li>Loads and runs test suite, redirects `unittest` results to memory stream</li><li>returns PM4-friendly output dictionary</li></ul> | `classname, data, modulename` | <ul><li>`classname` passes the test class name</li><li>`data` passes the configuration from PM4's config task</li><li>`modulename` passes `__main__` from test file</li></ul>
`parse_log_error`| <ul><li>Searches text for `'ERROR'`</li><li>returns `ERROR` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
`parse_log_warning`| <ul><li>Searches text for `'WARNING'`</li><li>returns `WARNING` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
`parse_results` | <ul><li>Searches unittest results for `.`, `E`, or `F`</li><li>returns `SUCCESS` or `FAIL`</li></ul> | `buffer` | <ul><li>`buffer` passes memory stream</li></ul>

