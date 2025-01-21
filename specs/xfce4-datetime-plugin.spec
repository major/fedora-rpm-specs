%global _hardened_build 1
%global minorversion 0.8
%global xfceversion 4.16

Name:           xfce4-datetime-plugin
Version:        0.8.2
Release:        8%{?dist}
Summary:        Date/time plugin for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-datetime-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}

%description
An alternative clock plugin for the Xfce panel. A calendar appears when you 
left-click on it.


%prep
%autosetup


%build
%configure --disable-static
%make_build


%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS THANKS
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 22 2024 Mukundan Ragavan <nonamedotc@gmail.com> - 0.8.2-7
- rebuild for xfce-4.20

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.2-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Kevin Fenzi <kevin@scrye.com> - 0.8.2-1
- Update to 0.8.2. Likely the last release, please move to the panel clock plugin.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.0-7
- added gcc as BR

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.0-6
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.0-1
- Update to 0.7.0
- [gtk3] Bump dependencies to check for libxfce4ui-2/libxfce4panel-2.0
- Spec clean-up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.6.2-5
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2
- Remove all patches (either upstreamed or obsolete)
- Add VCS key

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 0.6.1-11
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.6.1-10
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.1-8
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-6
- Patch for xfce4-panel 4.7

* Sat Dec 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-5
- Bring back tooltips (#609129)
- Update translations from Xfce Transifex

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-2
- Rebuild for Xfce 4.6 (Beta 3)

* Thu Nov 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1
- Include NEWS and THANKS docs

* Thu Jul 03 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0
- BuildRequire intltool
- No longer BuildRequire dbus-devel (requirement dropped upstream)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5.0-4
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-3
- Rebuild for BuildID feature
- Update license tag

* Sat Jun 09 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-2
- Multilib fix for desktop file (#228168).

* Sat Feb 24 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0.

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-2
- Rebuild for Xfce 4.4.
- Patch datetime.c to 0.4.2.

* Fri Dec 22 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1.

* Sun Oct 15 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0 on Xfce 4.4. RC1.
- Fix %%defattr.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.1-8
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-7
- Require xfce4-panel.

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-6
- Rebuild for Fedora Extras 5.

* Tue Nov 29 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-5
- Add libxfcegui4-devel BuildReqs.

* Fri Nov 25 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-4
- Rebuild with new source because of md5sum mismatch.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-3
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-2.fc4.cw
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-1.fc3.cw
- Initial RPM release.
