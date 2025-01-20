Name:    redshift
Version: 1.12
Release: 25%{dist}
Summary: Adjusts the color temperature of your screen according to time of day
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later

URL:     http://jonls.dk/redshift/
Source0: https://github.com/jonls/redshift/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: libtool
BuildRequires: intltool
BuildRequires: gettext-devel
BuildRequires: libdrm-devel
BuildRequires: libXrandr-devel
BuildRequires: libXxf86vm-devel
BuildRequires: GConf2-devel
BuildRequires: geoclue2-devel
Requires:      geoclue2
%{?systemd_requires}
BuildRequires: systemd

%description
Redshift adjusts the color temperature of your screen according to your
surroundings. This may help your eyes hurt less if you are working in
front of the screen at night.

The color temperature is set according to the position of the sun. A
different color temperature is set during night and daytime. During
twilight and early morning, the color temperature transitions smoothly
from night to daytime temperature to allow your eyes to slowly
adapt.

This package provides the base program.

%package -n %{name}-gtk
Summary:       GTK integration for Redshift

BuildRequires: desktop-file-utils
BuildRequires: python3-devel >= 3.2
Requires:      python3-gobject
Requires:      python3-pyxdg
Requires:      %{name} = %{version}-%{release}
Obsoletes:      gtk-%{name} < 1.7-7

%description -n %{name}-gtk
This package provides GTK integration for Redshift, a screen color
temperature adjustment program.

%prep
%autosetup -N -n %{name}-%{version}
autopoint -f && AUTOPOINT="intltoolize --automake --copy" autoreconf -f -i

%build
%configure --with-systemduserunitdir=%{_userunitdir}
%make_build V=1

%install
%make_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/redshift.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/redshift-gtk.desktop

%post
%systemd_user_post %{name}-gtk.service

%preun
%systemd_user_preun %{name}-gtk.service


%files -f %{name}.lang
%doc DESIGN CONTRIBUTING.md NEWS NEWS.md README README-colorramp README.md redshift.conf.sample
%license COPYING
%{_bindir}/redshift
%{_mandir}/man1/*
%{_datadir}/applications/redshift.desktop
%{_userunitdir}/%{name}.service

%files -n %{name}-gtk
%{_bindir}/redshift-gtk
%{python3_sitelib}/redshift_gtk/
%{_datadir}/icons/hicolor/scalable/apps/redshift*.svg
%{_datadir}/applications/redshift-gtk.desktop
%{_datadir}/appdata/redshift-gtk.appdata.xml
%{_userunitdir}/%{name}-gtk.service

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12-24
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.12-22
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.12-18
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.12-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.12-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Milos Komarcevic <kmilos@gmail.com> - 1.12-10
- Drop Python 2
- Explicitly require geoclue2 (#1492899)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.12-1
- Update to 1.12 (#1581005)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.11-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Milos Komarcevic <kmilos@gmail.com> - 1.11-1
- Update to 1.11 (#1295151)

* Mon Dec 07 2015 Milos Komarcevic <kmilos@gmail.com> - 1.10-6
- Fix broken doc symlinks (#1222341)

* Mon Dec 07 2015 Matěj Cepl <mcepl@redhat.com> - 1.10-5
- Make buildable on EPEL (#1204257)

* Sun Nov 22 2015 Milos Komarcevic <kmilos@gmail.com> - 1.10-4
- Add a redshift desktop file (#1214978)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 07 2015 Milos Komarcevic <kmilos@gmail.com> - 1.10-1
- Update to 1.10 (#1178819)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 23 2014 Milos Komarcevic <kmilos@gmail.com> - 1.9.1-1
- Update to 1.9.1 (#1090018)

* Sat Nov 30 2013 Milos Komarcevic <kmilos@gmail.com> - 1.8-1
- Update to 1.8 (#1029155)
- Source comes from GitHub now

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Milos Komarcevic <kmilos@gmail.com> - 1.7-5
- Run autoreconf to support aarch64 (#926436)
- Backport fix for geoclue client check (#954014)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 9 2011 Milos Komarcevic <kmilos@gmail.com> - 1.7-1
- Update to 1.7
- Add geoclue BuildRequires
- Change default geoclue provider from Ubuntu GeoIP to Hostip
- Remove manual Ubuntu icons uninstall

* Mon Feb 28 2011 Milos Komarcevic <kmilos@gmail.com> - 1.6-3
- Fix for clock applet detection (#661145)
- Require pyxdg explicitly (#675804)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010 Milos Komarcevic <kmilos@gmail.com> - 1.6-1
- Update to 1.6
- Remove BuildRoot tag and clean section

* Thu Aug 26 2010 Milos Komarcevic <kmilos@gmail.com> - 1.5-1
- Update to 1.5
- Install desktop file

* Mon Jul 26 2010 Milos Komarcevic <kmilos@gmail.com> - 1.4.1-2
- License updated to GPLv3+
- Added python macros to enable building on F12 and EPEL5
- Specific python version BR
- Subpackage requires full base package version
- Increased build log verbosity
- Preserve timestamps on install

* Thu Jun 17 2010 Milos Komarcevic <kmilos@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Thu Jun 10 2010 Milos Komarcevic <kmilos@gmail.com> - 1.3-1
- Initial packaging
