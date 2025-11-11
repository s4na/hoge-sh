#!/usr/bin/env python3
"""
リモートシェル実行サーバー
クライアントからの接続を受け付けて、コマンドを実行します
"""
import socket
import subprocess
import sys

HOST = '0.0.0.0'
PORT = 9999

def main():
    print(f"[*] リモートシェル実行サーバーを起動します (ポート: {PORT})")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[*] {HOST}:{PORT} で待機中...")

        while True:
            conn, addr = s.accept()
            print(f"[+] 接続を受け付けました: {addr}")

            with conn:
                try:
                    # クライアントからコマンドを受信
                    data = conn.recv(1024)
                    if not data:
                        break

                    command = data.decode('utf-8').strip()
                    print(f"[*] 受信したコマンド: {command}")

                    # コマンドを実行
                    try:
                        result = subprocess.run(
                            command,
                            shell=True,
                            capture_output=True,
                            text=True,
                            timeout=30
                        )
                        output = result.stdout + result.stderr
                        if not output:
                            output = "[コマンドは正常に実行されましたが、出力はありません]\n"
                    except subprocess.TimeoutExpired:
                        output = "[エラー] コマンドがタイムアウトしました\n"
                    except Exception as e:
                        output = f"[エラー] {str(e)}\n"

                    # 結果を送信
                    conn.sendall(output.encode('utf-8'))
                    print(f"[*] 実行結果を送信しました")

                except Exception as e:
                    print(f"[!] エラーが発生しました: {e}")

                print(f"[-] 接続を閉じました: {addr}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] サーバーを停止します")
        sys.exit(0)
