Name:           python-pytest-gitconfig
Version:        0.7.0
Release:        %autorelease
Summary:        Provide a Git config sandbox for testing

License:        MIT
URL:            https://github.com/noirbizarre/pytest-gitconfig
VCS:            git:%{url}.git
Source:         %{pypi_source pytest_gitconfig}

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  git-core

%global _description %{expand:
Provide a Git config sandbox for testing.}

%description %_description

%package -n     python3-pytest-gitconfig
Summary:        %{summary}

%description -n python3-pytest-gitconfig %_description


%prep
%autosetup -p1 -n pytest_gitconfig-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L pytest_gitconfig


%check
%pyproject_check_import
%pytest

%files -n python3-pytest-gitconfig -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
