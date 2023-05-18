// Login page JavaScript
  const loginForm = document.querySelector('form');
  const username = document.querySelector('#username');
  const password = document.querySelector('#password');
  const error = document.querySelector('.error');
  
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (username.value === '' || password.value === '') {
      error.innerHTML = 'Please enter username and password';
    } else if (username.value !== 'admin' || password.value !== 'password') {
      error.innerHTML = 'Invalid username or password';
    } else {
      loginForm.submit();
    }
  });


// Add student form validation
const addStudentForm = document.querySelector('#add-student-form');
const nameInput = document.querySelector('#name');
const classInput = document.querySelector('#class');
const addressInput = document.querySelector('#address');
const feePaidInput = document.querySelector('#fee_paid');
const feePendingInput = document.querySelector('#fee_pending');
const addStudentErrorLabel = document.querySelector('#add-student-error-label');

addStudentForm.addEventListener('submit', (event) => {
  event.preventDefault();

  if (nameInput.value === '' || classInput.value === '' || addressInput.value === '' || feePaidInput.value === '' || feePendingInput.value === '') {
    addStudentErrorLabel.textContent = 'All fields are required';
  } else if (isNaN(Number(feePaidInput.value)) || isNaN(Number(feePendingInput.value))) {
    addStudentErrorLabel.textContent = 'Fee paid and fee pending must be numbers';
  } else if (Number(feePaidInput.value) + Number(feePendingInput.value) <= 0) {
    addStudentErrorLabel.textContent = 'Fee paid and fee pending must be positive numbers';
  } else {
    // Submit form if validation passes
    addStudentForm.submit();
  }
});

// Reset error messages on input change
const inputs = document.querySelectorAll('input');

inputs.forEach(input => {
  input.addEventListener('input', () => {
    errorLabel.textContent = '';
    addStudentErrorLabel.textContent = '';
  });
});
