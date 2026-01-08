from mcp.server.fastmcp import FastMCP
from pathlib import Path

#MCPサーバ初期化
mcp = FastMCP("file-search-mcp")
BASE_DIR = Path("C:/mcp/test_docs")

# ---------- Tool: ファイル一覧取得 ----------
@mcp.tool()
def list_files() -> list[str]:
    """
    return a list of all files under the documents directory
    
    :return: 説明
    :rtype: list[str]
    """
    if not BASE_DIR.exists():
        print("DEBUG: BASE_DIR does not exist:", BASE_DIR)
        return []
    
    files = [
        str(path.relative_to(BASE_DIR))
        for path in BASE_DIR.rglob("*")
        if path.is_file()
    ]

    print("DEBUG: files found =", files)
    return files

# ---------- Tool: キーワード検索 ----------
@mcp.tool()
def search_files(keyword: str) -> list[str]:
    """
    Search files containing the given keyword
    
    :param keyword: 説明
    :type keyword: str
    :return: 説明
    :rtype: list[str]
    """
    results = []

    if not BASE_DIR.exists():
        return results
    
    for file_path in BASE_DIR.rglob("*"):
        if not file_path.is_file():
            continue

        try:
            content = file_path.read_text(encoding="utf-8")
            if keyword in content:
                results.append(str(file_path.relative_to(BASE_DIR)))
        except Exception:
            continue

    return results

# ---------- Resource: ファイル内容 ----------
@mcp.resource("file://{path}")
def read_file(path: str) -> str:
    """
    Read a file content safely.
    
    :param path: 説明
    :type path: str
    :return: 説明
    :rtype: str
    """
    target = BASE_DIR / path

    if not target.exists() or not target.is_file():
        return "File not found."
    
    try:
        return target.read_text(encoding="utf-8")
    except Exception as e:
        return f"Failed to read file: {e}"
    

if __name__ == "__main__":
    mcp.run()