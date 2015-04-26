<?php
session_start();
$user = $_SESSION["user"];

	$db	=	new	mysqli("localhost","root","","assignment3");
	if ($db->connect_error) {
		print "Error - Could not connect to MySQL";
		exit;
	}

$t_id = $_POST["ticket"];
$query1 = "select tickets.status from tickets where tickets.ticket_id = $t_id";
$current_status = $db->query($query1)->fetch_array()[0];

if ($current_status == 1) {
	$query2 = "update tickets set status=0 where tickets.ticket_id = $t_id";
	$db->query($query2);
	echo "0";
}

if ($current_status ==0) {
	$query2 = "update tickets set status=1 where tickets.ticket_id = $t_id";
	$db->query($query2);
	echo "1";
}
?>