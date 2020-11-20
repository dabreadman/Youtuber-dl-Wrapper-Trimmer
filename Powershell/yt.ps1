$strT = Read-Host 'Start Time'
$endT = Read-Host 'End Time'
$url = Read-Host 'URL'

function formatInputTime($strT){
	$time = "";
	for($i=0;$i -lt 6;$i++){
		$time = $time + $strT[$i];
		if($i%2 -eq 1 -and $i -ne 5) {
			$time = $time + ':';
		}
	}
	return $time;
}

& D:\Youtube-DLG\youtube-dl.exe --extract-audio --audio-format mp3 --postprocessor-args "-ss $(formatInputTime($strT)) -to $(formatInputTime($endT))" $url  -o 'D:\Music\%(title)s.%(ext)s' | out-null

write-host "Done"
