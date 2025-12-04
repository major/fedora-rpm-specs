Name:           cctz
Version:        2.5
%global sover   2
Release:        %autorelease
License:        Apache-2.0
Summary:        Translating between absolute and civil times using time zone rules
Url:            https://github.com/google/cctz
Source:         https://github.com/google/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          https://sources.debian.org/data/main/c/cctz/2.4%2Bdfsg1-2/debian/patches/0001-Compile-shared-lib-and-install-it.patch

BuildRequires:  tzdata
BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  gtest-devel >= 1.8.0
BuildRequires:  gmock-devel >= 1.8.0
BuildRequires:  google-benchmark-devel

Requires:       tzdata

%description
CCTZ contains two libraries that cooperate with <chrono> to give C++
programmers all the necessary tools for computing with dates, times, and time
zones in a simple and correct manner. The libraries in CCTZ are:
  * The Civil-Time Library - This is a header-only library that supports
    computing with human-scale time, such as dates (which are represented by
    the cctz::civil_day class).
  * The Time-Zone Library - This library uses the IANA time zone database that
    is installed on the system to convert between absolute time and civil time.


%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
Development files for %{name} library.


%prep
%autosetup -p1

%build
# Version and shared library version match Debian's.
%cmake -DVERSION=%{version} -DSOVERSION=%{sover}
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/time_tool
%{_libdir}/libcctz.so.%{sover}
%{_libdir}/libcctz.so.%{version}

%files devel
%doc examples
%{_includedir}/cctz
%{_libdir}/libcctz.so
%{_libdir}/cmake/cctz

%changelog
%autochangelog
