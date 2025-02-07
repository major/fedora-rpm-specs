%{?mingw_package_header}

%global qt_module qttranslations
#global pre rc

#global commit ad9181a543adb463badda61c10ab75574d285482
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.8.2
Release:        1%{?dist}
Summary:        Qt6 for Windows - QtTranslations component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qttools = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qttools = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtTranslations component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtTranslations component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%prep
%autosetup -p1 -n %{source_folder}


%build
%mingw_cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja


%install
%mingw_ninja_install


# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%dir %{mingw32_datadir}/qt6/translations/
%{mingw32_libdir}/qt6/sbom/qttranslations-6.8.2.spdx
%{mingw32_datadir}/qt6/translations/catalogs.json
%{mingw32_datadir}/qt6/translations/*.qm

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%dir %{mingw64_datadir}/qt6/translations/
%{mingw64_libdir}/qt6/sbom/qttranslations-6.8.2.spdx
%{mingw64_datadir}/qt6/translations/catalogs.json
%{mingw64_datadir}/qt6/translations/*.qm


%changelog
* Wed Feb 05 2025 Sandro Mani <manisandro@gmail.com> - 6.8.2-1
- Update to 6.8.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Sandro Mani <manisandro@gmail.com> - 6.8.1-2
- Explicitly mark *.qm as %%files

* Sat Dec 07 2024 Sandro Mani <manisandro@gmail.com> - 6.8.1-1
- Update to 6.8.1

* Wed Oct 23 2024 Sandro Mani <manisandro@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Sandro Mani <manisandro@gmail.com> - 6.7.2-1
- Update to 6.7.2

* Mon May 27 2024 Sandro Mani <manisandro@gmail.com> - 6.7.1-1
- Update to 6.7.1

* Sat Apr 13 2024 Sandro Mani <manisandro@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Sun Feb 18 2024 Sandro Mani <manisandro@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 03 2023 Sandro Mani <manisandro@gmail.com> - 6.6.1-1
- Update to 6.6.1

* Wed Oct 18 2023 Sandro Mani <manisandro@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Wed Oct 04 2023 Sandro Mani <manisandro@gmail.com> - 6.5.3-1
- Update to 6.5.3

* Mon Jul 31 2023 Sandro Mani <manisandro@gmail.com> - 6.5.2-1
- Update to 6.5.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Sandro Mani <manisandro@gmail.com> - 6.5.1-1
- Update to 6.5.1

* Fri Apr 07 2023 Sandro Mani <manisandro@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Wed Mar 29 2023 Sandro Mani <manisandro@gmail.com> - 6.4.3-1
- Update to 6.4.3

* Tue Mar 28 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 19 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Sat Nov 26 2022 Sandro Mani <manisandro@gmail.com> - 6.4.1-1
- Update to 6.4.1

* Fri Nov 04 2022 Sandro Mani <manisandro@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Sun May 01 2022 Sandro Mani <manisandro@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Thu Mar 31 2022 Sandro Mani <manisandro@gmail.com> - 6.3.2-1
- Update to 6.3.2
