%global sover 15

Name: log4cxx
Version: 1.3.1
Release: %autorelease
Summary: A port to C++ of the Log4j project

License: Apache-2.0
URL: http://logging.apache.org/log4cxx/index.html
Source0: http://www.apache.org/dist/logging/log4cxx/%{version}/apache-%{name}-%{version}.tar.gz

BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: openldap-devel

%description
Log4cxx is a popular logging package written in C++. One of its distinctive
features is the notion of inheritance in loggers. Using a logger hierarchy it
is possible to control which log statements are output at arbitrary
granularity. This helps reduce the volume of logged output and minimize the
cost of logging.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Header files for Log4xcc - a port to C++ of the Log4j project

%description devel
Header files and documentation you can use to develop with %{name}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep
%autosetup -n apache-%{name}-%{version}

%build
%cmake -DBUILD_SITE=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{_libdir}/liblog4cxx.so.%{sover}*

%doc NOTICE KEYS
%license LICENSE


%files devel
%{_includedir}/log4cxx
%{_libdir}/liblog4cxx.so
%{_libdir}/pkgconfig/liblog4cxx.pc
%{_libdir}/cmake/log4cxx

%files doc
%license LICENSE
%doc %{_vpath_builddir}/src/site/html/

%changelog
%autochangelog
