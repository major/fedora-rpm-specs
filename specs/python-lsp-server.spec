%global short_name lsp-server

%global _description %{expand:
A python implementation of language server protocol. pylsp provides for 
auto-completion, code linting (via pycodestyle and pyflakes) and other features.

This package provides the python-language-server package maintained by 
spyder-IDE maintainers.
}

Name:           python-%{short_name}
Version:        1.12.2
Release:        %autorelease
Summary:        Python implementation of language server protocol

%global forgeurl https://github.com/python-lsp/python-lsp-server
%forgemeta

# SPDX
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel, git-core
BuildRequires:  pyproject-rpm-macros

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

Provides:       pylsp = %{version}-%{release}


%description -n python3-%{short_name} %_description


%pyproject_extras_subpkg -n python3-%{short_name} all


%prep
%forgeautosetup -p1 -S git
# Remove version pinning from linters
# Do this inline instead of a patch for automatic updates using Packit
sed -r -i \
-e 's/(flake8)>.*"/\1"/g' \
-e '/pycodestyle>.*/d' \
-e '/pyflakes>.*/d' \
-e '/pylint>.*/d' pyproject.toml

# Unpin `autopep8`. Version 2.1.0 is coming to rawhide.
sed -r -i 's/(autopep8)>.*"/\1"/g' pyproject.toml

git add pyproject.toml
git commit -m '[Fedora] Remove version pinning where needed'
git tag v%{version}

%generate_buildrequires
%pyproject_buildrequires -x test,all

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pylsp

%check
%pytest --no-cov --ignore test/plugins/test_pyflakes_lint.py \
  -k "not (test_pylint or test_syntax_error_pylint)"

%files -n python3-%{short_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/pylsp

%changelog
%autochangelog
