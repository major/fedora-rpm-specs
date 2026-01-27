%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%global optflags %(echo %{optflags} -Wno-error=template-id-cdtor)
%endif

Name:           hmat-oss
Version:        1.11.0
Release:        %autorelease
Summary:        A hierarchical matrix C/C++ library
License:        GPL-2.0-or-later
URL:            https://github.com/jeromerobert/hmat-oss
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  flexiblas-devel
BuildRequires:  cmake(lapacke)
BuildRequires:  blas-devel
BuildRequires:  blas-static
BuildRequires:  lapack-devel
BuildRequires:  lapack-static

%description
hmat-oss is hierarchical matrix library written in C++. It has a C API. It
contains a LU and LLt solver, and a few other things.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1 -C

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_EXAMPLES=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libhmat.so.4
%{_libdir}/libhmat.so.1*

%files devel
%{_libdir}/libhmat.so
%{_includedir}/hmat/
%{_libdir}/cmake/hmat/

%changelog
%autochangelog
