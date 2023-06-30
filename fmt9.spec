%global appname fmt

Name: fmt9
Version: 9.1.0
Release: 4%{?dist}

License: BSD
Summary: Compatibility version of the %{appname} library
URL: https://github.com/fmtlib/%{appname}
Source0: %{url}/archive/%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
C++ Format is an open-source formatting library for C++. It can be used as a
safe alternative to printf or as a fast alternative to IOStreams.

Warning! This is a limited-time compatibility version of %{appname}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts: %{appname}-devel%{?_isa}

%description devel
This package contains the header file for using %{name}.

Warning! This is a limited-time compatibility version of %{appname}.

%prep
%autosetup -n %{appname}-%{version} -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DFMT_CMAKE_DIR:STRING=%{_libdir}/cmake/%{appname} \
    -DFMT_LIB_DIR:STRING=%{_libdir}
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.rst
%doc ChangeLog.rst README.rst
%{_libdir}/lib%{appname}.so.9*

%files devel
%{_includedir}/%{appname}
%{_libdir}/lib%{appname}.so
%{_libdir}/cmake/%{appname}
%{_libdir}/pkgconfig/%{appname}.pc

%changelog
* Mon May 29 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 9.1.0-4
- Converted to compatibility package.
