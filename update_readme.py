import os

def generate_markdown_link(path, base_url):
    """Markdown 링크 생성"""
    return f"[{os.path.basename(path)}]({base_url}/{path.replace(os.sep, '/')})"

def list_files(startpath, base_url):
    """디렉토리와 파일을 순회하며 Markdown 목차 생성"""
    markdown_lines = []
    for root, dirs, files in os.walk(startpath):
        if root == startpath:
            continue
        relative_path = os.path.relpath(root, startpath)
        markdown_lines.append(f"## {generate_markdown_link(relative_path, base_url)}\n")
        for file in files:
            if file.lower() != 'README.md':  # README.md 파일은 제외
                file_path = os.path.join(relative_path, file)
                markdown_lines.append(f"- {generate_markdown_link(file_path, base_url)}")
        markdown_lines.append("")  # 섹션 간 빈 줄 추가
    return "\n".join(markdown_lines)

if __name__ == "__main__":
    startpath = '.'  # 시작 디렉토리 설정
    base_url = "https://github.com/Dayoung1014/TIL"  # GitHub 기본 URL
    markdown_content = list_files(startpath, base_url)
    
    readme_path = os.path.join(startpath, 'README.md')
    with open(readme_path, 'r+', encoding='utf-8') as f:
        original_content = f.read()
        # `# TIL` 섹션 아래에 새로운 내용 추가
        insertion_point = original_content.find('# TIL\n') + 6
        updated_content = original_content[:insertion_point] + markdown_content + original_content[insertion_point:]
        f.seek(0)  # 파일 시작으로 이동
        f.write(updated_content)  # 업데이트된 내용 쓰기
        f.truncate()  # 파일 끝에서 남은 부분 제거
