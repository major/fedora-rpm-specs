Name: QXlsx
Version:  1.4.4
Release:  3%{?dist}
Summary:  Excel/XLSX file reader/writer library for Qt

License: MIT
URL: https://github.com/QtExcel/QXlsx
Source0: %{url}/archive/v%{version}/QtXslx-%{version}.tar.gz
Patch0: 8e83402db866ae7a67582da28aa68c83545f13c8.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  libxkbcommon-devel

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

%patch0 -p1

%build

%cmake QXlsx -DBUILD_SHARED_LIBS=ON -DQT_VERSION_MAJOR=6
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
* Fri Oct 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-3
- Rebuild for qt6

* Wed Oct 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-2
- Review fixes.

* Mon Oct 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-1
- Initial build
