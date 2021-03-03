"""hxlm.core.schema

TODO: document me
"""
# TODO: https://en.wikipedia.org/wiki/Standard_operating_procedure

# https://www.jsonschemavalidator.net/
# https://json-schema.org/

from hxlm.core.schema.conversor import (  # noqa: F401
    ConversorHSchema
)

# from hxlm.core.schema.util import *
from hxlm.core.schema.util import (  # noqa: F401
    export_schema_yaml,
    export_schema_json,
    get_schema,
    get_schema_as_hmeta,
    get_schema_vocab
)
# from hxlm.core.schema.conversor import *
