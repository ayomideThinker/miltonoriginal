function check() {
    var c = 0;
    // var q1 = document.quiz.question1.value;
    // var q2 = document.quiz.question2.value;
    // var q3 = document.quiz.question3.value;
    // var q4 = document.quiz.question4.value;
    // var q5 = document.quiz.question5.value;
    var q6 = document.quiz.question6.value;
    var q7 = document.quiz.question7.value;
    var q8 = document.quiz.question8.value;
    var q9 = document.quiz.question9.value;
    var q10 = document.quiz.question10.value;
    var result = document.getElementById('result');
    // if (q1 == "generous") {c++}
    // if (q2 == "dilligence") {c++}
    // if (q3 == "humble") {c++}
    // if (q4 == "popular") {c++}
    // if (q5 == "indifferent") {c++}
    if (q6 == "with") {c++}
    if (q7 == "is being considered") {c++}
    if (q8 == "In spite of") {c++}
    if (q9 == "away") {c++}
    if (q10 == "In the event of") {c++}
    
    result.textContent = `${c}`;
}