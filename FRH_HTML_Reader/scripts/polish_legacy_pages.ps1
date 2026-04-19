$ErrorActionPreference = 'Stop'

# Set path relative to script location (script is in /scripts, content is in /content)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$rootDir = Split-Path -Parent $scriptDir
$siteDir = Join-Path $rootDir 'content'

if (-not (Test-Path $siteDir)) {
    Write-Error "Content directory not found at $siteDir"
    return
}

$sheetFiles = @(
  'Ambrose_Augustus_Auggie_Fontaine(Joel).htm',
  'Autafon_Amber_Deliamber(Ashley).htm',
  'Crispin_Pollick(Paxton).htm',
  'Matthew_Bridges(Ben).htm',
  'Preston_Henderson.htm'
)

$docFiles = @(
  'Cloudburg_Colorado_Notes.html',
  'Edgar_Von_Haupt_Letter.html',
  'The_Path_of_the_Right_Hand.html'
)

function Update-LegacyFile {
  param(
    [string]$Path,
    [string]$Label,
    [string]$NavTarget
  )

  if (-not (Test-Path $Path)) {
      Write-Warning "File not found: $Path"
      return
  }

  $content = Get-Content -Raw -Path $Path

  # Add viewport meta if missing
  if ($content -notmatch 'name="viewport"') {
    $content = [regex]::Replace(
      $content,
      '(<meta[^>]*Content-Type[^>]*>\s*)',
      "`$1`r`n<meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">`r`n",
      1
    )
  }

  # Update or add stylesheet link to point to ../assets/css/
  if ($content -notmatch 'assets/css/thread_style.css') {
    if ($content -match 'href="thread_style.css"') {
        $content = $content -replace 'href="thread_style.css"', 'href="../assets/css/thread_style.css"'
    } else {
        $content = $content -replace '</head>', "  <link rel=""stylesheet"" href=""../assets/css/thread_style.css"">`r`n</head>"
    }
  }

  # Add legacy-main wrapper and updated navigation
  if ($content -notmatch 'legacy-main') {
    $navBlock = @"
<body class="legacy-page">
<main class="legacy-main">
  <div class="legacy-header">
    <p class="part">$Label</p>
    <div class="nav legacy-nav">
      <p><a href="../index.html">Reader Home</a> | <a href="01_contents.html">Contents</a> | <a href="$NavTarget">$Label Hub</a> | <a href="00_intro_and_setup.html">Begin Reading</a></p>
    </div>
  </div>
  <article class="legacy-article">
"@
    $content = [regex]::Replace($content, '<body[^>]*>', $navBlock, 1)
    $content = [regex]::Replace($content, '</body>', "`r`n  </article>`r`n</main>`r`n</body>", 1)
  } else {
    # If legacy-main already exists, ensure index.html links are updated to ../index.html
    $content = $content -replace 'href="index.html"', 'href="../index.html"'
  }

  Set-Content -Path $Path -Value $content -Encoding utf8
}

foreach ($file in $sheetFiles) {
  Update-LegacyFile -Path (Join-Path $siteDir $file) -Label 'Character Sheet' -NavTarget '01b_cast_at_a_glance.html'
}

foreach ($file in $docFiles) {
  Update-LegacyFile -Path (Join-Path $siteDir $file) -Label 'Reference Document' -NavTarget '01a_reference_gallery.html'
}
