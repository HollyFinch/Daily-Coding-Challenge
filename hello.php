<?php

function calc($input1, $input2, $operator)
{
    switch ($operator) {
        case "+":
            return $input1 + $input2;
        case "-":
            return $input1 - $input2;
        default:
            return "BEEEEEEP!!!! INVALID OPERATOR";
    }
}

$operator = readline("Please type + or - : ");
$input1 = readline("Please enter the first value: ");
$input2 = readline("Please enter the second value: ");

$result = calc($input1, $input2, $operator);

echo $result;
