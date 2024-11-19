# AUTO GENERATED FILE - DO NOT EDIT

#' @export
stripeDash <- function(id=NULL, amount=NULL, customConfirmMessage=NULL, errorMessage=NULL, label=NULL, paymentIntentId=NULL, paymentMethodDetails=NULL, paymentMethodId=NULL, paymentStatus=NULL, prePaymentMessage=NULL, referenceId=NULL, stripe_api=NULL, stripe_key=NULL, termsLink=NULL) {
    
    props <- list(id=id, amount=amount, customConfirmMessage=customConfirmMessage, errorMessage=errorMessage, label=label, paymentIntentId=paymentIntentId, paymentMethodDetails=paymentMethodDetails, paymentMethodId=paymentMethodId, paymentStatus=paymentStatus, prePaymentMessage=prePaymentMessage, referenceId=referenceId, stripe_api=stripe_api, stripe_key=stripe_key, termsLink=termsLink)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'StripeDash',
        namespace = 'stripe_dash',
        propNames = c('id', 'amount', 'customConfirmMessage', 'errorMessage', 'label', 'paymentIntentId', 'paymentMethodDetails', 'paymentMethodId', 'paymentStatus', 'prePaymentMessage', 'referenceId', 'stripe_api', 'stripe_key', 'termsLink'),
        package = 'stripeDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
