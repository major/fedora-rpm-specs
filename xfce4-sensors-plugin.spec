# Review at https://bugzilla.redhat.com/show_bug.cgi?id=173552
%global minor_version 1.4
%global xfceversion 4.16

Name:           xfce4-sensors-plugin
Version:        1.4.3
Release:        5%{?dist}
Summary:        Sensors plugin for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  lm_sensors-devel >= 2.8
BuildRequires:  hddtemp
BuildRequires:  libnotify-devel >= 0.4
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libtool

Requires:       xfce4-panel >= %{xfceversion}
Requires:       lm_sensors >= 2.8
Requires:       hddtemp
# lm_sensors is not available on s390 and s390x
ExcludeArch:    s390 s390x

%description
This plugin displays various hardware sensor values in the Xfce panel.

%package devel
Summary:        Development files for xfce4-sensors-plugin
Requires:       %{name} = %{version}-%{release}
Requires:       libxfce4util-devel

%description devel
Static libraries and header files for the xfce4-sensors-plugin.


%prep
%autosetup -p1
sed -i 's/libxfce4ui-1/libxfce4ui-2/g' lib/libxfce4sensors-1.0.pc.in


%build
%configure --disable-static \
        --enable-sysfsacpi=yes \
        --with-pathhddtemp=%{_bindir}/hddtemp
%make_build


%install
%make_install

%find_lang %{name}

find %{buildroot} -name '*.la' -exec rm -f {} ';'

desktop-file-install --vendor "" \
        --add-category "System" \
        --remove-category "Utility" \
        --dir %{buildroot}%{_datadir}/applications \
        --delete-original \
        %{buildroot}%{_datadir}/applications/xfce4-sensors.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO
%{_bindir}/xfce4-sensors
%dir %{_libdir}/xfce4/modules/
%{_libdir}/xfce4/modules/libxfce4sensors.so.*
%{_libdir}/xfce4/panel/plugins/libxfce4-sensors-plugin.so
%{_datadir}/applications/xfce4-sensors.desktop
%{_datadir}/icons/hicolor/*/apps/xfce-sensors.png
%{_datadir}/icons/hicolor/scalable/apps/xfce-sensors.svg
%{_datadir}/xfce4/panel/plugins/xfce4-sensors-plugin.*
%{_mandir}/man1/xfce4-sensors.1.gz

%files devel
%{_libdir}/pkgconfig/libxfce4sensors-1.0.pc
%{_libdir}/xfce4/modules/libxfce4sensors.so


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.3-4
- Fix requires for -devel (RHBZ# 2094743,2094764,2094776)

* Wed Feb 02 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Mon Jul 26 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.95-1
- Update to 1.3.95

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.92-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.3.92-4
- Fix FTBFS #1800268

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.92-1
- Update to 1.3.92

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 05 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Sat Feb 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.98-5
- Fix rawhide build + spec cleanup/modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.98-1
- Update to 1.2.98
- Drop conditional for xfceversion

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 12 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.6-1
- Update to 1.2.6
- [gtk3] Bump dependencies to check for libxfce4ui-2/libxfce4panel-2.0
- Spec clean-up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.2.5-2
- Rebuild for Xfce 4.12

* Sun Nov 30 2014 Kevin Fenzi <kevin@scrye.com> 1.2.5-1
- Update to 1.2.5. Fixes bug #1164400

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.2.3-5
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.2.3-4
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2.3-2
- Rebuild for new libpng

* Sun Jul 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3
- Remove all patches, they have been upstreamed

* Sun Jul 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-4
- Fix FTBFS. Thanks to Johannes Lips for the patch (#715838)
- Improve ACPI support. Thanks to Raphael Groner for the patches (#661933)

* Fri Jan 14 2011 Adam Williamson <awilliam@redhat.com> - 1.0.0-3
- fix some underlinking against xfcegui and xfcepanel (fixes build)

* Sat Nov 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-2
- Fix for libnotify 0.7.0

* Fri Jun 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Add patch by Robert Scheck to fix DSO linking (#564840)
- Update gtk-icon-cache scriptlets

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.99.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.99.6-4
- Own %%{_libdir}/xfce4/modules/ to fix unowned directory (#474587)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.99.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.99.6-2
- Rebuild for Xfce 4.6 (Beta 3)

* Thu Nov 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.99.6-1
- Update to 0.10.99.6
- Remove obsolete lm_sensors patch
- BuildRequire hddtemp and make sure it's path is detected correctly
- Update gtk-update-icon-cache scriptlets

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.10.99.2-4
- Autorebuild for GCC 4.3

* Fri Dec 07 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.99.2-3
- Rebuild for Xfce 4.4.2

* Mon Nov 19 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.99.2-2
- Add Hans de Goede's patch for lm_sensors-3.0.0-RC1

* Wed Nov 07 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.99.2-1
- Update to 0.10.99.2

* Sat Oct 27 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.99.1-1
- Update to 0.10.99.1
- Require hddtemp because it is supported now

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.0-6
- Rebuild for BuildID feature
- Update license tag

* Fri Jul 20 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.0-5
- Build for ppc(64) as lm_sensors is available on these architectures now.

* Thu May 17 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.0-4
- ExcludeArch ppc64

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.0-3
- Rebuild for Xfce 4.4.1

* Sun Jan 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.0-2
- Rebuild for XFCE 4.4.
- Update gtk-icon-cache scriptlets.

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.0-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser).

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.0-6
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.7.0-5
- Require xfce4-panel.

* Sat Feb 18 2006 Christoph Wickert <fedora wickert at arcor de> - 0.7.0-4
- Rebuild for Fedora Extras 5.

* Sun Jan 22 2006 Christoph Wickert <fedora wickert at arcor de> - 0.7.0-3
- ExcludeArch ppc.

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 0.7.0-2
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.7.0-1
- Initial Fedora Extras version.
- Update to 0.7.0.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.6.2-1.fc4.cw
- Update to 0.6.2.
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.0-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.0-1.fc3.cw
- Initial RPM release.
