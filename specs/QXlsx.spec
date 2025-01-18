Name: QXlsx
Version:  1.4.10
Release:  2%{?dist}
Summary:  Excel/XLSX file reader/writer library for Qt

License: MIT
URL: https://github.com/QtExcel/QXlsx
Source0: %{url}/archive/v%{version}/QtXslx-%{version}.tar.gz

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
%{_libdir}/libQXlsxQt6.so.0*
%{_libdir}/libQXlsxQt6.so.1*


%files devel
%{_libdir}/libQXlsxQt6.so
%{_includedir}/QXlsxQt6/
%{_libdir}/cmake/QXlsxQt6/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.4.10-1
- 1.4.10

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 1.4.9-2
- Rebuild (qt6)

* Fri Aug 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.4.9-1
- 1.4.9

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 17 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.4.8-1
- 1.4.8

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 1.4.7-6
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 1.4.7-5
- Rebuild (qt6)

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 1.4.7-4
- Rebuild (qt6)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4.7-1
- 1.4.7

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 1.4.6-9
- Rebuild (qt6)

* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 1.4.6-8
- Rebuild (qt6)

* Thu Oct 05 2023 Jan Grulich <jgrulich@redhat.com> - 1.4.6-7
- Rebuild (qt6)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 1.4.6-5
- Rebuild for qtbase private API version change

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 1.4.6-4
- Rebuild for qtbase private API version change

* Tue May 30 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4.6-3
- Patch include path.

* Mon May 29 2023 Jan Grulich <jgrulich@redhat.com> - 1.4.6-2
- Rebuild (qt6)

* Wed Apr 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4.6-1
- 1.4.6

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4.5-3
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4.5-1
- 1.4.5

* Fri Oct 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-3
- Rebuild for qt6

* Wed Oct 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-2
- Review fixes.

* Mon Oct 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-1
- Initial build
