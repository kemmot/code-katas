Param (
    [int] $ElfCount = 3,
    [string] $InputPath = 'day01_input2.txt'
)

# TODO: consider a draw with multiple elves carrying a joint highest amount of calories

$LineCounter = 1
$ElfCounter = 1
$CurrentElfCalories = 0

function Finish-Elf() {
    $Elf = New-Object PSObject -Property:@{ 'Index'=$ElfCounter; 'Calories'=$CurrentElfCalories }
    Write-Verbose "Elf $($Elf.Index) complete : $($Elf.Calories) callories"
    $script:CurrentElfCalories = 0
    $script:ElfCounter++
    return $Elf
}

$Elves = Get-Content $InputPath | %{
    Write-Debug "$LineCounter - $_"
    
    if ($_ -eq '') {
        Write-Output (Finish-Elf)
    } else {
        $CurrentElfCalories += [int]$_
        Write-Debug "Added $_ to elf $ElfCounter, now at $CurrentElfCalories"
    }
    
    $LineCounter += 1
}

if ($CurrentElfCalories -gt 0) {
    $Elves += (Finish-Elf)
}

$Elves | Sort-Object Calories -Descending | Select-Object -First $ElfCount | Measure-Object Calories -Sum
