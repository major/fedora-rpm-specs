%global richname SQLiteCpp

Name: sqlitecpp
Version: 3.3.2
Release: %autorelease

License: MIT
Summary: Smart and easy to use C++ SQLite3 wrapper
URL: https://github.com/SRombauts/%{richname}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gmock-devel
BuildRequires: gtest-devel
BuildRequires: sqlite-devel

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
SQLiteC++ (SQLiteCpp) is a smart and easy to use C++ SQLite3 wrapper.

SQLiteC++ offers an encapsulation around the native C APIs of SQLite,
with a few intuitive and well documented C++ classes.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{richname}-%{version} -p1

# Fixing W: wrong-file-end-of-line-encoding...
sed -e "s,\r,," -i README.md

# Removing bundled libraries...
rm -rf {sqlite3,googletest}

# Adding missing includes...
sed -e "17i #include <cstdint>" -i include/SQLiteCpp/Statement.h

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DSQLITECPP_BUILD_TESTS:BOOL=ON \
    -DSQLITECPP_BUILD_EXAMPLES:BOOL=OFF \
    -DSQLITECPP_INTERNAL_SQLITE:BOOL=OFF \
    -DSQLITECPP_RUN_CPPLINT:BOOL=OFF
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{_libdir}/lib%{richname}.so.0*

%files devel
%{_includedir}/%{richname}
%{_libdir}/cmake/%{richname}
%{_libdir}/lib%{richname}.so
%{_datadir}/%{richname}

%changelog
%autochangelog
