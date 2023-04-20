# Kikar om servern är fullt patchad

$criteria = "Type='software' and IsAssigned=1 and IsHidden=0 and IsInstalled=0"

$searcher = (New-Object -COM Microsoft.Update.Session).CreateUpdateSearcher()
$updates  = $searcher.Search($criteria).Updates

if ($updates.Count -ne 0) {
  # $updates pending
  write-host "Mindre bra"
} else {
  # system up-to-date
  write-host "Bra"
}