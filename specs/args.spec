# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_use_noarch_only_in_subpackages
%global debug_package %{nil}

Name:           args
Version:        6.4.16
Release:        %autorelease
Summary:        Simple, small, flexible, single-header C++11 argument parsing library
License:        MIT
URL:            https://github.com/Taywee/args
Source:         %{url}/archive/%{version}/args-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++


%description
A simple, small, flexible, single-header C++11 argument parsing library.  This
is designed to appear somewhat similar to Python's argparse, but in C++, with
static type checking, and hopefully a lot faster (also allowing fully nestable
group logic, where Python's argparse does not).


%package        devel
Summary:        Development files for %{name}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch


%description    devel
The %{name}-devel package contains header files for developing applications that
use %{name}.


%prep
%autosetup


%conf
%cmake \
    -DARGS_BUILD_EXAMPLE=OFF


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license LICENSE
%doc README.md
%{_includedir}/args.hxx
%{_datadir}/pkgconfig/args.pc
%{_datadir}/cmake/args


%changelog
%autochangelog
