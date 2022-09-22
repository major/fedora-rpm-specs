# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173657

%global _hardened_build 1
%global minorversion 1.6
%global xfceversion 4.16

Name:           xfce4-clipman-plugin
Version:        1.6.2
Release:        5%{?dist}
Summary:        Clipboard manager plugin for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  exo-devel >= 0.6.0
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  xorg-x11-proto-devel >= 7.0.0
BuildRequires:  libXtst-devel >= 1.0.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  qrencode-devel
Requires:       xfce4-panel >= %{xfceversion}

%description
This is a simple cliboard history for Xfce panel. It includes a "Clear 
clipboard" option, and a drag-and-drop paste feature.


%prep
%autosetup


%build
%configure --disable-static --enable-unique --enable-libqrencode
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original \
  %{buildroot}%{_datadir}/applications/xfce4-clipman.desktop

desktop-file-install \
  --dir %{buildroot}%{_sysconfdir}/xdg/autostart \
  --delete-original  \
  %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING
%config %{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%config(noreplace) %{_sysconfdir}/xdg/xfce4/panel/xfce4-clipman-actions.xml
%{_bindir}/xfce4-clipman
%{_bindir}/xfce4-clipman-history
%{_bindir}/xfce4-clipman-settings
%{_bindir}/xfce4-popup-clipman
%{_bindir}/xfce4-popup-clipman-actions
%{_libdir}/xfce4/panel/plugins/libclipman*
%{_datadir}/applications/xfce4-clipman-settings.desktop
%{_datadir}/applications/xfce4-clipman.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/xfce4/panel/plugins/%{name}.desktop
%{_datadir}/metainfo/xfce4-clipman.appdata.xml
%{_datadir}/icons/hicolor/16x16/apps/clipman-symbolic.svg

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.2-3
- drop BR on unique-devel

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Kevin Fenzi <kevin@scrye.com> - 1.6.2-1
- Update to 1.6.2.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 07 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Mon Mar 30 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sun Mar 01 2020 Kevin Fenzi <kevin@scrye.com> - 1.4.4-1
- Update to 1.4.4

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 1.4.3-3
- Rebuilt (libqrencode.so.4)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.2-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.4.2-5
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.4.2-1
- Update to 1.4.2, fixes rhbz#1404980
- Port to GtkApplication (this should help with keyboard shortcut issues)
- Translation updates: Catalan, Croatian, Danish, Dutch (Flemish),
  Greek, Indonesian, Italian, Kazakh, Lithuanian, Norwegian Bokmal,
  Serbian, Thai

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1
- Add new symbolic icon to files

* Sat Nov 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.4.0-2
- Spec clean up

* Thu Sep 15 2016 Kevin Fenzi <kevin@scrye.com> - 1.4.0-1
- Update to 1.4.0. Move to gtk3 based.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Kevin Fenzi <kevin@scrye.com> 1.2.6-6
- Enable qr code

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.2.6-5
- Rebuild for Xfce 4.12

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.2.6-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Kevin Fenzi <kevin@scrye.com> 1.2.6-1
- Update to 1.2.6

* Wed Feb 05 2014 Kevin Fenzi <kevin@scrye.com> 1.2.5-1
- Update to 1.2.5

* Mon Feb 03 2014 Kevin Fenzi <kevin@scrye.com> 1.2.4-1
- Update to 1.2.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Kevin Fenzi <kevin@scrye.com> - 1.2.3-1
- Update to 1.2.3

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.2.2-4
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.2.2-3
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2
- Enable support for unique

* Mon Oct 31 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1
- Drop all patches
- New BR xorg-x11-xproto-devel and libXtst-devel
- No longer BR libglade2-devel
- No longer require xfce4-doc (#721291)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Kevin Fenzi <kevin@tummy.com> - 1.1.3-3
- Add patch to build with new exo

* Thu Jan 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.3-2
- Fix possible NULL values (#552892 and #552895)

* Mon Nov 16 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Thu Oct 01 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Fri Sep 04 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Thu Jun 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-2
- BR desktop-file-utils

* Thu May 14 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Tue Apr 21 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Require xfce4-doc

* Mon Mar 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.1-2
- Update to 0.9.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.0-2
- Update to 0.9.0
- Update license tag to GPLv2+

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.1-2
- Rebuild for Xfce 4.6 (Beta 3)

* Fri Mar 07 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1 (fixes bugzilla.xfce.org #3304)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.0-4
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-3
- Rebuild for BuildID feature

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-2
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0 on Xfce 4.4.

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.99.1-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.99.1-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser).

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.99.1-1
- Update to 0.5.99.1.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.90.2-1
- Update to 0.5.90.2 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-7
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.4.1-6
- Require xfce4-panel.

* Wed Feb 15 2006 Christoph Wickert <fedora wickert at arcor de> - 0.4.1-5
- Rebuild for Fedora Extras 5.

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.1-4
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.1-3
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.1-2.fc4.cw
- Update to 0.4.1.
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.1-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.1-1.fc3.cw
- Initial RPM release.
