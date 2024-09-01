<?php

$setNumber = mt_rand(1, 100);
$numberOfGuesses = 0;
do {
    $playerInput = readline("Please guess a number from 1 to 100:  \n");
    $numberOfGuesses++;

    if ($setNumber - $playerInput > 0):
        echo ("The number is too low.\n");
    elseif ($setNumber - $playerInput < 0):
        echo ("The number is too high.\n");
    else:
        echo ("You guessed correctly!\n");
        echo "It took you $numberOfGuesses guesses.\n";
        break;
    endif;
} while (true);
