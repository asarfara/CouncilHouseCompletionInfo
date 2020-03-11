class CouncilInfo:
    def __init__(self, occupancy_permit: bool, nbn_installed: bool):
        """
        Create a council info object.
        Args:
            occupancy_permit (bool): Occupancy permit granted.
            nbn_installed (bool): NBN installed.
        """

        self.occupancy_permit = occupancy_permit
        self.nbn_installed = nbn_installed