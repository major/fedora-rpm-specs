%global pypi_name json5

Name:           python-%{pypi_name}
Version:        0.12.1
Release:        %autorelease
Summary:        Python implementation of the JSON5 data format

License:        Apache-2.0
URL:            https://github.com/dpranke/pyjson5
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JSON5 extends the JSON data interchange format to make it slightly more usable
as a configuration language:

- JavaScript-style comments (both single and multi-line) are legal.
- Object keys may be unquoted if they are legal ECMAScript identifiers
- Objects and arrays may end with trailing commas.
- Strings can be single-quoted, and multi-line string literals are allowed.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)

%description -n python3-%{pypi_name}
JSON5 extends the JSON data interchange format to make it slightly more usable
as a configuration language:

- JavaScript-style comments (both single and multi-line) are legal.
- Object keys may be unquoted if they are legal ECMAScript identifiers
- Objects and arrays may end with trailing commas.
- Strings can be single-quoted, and multi-line string literals are allowed.

%package -n pyjson5
Summary:        Tool for working with the JSON5 data format

Requires:       python3-%{pypi_name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n pyjson5
Command-line tool for working with the JSON5 data format.

%prep
%autosetup -n py%{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%files -n pyjson5
%doc README.md
%license LICENSE
%{_bindir}/pyjson5

%changelog
%autochangelog
