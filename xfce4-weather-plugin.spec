# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173105

%global minorversion 0.11

%global xfceversion 4.16

Name:           xfce4-weather-plugin
Version:        0.11.0
Release:        4%{?dist}
Summary:        Weather plugin for the Xfce panel

License:        BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-weather-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libsoup-devel >= 2.26.0
BuildRequires:  upower-devel >= 0.9.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libxml2-devel >= 2.4.0
Requires:       xfce4-panel >= %{xfceversion}

%description
A weather plugin for the Xfce panel. It shows the current temperature and 
weather condition, using weather data provided by xoap.weather.com.


%prep
%autosetup

%build
%configure
%make_build

%install
%make_install


# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/weather


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 11 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.10.2-1
- Update to 0.10.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.10.1-2
- Enable scrolling in details pane

* Sun Feb 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.11-1
- Update to 0.8.11

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.4-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.10-1
- Update to 0.8.10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.9-1
- Update to 0.8.9
- spec clean up (old macros, upstreamed translation fixes)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.8-2
- Add a translation fix
- Fixes #1377672

* Thu Sep 01 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.8-1
- Update to 0.8.8 (uses new api)

* Thu Apr 21 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7-1
- Updated to v0.8.7

* Fri Apr 15 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.6-3
- Add EL conditional to xfce version logic
- Minor spec file clean up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Kevin Fenzi <kevin@scrye.com> 0.8.6-1
- Update to 0.8.6

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.8.5-2
- Rebuild for Xfce 4.12

* Tue Dec 23 2014 Kevin Fenzi <kevin@scrye.com> 0.8.5-1
- Update to 0.8.5

* Tue Nov 04 2014 Kevin Fenzi <kevin@scrye.com> 0.8.4-1
- Update to 0.8.4

* Fri Oct 17 2014 Kevin Fenzi <kevin@scrye.com> 0.8.3-8
- Add patch to fix color typo that prevented colors from being saved. 
- Fixes bug #983194

* Sat Oct 11 2014 Kevin Fenzi <kevin@scrye.com> 0.8.3-7
- Add upstream patches to switch to new v1.2 weather api. 
- Upstream bug https://bugzilla.xfce.org/show_bug.cgi?id=10916
- Fixes bugs #1150329 #1119857

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 0.8.3-6
- Rebuilt for upower 0.99.1 soname bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 30 2013 Kevin Fenzi <kevin@scrye.com> 0.8.3-3
- Rebuild for new upower

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3
- BuildRequire upower-devel and libsoup-devel

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 15 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Mon Aug 06 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Mon Jul 23 2012 Kevin Fenzi <kevin@scrye.com> - 0.8.0-1
- Update to 0.8.0

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 0.7.4-6
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.7.4-5
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.4-3
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Kevin Fenzi <kevin@tummy.com> - 0.7.4-1
- Update to 0.7.4

* Thu Jan 13 2011 Kevin Fenzi <kevin@tummy.com> - 0.7.3-2
- Rebuild for Xfce 4.8

* Sun Aug 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3, fixes cache directory creation

* Tue Jul 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2
- No longer contains weather.com logo, downloaded to cache at runtime (#513057)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Wed Jun 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Sat Jun 13 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2-4
- Rebuild for Xfce 4.6 (Beta 3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.2-3
- Autorebuild for GCC 4.3

* Fri Dec 07 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2-2
- Rebuild for Xfce 4.4.2

* Mon Nov 19 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2-1
- Update to 0.6.0 on Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0 on Xfce 4.4.
- Update gtk-icon-cache scriptlets.

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.99.1-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.99.1-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser).

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.99.1-1
- Update to 0.5.99.1.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.90.2-1
- Update to 0.5.90.2 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-7
- Mass rebuild for Fedora Core 6.

* Sat Jul 29 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-6
- BuildRequire gettext (#193444)
- Require xfce4-panel.

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 0.4.9-5
- Rebuild for Fedora Extras 5.

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.9-4
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.9-3
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.9-2.fc4.cw
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.9-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.4.9-1.fc3.cw
- Updated to version 0.4.9.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.9.1-1.fc3.cw
- Initial RPM release.
