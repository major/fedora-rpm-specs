%global short_name lsp-server
%global forgeurl https://github.com/python-lsp/python-lsp-server

%global _description %{expand:
A python implementation of language server protocol. pylsp provides for 
auto-completion, code linting (via pycodestyle and pyflakes) and other features.

This package provides the python-language-server package maintained by 
spyder-IDE maintainers.
}

Name:           python-%{short_name}
Version:        1.7.4
Release:        %autorelease
Summary:        Python implementation of language server protocol
%forgemeta
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
# Backport of PR 416: Bump Jedi upper pin to <0.20
Patch:          https://patch-diff.githubusercontent.com/raw/python-lsp/python-lsp-server/pull/416.patch

BuildArch:      noarch

BuildRequires:  python3-devel, git-core
BuildRequires:  pyproject-rpm-macros

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

Provides:       pylsp = %{version}-%{release}
Requires:       python3dist(autopep8)
Requires:       python3dist(flake8)
Requires:       python3dist(mccabe)
Requires:       python3dist(pycodestyle)
Requires:       python3dist(pydocstyle)
Requires:       python3dist(pyflakes)
Requires:       python3dist(pylint)
Requires:       python3dist(rope)
Requires:       python3dist(yapf)


%description -n python3-%{short_name} %_description


%prep
%autosetup -n %{name}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires -x test,all

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pylsp

%check
%pytest --no-cov --ignore test/plugins/test_pyflakes_lint.py \
  -k "not (test_pylint or test_syntax_error_pylint)"

%files -n python3-%{short_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/pylsp

%changelog
%autochangelog
