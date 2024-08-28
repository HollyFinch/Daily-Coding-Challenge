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

        // Check if input1 is a number
        if (!is_numeric($input1)) {
            echo "nope\n"; // Output "nope" immediately for non-numeric input1
        } else {
            $input2 = ($operator !== "root") ? readline("Please enter the second value: ") : null;

            // Check if input2 is a number only if operator is not "root"
            if ($operator !== "root" && !is_numeric($input2)) {
                echo "nope\n";
            } else {
                $result = calc($input1, $input2, $operator);
                echo $result . "\n";
                break;
            }
        }
    }
} while (true);
