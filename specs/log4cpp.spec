Name:           log4cpp
Version:        1.1.6
Release:        %autorelease
Summary:        C++ logging library
License:        LGPL-2.1-only
URL:            https://log4cpp.sourceforge.net/
Source0:        https://sourceforge.net/projects/log4cpp/files/REL_%{version}_Mar_12_2026/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix
Obsoletes:      log4cpp-doc < 0:1.1.6

# This patch modifies CMake file to create a versioned soname library
Patch0:         log4cpp-1.1.6-fix_soname.patch

%description
A library of C++ classes for flexible logging to files, syslog, IDSA and
other destinations. It is modeled after the Log for Java library
(http://www.log4j.org), staying as close to their API as is reasonable.

%package devel
Summary:        Header files, libraries and development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and development
man pages for %{name}.

%prep
%autosetup -n log4cpp -p 1

# Delete non-free (but freely distributable) file under Artistic 1.0
# just to be sure we're not using it.
rm -rf src/snprintf.c

# Convert line endings.
dos2unix --keepdate ChangeLog

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc ChangeLog THANKS TODO
%license COPYING
%{_libdir}/liblog4cpp.so.5
%{_libdir}/liblog4cpp.so.5.0.6

%files devel
%{_includedir}/log4cpp/
%{_libdir}/liblog4cpp.so
%{_libdir}/cmake/log4cpp/

%changelog
%autochangelog
