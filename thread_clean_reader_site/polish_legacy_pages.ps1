$ErrorActionPreference = 'Stop'

# Use the directory where the script is located as the site directory
$siteDir = $PSScriptRoot
if (-not $siteDir) { $siteDir = Get-Location }

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
  'The_Path_of_the_Right_Hand.html',
  'Chimneyrue Entry.html'
)

function Update-LegacyFile {
  param(
    [string]$Path,
    [string]$Label,
    [string]$NavTarget
  )

  $content = Get-Content -Raw -Path $Path

  if ($content -notmatch 'name="viewport"') {
    $content = [regex]::Replace(
      $content,
      '(<meta[^>]*Content-Type[^>]*>\s*)',
      "`$1`r`n<meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">`r`n",
      1
    )
  }

  if ($content -notmatch 'thread_style.css') {
    $content = $content -replace '</head>', "  <link rel=""stylesheet"" href=""thread_style.css"">`r`n</head>"
  }

  if ($content -notmatch 'legacy-main') {
    $navBlock = @"
<body class="legacy-page">
<main class="legacy-main">
  <div class="legacy-header">
    <p class="part">$Label</p>
    <div class="nav legacy-nav">
      <p><a href="index.html">Reader Home</a> | <a href="01_contents.html">Contents</a> | <a href="$NavTarget">$Label Hub</a> | <a href="00_intro_and_setup.html">Begin Reading</a></p>
    </div>
  </div>
  <article class="legacy-article">
"@
    $footerBlock = @"
  </article>
  <div class="page-footer">
    <div class="chapter-nav">
      <a href="$NavTarget">Back to $Label Hub</a>
      <a class="primary" href="00_intro_and_setup.html">Begin Reading</a>
      <a href="index.html">Reader Home</a>
    </div>
  </div>
</main>
</body>
"@
    $content = [regex]::Replace($content, '<body[^>]*>', $navBlock, 1)
    $content = [regex]::Replace($content, '</body>', $footerBlock, 1)
  }

  Set-Content -Path $Path -Value $content -Encoding utf8
}

foreach ($file in $sheetFiles) {
  Update-LegacyFile -Path (Join-Path $siteDir $file) -Label 'Character Sheet' -NavTarget '01b_cast_at_a_glance.html'
}

foreach ($file in $docFiles) {
  Update-LegacyFile -Path (Join-Path $siteDir $file) -Label 'Reference Document' -NavTarget '01a_reference_gallery.html'
}
