Name:           maliit-keyboard
Version:        2.3.1
Release:        3%{?dist}
Summary:        Maliit Keyboard 2

License:        LGPLv3 and BSD
URL:            https://maliit.github.io/
Source0:        https://github.com/maliit/keyboard/archive/%{version}/%{name}-%{version}.tar.gz 


BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: maliit-framework-devel >= 2.3.0
BuildRequires: glib2-devel
BuildRequires: hunspell-devel
BuildRequires: gettext

BuildRequires: anthy-unicode-devel
BuildRequires: libpinyin-devel
BuildRequires: libchewing-devel

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtfeedback-devel
BuildRequires: qt5-qtquickcontrols2-devel


%description
Based on Ubuntu Keyboard. Ubuntu Keyboard was a QML and C++ based Keyboard
Plugin for Maliit, based on the Maliit Reference plugin, taking into account the
special UI/UX requests of Ubuntu Phone.


%prep
%autosetup -n keyboard-%{version} -p1


%build
%cmake -Denable-presage=OFF

%cmake_build


%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/doc/maliit-keyboard
%find_lang %{name}

%files -f %{name}.lang
%license COPYING.BSD COPYING.LGPL COPYING
%doc README.md
%{_bindir}/maliit-keyboard
%dir %{_libdir}/maliit/
%{_libdir}/maliit/keyboard2/
%{_libdir}/maliit/plugins/
%dir %{_datadir}/maliit/
%{_datadir}/maliit/keyboard2/
%{_datadir}/glib-2.0/schemas/org.maliit.keyboard.maliit.gschema.xml
%{_datadir}/applications/com.github.maliit.keyboard.desktop
%{_metainfodir}/com.github.maliit.keyboard.metainfo.xml


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Peng Wu <pwu@redhat.com> - 2.3.1-2
- Rebuild for libpinyin soname bump

* Tue Sep 20 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.3.1-1
- 2.3.1
- Old patches removed
- BR qt5-qtquickcontrols2-devel added
- Licenses are LGPLv3 and BSD

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Takao Fujiwara <tfujiwar@redhat.com> - 2.2.0-2
- add anthy-unicode build

* Tue Feb 15 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.2.0-1
- Version 2.2.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Troy Dawson <tdawson@redhat.com> - 2.0.0-4
- anthy is depricated.  Use anthy-unicode-devel (#2005423)

* Mon Aug 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-3
- fix %%files ownership
- drop explicit BR: make (already pulled in by cmake)
- drop needless ldconfig scriptlet

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Jan Grulich <jgrulich@redhat.com> - 2.0.0-1
- 2.0.0
