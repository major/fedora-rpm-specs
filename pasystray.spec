Name:           pasystray
Version:        0.8.0
Release:        6%{?dist}
Summary:        PulseAudio system tray
License:        LGPLv2+
URL:            https://github.com/christophgysin/pasystray

Source0:        https://github.com/christophgysin/pasystray/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/christophgysin/pasystray/issues/151, fixed post-0.8.0
Patch0:         pasystray-0.8.0-symbolic-icons.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1471192
# https://bugzilla.redhat.com/show_bug.cgi?id=2035305
Patch1:         pasystray-0.8.0-wayland.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  desktop-file-utils

%if 0%{?fedora}
Suggests:       paman
Suggests:       pavucontrol
Suggests:       pavumeter
#Suggests:       paprefs
#Suggests:       pulseaudio-qpaeq
%endif

%description
A replacement for the deprecated padevchooser.
pasystray allows setting the default PulseAudio source/sink and moving streams
on the fly between sources/sinks without restarting the client applications.

%prep
%autosetup -p1

%build
autoreconf -i
%configure
%make_build

%install
%make_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 0.8.0-4
- Really make operational on Wayland (#2035305)

* Thu Dec 23 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 0.8.0-3
- Fix new crashes on Wayland (#2035305)

* Wed Dec 22 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 0.8.0-2
- Enable StatusNotifierItem instead of X11 tray icon
- Drop Suggests: paprefs, which does not work with PipeWire

* Tue Nov 30 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 0.7.1-1
- Update to 0.7.1
- Fix crashes on Wayland (#1471192, #1911962, #1912850)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Michael Simacek <msimacek@redhat.com> - 0.6.0-7
- Add BR on gcc and make

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 17 2016 Michael Simacek <msimacek@redhat.com> - 0.6.0-1
- Update to upstream version 0.6.0

* Sun Jun 19 2016 Michael Simacek <msimacek@redhat.com> - 0.5.2-1
- Initial packaging
