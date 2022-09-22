Summary:        Application matching framework
Name:           bamf
Version:        0.5.5
Release:        4%{?dist}
# Library bits are LGPLv2 or LGPLv3 (but not open-ended LGPLv2+);
# non-lib bits are GPLv3.
# pbrobinson points out that three files in the lib are actually
# marked GPL in headers, making library GPL, though we think this
# may not be upstream's intention. For now, marking library as
# GPL.
# License:      LGPLv2 or LGPLv3
License:        GPLv2 or GPLv3
URL:            https://launchpad.net/bamf
Source0:        http://launchpad.net/bamf/0.5/%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires:  vala
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  systemd-rpm-macros
# for tests
BuildRequires:  dbus-daemon
BuildRequires:  xorg-x11-server-Xvfb

%description
BAMF removes the headache of applications matching into a simple DBus
daemon and C wrapper library. Currently features application matching
at amazing levels of accuracy (covering nearly every corner case).

%package        devel
Summary:        Development files for %{name}
License:        GPLv2 or GPLv3
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        daemon
Summary:        Application matching framework
License:        GPLv3
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description    daemon
BAMF removes the headache of applications matching into a simple DBus
daemon and C wrapper library. Currently features application matching
at amazing levels of accuracy (covering nearly every corner case). This
package contains the bamf daemon and supporting data.


%prep
%autosetup -p1
NOCONFIGURE=1 ./autogen.sh


%build
%configure --disable-static --disable-webapps --enable-gtk-doc
%make_build


%install
%make_install

find %{buildroot} -regex ".*\.la$" | xargs rm -f --


%check
# tests currently do not 100% pass and are non-blocking
dbus-run-session xvfb-run make check


%ldconfig_scriptlets

%post daemon
%systemd_user_post %{name}daemon.service

%preun daemon
%systemd_user_preun %{name}daemon.service


%files
%license COPYING.LGPL COPYING
%{_libdir}/libbamf3.so.*
%{_libdir}/girepository-1.0/Bamf*.typelib

%files devel
%doc ChangeLog TODO
%{_includedir}/libbamf3
%{_libdir}/libbamf3.so
%{_libdir}/pkgconfig/libbamf3.pc
%{_datadir}/gtk-doc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Bamf*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libbamf3.vapi

%files daemon
%doc COPYING
%{_libexecdir}/bamf
%{_datadir}/dbus-1/services/*.service
%{_userunitdir}/bamfdaemon.service
%exclude %{_datadir}/upstart/sessions/bamfdaemon.conf

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5
- Enable tests
- Fix preun scriptlet, it should be part of the daemon subpackage

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-3
- Build with Python 3 instead of Python 2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun  2 2019 Michel Alexandre Salim <michel@lumiere.local> - 0.5.4-1.1
- Fix incorrect obsoletes

* Sun Jun  2 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.5.3-9
- Update BRs for vala packaging changes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.3-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 0.5.3-2
- Rebuilt for libgtop2 soname bump

* Tue Feb 21 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.3-1
- Update to 0.5.3
- Package systemd user unit
- Move Bamf-3.typelib back to main package

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 19 2016 Adam Miller <maxamillion@fedoraproject.org> - 0.5.1-1
- Update to latest upstream (BZ#1017540)
- Remove patches that were merged upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.5.0-4
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 Kalev Lember <kalevlember@gmail.com> - 0.5.0-2
- Rebuilt for libgtop2 soname bump

* Fri Feb 14 2014 Michel Salim <salimma@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Michel Salim <salimma@fedoraproject.org> - 0.3.6-3
- Spec clean-ups

* Thu Apr 25 2013 Tom Callaway <spot@fedoraproject.org> - 0.3.6-2
- fix build

* Sat Apr 20 2013 Michel Salim <salimma@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.104-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Adam Williamson <awilliam@redhat.com> - 0.2.104-1
- new version, adjust for various upstream fixes
- rebuild against new libpng
- build both gtk+2 and gtk+3 libs, and package separately (like Ubuntu)

* Wed May 25 2011 Adam Williamson <awilliam@redhat.com> - 0.2.90-2
- don't depend on gtk-doc but own /usr/share/gtk-doc instead (#707545)

* Wed May 11 2011 Adam Williamson <awilliam@redhat.com> - 0.2.90-1
- new release 0.2.90

* Wed Mar 23 2011 Adam Williamson <awilliam@redhat.com> - 0.2.80-1
- new release 0.2.80

* Mon Mar 07 2011 Adam Williamson <awilliam@redhat.com> - 0.2.78-1
- new release 0.2.78

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Adam Williamson <awilliam@redhat.com> - 0.2.74-1
- new release 0.2.74
- update license of library (thanks pbrobinson)
- fix build by disabling a strict warning which seems to have showed
  up in gcc-4.6.0-0.3
- gir and vala devel files aren't getting installed any more

* Fri Dec 03 2010 Adam Williamson <awilliam@redhat.com> - 0.2.64-1
- initial package
