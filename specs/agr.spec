Name:           agr
Version:        0.8.4
Release:        %autorelease
Summary:        A package manager for AI agents

License:        MIT
URL:            https://github.com/computerlovetech/agr
Source:         %{url}/archive/v%{version}/agr-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  git-core

%py_provides python3-agr

%global _description %{expand:
A package manager for AI agents. Install agent skills from GitHub
with a single command.}

%description %_description


%prep
%autosetup

# Remove linters/coverage
sed -i -e '/ruff/ d' \
    -e '/pytest-cov/ d' \
    -e '/ty>/ d' \
    -e '/mkdocs-material/ d' \
    pyproject.toml

echo "*** pyproject.toml ***"
cat pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -g dev


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l agr agrx


%check
# skip tests requiring network connections
k="${k:+$k and} not test_download"
k="${k:+$k and} not test_add_remote_skill_to_copilot_flat_structure"
k="${k:+$k and} not test_add_remote_skill_to_cursor_flat_structure"
k="${k:+$k and} not test_nonexistent_repo_without_token_mentions_token"
k="${k:+$k and} not test_add_public_skill_without_token"
k="${k:+$k and} not test_add_remote_skill"

echo "Pytest -k flag: ${k}"
%pytest "${k:+-k $k}"
%pyproject_check_import


%files -f %{pyproject_files}
%doc README.*
%{_bindir}/agr
%{_bindir}/agrx

%changelog
%autochangelog
