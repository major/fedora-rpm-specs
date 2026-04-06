%global appname fmt

Name:           fmt11
Version:        11.2.0
Release:        %autorelease

License:        MIT
Summary:        Compatibility version of the %{appname} library (soversion 11)
URL:            https://github.com/fmtlib/%{appname}
Source0:        %{url}/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

%description
C++ Format is an open-source formatting library for C++. It can be used as a
safe alternative to printf or as a fast alternative to IOStreams.

Warning! This is a limited-time compatibility version of %{appname}.
It provides libfmt.so.11 during the fmt 11->12 soname transition.
Once all dependent packages have been rebuilt against fmt 12, this
package will be retired.

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
# Remove devel files — provided by fmt-devel (fmt 12) instead
rm -rf %{buildroot}%{_includedir}/%{appname}
rm -f  %{buildroot}%{_libdir}/lib%{appname}.so
rm -rf %{buildroot}%{_libdir}/cmake/%{appname}
rm -f  %{buildroot}%{_libdir}/pkgconfig/%{appname}.pc

%check
%ctest

%files
%license LICENSE
%doc ChangeLog.md README.md
%{_libdir}/lib%{appname}.so.11*

%changelog
%autochangelog
