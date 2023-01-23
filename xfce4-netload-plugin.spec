%global _hardened_build 1
%global minor_version 1.4
%global xfceversion 4.16

Name:           xfce4-netload-plugin
Version:        1.4.0
Release:        5%{?dist}
Summary:        Network-load monitor for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  gettext, intltool

Requires:       xfce4-panel >= %{xfceversion}

%description
A network-load monitor plugin for the Xfce panel.


%prep
%autosetup

%build
%configure
%make_build


%install
%make_install
%find_lang %{name}
chmod 755 %{buildroot}/%{_libdir}/xfce4/panel/plugins/libnetload.so
rm -f %{buildroot}/%{_libdir}/xfce4/panel/plugins/libnetload.la


%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/xfce4/panel/plugins/libnetload.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 11 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Tue Feb 02 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.2-5
- Fix FTBFS/rebuild for xfce 4.16

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.1-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.1-5
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 09 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1 (bugfix update)

* Sat Nov 05 2016 Kevin Fenzi <kevin@scrye.com> - 1.3.0-1
- Update to 1.3.0. (gtk3)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.2.4-2
- Rebuild for Xfce 4.12

* Sat Nov 22 2014 Kevin Fenzi <kevin@scrye.com> 1.2.4-1
- Update to 1.2.4. Fixes bug #1157193

* Sun Nov 16 2014 Kevin Fenzi <kevin@scrye.com> 1.2.3-1
- Update to 1.2.3

* Tue Nov 04 2014 Kevin Fenzi <kevin@scrye.com> 1.2.2-1
- Update to 1.2.2.

* Tue Oct 28 2014 Kevin Fenzi <kevin@scrye.com> 1.2.0-6
- Add patch to increase network interface name length to 20.
- Fixes bug #1002329

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Kevin Fenzi <kevin@scrye.com> - 1.2.0-1
- Update to 1.2.0 

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.1.0-4
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.1.0-3
- Rebuild for Xfce 4.10

* Fri Mar 09 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-2
- Don't use libxecdir if possible

* Sat Jan 14 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Add VCS key

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-4
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-2
- Rebuild for xfce4-panel 4.7

* Fri Dec 10 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Remove all patches (upstreamed)

* Wed Sep 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-12
- Fix bar colors (#505214)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-10
- Bring back tooltips in GTK 2.16 with Dimitar Zhekov's patch (#508637)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-8
- Rebuild for Xfce 4.6 (Beta 3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-7
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-6
- Rebuild for BuildID feature
- Update license tag

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-5
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-4
- Rebuild for Xfce 4.4.
- Patch to compile with -Wl,--as-needed (bugzilla.xfce.org #2782)

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-2
- BR perl(XML::Parser).

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4 on XFCE 4.3.90.2.
- Remove bufsize-patch for now.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.3-7
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-6
- Require xfce4-panel.

* Sat Feb 18 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-5
- Rebuild for Fedora Extras 5.
- Modify bufsize-patch.

* Thu Feb 02 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-4
- Add bufsize-patch (#179686).

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-3
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-2
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-1.fc4.cw
- Updated to version 0.3.3.
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-1.fc4.cw
- Updated to version 0.3.2.
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-1.fc3.cw
- Updated to version 0.3.1.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.3-1.fc3.cw
- Initial RPM release.
