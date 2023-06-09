function validatePhoneNumber() {
  var phoneNumberInput = document.getElementById('id_phoneNumber');
  var phoneNumber = phoneNumberInput.value;
  var pattern = /^\+375\ \d{2}\ \d{3}\-\d{2}\-\d{2}$/;
  var errorSpan = document.getElementById('phone-error');

  if (phoneNumber !== '' && !pattern.test(phoneNumber)) {
    errorSpan.textContent = 'Неверный формат номера телефона';
    phoneNumberInput.focus();
    return false;
  }
  return true;
}

function goBack() {
  window.history.back();
}
document.addEventListener('DOMContentLoaded', function() {
        // Ваш код с добавлением обработчика события
        var passwordInput = document.getElementById('password');
        var showPasswordButton = document.getElementById('show-password');

        showPasswordButton.addEventListener('mousedown', function() {
            passwordInput.type = 'text';
        });

        showPasswordButton.addEventListener('mouseup', function() {
            passwordInput.type = 'password';
        });
    });