Name: QXlsx
Version:  1.4.4
Release:  2%{?dist}
Summary:  Excel/XLSX file reader/writer library for Qt

License: MIT
URL: https://github.com/QtExcel/QXlsx
Source0: %{url}/archive/v%{version}/QtXslx-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel

%package devel
Summary: Development files for QtXslx
Requires: %{name} = %{version}-%{release}

%description
QXlsx is excel file(*.xlsx) reader/writer library.

%description devel
QXlsx is excel file(*.xlsx) reader/writer library.

These are the development files.

%prep
%setup -q

%build

%cmake QXlsx -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README*
%{_libdir}/libQXlsx.so.0*
%{_libdir}/libQXlsx.so.1*


%files devel
%{_libdir}/libQXlsx.so
%{_includedir}/QXlsx/
%{_libdir}/cmake/QXlsx/


%changelog
* Wed Oct 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-2
- Review fixes.

* Mon Oct 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-1
- Initial build
