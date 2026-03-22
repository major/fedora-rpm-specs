%bcond_without tests

Name:           python-pycparser
Summary:        C parser and AST generator written in Python
Version:        3.00
Release:        %autorelease
License:        BSD-3-Clause

URL:            https://github.com/eliben/pycparser
Source0:        %{url}/archive/release_v%{version}/pycparser-release_v%{version}.tar.gz
Source1:        pycparser-3.00-remove-relative-sys-path.py

BuildArch:      noarch

BuildRequires:  python3-devel

# for unit tests
%if %{with tests}
BuildRequires:  gcc
%endif

%description
pycparser is a complete parser for the C language, written in pure Python.
It is a module designed to be easily integrated into applications that
need to parse C source code.

%package -n python3-pycparser
Summary:        %{summary}

%description -n python3-pycparser
pycparser is a complete parser for the C language, written in pure Python.
It is a module designed to be easily integrated into applications that
need to parse C source code.

%prep
%autosetup -p1 -n pycparser-release_v%{version}

# Remove relative sys.path from the examples
%{python3} %{SOURCE1} examples

%generate_buildrequires
%pyproject_buildrequires

%build
pushd pycparser
%{python3} _ast_gen.py
popd
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pycparser

%check
%pyproject_check_import
export %{py3_test_envvars}
%if %{with tests}
%{python3} -m unittest discover
%endif
 
%files -n python3-pycparser -f %{pyproject_files}
%doc README.rst
%doc examples

%changelog
%autochangelog
