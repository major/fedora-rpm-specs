%undefine __cmake_in_source_build

Name:           xtensor-python
Version:        0.28.0
Release:        %autorelease
Summary:        Python bindings for xtensor
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://xtensor-python.readthedocs.io/

%global github  https://github.com/QuantStack/xtensor-python
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{github}/pull/324.diff
Patch1:         %{github}/pull/326.diff
Patch2:         %{github}/pull/325.diff
Patch3:         %{github}/pull/327.diff

# because xtensor does so for armv7hl, ppc64le and s390x
ExcludeArch:    armv7hl ppc64le s390x

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  python3-pytest
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  xtensor-devel
BuildRequires:  python3-numpy


# there is no actual arched content - this is a header only library
%global debug_package %{nil}

%global _description %{expand:
xtensor-python enables in-place use of Numpy arrays in C++ with all the
benefits from xtensor:
- C++ universal function and broadcasting.
- STL-compliant APIs.
- A broad coverage of NumPy APIs.}


%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Requires:       pybind11-devel
Requires:       python3-devel
Requires:       xtensor-devel
Requires:       python3-numpy

%description devel %_description

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%make_build -C %{_vpath_builddir} xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
