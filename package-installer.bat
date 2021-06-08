@echo off
echo 事前にPython 3.8.9のインストールが必要です。
echo インストールしていない場合はpython.orgからインストールを行ってください。
echo 続行する場合は何かキーを押してください。
pause>nul
cls
echo 実行に必要なPythonライブラリをインストールします。
echo 開始してもよろしければ何かキーを押してください。
pause>nul
cls
py -3.8 -m requests
py -3.8 -m discord
cls
echo インストールが完了しました。
echo 終了してもよろしければ何かキーを押してください。