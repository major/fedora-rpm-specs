%global debug_package %{nil}

%global commit 5936c62511305227fbd59b2d5a43aaf89ec3a0b6
%global date 20220215
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global common_description %{expand:
This library provides a consistent C interface to a few matrix backends.

The interface itself is a little more sane than raw lapack / blas calls, and is
meant to be reasonably performant for medium to large matrices. It should also
be cross platform and work reasonably well on embedded low latency systems; as
it consistently tries to avoid heap allocations.}

Name:           cnmatrix
Version:        0.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        A consistent C interface to a few matrix backends
# cmake/FindEigen3.cmake is BSD-2-Clause
License:        MIT and BSD-2-Clause
URL:            https://github.com/cntools/cnmatrix

Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-shared.patch

BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++

%description    %{common_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconf-pkg-config

%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake -DENABLE_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.0

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
