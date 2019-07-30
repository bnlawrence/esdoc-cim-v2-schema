def cmip_dataset():
    """
    A CMIP dataset
    """
    return {
        'type': 'class',
        'base': 'data.dataset',
        'is_abstract': False,
        'is_document': True,
        'pstr': ('{}', ('name',)),
        'properties': [
            # FIXME: Should we specialise the availability online reosurce rather than do this?
            ('drs_location', 'drs.drs_publication_dataset', '0.N',
             "DRS identifier of dataset."),
            ('originating_simulation', 'linked_to(activity.simulation)', '0.1',
             "Makes a link back to originating activity."),
        ]
    }


def cmip_simulation():
    """
    A CMIP simulation. In most CMIP cases this should be auto-generated
    from output dataset file headers.
    """

    return {
        'type': 'class',
        'base': 'activity.simulation',
        'is_abstract': False,
        'is_document': True,
        'pstr': "#FIXME: TBD",
        'properties': [
            # Ensemble member attributes
            # FIXME: There is a DRS class for this collection of attributes, join or not?
            ('realization_index', 'int', '0.1',
             'realization number, e.g. 5'),
            ('initialization_index', 'int', '0.1',
             'Index variant of initialization method, e.g. 1'),
            ('physics_index', 'int', '0.1',
             'index for model physics, e.g. 3'),
            ('forcing_index', 'int', '0.1',
             'index for variant of forcing, e.g. 2'),
            ('variant_info', 'str', '0.1',
             'description of run variant differences, e.g. forcing: black carbon aerosol only'),
        ]
    }