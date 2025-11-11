#!/usr/bin/env python3
"""
リモートシェル実行クライアント
サーバーに接続してコマンドを実行します
"""
import socket
import sys

def execute_remote_command(host, port, command):
    """リモートサーバーでコマンドを実行"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"[*] {host}:{port} に接続中...")
            s.connect((host, port))
            print(f"[+] 接続成功")

            # コマンドを送信
            print(f"[*] コマンドを送信: {command}")
            s.sendall(command.encode('utf-8'))

            # 結果を受信
            result = b''
            while True:
                data = s.recv(4096)
                if not data:
                    break
                result += data

            output = result.decode('utf-8')
            print(f"[*] 実行結果:")
            print(output)
            return output

    except ConnectionRefusedError:
        print(f"[!] エラー: {host}:{port} に接続できません。サーバーが起動していることを確認してください。")
        sys.exit(1)
    except Exception as e:
        print(f"[!] エラーが発生しました: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("使用法: python3 client.py <コマンド> [ホスト] [ポート]")
        print("例: python3 client.py 'echo hoge'")
        print("例: python3 client.py 'ls -la' localhost 9999")
        sys.exit(1)

    command = sys.argv[1]
    host = sys.argv[2] if len(sys.argv) > 2 else 'localhost'
    port = int(sys.argv[3]) if len(sys.argv) > 3 else 9999

    execute_remote_command(host, port, command)

if __name__ == '__main__':
    main()
