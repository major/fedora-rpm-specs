# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173105
%global _hardened_build 1

%global minorversion 1.1
%global xfceversion 4.16

Name:           xfce4-battery-plugin
Version:        1.1.4
Release:        5%{?dist}
Summary:        Battery monitor for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-battery-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}

%description
A battery monitor plugin for the Xfce panel, compatible with APM and ACPI.


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
%doc AUTHORS COPYING.LIB ChangeLog README.md
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2

* Sat Sep 22 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.0-7
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.0-2
- Drop unneeded patch

* Sat Nov 05 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.0-1
- Update to stable release of gtk3 port - version 1.1.0
- Minor spec file clean up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 19 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.0.5-9
- fix build on aarch64

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.0.5-8
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.5-2
- Define the Xfce version conditionally

* Sat Jun 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Mon May 14 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Sun May 13 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Mon Apr 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (Xfce 4.10 final)
- Add VCS key

* Tue Apr 24 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-2
- Fix -debuginfo.

* Sat Apr 21 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.1-1
- Update to 1.0.1

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-6
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-5
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-3
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Patch for xfce4-panel >= 4.7.7

* Sat Dec 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-6
- Rebuild for xfce4-panel 4.7

* Sat Dec 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-5
- Use sysfs instead of procfs (bugzilla.xfce.org #3793)
- Correctly handle case when no battery is present (bugzilla.xfce.org #3546)
- Update translations from Xfce Transifex
- Use parallel make
- Fix Source0 URL
- Update icon-cache scriptlets

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-2
- Rebuild for Xfce 4.6 (Beta 3)

* Fri Sep 05 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1
- Remove acpi.patch (included upstream)
- Remove lower-acpi-polling.patch (upstream use different values)

* Sat Apr 05 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-4
- Fix for kernel 2.6.24  (bugzilla.xfce.org #3938)
- Lower acpi polling. (bugzilla.xfce.org #2948)
- Rebuild with gcc 4.3.0

* Tue Aug 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-3
- Fix for x86_64 kernels >= 2.6.21. (bugzilla.xfce.org #3190)
- Update license tag

* Mon Apr 23 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-2
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0 on Xfce 4.4.

* Sat Nov 11 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.90.3-1
- Update to 0.4.90.3 on XFCE 4.3.99.2.

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.90.2-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.90.2-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser).

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.90.2-1
- Update to 0.4.90.2 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-7
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.0-6
- Require xfce4-panel.
- Change license back to LGPL (#173105).

* Wed Feb 15 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.0-5
- Rebuild for Fedora Extras 5.

* Fri Dec 30 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.0-4
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Sat Nov 19 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.0-3
- Use {?_smp_mflags}.
- Replace wrong BSD license with a copy of the GPL (#173105).

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.0-2
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.0-1.fc4.cw
- Update to 0.3.0.
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.0-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.0-1.fc3.cw
- Initial RPM release.
