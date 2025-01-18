%if 0%{?fedora} < 36 && 0%{?rhel} < 10
%bcond_with gtk4
%else
%bcond_without gtk4
%endif

Summary:   NetworkManager VPN plugin for PPTP
Name:      NetworkManager-pptp
Epoch:     1
Version:   1.2.12
Release:   9%{?dist}
License:   GPL-2.0-or-later
URL:       http://www.gnome.org/projects/NetworkManager/

Source0:   https://download.gnome.org/sources/NetworkManager-pptp/1.2/%{name}-%{version}.tar.xz
#Patch1: 0001-example.patch

%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo bad)

BuildRequires: make
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1:1.2.0
BuildRequires: libnma-devel >= 1.2.0
BuildRequires: pkgconfig
BuildRequires: ppp-devel >= 2.5.0
BuildRequires: libtool intltool gettext
BuildRequires: libsecret-devel
%if %with gtk4
BuildRequires: libnma-gtk4-devel
%endif

Requires: dbus-common
Requires: NetworkManager >= 1:1.2.0
Requires: pptp
Requires: ppp = %{ppp_version}


%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating VPN capabilities with
the PPTP server with NetworkManager.


%package -n NetworkManager-pptp-gnome
Summary: NetworkManager VPN plugin for PPTP - GNOME files

Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: NetworkManager-pptp < 1:0.9.8.2-3

%description -n NetworkManager-pptp-gnome
This package contains software for integrating VPN capabilities with
the PPTP server with NetworkManager (GNOME files).


%prep
%autosetup -p1


%build
%configure \
	--disable-static \
%if %with gtk4
	--with-gtk4 \
%endif
	--enable-more-warnings=yes \
	--with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version} \
	--with-dist-version=%{version}-%{release}
make %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la
rm -f %{buildroot}%{_libdir}/pppd/%{ppp_version}/*.la

%find_lang %{name}


%files -f %{name}.lang
%{_libdir}/NetworkManager/libnm-vpn-plugin-pptp.so
%{_datadir}/dbus-1/system.d/nm-pptp-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-pptp-service.name
%{_libexecdir}/nm-pptp-service
%{_libdir}/pppd/%{ppp_version}/nm-pptp-pppd-plugin.so
%doc AUTHORS README NEWS
%license COPYING

%files -n NetworkManager-pptp-gnome
%{_libexecdir}/nm-pptp-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-pptp-editor.so
%{_metainfodir}/network-manager-pptp.metainfo.xml

%if %with gtk4
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-pptp-editor.so
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Adam Williamson <awilliam@redhat.com> - 1.2.12-8
- Rebuild for ppp 2.5.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 03 2023 Íñigo Huguet <ihuguet@redhat.com> - 1.2.12-4
- Migrated to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Adam Williamson <awilliam@redhat.com> - 1.2.12-2
- Rebuild for new ppp

* Thu Mar 09 2023 Lubomir Rintel <lkundrak@v3.sk> - 1.2.12-1
- Update to 1.2.12 release

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Lubomir Rintel <lkundrak@v3.sk> - 1.2.10-1
- Update to 1.2.10 release

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.8-3
- Move dbus service file into /usr/share/dbus-1

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.8-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.8-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 25 2020 Thomas Haller <thaller@redhat.com> - 1:1.2.8-2
* Rebuild for ppp 2.4.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.8-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.8-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.8-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct  4 2018 Thomas Haller <thaller@redhat.com> - 1.2.8-1
- Update to 1.2.8 release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Thomas Haller <thaller@redhat.com> - 1.2.6-1
- Update to 1.2.6 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.4-5
- Drop libnm-glib for Fedora 28

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct  3 2016 Thomas Haller <thaller@redhat.com> - 1.2.4-1
- Update to 1.2.4 release

* Mon Sep 12 2016 Thomas Haller <thaller@redhat.com> - 1.2.4-0.1
- Update to 1.2.4 pre-release
- Remove GTK dependency from base openvpn package (rh#1088677)
- Introduce new GTK-free VPN plugin base-library to nm-pptp package
- Don't require nm-connection-editor anymore
- Support NM_VPN_LOG_LEVEL environment variable to control logging

* Wed May 11 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.2-1
- Update to 1.2.2 release

* Wed Apr 20 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-1
- Update to 1.2.0 release

* Thu Apr 14 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.0-0.4.rc1
- Fix a crash

* Tue Apr  5 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.0-0.3.rc1
- Update to NetworkManager-pptp 1.2-rc1

* Tue Mar 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.0-0.3.beta3
- Update to NetworkManager-pptp 1.2-beta3

* Tue Mar  1 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.0-0.3.beta2
- Update to NetworkManager-pptp 1.2-beta2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.0-0.2.beta1
- Update to NetworkManager-pptp 1.2-beta1

* Wed Dec 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.0-0.1.20151223gitde50986
- Update the git snapshot

* Tue Oct 27 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.0-0.1.20151027gita2e7ffa
- Update the git snapshot
- Fix the el7 build

* Thu Sep 3 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:1.2.0-0.1.20150901git345c34e
- Update to 1.2 git snapshot with libnm-based properties plugin

* Thu Sep 3 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:1.1.0-3.20150428git695d4f2
- Avoid requiring NetworkManager-gnome

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.0-2.20150428git695d4f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Jiří Klimeš <jklimes@redhat.com> - 1:1.1.0-1.20150428git695d4f2
- Update to a git snapshot (git sha 695d4f2)
- all: add "unit" option for pppd to define ppp<n> name (bgo #736485)
- service: try to load nf_conntrack_pptp kernel module (rh #1214643)
- updated translations

* Mon Dec 22 2014 Dan Williams <dcbw@redhat.com> - 1:1.0.0-1
- Update to 1.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Jiří Klimeš <jklimes@redhat.com> - 1:0.9.8.2-4
- Rebuild against pppd 2.4.6

* Fri Jul 26 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.9.8.2-3
- Fixing Obsoletes to ensure NetworkManager-pptp-gnome installs on update (rh #986368)

* Thu Jul 11 2013 Stef Walter <stefw@gnome.org> - 1:0.9.8.2-2
- Depend on libgnome-keyring (the client library), not gnome-keyring (daemon) (rh #811930)

* Thu Jul 11 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.9.8.2-1
- Update to 0.9.8.2 release

* Sun Apr 07 2013 Dan Fruehauf <malkodan@gmail.com> - 1:0.9.8.0-1
- Refactored spec file

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.3.997-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.3.997-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 1:0.9.3.997-2
- Remove unnecessary ldconfig calls from scriptlets (#737333).

* Mon Mar 19 2012 Dan Williams <dcbw@redhat.com> - 1:0.9.3.997-1
- Update to 0.9.3.997 (0.9.4-rc1)

* Fri Mar  2 2012 Dan Williams <dcbw@redhat.com> - 1:0.9.3.995-1
- Update to 0.9.3.995 (0.9.4-beta1)
- ui: add support for external UI mode, eg GNOME Shell
- ui: tooltips now refer to pppd/pptp config options

* Thu Mar  1 2012 Bill Nottingham <notting@redhat.com> - 1:0.9.0-5
- Remove obsolete and broken gtk2 requirement

* Sun Feb 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1:0.9.0-4
- Update for unannounced gnome-keyring devel changes

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Adam Jackson <ajax@redhat.com> 0.9.0-2
- Rebuild for new libpng
- Build with -Wno-error=deprecated-declarations for now

* Fri Aug 26 2011 Dan Williams <dcbw@redhat.com> - 1:0.9.0-1
- Update to 0.9.0 release
- ui: updated translations

* Thu Jul 21 2011 Dan Williams <dcbw@redhat.com> - 1:0.8.999-2.git20110721
- ui: ensure secrets are saved when required and not saved when not required

* Tue May 03 2011 Dan Williams <dcbw@redhat.com> - 1:0.8.999-1
- Update to 0.8.999 (0.9-rc2)
- ui: default to user-stored secrets for new connections
- ui: updated translations

* Tue Apr 05 2011 Dan Williams <dcbw@redhat.com> - 1:0.8.998-1
- Update to 0.8.998 (0.9.0-rc1)
- Fix issues with secrets flags and password saving/retrieval
- Fix issues with PPTP pools using the same DNS name for different servers

* Sat Mar 26 2011 Christopher Aillon <caillon@redhat.com> - 1:0.8.995-1
- Update to 0.8.995

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 Dan Williams <dcbw@redhat.com> - 1:0.8.1-1
- Update to 0.8.1 release
- MPPE auth method UI fixes
- Lower default pptp log level and add debugging capability

* Sun Apr 11 2010 Dan Williams <dcbw@redhat.com> - 1:0.8.0-1
- Fix saving of MPPE security levels
- Updated translations

* Mon Feb  1 2010 Dan Williams <dcbw@redhat.com> - 1:0.7.997-3.git20100120
- Really fix pppd plugin directory path

* Wed Jan 20 2010 Dan Williams <dcbw@redhat.com> - 1:0.7.997-2.git20100120
- Rebuild for new pppd

* Mon Dec 14 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.997-1
- Add debugging helpers
- Fix saving MPPE-related settings from the properties dialog
- Resolve PPTP gateway hostname if necessary

* Mon Oct  5 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.996-4.git20090921
- Rebuild for updated NetworkManager

* Mon Sep 21 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.996-2
- Rebuild for updated NetworkManager

* Fri Aug 28 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.996-1
- Rebuild for updated NetworkManager
- Fix window title of Advanced dialog

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Dan Williams <dcbw@redhat.com> 1:0.7.0.99-1
- Update to 0.7.1rc3

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Dan Williams <dcbw@redhat.com> 1:0.7.0.97-1
- Update to 0.7.1rc1
- Set a reasonable MTU
- Ensure 'noauth' is used
- Fix domain-based logins
- Fix saving MPPE values in connection editor

* Sat Jan  3 2009 Dan Williams <dcbw@redhat.com> 1:0.7.0-1.svn16
- Rebuild for updated NetworkManager
- Fix some specfile issues (rh #477153)
- Allow the EAP authentication method

* Fri Nov 21 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-12.svn4326
- Rebuild for updated NetworkManager

* Wed Oct 29 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-12.svn4229
- Fix hang in auth dialog (rh #467007)

* Mon Oct 27 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-11.svn4229
- Rebuild for updated NetworkManager
- Ensure that certain PPP options are always overriden

* Sun Oct 12 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-11.svn4178
- Rebuild for updated NetworkManager
- Allow changing passwords from the connection editor

* Sun Oct 05 2008 Lubomir Rintel <lkundrak@v3.sk> 1:0.7.0-11.svn4027
- Add pptp dependency (#465644)

* Fri Aug 29 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-10.svn4027
- Resurrect from the dead

* Mon Apr 21 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.6.4-2
- Take Dan Horak's review into account (#443807):
- Do not install versioned .so-s for properties module
- Do not do useless ldconfigs
- Remove leftover dependencies

* Mon Apr 21 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.6.4-1
- Branch this for EPEL, go back to:
- 0.6.4
- NetworkManager-pptp from NetworkManager-ppp_vpn
- Install pppd plugin correctly

* Wed Nov 21 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.7.0-0.3.svn3549
- Update against trunk

* Wed Nov 21 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.7.0-0.2.svn3085
- Do not exclude .so for NM, and properly generate the .name file

* Thu Nov 15 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.7.0-0.1.svn3085
- Initial packaging attempt, inspired by NetworkManager-openvpn
- Nearly completly rewritten spec, all bugs in it are solely my responsibility
