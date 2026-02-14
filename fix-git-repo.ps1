# Fix Git Repository - Remove Submodules and Create Clean Repo
# Run this script in PowerShell from the repository root

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Fixing Git Repository Structure" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Remove all .git folders from subdirectories
Write-Host "Step 1: Removing embedded .git folders..." -ForegroundColor Yellow
Get-ChildItem -Path . -Directory | ForEach-Object {
    if (Test-Path "$($_.FullName)\.git") {
        Remove-Item -Path "$($_.FullName)\.git" -Recurse -Force
        Write-Host "  ✓ Removed .git from $($_.Name)" -ForegroundColor Green
    }
}

# Step 2: Remove .gitmodules file if exists
Write-Host ""
Write-Host "Step 2: Removing .gitmodules file if it exists..." -ForegroundColor Yellow
if (Test-Path ".gitmodules") {
    Remove-Item ".gitmodules" -Force
    Write-Host "  ✓ Removed .gitmodules" -ForegroundColor Green
} else {
    Write-Host "  ℹ No .gitmodules file found" -ForegroundColor Gray
}

# Step 3: Clear git cache
Write-Host ""
Write-Host "Step 3: Clearing git cache..." -ForegroundColor Yellow
git rm -r --cached . 2>$null
Write-Host "  ✓ Cache cleared" -ForegroundColor Green

# Step 4: Re-add all files
Write-Host ""
Write-Host "Step 4: Re-adding all files as normal files..." -ForegroundColor Yellow
git add .
Write-Host "  ✓ Files re-added" -ForegroundColor Green

# Step 5: Commit
Write-Host ""
Write-Host "Step 5: Committing changes..." -ForegroundColor Yellow
git commit -m "Initial commit: Add all mini projects as regular folders"
Write-Host "  ✓ Committed" -ForegroundColor Green

# Step 6: Display status
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Git Status:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
git status

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Repository cleaned successfully!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Create a repository on GitHub named 'python-mini-projects-portfolio'" -ForegroundColor White
Write-Host "2. Run: git remote add origin https://github.com/YOUR_USERNAME/python-mini-projects-portfolio.git" -ForegroundColor White
Write-Host "   (or if remote exists: git remote set-url origin https://github.com/YOUR_USERNAME/python-mini-projects-portfolio.git)" -ForegroundColor White
Write-Host "3. Run: git branch -M main" -ForegroundColor White
Write-Host "4. Run: git push -u origin main" -ForegroundColor White
Write-Host "   (use --force if you need to overwrite existing remote)" -ForegroundColor White
Write-Host ""
