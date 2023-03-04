Name:			rkcommon
Version:		1.11.0
Release:		%autorelease
Summary:		Intel RenderKit common C++/CMake infrastructure

License:		Apache-2.0
URL:			https://github.com/ospray/rkcommon
Source0:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# This package only supports x86 and ARM 64bit arches for now
ExclusiveArch:	x86_64 aarch64

BuildRequires:	cmake3
BuildRequires:	gcc-c++
BuildRequires:	tbb-devel

%description
This project represents a common set of C++ infrastructure and CMake utilities
used by various components of Intel® oneAPI Rendering Toolkit.

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
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/rkcommon
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}-%{version}/

%changelog
%autochangelog
