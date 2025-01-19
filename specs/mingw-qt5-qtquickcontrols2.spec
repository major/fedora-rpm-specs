%?mingw_package_header

%global qt_module qtquickcontrols2
#global pre beta

#global commit 9f085b889524a80d4064d6ac01dbdc817bb31060
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-%{qt_module}
Version:        5.15.15
Release:        2%{?dist}
Summary:        Qt5 for Windows - QtQuickControls2 component

# Automatically converted from old format: GPLv3 with exceptions or LGPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv3-with-exceptions OR LGPL-2.0-or-later WITH FLTK-exception
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtdeclarative = %{version}
BuildRequires:  mingw32-qt5-qmldevtools-devel = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtdeclarative = %{version}
BuildRequires:  mingw64-qt5-qmldevtools-devel = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtQuickControls2 component
Requires:       mingw32-qt5-qtdeclarative

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-%{qt_module}-static
Summary:       Static version of the mingw32-qt5-qtquickcontrols2 library
Requires:      mingw32-qt5-%{qt_module} = %{version}-%{release}
Requires:      mingw32-qt5-qtbase-static
Requires:      mingw32-qt5-qtdeclarative-static

%description -n mingw32-qt5-%{qt_module}-static
Static version of the mingw32-qt5-qtquickcontrols2 library.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtQuickControls2 component
Requires:       mingw64-qt5-qtdeclarative

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-%{qt_module}-static
Summary:       Static version of the mingw64-qt5-qtquickcontrols2 library
Requires:      mingw64-qt5-%{qt_module} = %{version}-%{release}
Requires:      mingw64-qt5-qtbase-static
Requires:      mingw64-qt5-qtdeclarative-static

%description -n mingw64-qt5-%{qt_module}-static
Static version of the mingw64-qt5-qtquickcontrols2 library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif


%build
MINGW_BUILDDIR_SUFFIX=_static %mingw_qmake_qt5 ../%{qt_module}.pro CONFIG+=static
MINGW_BUILDDIR_SUFFIX=_static %mingw_make_build

MINGW_BUILDDIR_SUFFIX=_shared %mingw_qmake_qt5 ../%{qt_module}.pro CONFIG+=shared
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make_build


%install
MINGW_BUILDDIR_SUFFIX=_static %mingw_make install INSTALL_ROOT=%{buildroot}
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make install INSTALL_ROOT=%{buildroot}

# Remove .la leftovers
rm -f %{buildroot}%{_qt5_libdir}/libQt5*.la


# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt5QuickControls2.dll
%{mingw32_bindir}/Qt5QuickTemplates2.dll
%{mingw32_libdir}/Qt5QuickControls2.prl
%{mingw32_libdir}/Qt5QuickTemplates2.prl
%{mingw32_libdir}/qt5/qml/Qt/labs/calendar
%{mingw32_libdir}/qt5/qml/Qt/labs/platform
%{mingw32_libdir}/qt5/qml/QtQuick/Controls.2/
%{mingw32_libdir}/qt5/qml/QtQuick/Templates.2/
%{mingw32_includedir}/qt5/QtQuickControls2/
%{mingw32_includedir}/qt5/QtQuickTemplates2/
%{mingw32_libdir}/cmake/Qt5QuickControls2
%{mingw32_libdir}/cmake/Qt5QuickTemplates2
%{mingw32_libdir}/pkgconfig/*.pc
%{mingw32_datadir}/qt5/mkspecs/modules/
%exclude %{mingw32_libdir}/qt5/qml/Qt/labs/calendar/libqtlabscalendarplugin.a
%exclude %{mingw32_libdir}/qt5/qml/Qt/labs/calendar/libqtlabscalendarplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Controls.2/Fusion/libqtquickcontrols2fusionstyleplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Controls.2/Imagine/libqtquickcontrols2imaginestyleplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Controls.2/Universal/libqtquickcontrols2universalstyleplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Controls.2/libqtquickcontrols2plugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Templates.2/libqtquicktemplates2plugin.a

%files -n mingw32-qt5-%{qt_module}-static
%{mingw32_libdir}/libQt5QuickControls2.a
%{mingw32_libdir}/libQt5QuickControls2.dll.a
%{mingw32_libdir}/libQt5QuickTemplates2.a
%{mingw32_libdir}/libQt5QuickTemplates2.dll.a
%{mingw32_libdir}/qt5/qml/Qt/labs/calendar/libqtlabscalendarplugin.a
%{mingw32_libdir}/qt5/qml/Qt/labs/platform/libqtlabsplatformplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Controls.2/Fusion/libqtquickcontrols2fusionstyleplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Controls.2/Imagine/libqtquickcontrols2imaginestyleplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Controls.2/Universal/libqtquickcontrols2universalstyleplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Controls.2/libqtquickcontrols2plugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Templates.2/libqtquicktemplates2plugin.a

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5QuickControls2.dll
%{mingw64_bindir}/Qt5QuickTemplates2.dll
%{mingw64_libdir}/qt5/qml/Qt/labs/calendar
%{mingw64_libdir}/qt5/qml/Qt/labs/platform
%{mingw64_libdir}/qt5/qml/QtQuick/Controls.2/
%{mingw64_libdir}/qt5/qml/QtQuick/Templates.2/
%{mingw64_includedir}/qt5/QtQuickControls2/
%{mingw64_includedir}/qt5/QtQuickTemplates2/
%{mingw64_libdir}/Qt5QuickControls2.prl
%{mingw64_libdir}/Qt5QuickTemplates2.prl
%{mingw64_libdir}/cmake/Qt5QuickControls2
%{mingw64_libdir}/cmake/Qt5QuickTemplates2
%{mingw64_libdir}/pkgconfig/*.pc
%{mingw64_datadir}/qt5/mkspecs/modules/
%exclude %{mingw64_libdir}/qt5/qml/Qt/labs/calendar/libqtlabscalendarplugin.a
%exclude %{mingw64_libdir}/qt5/qml/Qt/labs/calendar/libqtlabscalendarplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Controls.2/Fusion/libqtquickcontrols2fusionstyleplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Controls.2/Imagine/libqtquickcontrols2imaginestyleplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Controls.2/Universal/libqtquickcontrols2universalstyleplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Controls.2/libqtquickcontrols2plugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Templates.2/libqtquicktemplates2plugin.a

%files -n mingw64-qt5-%{qt_module}-static
%{mingw64_libdir}/libQt5QuickControls2.a
%{mingw64_libdir}/libQt5QuickControls2.dll.a
%{mingw64_libdir}/libQt5QuickTemplates2.a
%{mingw64_libdir}/libQt5QuickTemplates2.dll.a
%{mingw64_libdir}/qt5/qml/Qt/labs/calendar/libqtlabscalendarplugin.a
%{mingw64_libdir}/qt5/qml/Qt/labs/platform/libqtlabsplatformplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Controls.2/Fusion/libqtquickcontrols2fusionstyleplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Controls.2/Imagine/libqtquickcontrols2imaginestyleplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Controls.2/Universal/libqtquickcontrols2universalstyleplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Controls.2/libqtquickcontrols2plugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Templates.2/libqtquicktemplates2plugin.a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 06 2024 Sandro Mani <manisandro@gmail.com> - 5.15.15-1
- Update to 5.15.15

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.15.14-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Sandro Mani <manisandro@gmail.com> - 5.15.14-1
- Update to 5.15.14

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 5.15.13-1
- Update to 5.15.13

* Thu Feb 15 2024 Sandro Mani <manisandro@gmail.com> - 5.15.12-1
- Update to 5.15.12

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 14 2023 Sandro Mani <manisandro@gmail.com> - 5.15.11-1
- Update to 5.15.11

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Sandro Mani <manisandro@gmail.com> - 5.15.10-1
- Update to 5.15.10

* Thu Apr 13 2023 Sandro Mani <manisandro@gmail.com> - 5.15.9-1
- Update to 5.15.9

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Sandro Mani <manisandro@gmail.com> - 5.15.8-1
- Update to 5.15.8

* Fri Nov 04 2022 Sandro Mani <manisandro@gmail.com> - 5.15.7-1
- Update to 5.15.7

* Thu Sep 22 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-1
- Update to 5.15.6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Sandro Mani <manisandro@gmail.com> - 5.15.5-1
- Update to 5.15.5

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 5.15.4-1
- Update to 5.15.4

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 5.15.3-2
- Rebuild with mingw-gcc-12

* Tue Mar 15 2022 Sandro Mani <manisandro@gmail.com> - 5.15.3-1
- Update to 5.15.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 18:36:49 CET 2020 Sandro Mani <manisandro@gmail.com> - 5.15.2-1
- Update to 5.15.2

* Mon Nov 2 2020 Jan Grulich <Jan Grulich> - 5.15.1-1
- Initial release (5.15.1)
