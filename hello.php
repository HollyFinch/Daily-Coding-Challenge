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
        case "%":
            return $input1 % $input2;
        case "√":
            return sqrt($input1);
        default:
            return "BEEEEEEP!!!! INVALID OPERATOR";
    }
}

$operator = readline("Please type +, -, *, /, %, or √ : ");
$input1 = readline("Please enter the first value: ");
$input2 = ($operator !== "√") ? readline("Please enter the second value: ") : null;

$result = calc($input1, $input2, $operator);

echo $result;
