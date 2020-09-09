from typing import Tuple
from flasgger import swag_from


@swag_from('swagger_doc/testsubmodule_get.yml')
def testsubmodule() -> Tuple[str, int]:
    return '', 200