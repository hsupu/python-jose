param()

Push-Location $PSScriptRoot
try {
    & python setup.py sdist register -r local upload -r local
}
finally {
    Pop-Location
}
