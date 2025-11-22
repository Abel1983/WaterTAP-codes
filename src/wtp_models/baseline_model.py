"""
Baseline Water Treatment Plant (WTP) model utilities.

You can move functions from your notebook into this file
to make them reusable across notebooks and scripts.
"""


def example_flow_balance(q_in: float, q_loss: float = 0.0) -> float:
    """
    Very simple example: compute outlet flow from an inlet and losses.

    Parameters
    ----------
    q_in : float
        Inlet flow rate (e.g. ML/d).
    q_loss : float, optional
        Flow losses (e.g. filter backwash, sludge wasting), by default 0.0.

    Returns
    -------
    float
        Outlet flow rate.
    """
    return q_in - q_loss
