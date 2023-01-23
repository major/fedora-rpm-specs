# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173549

%global _hardened_build 1
%global minorversion 1.1
%global xfceversion 4.16

Name:           xfce4-mount-plugin
Version:        1.1.5
Release:        6%{?dist}
Summary:        Mount/unmount utility for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-diskperf-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}

%description
Mount and unmount filesystems from the Xfce panel.

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
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/apps/xfce-mount.svg

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5

* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.3-20
- Rebuilt (xfce 4.13)

* Tue Jul 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.2-5
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2

* Sun Feb 19 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (bugfix release)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- gtk3 port

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.6.7-4
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 Kevin Fenzi <kevin@scrye.com> 0.6.7-1
- Update to 0.6.7

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Kevin Fenzi <kevin@scrye.com> - 0.6.3-1
- Update to 0.6.3

* Tue Apr 24 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-2
- Fix -debuginfo.

* Sat Apr 21 2012 Kevin Fenzi <kevin@scrye.com> - 0.6.1-1
- Update to 0.6.1

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 0.5.5-10
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.5.5-9
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.5-7
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-5
- Rebuild for xfce4-panel 4.7
- Update Source0 URL
- Update icon-cache scriptlets

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-2
- Rebuild for Xfce 4.6 (Beta 3)

* Sat May 24 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5. Can now mount devices by UUID

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5.1-4
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-3
- Rebuild for BuildID feature
- Update license tag

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-2
- Rebuild for Xfce 4.4.1

* Sat Mar 03 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1.

* Fri Mar 02 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0.

* Sun Jan 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.8-2
- Rebuild for Xfce 4.4.
- Update gtk-icon-cache scriptlets.

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.8-1
- Update to 0.4.8.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.5-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser), drop BR intltool.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.5-1
- Update to 0.4.5 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.3-5
- Mass rebuild for Fedora Core 6.

* Sat Jun 03 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-4
- BuildRequire intltool (#193444) and gettext.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-3
- Require xfce4-panel.

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-2
- Rebuild for Fedora Extras 5.

* Sat Jan 21 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-1
- Update to 0.3.3.

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-3
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-2
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-1.fc4.cw
- Updated to version 0.3.2.
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3-1.fc4.cw
- Updated to version 0.3.
- Rebuild for Core 4.

* Thu Apr 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.1-1.fc3.cw
- Initial RPM release.
