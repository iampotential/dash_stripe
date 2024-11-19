# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class StripeDash(Component):
    """A StripeDash component.


Keyword arguments:

- id (string; optional)

- amount (number; optional)

- customConfirmMessage (string; optional)

- errorMessage (string; optional)

- label (string; required)

- paymentIntentId (string; optional)

- paymentMethodDetails (string; optional)

- paymentMethodId (string; optional)

- paymentStatus (string; optional)

- prePaymentMessage (string; optional)

- referenceId (string; optional)

- stripe_api (string; required)

- stripe_key (string; required)

- termsLink (string | a list of or a singular dash component, string or number; optional)"""
    _children_props = ['termsLink']
    _base_nodes = ['termsLink', 'children']
    _namespace = 'stripe_dash'
    _type = 'StripeDash'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.REQUIRED, paymentStatus=Component.UNDEFINED, errorMessage=Component.UNDEFINED, paymentMethodId=Component.UNDEFINED, referenceId=Component.UNDEFINED, paymentMethodDetails=Component.UNDEFINED, paymentIntentId=Component.UNDEFINED, customConfirmMessage=Component.UNDEFINED, amount=Component.UNDEFINED, prePaymentMessage=Component.UNDEFINED, stripe_key=Component.REQUIRED, stripe_api=Component.REQUIRED, termsLink=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'amount', 'customConfirmMessage', 'errorMessage', 'label', 'paymentIntentId', 'paymentMethodDetails', 'paymentMethodId', 'paymentStatus', 'prePaymentMessage', 'referenceId', 'stripe_api', 'stripe_key', 'termsLink']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'amount', 'customConfirmMessage', 'errorMessage', 'label', 'paymentIntentId', 'paymentMethodDetails', 'paymentMethodId', 'paymentStatus', 'prePaymentMessage', 'referenceId', 'stripe_api', 'stripe_key', 'termsLink']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['label', 'stripe_api', 'stripe_key']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(StripeDash, self).__init__(**args)
