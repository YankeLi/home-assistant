"""
Support for INSTEON PowerLinc Modem.

For more details about this component, please refer to the documentation at
https://home-assistant.io/components/insteon_plm/
"""
import asyncio
import logging

_LOGGER = logging.getLogger(__name__)


@asyncio.coroutine
def async_setup(hass, config):
    """Setup the insteon_plm component.

    This component is depreciated as of release 0.77 and should be removed in
    release 0.90.
    """
    _LOGGER.warning('The insteon_plm comonent has been replaced by '
                    'the insteon component')
    _LOGGER.warning('Please see https://home-assistant.io/components/insteon')

    hass.components.persistent_notification.create(
        'insteon_plm has been replaced by the insteon component.<br />'
        'Please see https://home-assistant.io/components/insteon',
        title='insteon_plm Component Deactivated',
        notification_id='insteon_plm')

    return False
