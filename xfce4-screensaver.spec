%global majorver 4.16

Name:           xfce4-screensaver
Version:        4.16.0
Release:        5%{?dist}
Summary:        Screensaver application for Xfce Desktop

License:        GPLv2 and LGPLv2
URL:            https://git.xfce.org/apps/xfce4-screensaver/
Source0:        https://archive.xfce.org/src/apps/%{name}/%{majorver}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(garcon-gtk3-1)
BuildRequires:  libwnck3-devel
BuildRequires:  systemd-devel
BuildRequires:  pam-devel
BuildRequires:  desktop-file-utils

Requires:       xfdesktop
Requires:       xfconf
Requires:       xfce4-session

%description
Xfce Screensaver is a port of MATE Screensaver, itself a port of GNOME 
Screensaver. It has been tightly integrated with the Xfce desktop, utilizing 
Xfce libraries and the Xfconf configuration backend.


%prep
%autosetup


%build
%configure --with-systemd --enable-pam --enable-locking

%make_build

%install
%make_install

for file in %{buildroot}%{_datadir}/applications/screensavers/*.desktop ; do
     desktop-file-install \
         --add-category="X-XFCE" \
         --delete-original \
         --dir=%{buildroot}%{_datadir}/applications/screensavers \
         $file
done

desktop-file-install \
      --add-category="X-XFCE" \
      --delete-original \
      --dir=%{buildroot}%{_datadir}/applications \
      %{buildroot}%{_datadir}/applications/%{name}-preferences.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYING.LGPL
%{_sysconfdir}/pam.d/xfce4-screensaver
%{_sysconfdir}/xdg/autostart/xfce4-screensaver.desktop
%{_sysconfdir}/xdg/menus/xfce4-screensavers.menu
%{_bindir}/%{name}
%{_bindir}/xfce4-screensaver-command
%{_bindir}/xfce4-screensaver-configure
%{_bindir}/xfce4-screensaver-preferences
%{_libexecdir}/xfce4-screensaver-dialog
%{_libexecdir}/xfce4-screensaver-gl-helper
%{_datadir}/icons/hicolor/*/apps/org.xfce.ScreenSaver.*
%{_datadir}/applications/screensavers/xfce-personal-slideshow.desktop
%{_datadir}/applications/screensavers/xfce-popsquares.desktop
%{_datadir}/applications/screensavers/xfce-floaters.desktop
%{_datadir}/applications/xfce4-screensaver-preferences.desktop
%{_datadir}/dbus-1/services/org.xfce.ScreenSaver.service
%{_datadir}/desktop-directories/xfce4-screensaver.directory
%{_mandir}/man1/xfce4-screensaver-command.1.*
%{_mandir}/man1/xfce4-screensaver-preferences.1.*
%{_mandir}/man1/xfce4-screensaver.1.*
%{_datadir}/pixmaps/xfce-logo-white.svg
%{_libexecdir}/%{name}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.0-1
- Update to 4.16.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10

* Tue Mar 24 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.8-2
- Add libwnck3-devel as buildrequires

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.6-2
- Drop *.pc file

* Mon Jul 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Thu Jun 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Sat Mar 23 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Dan Horák <dan[at]danny.cz> - 0.1.3-2
- Add BR: desktop-file-utils explicitly

* Tue Nov 27 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Thu Nov 01 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Wed Oct 31 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.1-2
- Fix files section

* Wed Oct 31 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Tue Oct 23 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.0-3
- Fix requires
- Add --enable-locking configure flag

* Fri Oct 19 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 0.1.0-2
- Fixed package review issues

* Fri Oct 19 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 0.1.0-1
- Initial pacakge
