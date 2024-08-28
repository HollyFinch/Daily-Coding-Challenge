<?php

function calc($input1, $input2, $operator)
{
    switch ($operator) {
        case "+":
            return $input1 + $input2;
        case "-":
            return $input1 - $input2;
        case "*":
            return $input1 * $input2;
        case "/":
            return $input2 != 0 ? $input1 / $input2 : "BEEEEEEP!!!! DIVISION BY ZERO";
        case "mod":
            return $input1 % $input2;
        case "root":
            return sqrt($input1);
        default:
            return "BEEEEEEP!!!! INVALID OPERATOR";
    }
}

do {
    $operator = readline("Please type +, -, *, /, mod, or root : ");
    if (!in_array($operator, ['+', '-', '*', '/', 'mod', 'root'])) {
        echo "nope\n";
    } else {
        $input1 = readline("Please enter the first value: ");
        $input2 = ($operator !== "root") ? readline("Please enter the second value: ") : null;
        $result = calc($input1, $input2, $operator);
        echo $result . "\n";
        break;
    }
} while (true);
