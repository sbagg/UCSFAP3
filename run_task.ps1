##################################################
##################################################
##################################################
##################################################
##################################################
################# Start of Powershell Script
##################################################
##################################################
##################################################
##################################################


##################################################
################# Set the varuables
################# 
##################################################
$email = Read-Host -Prompt 'Input your email to get CSV Report'
$fileCSV = '.\read_file.py '
$checkCSV = 'temp\incoming\users.csv'
$csv_file_cmd = $fileCSV + $email
$curDir = Get-Location
$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
$scriptPath = $scriptPath.Split(":")[1]


# $curDir = $curDir.ToString() + "\"
# $curDir = $curDir -split "C:"
# $curDir = $curDir -split " "
# $x = $curDir
Write-Host "$scriptPath"
##################################################
################# Registers the task in the system
################# 
##################################################
$taskName = "CSVFiltered"
$taskExists = Get-ScheduledTask | Where-Object {$_.TaskName -like $taskName }
if(-Not $taskExists){
    $PS_action = New-ScheduledTaskAction -Execute "python" -Argument $csv_file_cmd 
    $PS_trigger = New-ScheduledTaskTrigger -Once -At 3am
    Register-ScheduledTask -TaskName $taskName -TaskPath $scriptPath -Action $PS_action -Trigger $PS_trigger
}


##################################################
################# Start the Process Python Script
################# 
##################################################
if(Test-Path -Path $checkCSV){
    Start-Process "python" -ArgumentList $csv_file_cmd -WorkingDirectory $curDir
    Write-Output "Finished Tasked!"
}else {
    Write-Output "There is no file to process."
}


##################################################
##################################################
##################################################
##################################################
##################################################
################# End of Powershell Script
##################################################
##################################################
##################################################
##################################################