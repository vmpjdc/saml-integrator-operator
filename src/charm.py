#!/usr/bin/env python3

# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""SAML Integrator Charm service."""

from ops.charm import CharmBase


class SAMLIntegratorOperatorCharm(CharmBase):
    """Charm for SAML Integrator on kubernetes."""

    def __init__(self, *args):
        """Construct.

        Args:
            args: Arguments passed to the CharmBase parent constructor.
        """
        super().__init__(*args)
