# study_python
just for my study


# ERROR が出た時にどうやって解決したか

```
$ python3.12 -m pip install --upgrade pip
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try brew install
    xyz, where xyz is the package you are trying to
    install.
```

今回はpython3.12 を使っていたので、下のバージョンを使った。

python3.12 の部分は、もしかしたら数字が変わる可能性があるので注意

```
$ python3 -m venv ~/mypy
$ source ~/mypy/bin/activate
(mypy)$ python3.12 -m pip install --upgrade pip
```