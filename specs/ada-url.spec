# WARNING: do not enable testing for release builds!
# with ADA_TESTING, std_regex_provider will be enabled for testing purposes
# It is not recommended to enable this flag and use std::regex under
# production environments due to several security issues.
%bcond_with check

Name:		ada-url
Version:	3.2.7

%global forgeurl https://github.com/%{name}/ada
%forgemeta

Release:	%autorelease
Summary:	WHATWG-compliant and fast URL parser written in modern C++

License:	Apache-2.0 OR MIT
URL:		https://www.ada-url.com/
Source0:	%forgesource

Patch0:		1000-Remove-cmake-CPM.patch

BuildRequires:	cmake
BuildRequires:	gcc-c++

BuildRequires:	cmake(fmt)
BuildRequires:	cmake(cxxopts)

%if %{with check}
BuildRequires:	cmake(GTest)
%endif
BuildRequires:	cmake(simdjson)
BuildRequires:	cmake(simdutf)

BuildRequires:	doxygen

%description
Ada is a fast and spec-compliant URL parser written in C++.
Specification for URL parser can be found from the WHATWG website.

The Ada library passes the full range of tests from the specification,
across a wide range of platforms.
It fully supports the relevant Unicode Technical Standard.

%package tools
Summary:	Tools for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains command line utility for parsing URL.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:	Developer documentation for %{name}
Recommends:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
The %{name}-doc package contains developer documentation for
the %{name} package.

%prep
%forgeautosetup -p1

%build
%cmake \
  -DADA_TOOLS:BOOL=ON \
%if %{with check}
  -DADA_TESTING:BOOL=ON \
%endif
  -DADA_USE_SIMDUTF:BOOL=ON
%cmake_build

doxygen ./doxygen

%install
%cmake_install


%check
%ctest

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md docs/cli.md
%{_libdir}/libada.so.3*

%files tools
%{_bindir}/adaparse

%files devel
%{_libdir}/libada.so
%{_libdir}/cmake/ada/
%{_libdir}/pkgconfig/ada.pc
%{_includedir}/ada/
%{_includedir}/ada.h
%{_includedir}/ada_c.h

%files doc
%doc docs/html/

%changelog
%autochangelog

