<?php

function showIssue($Serverity , $lineCount , $Line , $Message) {
    $Line = preg_replace(',' , 'COMMA' , $Line)
    echo $Serverity . ',' . $lineCount . ',' . $Line . ',' . $Message;
}

function returnFalse() {
    echo "False";
}

?>
