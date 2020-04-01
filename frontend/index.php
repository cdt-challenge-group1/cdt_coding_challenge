<?php

if (isset($_GET["run"])) {
	$output = shell_exec("python3 " . __DIR__ . "/../model/dock_advice.py 2>/dev/null");
	/*$matches;
	preg_match("/^The boat should (.*) today$/", $output, $matches);
	$shouldDock = $matches[1] == "should";*/
	
	?><pre><?php echo $output; ?></pre><?php
} else {
	?>
	<a href=".?run">Re-run</a><br/>
	<br/>
	<img src="prediction_graph_output.svg" width="100%" height="100%" />
	<?php
}
