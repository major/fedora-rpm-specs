# header-only library
%global debug_package %{nil}

%bcond_without check

%global forgeurl https://github.com/yixuan/spectra
%global date 20230801
%global commit 1f53e26d2242cbd848cd5741f2019a91d893a9aa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta

Name:           spectra
Version:        1.0.1
Release:        %autorelease
Summary:        A header-only C++ library for large scale eigenvalue problems
License:        MPL-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}
# Use GNUInstallDirs; Fix install location of CMake config files
# include CMakeFindDependencyMacro module
# https://github.com/yixuan/spectra/pull/169
Patch0:         spectra-fix-cmake.patch

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
The %{name}-devel package contains development files for %{name}.

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

%if %{with check}
%check
%ctest
%endif

%files devel
%license LICENSE
%doc README.md
%{_includedir}/Spectra/
%{_datadir}/cmake/Spectra

%changelog
%autochangelog
