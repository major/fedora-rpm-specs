%global desc %{expand: \
The Instrumentation and Tracing Technology (ITT) API enables your application
to generate and control the collection of trace data during its execution
across different Intel tools.}

Name:		ittapi
Version:	3.25.4
Release:	%autorelease
Summary:	Intel Instrumentation and Tracing Technology and Just-In-Time API

License:	BSD-3-Clause and GPL-2.0-only
URL:		https://github.com/intel/ittapi
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	test.cpp

Patch0:		ittapi-fedora.patch

BuildRequires:	cmake >= 3.1
BuildRequires:	gcc-c++

# C header file library for x86 processors.
ExclusiveArch:	x86_64

%description
%{desc}
	
%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{desc}

%prep
%autosetup -p1
cp %{SOURCE1} .

%build
%cmake \
	-DITT_API_IPT_SUPPORT=1 \
	-DITT_API_FORTRAN_SUPPORT=0
%cmake_build

%install
%cmake_install

%check
$CXX -I%{buildroot}%{_includedir} -L%{buildroot}%{_libdir} -littnotify -o test test.cpp
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test

%files
%license LICENSES/BSD-3-Clause.txt LICENSES/GPL-2.0-only.txt
%doc README.md
%{_libdir}/libittnotify.so.%{version}
%{_libdir}/libittnotify.so.3

%files devel
%{_includedir}/*
%{_libdir}/libittnotify.so
%{_libdir}/cmake/%{name}

%changelog
%autochangelog
