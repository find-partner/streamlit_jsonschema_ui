import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_jsonschema_ui",
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend", "dist")
    print(build_dir)
    _component_func = components.declare_component(
        "streamlit_jsonschema_ui",
        path=build_dir
    )

def streamlit_jsonschema_ui(schema: dict, data=None, key=None):
    """Create a new instance of "streamlit_jsonschema_ui".

    Parameters
    ----------
    schema: jsonschema
        The jsonschema to be used for the ui
    data: dict, optional
        The data to be used for the ui
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    dict
        The number of times the component's "upload" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    if data is None:
        data = {}
    component_value = _component_func(schema=schema, data=data, key=key, default={})

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value