Name:           python-cffi
Version:        2.0.0
Release:        %autorelease
Summary:        Foreign Function Interface for Python to call C code
# cffi is MIT
# cffi/_imp_emulation.py has bits copied from CPython (PSF-2.0)
License:        MIT AND PSF-2.0
URL:            https://github.com/python-cffi/cffi
Source:         %{url}/archive/v%{version}/cffi-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  make
BuildRequires:  libffi-devel
BuildRequires:  gcc

# For tests:
BuildRequires:  gcc-c++

%description
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.


%package -n python3-cffi
Summary:        %{summary}

%description -n python3-cffi
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.


%package doc
Summary:        Documentation for CFFI
BuildArch:      noarch
BuildRequires:  python3-sphinx

%description doc
Documentation for CFFI, the Foreign Function Interface for Python.


%prep
%autosetup -p1 -n cffi-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

cd doc
make html
rm build/html/.buildinfo


%install
%pyproject_install
%pyproject_save_files _cffi_backend cffi


%check
%pytest


%files -n python3-cffi -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc doc/build/html


%changelog
%autochangelog
