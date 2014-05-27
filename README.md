z.py
====

A python clone of https://github.com/rupa/z

The motive is the need of z for shells are not bash alike, e.g. fish,
which has no string manipulation functionalities. (yet)

It's implemented with the very basic functions, which are all I need.

### Usage ###

Example:

config.fish:

```
. /to/path/z.py/z.fish

function fish_prompt
z -- add "$PWD"
end
```

fish:

```
~ $ z cache homebrew
~/Library/Caches/Homebrew $
```
