<?php

function showIssue($Serverity , $lineCount , $Line , $Message) {
    echo $Serverity . ',' . $lineCount . ',' . $Line . ',' . $Message;
}

function returnFalse() {
    echo "False";
}

?>
