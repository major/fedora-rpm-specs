%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%global optflags %(echo %{optflags} -Wno-error=template-id-cdtor)
%endif

%global forgeurl https://github.com/jeromerobert/hmat-oss
Version:        1.11.0
%global tag %{version}
%forgemeta

Name:           hmat-oss
Release:        %autorelease
Summary:        A hierarchical matrix C/C++ library
License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  flexiblas-devel
BuildRequires:  cmake(lapacke)
BuildRequires:  blas-static
BuildRequires:  lapack-static

%description
hmat-oss is hierarchical matrix library written in C++. It has a C API. It
contains a LU and LLt solver, and a few other things.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_EXAMPLES=ON \

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
