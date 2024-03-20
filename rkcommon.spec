Name:			rkcommon
Version:		1.13.0
Release:		%autorelease
Summary:		Intel renderKit common C++/CMake infrastructure

License:		Apache-2.0
URL:			https://github.com/ospray/rkcommon
Source0:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Upstream only supports x86-64 and ARM64 architectures
ExclusiveArch:	x86_64 aarch64

BuildRequires:	cmake >= 3.1
BuildRequires:	gcc-c++
BuildRequires:	tbb-devel

%description
This project represents a common set of C++ infrastructure and CMake utilities
used by various components of Intel oneAPI rendering toolkit.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/rkcommon_test_suite
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}-%{version}/

%changelog
%autochangelog
