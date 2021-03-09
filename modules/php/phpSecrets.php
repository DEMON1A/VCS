<?php
error_reporting(0);
include('utils/php/outputFunction.php');

$linesCount = 0;
$issuesFound = False;

$filePath = $argv[1];
$fileLines = fopen($filePath , "r");

$secretsList = array(
    "GITHUB_TOKEN",
    "SLACK_WEBHOOK",
    "API_KEY",
    "DB_PASSWORD",
    "DB_USERNAME",
    "DISCORD_WEBHOOK",
    "API_TOKEN",
    "DB_HOST",
    "JIRA_PASSWORD",
    "FTP_PASSWORD",
    "AUTHORIZE_TOKEN",
    "SECRET_KEY",
    "SECRET_TOKEN",
);

while (( !feof($fileLines) )) {
    $line = fgets($fileLines);
    $line = preg_replace('~[\r\n]+~', '', $line);
    $linesCount++;

    $parsedString = str_replace(' ', '', $line);
    $parsedString = strtoupper($parsedString);

    foreach ( $secretsList as $secret => $secretItem ){
        if ( strpos($parsedString, $secretItem) !== false ) {
            showIssue("info" , $linesCount , $line , "Possible Hardcoded Secrets On The Code.");
            $issuesFound = true;
        }
    }
}

fclose($fileLines);
if (!$issuesFound) { returnFalse(); }
?>
