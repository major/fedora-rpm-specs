# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173660

%global _hardened_build 1
%global minorversion 2.7
%global xfceversion 4.16

Name:           xfce4-diskperf-plugin
Version:        2.7.0
Release:        4%{?dist}
Summary:        Disk performance plugin for the Xfce panel

License:        BSD
URL:            http://goodies.xfce.org/panel-plugins/{%name}
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
The DiskPerf plugin displays disk/partition performance (bytes transfered per
second) based on data provided by the kernel.

%prep
%autosetup

%build
%configure --disable-static
%make_build


%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 7 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.3-1
- Update to 2.6.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.1-20
- Rebuilt (xfce 4.13)

* Tue Jul 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.1-7
- Add fix for glibc-2.25+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.6.1-5
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.6.0-1
- Update to 2.6.0
- [gtk3] Bump dependencies to check for libxfce4ui-2/libxfce4panel-2.0
- Spec clean-up

* Fri Apr 15 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.5-4
- Added EL conditional for Xfce 4.12

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 04 2015 Kevin Fenzi <kevin@scrye.com> 2.5.5-1
- Update to 2.5.5

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 2.5.4-8
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 2.5.4-2
- Define the Xfce version conditionally

* Sat Jun 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 2.5.4-1
- Update to 2.5.4

* Sun May 13 2012 Christoph Wickert <cwickert@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3

* Mon Apr 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2 (Xfce 4.10 final)
- Add VCS key

* Tue Apr 24 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.5.1-2
- Fix -debuginfo.

* Sat Apr 21 2012 Kevin Fenzi <kevin@scrye.com> - 2.5.1-1
- Update to 2.5.1

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 2.3.0-5
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 2.3.0-4
- Rebuild for Xfce 4.10

* Tue Feb 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.0-3
- Add patch to fix DSO linking
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
- Rebuild for new libpng

* Mon Jun 06 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.0-2
- Rebuild to fix build bug with FORTIFY_SOURCE (#702869)

* Fri Feb 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0
- Remove all patches

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Adam Williamson <awilliam@redhat.com> - 2.2.0-7
- 01_fix-linking-libxfcegui4.patch: fix underlinking (Landry Breuil)
- 02_fix-libtool.patch: fix autoconf (upstream via Debian)

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.0-6
- Add patch to fix DSO linking (#564985)

* Thu Sep 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.0-5
- Fix custom bar colors at startup (bugzilla.xfce.org #3074)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.0-2
- Rebuild for Xfce 4.6 (Beta 3)

* Sun Apr 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.0-5
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.0-4
- Rebuild for BuildID feature

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.0-3
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.0-2
- Rebuild for Xfce 4.4.

* Sat Jan 20 2007 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0.
- Remove patch for #215863, fixed upstream.

* Sat Nov 25 2006 Christoph Wickert <cwickert@fedoraproject.org> - 2.0-4
- Add patch to fix bug bugzilla.xfce.org #1842 (#215863)

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 2.0-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 2.0-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser).

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 2.0-1
- Update to 2.0 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 1.5-7
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 1.5-6
- Require xfce4-panel.

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 1.5-5
- Rebuild for Fedora Extras 5.

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 1.5-4
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 1.5-3
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 1.5-2.fc4.cw
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 1.5-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 1.5-1.fc3.cw
- Initial RPM release.
