%global pypi_name jsonpath-rw

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        %autorelease
Summary:        Extended implementation of JSONPath for Python

License:        Apache-2.0
URL:            https://github.com/kennknowles/python-jsonpath-rw
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-ply
BuildRequires:  python3-decorator
BuildRequires:  python3-six
BuildRequires:  python-pytest

%description -n python3-%{pypi_name}
This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jsonpath_rw

%check
%pyproject_check_import

%{pytest} -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/jsonpath.py

%changelog
%autochangelog
