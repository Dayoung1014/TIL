import os

def generate_markdown_link(path, base_url, is_file=True):
    """Markdown 링크 생성, 파일은 blob과 디렉토리는 tree 경로 사용"""
    # 파일 이름에서 확장자 제거
    file_name, file_ext = os.path.splitext(os.path.basename(path))
    if is_file:
        link_text = file_name  # 파일의 경우 확장자 제외
        link_type = "blob"
    else:
        link_text = os.path.basename(path)  # 디렉토리의 경우 전체 이름 사용
        link_type = "tree"

    encoded_path = os.path.relpath(path, startpath).replace(" ", "%20").replace(os.sep, '/')
    # 파일과 디렉토리에 따라 URL 구성 변경
    full_url = f"{base_url}/{link_type}/main/{encoded_path}"

    return f"[{link_text}]({full_url})"

def list_files(startpath, base_url, exclude_dirs=None):
    """디렉토리와 파일을 순회하며 Markdown 목차 생성, 특정 디렉토리 제외하고 계층 구조 반영"""
    if exclude_dirs is None:
        exclude_dirs = ['.git', '.github', 'src']  # 기본적으로 제외할 디렉토리
    markdown_lines = ["# TIL\n\n"]  # README.md 파일의 시작 부분
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]  # 제외할 디렉토리 건너뛰기
        level = root.replace(startpath, '').count(os.sep)  # 현재 디렉토리의 깊이 계산
        indent = '  ' * (level - 1)  # 들여쓰기 (루트 디렉토리를 제외한 깊이에 맞춰 조정)
        header_size = '##' + '#' * (level - 1)  # h2부터 시작하여 깊이에 따라 글자 크기 조정
        
        if root != startpath:
            relative_path = os.path.relpath(root, startpath)
            markdown_lines.append(f"{indent}{header_size} {generate_markdown_link(relative_path, base_url, is_file=False)}\n")
        
        for file in files:
            if file.lower() != 'readme.md':  # README.md 파일은 제외
                file_path = os.path.join(root, file)
                markdown_lines.append(f"{indent}- {generate_markdown_link(file_path, base_url)}")
        markdown_lines.append("")  # 디렉토리 간 빈 줄 추가
    return "\n".join(markdown_lines)

if __name__ == "__main__":
    startpath = '.'  # 시작 디렉토리 설정
    base_url = "https://github.com/Dayoung1014/TIL"  # GitHub 기본 URL
    markdown_content = list_files(startpath, base_url)
    
    readme_path = os.path.join(startpath, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:  # 'w' 모드로 파일을 열어 기존 내용을 삭제하고 새로 작성
        f.write(markdown_content)  # 새로운 내용 쓰기
