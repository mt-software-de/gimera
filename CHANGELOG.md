# 0.6.55
  * [NEW] strict at patchs of patch files
# 0.6.54
  * [FIX] submodule path resolving
    [NEW] --strict option integrated modules force submodules usually to also be integrated; with strict, the gimera file is used
# 0.6.51
  * [FIX] helping rsync --delete-after with non empty directories

# 0.6.50
  * [FIX] wild life stable switch between integrated and submodule: deleting invalid cached modules in .git/modules when they are not bare
# 0.6.39

  * If submodule's sha matches the branch then the branch is checked out instead of the pure sha. Advantage: no fiddling at commit and pushing.

# 0.6.8

Tested the switching between submodule and integrated in real world
repositories and fixed a lot of stuff like remaining directories with
certain marker in git.
https://stackoverflow.com/questions/4185365/no-submodule-mapping-found-in-gitmodule-for-a-path-thats-not-a-submodule

# 0.6.2

* Handling gitignores when switching submodule to integrated repos
# 0.6.0

* added  thousand lines of tests
* rewritten shell commands with generic wrapper
* abstract some more git classes like remotes

# 0.5.23

* get rid of annoying message about changed files - ignoring updated gimera.yml
# 0.3.17

- added completion for: bash

# 0.3.8

- added force option at adding submodules
