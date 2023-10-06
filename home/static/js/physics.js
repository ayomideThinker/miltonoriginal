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
    if (q1 == "diretion of current in the wire") {c++}
    if (q2 == "holes are the majority charge carriers") {c++}
    if (q3 == "size") {c++}
    if (q4 == "kilowatt-hour") {c++}
    if (q5 == "friction") {c++}
    if (q6 == "add-up to produce white light") {c++}
    if (q7 == "flute and the trumpet") {c++}
    if (q8 == "70.0") {c++}
    if (q9 == "330.0ms<sup>-1</sup>") {c++}
    if (q10 == "between the center of curvature and the focus") {c++}
    
    result.textContent = `${c}`;
}