# review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173661

%global _hardened_build 1
%global minorversion 1.1
%global xfceversion 4.16

Name:           xfce4-fsguard-plugin
Version:        1.1.2
Release:        5%{?dist}
Summary:        Filesystem-Guard plugin for the Xfce panel

License:        BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-fsguard-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}

%description
A little Xfce plugin, which checks the free space on the chosen mountpoint 
frequently. It displays 4 different icons and a message box, depending on the
free space. The amount of free disk space is visible in a tooltip. If you 
left-click on its icon, it opens the mountpoint directory in the file manager.


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
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.0-6
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.0-1
- Update to 1.1.0
- [gtk3] Bump dependencies to check for libxfce4ui-2/libxfce4panel-2.0
- Spec clean-up

* Mon Apr 18 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.2-4
- Added EL conditional

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 04 2015 Kevin Fenzi <kevin@scrye.com> 1.0.2-1
- Update to 1.0.2

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.0.1-7
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1
- Define the Xfce version conditionally
- Add review # and VCS key

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-7
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-6
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-4
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-2
- Rebuild for xfce4-panel 4.7

* Thu Dec 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Update icon-cache scriptlets

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-2
- Rebuild for Xfce 4.6 (Beta 3)

* Thu Nov 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2
- BR intltool
- Update gtk-update-icon-cache scriptlets

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.1-2
- Autorebuild for GCC 4.3

* Sun Jan 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Fri Dec 07 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-2
- Rebuild for Xfce 4.4.2

* Thu Nov 08 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Fri Aug 24 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-6
- Rebuild for BuildID feature

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-5
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-4
- Rebuild for Xfce 4.4
- Patch to compile with -Wl,--as-needed (bugzilla.xfce.org #2783)

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser).

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-5
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.2.1-4
- Require xfce4-panel.

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 0.2.1-3
- Rebuild for Fedora Extras 5.

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.1-2
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.1-1
- Initial Fedora Extras version.
- Update to 0.2.1.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.0-2.fc4.cw
- Add libxml2 BuildReqs.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.0-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.0-1.fc3.cw
- Initial RPM release.
