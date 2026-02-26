%global with_tests 1

Name: autowrap
Summary: Generates Python Extension modules from [Cython] PXD files
Version: 0.26.0
Release: %autorelease
License: BSD-3-Clause
URL: https://pypi.org/project/autowrap/
Source0: https://github.com/OpenMS/autowrap/archive/refs/tags/release/%{version}/%{name}-release-%{version}.tar.gz
Patch0:  %{name}-fix_configuration_for_old_setuptools.patch
BuildArch: noarch

## For testing
BuildRequires: boost-devel
BuildRequires: gcc
BuildRequires: gcc-c++

%description
This module uses the Cython "header" .pxd files to automatically generate
Cython input (.pyx) files. It does so by parsing the header files and possibly
annotations in the header files to generate correct Cython code.

%package -n python3-autowrap
Summary: Generates Python3 Extension modules from [Cython] PXD files
%py_provides python3-%{name}
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest
BuildRequires: python3-Cython
Obsoletes: python2-autowrap < 0:%{version}-%{release}

%description -n python3-autowrap
%{summary}.

%prep
%autosetup -n %{name}-release-%{version} -N

%if 0%{?fedora} < 43
%patch -P 0 -p1
%endif

##Remove bundled files
rm -rf %{name}-release-%{version}/autowrap/data_files/boost

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files autowrap

%if 0%{?with_tests}
%check
export CFLAGS="-I%{_includedir}/boost"
%pytest -v -m "not network"
%endif

%files -n python3-autowrap -f %{pyproject_files}
%{_bindir}/autowrap

%changelog
%autochangelog
