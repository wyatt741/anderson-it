$ErrorActionPreference = 'Stop'

$fontDirectory = Join-Path $PSScriptRoot '..\assets\fonts'
New-Item -ItemType Directory -Force -Path $fontDirectory | Out-Null

$cssUrl = 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap'
$headers = @{ 'User-Agent' = 'Mozilla/5.0 AppleWebKit/537.36 Chrome/124 Safari/537.36' }
$css = (Invoke-WebRequest -Uri $cssUrl -Headers $headers).Content
$blocks = [regex]::Matches($css, '(?s)/\*\s*latin\s*\*/\s*@font-face\s*\{(.*?)\}')

$expected = @{
  'Plus Jakarta Sans' = 'plus-jakarta-sans.woff2'
  'Space Grotesk' = 'space-grotesk.woff2'
}
$downloaded = @{}

foreach ($block in $blocks) {
  $body = $block.Groups[1].Value
  $family = [regex]::Match($body, "font-family:\s*'([^']+)'").Groups[1].Value
  $url = [regex]::Match($body, 'src:\s*url\((https://[^)]+\.woff2)\)').Groups[1].Value
  if (-not $expected.ContainsKey($family) -or -not $url -or $downloaded.ContainsKey($family)) { continue }
  $destination = Join-Path $fontDirectory $expected[$family]
  Invoke-WebRequest -Uri $url -Headers $headers -OutFile $destination
  $downloaded[$family] = $destination
}

$missing = foreach ($family in $expected.Keys) { if (-not $downloaded.ContainsKey($family)) { $family } }
if ($missing) { throw "Missing font files: $($missing -join ', ')" }

$downloaded.GetEnumerator() | Sort-Object Name | ForEach-Object {
  $file = Get-Item $_.Value
  "{0}: {1} bytes" -f $_.Name, $file.Length
}
