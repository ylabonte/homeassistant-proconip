"""ProconipEntity class"""
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import ATTRIBUTION
from .const import DOMAIN
from .const import NAME
from .const import MANUFACTURER
from .const import VERSION


class ProconipEntity(CoordinatorEntity):
    """Proconip entity."""

    def __init__(self, coordinator, config_entry):
        """Initialize new entity."""
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return self.config_entry.entry_id

    @property
    def device_info(self):
        """Get device info."""
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": MANUFACTURER,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": str(self.coordinator.data.get("id")),
            "integration": DOMAIN,
        }
