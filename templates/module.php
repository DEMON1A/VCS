<?php
error_reporting(0);
include('utils/php/outputFunction.php');

$linesCount = 0;
$issuesFound = False;

$filePath = $argv[1];
$fileLines = fopen($filePath , "r");

while (( !feof($fileLines) )) {
    $line = fgets($fileLines);
    $line = preg_replace('~[\r\n]+~', '', $line);
    $linesCount++;

    /*
    your scan code here
    */
}

fclose($fileLines);
if (!$issuesFound) { returnFalse(); }
?>
