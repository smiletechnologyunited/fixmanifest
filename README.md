# fixmanifest
Pythonモジュールのマニフェスト情報を修正してMayaで読み込めるように修正する。

# 簡単な使い方

1. wheelファイルをダウンロードしてくる。（[pypi](https://pypi.python.org/pypi)または[unofficial python binaries](http://www.lfd.uci.edu/~gohlke/pythonlibs/)）。
1. whlを展開する。
1. fixmanifestを実行する。
1. whlに再圧縮する。

そしてmayapy.exe -m pip install hoge.whlしたらいい。

以上。
