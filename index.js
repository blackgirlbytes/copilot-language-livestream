// validate a phone number
function validatePhone(phone) {
    const phoneRegex = /^(\+?1)?[2-9]\d{2}[2-9](?!11)\d{6}$/;
    return phoneRegex.test(phone)
}
console.log(validatePhone('8572611633')); // true