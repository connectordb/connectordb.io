var input = CodeMirror.fromTextArea(document.getElementById("input"), {
	matchBrackets: true,
	autoCloseBrackets: true,
	mode: "application/json",
	lineWrapping: true
});
var output = CodeMirror.fromTextArea(document.getElementById("output"), {
	matchBrackets: true,
	autoCloseBrackets: true,
	mode: "application/json",
	lineWrapping: true,
	readOnly: true
});

input.setValue(JSON.stringify(JSON.parse('[{"t": 1,"d": {"steps": 14,"activity": "walking"}},\
{"t": 2,"d": { "steps": 10,"activity": "running"}},\
{"t": 3,"d": {"steps": 12,"activity": "walking"}},\
{"t": 4,"d": {"steps": 5,"activity": "running"}}]'), null, 2));

output.setValue("Loading PipeScript...");


function runScript() {
	output.setValue("Running...");
	try {
		s = pipescript.Script($("#script").val());
		result = s.Run(input.getValue());
		output.setValue(result);
	} catch (e) {
		output.setValue(e.toString());
	}
}

$("#scriptbtn").click(function (e) {
	e.preventDefault();
	runScript();
});
