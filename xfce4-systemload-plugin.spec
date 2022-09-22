# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173668

%global minorversion 1.3
%global xfceversion 4.16

Name:           xfce4-systemload-plugin
Version:        1.3.1
Release:        4%{?dist}
Summary:        Systemload monitor for the Xfce panel

License:        BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-systemload-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  upower-devel
BuildRequires:  gettext
BuildRequires:  intltool

Requires:       xfce4-panel >= %{xfceversion}

%description
A system-load monitor plugin for the Xfce panel. It displays the current CPU 
load, the memory in use, the swap space and the system uptime.


%prep
%setup -q


%build
%configure --disable-static
%make_build


%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# FIXME: make sure debuginfo is generated properly (#795107)
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.systemload.*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Thu Mar 11 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 09 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sat Nov 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.0-1
- Update to 1.2.0
- [gtk3] Bump dependencies to check for libxfce4ui-2/libxfce4panel-2.0
- Spec clean-up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.1.2-2
- Rebuild for Xfce 4.12

* Fri Nov 21 2014 Kevin Fenzi <kevin@scrye.com> 1.1.2-1
- Update to 1.1.2. Fixes bugs #1165421 and #1166890

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 1.1.1-8
- Rebuilt for upower 0.99.1 soname bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 30 2013 Kevin Fenzi <kevin@scrye.com> 1.1.1-5
- Rebuild for new upower

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1
- Enably power-saving interval option through upower

* Tue Apr 24 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.1.0-2
- Fix -debuginfo.

* Sat Apr 21 2012 Kevin Fenzi <kevin@scrye.com> - 1.1.0-1
- Update to 1.1.0

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-6
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-5
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-3
- Rebuild for new libpng

* Fri Dec 10 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-2
- Rebuild for xfce4-panel 4.7

* Fri Dec 10 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Wed Sep 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-8
- Bring back tooltips in GTK >= 2.16 (#508637, bugzilla.xfce.org #5175)
- Fix bar colors (#505214, bugzilla.xfce.org #1889)
- Fix wrong free memory value (bugzilla.xfce.org #4215)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-5
- Rebuild for Xfce 4.6 (Beta 3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.2-4
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-3
- Rebuild for BuildID feature

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-2
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2 on Xfce 4.4.

* Fri Dec 22 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1.

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser).

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.6-7
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.6-6
- Require xfce4-panel.

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.6-5
- Rebuild for Fedora Extras 5.

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.6-4
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.6-3
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.6-2.fc4.cw
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.6-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.6-1.fc3.cw
- Updated to version 0.3.6.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.4-1.fc3.cw
- Initial RPM release.
