Name:           python-admesh
Version:        0.98.9
Release:        %autorelease
Summary:        Python bindings for ADMesh, STL manipulation library

License:        GPL-2.0-or-later
URL:            https://github.com/admesh/python-admesh
Source0:        https://files.pythonhosted.org/packages/source/a/admesh/admesh-%{version}.tar.gz

# https://github.com/admesh/python-admesh/issues/15
Source1:        %{url}/raw/v%{version}/test/utils.py

# Drop pytest-runner and "setup.py test" support
# https://github.com/admesh/python-admesh/pull/17
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch:          %{url}/pull/17.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
ExcludeArch:    %{ix86}
%endif

BuildRequires:  gcc

BuildRequires:  admesh-devel >= 0.98

BuildRequires:  python3-devel

%description
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.

%package -n     python3-admesh
Summary:        Python 3 bindings for ADMesh, STL manipulation library

%description -n python3-admesh
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.


%prep
%autosetup -n admesh-%{version} -p1
cp %{SOURCE1} test/

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l admesh

%check
%pyproject_check_import
%pytest -v

%files -n python3-admesh -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
