%global qt_module qtvirtualkeyboard

Summary: Qt5 - VirtualKeyboard component
Name:    qt5-%{qt_module}
Version: 5.15.16
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

## upstreamable patches

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel >= %{version}
BuildRequires: qt5-qtsvg-devel >= %{version}
BuildRequires: hunspell-devel

# version unknown
Provides: bundled(libpinyin)

%description
The Qt Virtual Keyboard project provides an input framework and reference keyboard frontend
for Qt 5.  Key features include:
* Customizable keyboard layouts and styles with dynamic switching.
* Predictive text input with word selection.
* Character preview and alternative character view.
* Automatic capitalization and space insertion.
* Scalability to different resolutions.
* Support for different character sets (Latin, Simplified/Traditional Chinese, Hindi, Japanese, Arabic, Korean, and others).
* Support for most common input languages, with possibility to easily extend the language support.
* Left-to-right and right-to-left input.
* Hardware key support for 2-way and 5-way navigation.
* Handwriting support, with gestures for fullscreen input.
* Audio feedback.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%{qmake_qt5} \
  CONFIG+=lang-all

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%license LICENSE.*
%{_qt5_libdir}/libQt5HunspellInputMethod.so.5*
%{_qt5_libdir}/libQt5VirtualKeyboard.so.5*
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QVirtualKeyboardPlugin.cmake
%{_qt5_plugindir}/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_qt5_plugindir}/virtualkeyboard/
%{_qt5_qmldir}/QtQuick/VirtualKeyboard/

%files devel
%{_qt5_headerdir}/QtHunspellInputMethod/
%{_qt5_headerdir}/QtVirtualKeyboard/
%{_qt5_libdir}/libQt5HunspellInputMethod.prl
%{_qt5_libdir}/libQt5HunspellInputMethod.so
%{_qt5_libdir}/libQt5VirtualKeyboard.prl
%{_qt5_libdir}/libQt5VirtualKeyboard.so
%{_qt5_libdir}/cmake/Qt5HunspellInputMethod/
%{_qt5_libdir}/cmake/Qt5VirtualKeyboard/
%{_qt5_libdir}/pkgconfig/Qt5VirtualKeyboard.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_hunspellinputmethod*.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_virtualkeyboard*.pri

%files examples
%{_qt5_examplesdir}/


%changelog
* Thu Jan 09 2025 Zephyr Lykos <fedora@mochaa.ws> - 5.15.16-1
- 5.15.16

* Wed Sep 04 2024 Jan Grulich <jgrulich@redhat.com> - 5.15.15-1
- 5.15.15

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 Jan Grulich <jgrulich@redhat.com> - 5.15.14-1
- 5.15.14

* Thu Mar 14 2024 Jan Grulich <jgrulich@redhat.com> - 5.15.13-1
- 5.15.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Jan Grulich <jgrulich@redhat.com> - 5.15.12-1
- 5.15.12

* Fri Oct 06 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.11-1
- 5.15.11

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.10-1
- 5.15.10

* Tue Apr 11 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.9-1
- 5.15.9

* Tue Jan 31 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.8-4
- migrated to SPDX license

* Mon Jan 23 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 5.15.8-3
- Enable the Hunspell input method

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.8-1
- 5.15.8

* Mon Oct 31 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.7-1
- 5.15.7

* Tue Sep 20 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.6-1
- 5.15.6

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.5-1
- 5.15.5

* Mon May 16 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.4-1
- 5.15.4

* Fri Mar 04 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.3-1
- 5.15.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 07:54:16 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.2-2
- Rebuild for qtbase with -no-reduce-relocations option

* Fri Nov 20 09:30:47 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.2-1
- 5.15.2

* Thu Sep 10 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.1-1
- 5.15.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.14.2-1
- 5.14.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.13.2-1
- 5.13.2

* Tue Sep 24 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.5-1
- 5.12.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.4-1
- 5.12.4

* Tue Jun 04 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.3-1
- 5.12.3

* Fri Feb 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-1
- 5.12.1
- restore -devel subpkg

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.3-1
- 5.11.3

* Wed Oct 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.2-2
- do not log keypresses in release mode

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.2-1
- 5.11.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.1-1
- 5.11.1

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.0-1
- 5.11.0
- use %%make_build %%ldconfig_scriptlets

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 5.10.1-1
- 5.10.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Jan Grulich <jgrulich@redhat.com> - 5.10.0-1
- 5.10.0

* Thu Nov 23 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.3-1
- 5.9.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.2-1
- 5.9.2, BR: qt5-qtbase-private-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.1-1
- 5.9.1

* Fri Jun 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.0-2
- drop shadow/out-of-tree builds (#1456211,QTBUG-37417)

* Wed May 31 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-1
- Upstream official release

* Fri May 26 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.1.rc
- Upstream Release Candidate retagged

* Tue May 09 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.3
- Upstream beta 3

* Mon Apr 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.8.0-2
- update URL, %%description

* Thu Mar 30 2017 Helio Chissini de Castro <helio@kde.org> - 5.8.0-1
- New upstream version

* Fri Mar 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-4
- %%build: CONFIG+=lang-all, drop -devel (*Plugin.cmake can go in main)
- Provides: bundled(libpinyin)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-2
- updated sources, drop pkgconfig-style deps (for now)

* Wed Nov 09 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.1-1
- New upstream version

* Tue Jul 05 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-1
- New Qt 5.7.0 package
