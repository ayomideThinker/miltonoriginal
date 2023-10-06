function check() {
    var c = 0;
    var q1 = document.quiz.question1.value;
    var q2 = document.quiz.question2.value;
    var q3 = document.quiz.question3.value;
    var q4 = document.quiz.question4.value;
    var q5 = document.quiz.question5.value;
    var q6 = document.quiz.question6.value;
    var q7 = document.quiz.question7.value;
    var q8 = document.quiz.question8.value;
    var q9 = document.quiz.question9.value;
    var q10 = document.quiz.question10.value;
    var result = document.getElementById('result');
    if (q1 == "4cm<sup>2</sup>") {c++}
    if (q2 == "D8,000.00") {c++}
    if (q3 == "3.5cm") {c++}
    if (q4 == "180cm") {c++}
    if (q5 == "7") {c++}
    if (q6 == "(3x - y)(x + 7y)") {c++}
    if (q7 == "3") {c++}
    if (q8 == "2√13") {c++}
    if (q9 == "80<sup>0</sup>") {c++}
    if (q10 == "69<sup>0</sup>") {c++}
    
    result.textContent = `${c}`;
}