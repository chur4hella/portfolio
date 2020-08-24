let username = document.querySelector('#username'),
    usernameError = document.querySelector('#error-username'),
    email = document.querySelector('#email'),
    emailError = document.querySelector('#error-email'),
    CSRFToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
    requestCategories = {
        1: 'username',
        2: 'email',
        3: 'submit'
    };

const request = new XMLHttpRequest(), url = 'registration';

request.responseType = 'json';

function validationField(requestCategory, fieldValue) {
    const params = 'category=' + requestCategory + '&value=' + fieldValue;
    request.open('POST', url, true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.setRequestHeader("X-CSRFToken", CSRFToken);
    request.send(params);
}

function validationUsername() {
    let usernameVal = this.value;
    validationField(requestCategories[1], usernameVal);
}

function validationEmail(e){
    let emailVal = this.value, indexAt = emailVal.indexOf('@'), indexDot = emailVal.lastIndexOf('.'),
        errorMessage = 'Некорректный e-mail';

    if(emailVal < 1){
        this.classList.remove('form__field_verified', 'form__field_error');
        emailError.innerText = '';
    }else if((indexAt < 0 || indexDot < 0) ||
        ((indexAt > -1 && indexDot > -1) && (indexDot - indexAt < 2 || ((emailVal.length - 1) - indexDot) < 2))){
        email.classList.remove('form__field_verified');
        email.classList.add('form__field_error');
        emailError.innerText = errorMessage;
    }else {
        validationField(requestCategories[2], emailVal);
    }
}


request.addEventListener('readystatechange', function () {
    if(request.readyState == 4 && request.status == 200){
        let response = request.response, field = document.querySelector('#' + response.category),
            fieldError = document.querySelector('#error-' + response.category), error = 'error';
        if (error in response && field.value.length > 0){
            field.classList.remove('form__field_verified');
            field.classList.add('form__field_error');
            fieldError.innerText = response.error;
        }else if(!(error in response) && field.value.length > 0){
            field.classList.remove('form__field_error');
            fieldError.innerText = '';
            field.classList.add('form__field_verified');
        }else {
            field.classList.remove('form__field_verified', 'form__field_error');
            fieldError.innerText = '';
        }
    }

});
email.addEventListener('input', validationEmail);
username.addEventListener('input', validationUsername);
