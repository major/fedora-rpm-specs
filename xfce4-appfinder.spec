%global xfceversion 4.16

Name:           xfce4-appfinder
Version:        4.16.1
Release:        5%{?dist}
Summary:        Appfinder for the Xfce4 Desktop Environment

License:        GPLv2+
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfce4-appfinder
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.84
BuildRequires:  pkgconfig(garcon-1) >= 0.1.7
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfceversion}
BuildRequires:  startup-notification-devel
BuildRequires:  gettext 
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
xfce-appfinder shows system wide installed applications.


%prep
%setup -q

# fix icon problems - GTK-3.10+
sed -i 's/gtk-find/edit-find/g' data/xfce4-appfinder.desktop.in
sed -i 's/gtk-execute/system-run/g' data/xfce4-run.desktop.in

%build
%configure

%make_build

%install
%make_install


desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/xfce4-run.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.xfce.%{name}.appdata.xml

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc TODO ChangeLog AUTHORS
%{_bindir}/xfce4-appfinder
%{_bindir}/xfrun4
%{_datadir}/applications/xfce4-*.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.appfinder*
%{_metainfodir}/org.xfce.%{name}.appdata.xml

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.1-1
- Update to 4.16.1

* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.0-1
- Update to 4.16.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.14.0-1
- Update to 4.14.0

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.5-1
- Update to 4.13.5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.4-1
- Update to 4.13.4

* Sat May 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.3-1
- Update to 4.13.3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.2-1
- Update to 4.13.2

* Thu Aug 23 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.1-1
- Update to 4.13.1

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.0-20
- Update to 4.13.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 08 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.0-3
- Fix for icon not displaying for "Run Program" menu item

* Sun Mar 08 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.0-2
- Fix for icon not displaying in menu - bug# 1199225

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.0-1
- Update to latest stable release 4.12
- spec cleanup

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 4.10.1-5
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 05 2013 Kevin Fenzi <kevin@scrye.com> 4.10.1-1
- Update to 4.10.1, drop upstreamed patches

* Fri Mar 29 2013 Kevin Fenzi <kevin@scrye.com> 4.10.0-5
- Add patch to fix segfault with icon theme handling
- https://bugzilla.xfce.org/show_bug.cgi?id=9730

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-3
- Use full patch for bugzilla.xfce.org #9109 from upstream (#826486)

* Wed Jul 18 2012 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 4.10.0-2
- Patch for https://bugzilla.xfce.org/show_bug.cgi?id=9109

* Sun Apr 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-1
- Update to 4.10.0 final
- Add VCS key

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.5-1
- Update to 4.9.5 (Xfce 4.10pre2)

* Tue Apr 03 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.4-1
- Update to 4.9.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.9.3-1
- Update to 4.9.3
- Make build more verbose
- Switch to pkgconfig-style BuildRequires

* Fri Nov 04 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.9.2-1
- Update to 4.9.2
- Remove icon-cache scriptlets because this package no longer installs icons

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.0-1
- Update to 4.8.0

* Sun Jan 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Mon Nov 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.1-1
- Update to 4.7.1

* Sun Sep 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.0-1
- Update to 4.7.0
- Update icon-cache scriptlets

* Fri May 21 2010 Kevin Fenzi <kevin@tummy.com> - 4.6.2-1
- Update to 4.6.2

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 19 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.1-1
- Update to 4.6.1

* Thu Feb 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.0-1
- Update to 4.6.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.99.1-1
- Update to 4.5.99.1

* Tue Jan 13 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.93-1
- Update to 4.5.93

* Tue Dec 23 2008 Kevin Fenzi <kevin@tummy.com> - 4.5.92-1
- Update to 4.5.92

* Mon Oct 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.3-1
- Update to 4.4.3
- Update gtk-update-icon-cache scriptlets

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-2
- Rebuild for gcc43

* Sun Nov 18 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.2-1
- Update to 4.4.2

* Mon Aug 27 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-2
- Update License tag

* Sun Apr 15 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-1
- Update to 4.4.1
- Own some unowned directories

* Sun Jan 21 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.0-1
- Update to 4.4.0

* Fri Nov 10 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.2-1
- Update to 4.3.99.2

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-3
- Add period to description
- Fix defattr
- Add gtk-update-icon-cache

* Wed Oct  4 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-2
- Bump release for devel checkin

* Sun Sep  3 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-1
- Upgrade to 4.3.99.1
- Remove 0 length NEWS file
- Clean up macros in changelog

* Wed Jul 12 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.90.2-1
- Upgrade to 4.3.90.2

* Thu May 18 2006 Kevin Fenzi <kevin@tummy.com> - 4.2.3-3
- Add patch to fix crash in information selection (fixes #192195)

* Thu Feb 16 2006 Kevin Fenzi <kevin@tummy.com> - 4.2.3-2.fc5
- Rebuild for fc5 

* Mon Nov  7 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.3-1.fc5
- Update to 4.2.3
- Added dist tag
- Added doc/he

* Tue May 17 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.2-1.fc4
- Update to 4.2.2
- Add doc/fr

* Fri Mar 25 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-3.fc4
- lowercase Release

* Sun Mar 20 2005 Warren Togami <wtogami@redhat.com> - 4.2.1-2
- fix BuildReqs

* Tue Mar 15 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-1
- Updated to 4.2.1 version
- Fixed %%files section to not list lang files twice

* Tue Mar  8 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.0-2
- Fixed to use %%find_lang
- Removed generic INSTALL from %%doc
- Fixed case on Xfce

* Sun Mar  6 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.0-1
- Inital Fedora Extras version
