# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173544

%global _hardened_build 1
%global minor_version 4.1
%global xfceversion 4.16

Name:           xfce4-genmon-plugin
Version:        4.1.1
Release:        6%{?dist}
Summary:        Generic monitor plugin for the Xfce panel

License:        LGPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-genmon-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  intltool
BuildRequires:  gettext
Requires:       xfce4-panel >= %{xfceversion}

%description
The GenMon plugin cyclically spawns the indicated script/program,
captures its output and displays it as a string into the panel.


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
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/icons/hicolor/*/apps/org.xfce.genmon.*g
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Filipe Rosset <rosset.filipe@gmail.com> - 4.1.1-1
- Update to 4.1.1

* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.0.1-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.1-3
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 25 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.0.0-2
- spec file cleanup

* Sat Feb 25 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.0.0-1
- GTK3 update
- Bugfixes

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 3.4.0-7
- Rebuild for Xfce 4.12
:
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 12 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0
- Remove upstreamed initialize-timer patch
- Remove icon hack as utilities-system-monitor is a valid XDG named icon

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 3.3.0-7
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 3.3.0-6
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.3.0-4
- Rebuild for new libpng

* Mon Jun 13 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.3.0-3
- Make sure the plugin is shown after adding it to the panel (#695025)

* Sat Apr 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.3.0-2
- Fix icon in 'Add new panel item' dialog (#694902)

* Fri Mar 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0
- Fix Source0 URL
- Remove upstreamed patches

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Adam Williamson <awilliam@redhat.com> - 3.2-6
- fix a couple of underlinking issues (underlink.patch)

* Sat Dec 11 2010 Christoph Wickert <cwickert@fedoraproject.org> - 3.2-5
- Fix zombie process (bugzilla.xfce.org #3896)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 3.2-2
- Rebuild for Xfce 4.6 (Beta 3)

* Wed Mar 19 2008 Christoph Wickert <cwickert@fedoraproject.org> - 3.2-1
- Update to 0.3.2.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1-4
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Christoph Wickert <cwickert@fedoraproject.org> - 3.1-3
- Rebuild for BuildID feature
- Update license tag

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 3.1-2
- Rebuild for Xfce 4.4.1

* Sat Feb 24 2007 Christoph Wickert <cwickert@fedoraproject.org> - 3.1-1
- Update to 0.3.1.
- Fix bugzilla.xfce.org #2435 and #2722, drop xfce4-dev-tools BR.

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 3.0-3
- Rebuild for XFCE 4.4.
- Patch to compile with -Wl,--as-needed (bugzilla.xfce.org #2722)

* Sat Nov 11 2006 Christoph Wickert <cwickert@fedoraproject.org> - 3.0-2
- Rebuild for XFCE 4.3.99.2.

* Tue Oct 31 2006 Christoph Wickert <cwickert@fedoraproject.org> - 3.0-1
- Update to 3.0.
- BR xfce4-dev-tools (bugzilla.xfce.org #2435) and gettext.

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 2.0-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 2.0-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser).

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 2.0-1
- Update to 2.0 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 1.1-7
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 1.1-6
- Require xfce4-panel.

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 1.1-5
- Rebuild for Fedora Extras 5.

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 1.1-4
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 1.1-3
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 1.1-2.fc4.cw
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 1.1-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 1.1-1.fc3.cw
- Initial RPM release.
