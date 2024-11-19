# AUTO GENERATED FILE - DO NOT EDIT

export stripedash

"""
    stripedash(;kwargs...)

A StripeDash component.

Keyword arguments:
- `id` (String; optional)
- `amount` (Real; optional)
- `customConfirmMessage` (String; optional)
- `errorMessage` (String; optional)
- `label` (String; required)
- `paymentIntentId` (String; optional)
- `paymentMethodDetails` (String; optional)
- `paymentMethodId` (String; optional)
- `paymentStatus` (String; optional)
- `prePaymentMessage` (String; optional)
- `referenceId` (String; optional)
- `stripe_api` (String; required)
- `stripe_key` (String; required)
- `termsLink` (String | a list of or a singular dash component, string or number; optional)
"""
function stripedash(; kwargs...)
        available_props = Symbol[:id, :amount, :customConfirmMessage, :errorMessage, :label, :paymentIntentId, :paymentMethodDetails, :paymentMethodId, :paymentStatus, :prePaymentMessage, :referenceId, :stripe_api, :stripe_key, :termsLink]
        wild_props = Symbol[]
        return Component("stripedash", "StripeDash", "stripe_dash", available_props, wild_props; kwargs...)
end

