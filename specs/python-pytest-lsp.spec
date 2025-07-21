Name:           python-pytest-lsp
Version:        1.0.0b2
Release:        %autorelease
Summary:        A pytest plugin for end-to-end testing of language servers

License:        MIT
URL:            https://github.com/swyddfa/lsp-devtools
Source:         %{url}/releases/download/pytest-lsp-v%{version}/pytest_lsp-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
pytest-lsp is a pytest plugin for writing end-to-end tests for language servers.

It works by running the language server in a subprocess and communicating with
it over stdio, just like a real language client. This also means pytest-lsp can
be used to test language servers written in any language - not just Python.

pytest-lsp relies on the pygls library for its language server protocol
implementation.}

%description %_description

%package -n     python3-pytest-lsp
Summary:        %{summary}

%description -n python3-pytest-lsp %_description

%prep
%autosetup -p1 -n pytest_lsp-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_lsp

%check
%pytest -v || :

%files -n python3-pytest-lsp -f %{pyproject_files}

%changelog
%autochangelog
