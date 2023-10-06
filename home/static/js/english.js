document.getElementById('quiz-form').addEventListener('submit', function(event) {
    var radioInputs = document.querySelectorAll('input[type="radio"]');
    var selectedOptions = Array.from(radioInputs).some(function(input) {
      return input.checked;
    });
  
    if (!selectedOptions) {
      event.preventDefault();
      alert('Note! All questions must be completed');
    }
  });
  