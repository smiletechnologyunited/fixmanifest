# fixmanifest
Pythonモジュールのマニフェスト情報を修正してMayaで読み込めるように修正する。

＜注意＞あくまで強引に動くようにする対処なので、本番はちゃんとソースコードから適切なコンパイラでビルドしてください。

# 簡単な使い方

## 準備
python27からmanifest情報を取り出してpy27.manifestとして保存しておく。
```
C:\Program Files (x86)\Windows Kits\8.1\bin\x64\mt.exe -out:py27.manifest -inputresource:C:\Python27\python.exe
```

## 実行

1. wheelファイルをダウンロードしてくる。（[pypi](https://pypi.python.org/pypi)または[unofficial python binaries](http://www.lfd.uci.edu/~gohlke/pythonlibs/)）。
1. whlを展開する。
1. fixmanifestを実行する。
1. whlに再圧縮する。

そしてmayapy.exe -m pip install hoge.whlしたらいい。

以上。
