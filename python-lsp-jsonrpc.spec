%global short_name lsp-jsonrpc

# Use forge macros for pulling from GitHub
%global forgeurl https://github.com/python-lsp/python-lsp-jsonrpc

%global _description %{expand:
A python server implementation of JSON RPC 2.0 protocol. This library
has been pulled out of the python LSP server project (a community maintained
fork of python-language-server).
}

Name:           python-%{short_name}
Version:        1.1.2
Release:        %autorelease
Summary:        Python implementation of JSON RPC 2.0 protocol
%forgemeta
License:        MIT
URL:            https://github.com/python-lsp/python-lsp-jsonrpc
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git-core

# Everything in the “test” extra except pytest is a coverage analysis or
# linting tool.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest}

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

%description -n python3-%{short_name} %_description


%prep
%forgeautosetup -S git
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^addopts = "[^"]*"/# &/' pyproject.toml
git add pyproject.toml
git commit -m '[Fedora] Remove pytest options pertaining to coverage analysis'
git tag v%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pylsp_jsonrpc

%check
%pytest -v -k "not test_writer_bad_message"

%files -n python3-%{short_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
