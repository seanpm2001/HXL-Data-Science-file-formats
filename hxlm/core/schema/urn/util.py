"""hxlm.core.schema.urn.util is (TODO: document this)
"""

import os

__all__ = ['get_urn_vault_local_info']


# TODO: move these variables to somewere else
HXLM_CONFIG_BASE = os.getenv(
    'HXLM_CONFIG_BASE', os.getenv('HOME') + '/.config/hxlm/')

HXLM_DATA_POLICY_BASE = os.getenv(
    'HXLM_DATA_POLICY_BASE', os.getenv('HOME') + '/.config/hxlm/policy/')

HXLM_DATA_VAULT_BASE = os.getenv(
    'HXLM_DATA_VAULT_BASE', os.getenv('HOME') + '/.local/var/hxlm/data/')

HXLM_DATA_VAULT_BASE_ALT = os.getenv('HXLM_DATA_VAULT_BASE_ALT')
HXLM_DATA_VAULT_BASE_ACTIVE = os.getenv(
    'HXLM_DATA_VAULT_BASE_ACTIVE', HXLM_DATA_VAULT_BASE)


# from typing import (
#     Union
# )

# import json
# import yaml

# from hxlm.core.model.meta import (
#     HMeta
# )
# from hxlm.core.schema.vocab import (
#     ItemHVocab
# )

# __all__ = ['export_schema_yaml', 'export_schema_json', 'get_schema',
#            'get_schema_as_hmeta', 'get_schema_vocab']
# TODO: This path is obvlously hardcoded. Generalize it.
#       https://stackoverflow.com/questions/4028904
#       /how-to-get-the-home-directory-in-python

# _HXLM_BASE = str(Path.home() + "/.config/hxlm/"
# HXLM_CORE_URN_DATA_BASE_DEFAULT = str(Path.home() + "/.config/hxlm/urn/data/"

def is_urn_data_prepared(exact_path: str = None, required: bool = False):
    if exact_path:
        if not os.path.exists(exact_path) and required:
            raise RuntimeError('Path [' + exact_path + '] required')
        return exact_path
    if HXLM_DATA_VAULT_BASE and os.path.exists(HXLM_DATA_VAULT_BASE):
        return HXLM_DATA_VAULT_BASE
    if HXLM_DATA_VAULT_BASE_ALT and os.path.exists(HXLM_DATA_VAULT_BASE_ALT):
        return HXLM_DATA_VAULT_BASE_ALT
    if HXLM_DATA_VAULT_BASE_ALT and os.path.exists(HXLM_DATA_VAULT_BASE_ALT):
        return HXLM_DATA_VAULT_BASE_ALT
    if required:
        raise RuntimeError(
            'Path HXLM_DATA_VAULT_BASE ['
            + str(HXLM_DATA_VAULT_BASE) + '] or ' +
            'HXLM_DATA_VAULT_BASE_ALT [' + str(HXLM_DATA_VAULT_BASE_ALT) +
            '] required for this operation. Aborting.')
    return None


def debug_local_data(judistiction: str, organization: str):
    print('is_urn_data_prepared', is_urn_data_prepared(required=True))
    print('HXLM_CONFIG_BASE', HXLM_CONFIG_BASE)
    print('HXLM_DATA_POLICY_BASE', HXLM_DATA_POLICY_BASE)
    print('HXLM_DATA_VAULT_BASE', HXLM_DATA_VAULT_BASE)
    print('HXLM_DATA_VAULT_BASE_ALT', HXLM_DATA_VAULT_BASE_ALT)
    print('HXLM_DATA_VAULT_BASE_ACTIVE', HXLM_DATA_VAULT_BASE_ACTIVE)
    print('TODO: get_urn_vault_local_info', judistiction, organization)


def get_urn_vault_local_info(judistiction: str, organization: str):
    print('HXLM_CONFIG_BASE', HXLM_CONFIG_BASE)
    print('HXLM_DATA_POLICY_BASE', HXLM_DATA_POLICY_BASE)
    print('HXLM_DATA_VAULT_BASE', HXLM_DATA_VAULT_BASE)
    print('HXLM_DATA_VAULT_BASE_ALT', HXLM_DATA_VAULT_BASE_ALT)
    print('HXLM_DATA_VAULT_BASE_ACTIVE', HXLM_DATA_VAULT_BASE_ACTIVE)
    print('TODO: get_urn_vault_local_info', judistiction, organization)
