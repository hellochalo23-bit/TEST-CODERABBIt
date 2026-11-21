# Manual publishing and live shootout

Nothing has been pushed and no GitHub App has been installed by this task.
Create an empty repository in your GitHub account, choose public visibility deliberately, and
install/configure CodeRabbit yourself for that repository. The local arena contains synthetic data only.

In PowerShell, from this repository, replace YOUR_ACCOUNT and YOUR_REPOSITORY once:

```powershell
$arenaRemote = "https://github.com/YOUR_ACCOUNT/YOUR_REPOSITORY.git"
git remote add origin $arenaRemote
git push -u origin main
git push origin pr-01-clean-control pr-02-domain1-concurrency pr-03-domain2-nextjs-auth pr-04-domain3-resource-leak pr-05-domain5-security
git push origin pr-01-clean-control-patched pr-02-domain1-concurrency-patched pr-03-domain2-nextjs-auth-patched pr-04-domain3-resource-leak-patched pr-05-domain5-security-patched
```

For each branch, create the introducing PR against main at:
`https://github.com/YOUR_ACCOUNT/YOUR_REPOSITORY/compare/main...BRANCH?expand=1`.
After the first review completes, create the fix PR with base BRANCH and head BRANCH-patched:
`https://github.com/YOUR_ACCOUNT/YOUR_REPOSITORY/compare/BRANCH...BRANCH-patched?expand=1`.
Replace BRANCH with each exact pr-01 through pr-05 branch name above. These browser compare URLs
open the PR creation form; no gh CLI is required. Record branch SHAs before changing anything.

Local runtime checks (one branch checked out at a time):

```powershell
python checks/runtime.py all
```

Expected: main and patched branches exit0; each outage branch fails its corresponding behavior check.
The clean-control branch also exits0. For scanner checks set your actual installed engine path:

```powershell
$zeroNitEngine = "E:/Website/Plans/Code Rabbit"
python "$zeroNitEngine/zeronit.py" scan . --scope all --json
```

Stock `zeronit diff` reads working-tree/index changes; it does not accept base/head commit flags.
The certification harness materializes an exact committed comparison in an isolated index/worktree
and checks its tree ID. Do not run a naive diff on a clean checked-out commit and claim PR coverage.

Save raw API pull/files/reviews/inline/issue-comments/commits responses after CodeRabbit finishes.
Separate first-post timestamps from edited bodies, review event gaps from cloud processing time,
and useful correctness findings from summaries, documentation or style observations. Report all
ZeroNit misses/false positives and actual CodeRabbit feedback. This local certification contains
no live CodeRabbit results for the arena. Local inference/API spend is zero; hardware costs remain.
