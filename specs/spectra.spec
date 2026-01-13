# header-only library
%global debug_package %{nil}
%bcond check 0

Name:           spectra
Version:        1.2.0
Release:        %autorelease
Summary:        A header-only C++ library for large scale eigenvalue problems
License:        MPL-2.0
URL:            https://github.com/yixuan/spectra
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         spectra-fix.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
%if %{with check}
BuildRequires:  eigen3-devel
%endif

%global _description %{expand:
Spectra stands for Sparse Eigenvalue Computation Toolkit as a Redesigned ARPACK.
It is a C++ library for large scale eigenvalue problems, built on top of Eigen,
an open source linear algebra library.

Spectra is implemented as a header-only C++ library, whose only dependency,
Eigen, is also header-only. Hence Spectra can be easily embedded in C++ projects
that require calculating eigenvalues of large matrices.}

%description
%_description

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
Requires:       eigen3-devel

%description    devel
%_description

%prep
%autosetup -p1 -C

%build
%cmake \
%if %{with check}
    -DBUILD_TESTS=ON \
%endif

%cmake_build

%install
%cmake_install

%check
# https://github.com/yixuan/spectra/issues/177
%ifarch s390x
%ctest -E Example1
%else
%ctest
%endif

%files devel
%license LICENSE
%doc README.md
%{_includedir}/Spectra/
%{_datadir}/cmake/Spectra

%changelog
%autochangelog
