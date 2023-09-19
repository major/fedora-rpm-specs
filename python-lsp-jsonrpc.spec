%global short_name lsp-jsonrpc

%global _description %{expand:
A python server implementation of JSON RPC 2.0 protocol. This library
has been pulled out of the python LSP server project (a community maintained
fork of python-language-server).
}

Name:           python-%{short_name}
Version:        1.1.1
Release:        %autorelease
Summary:        Python implementation of JSON RPC 2.0 protocol

License:        MIT
URL:            https://github.com/python-lsp/python-lsp-jsonrpc
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

%description -n python3-%{short_name} %_description


%prep
%autosetup -n %{name}-%{version}

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
