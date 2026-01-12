"""Patched clarifier unit model to support MCAS property packages."""

from idaes.core import declare_process_block_class
from pyomo.environ import units as pyunits
from watertap.unit_models.clarifier import ClarifierData


@declare_process_block_class("PatchedClarifier")
class PatchedClarifierData(ClarifierData):
    """Clarifier with electricity constraint using state block flow."""

    def build(self):
        super().build()

        if hasattr(self, "rule_electricity_consumption"):
            self.del_component(self.rule_electricity_consumption)

        state_block = getattr(self, "mixed_state", None)
        if state_block is None:
            state_block = getattr(self, "inlet_state", None)
        if state_block is None:
            raise AttributeError(
                "PatchedClarifier requires mixed_state or inlet_state with flow_vol."
            )

        @self.Constraint(
            self.flowsheet().time,
            doc="Constraint for electricity consumption based on inlet volume flow",
        )
        def rule_electricity_consumption(self, t):
            return self.electricity_consumption[t] == (
                self.energy_electric_flow_vol_inlet
                * pyunits.convert(
                    state_block[t].flow_vol,
                    to_units=pyunits.m**3 / pyunits.hr,
                )
            )
