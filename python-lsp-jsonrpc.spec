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
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  git-core

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

%description -n python3-%{short_name} %_description


%prep
%forgeautosetup -S git
git tag v%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pylsp_jsonrpc

%check
%pytest -v --no-cov -k "not test_writer_bad_message"

%files -n python3-%{short_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
