<?php

if (isset($_GET["run"])) {
	$output = shell_exec("python3 " . __DIR__ . "/../model/dock_advice.py 2>/dev/null");
	/*$matches;
	preg_match("/^The boat should (.*) today$/", $output, $matches);
	$shouldDock = $matches[1] == "should";*/
	
	?><pre><?php echo $output; ?></pre><?php
} else if (isset($_GET["graph"])) {
	/*$data = file_get_contents("prediction_graph_output.png") or die("Failed to get graph");
	echo $data;
	die();*/
	?>
	<img src="prediction_graph_output.png" />
	<?php
} else {
	?>
	<a href=".?run">Run</a><br/>
	<a href=".?graph">Graph (run first, large download)</a>
	<?php
}
