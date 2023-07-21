Param (
    [string] $InputPath = 'day01_input2.txt'
)

write-host $InputPath

# TODO: consider a draw with multiple elves carrying a joint highest amount of calories

$LineCounter = 1
$ElfCounter = 1
$CurrentElfCalories = 0
$MostElfCalories = -1
$ElfWithMostCalories = -1

function Write-BestElf() {
    Write-Host "Elf with most calories is elf $ElfWithMostCalories : $MostElfCalories calories"
}

function Check-Elf($Index, $CalorieCount) {
    if ($CalorieCount -gt $MostElfCalories) {
        $script:MostElfCalories = $CalorieCount
        $script:ElfWithMostCalories = $Index
        Write-BestElf
    }
}

function Finish-Elf() {
    Write-Verbose "Elf $ElfCounter complete : $CurrentElfCalories callories"
    Check-Elf $ElfCounter $CurrentElfCalories
    $script:CurrentElfCalories = 0
    $script:ElfCounter++
}

Get-Content $InputPath | %{
    Write-Debug "$LineCounter - $_"
    
    if ($_ -eq '') {
        Finish-Elf
    } else {
        $CurrentElfCalories += [int]$_
        Write-Debug "Added $_ to elf $ElfCounter, now at $CurrentElfCalories"
    }
    
    $LineCounter += 1
}

if ($CurrentElfCalories -gt 0) {
    Finish-Elf
}

Write-BestElf