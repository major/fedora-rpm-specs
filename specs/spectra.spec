# header-only library
%global debug_package %{nil}
%bcond check 1

%global forgeurl https://github.com/yixuan/spectra
Version:        1.1.0
%forgemeta

Name:           spectra
Release:        %autorelease
Summary:        A header-only C++ library for large scale eigenvalue problems
License:        MPL-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  eigen3-devel

%description
Spectra stands for Sparse Eigenvalue Computation Toolkit as a Redesigned ARPACK.
It is a C++ library for large scale eigenvalue problems, built on top of Eigen,
an open source linear algebra library.

Spectra is implemented as a header-only C++ library, whose only dependency,
Eigen, is also header-only. Hence Spectra can be easily embedded in C++ projects
that require calculating eigenvalues of large matrices.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
%{description}

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
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
