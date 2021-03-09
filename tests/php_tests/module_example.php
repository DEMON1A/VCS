<?php
error_reporting(0);
$filePath = $argv[1];

if (!isset($filePath)) {
    echo "lol";
} else {
    include('function.php');
    test();
}
?>
