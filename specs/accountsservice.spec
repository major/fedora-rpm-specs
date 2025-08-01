Name:           accountsservice
Version:        23.13.9
Release:        9%{?dist}
Summary:        D-Bus interfaces for querying and manipulating user account information
License:        GPL-3.0-or-later
URL:            https://www.freedesktop.org/wiki/Software/AccountsService/

#VCS: git:git://gitlab.freedesktop.org/accountsservice/accountsservice
Source0:        https://www.freedesktop.org/software/accountsservice/accountsservice-%{version}.tar.xz

BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  glib2-devel
BuildRequires:  polkit-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  python3-dbusmock
BuildRequires:  libxcrypt-devel

Requires:       polkit
Requires:       shadow-utils
%{?systemd_requires}

# https://bugzilla.redhat.com/show_bug.cgi?id=2185850
Patch10001:     0001-mocklibc-Fix-compiler-warning.patch
Patch10002:     0002-user-manager-Fix-another-compiler-warning.patch
Patch10003:     0003-act-user-Use-the-reentrant-interfaces-of-crypt-_gens.patch

%description
The accountsservice project provides a set of D-Bus interfaces for
querying and manipulating user account information and an implementation
of these interfaces, based on the useradd, usermod and userdel commands.

%package libs
Summary: Client-side library to talk to accountsservice
Requires: %{name}%{?_isa} = %{version}-%{release}

%description libs
The accountsservice-libs package contains a library that can
be used by applications that want to interact with the accountsservice
daemon.

%package devel
Summary: Development files for accountsservice-libs
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The accountsservice-devel package contains headers and other
files needed to build applications that use accountsservice-libs.


%prep
%autosetup -S git

%build
%meson \
 -Dgtk_doc=true \
 -Dadmin_group=wheel
%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/accountsservice/interfaces/

%find_lang accounts-service

%ldconfig_scriptlets libs

%post
%systemd_post accounts-daemon.service

%preun
%systemd_preun accounts-daemon.service

%postun
%systemd_postun accounts-daemon.service

%files -f accounts-service.lang
%license COPYING
%doc README.md AUTHORS
%{_libexecdir}/accounts-daemon
%dir %{_datadir}/accountsservice/
%dir %{_datadir}/accountsservice/interfaces/
%{_datadir}/accountsservice/user-templates/
%{_datadir}/dbus-1/interfaces/org.freedesktop.Accounts.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Accounts.User.xml
%{_datadir}/dbus-1/system.d/org.freedesktop.Accounts.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.Accounts.service
%{_datadir}/polkit-1/actions/org.freedesktop.accounts.policy
%dir %{_localstatedir}/lib/AccountsService/
%dir %{_localstatedir}/lib/AccountsService/users/
%dir %{_localstatedir}/lib/AccountsService/icons/
%{_unitdir}/accounts-daemon.service

%files libs
%{_libdir}/libaccountsservice.so.*
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/AccountsService-1.0.typelib

%files devel
%{_includedir}/accountsservice-1.0
%{_libdir}/libaccountsservice.so
%{_libdir}/pkgconfig/accountsservice.pc
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/AccountsService-1.0.gir
%dir %{_datadir}/gtk-doc/html/libaccountsservice
%{_datadir}/gtk-doc/html/libaccountsservice/*
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/accountsservice.*

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.13.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 23.13.9-8
- Add patch to use the reentrant interfaces of libxcrypt

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 23.13.9-7
- Add explicit BR: libxcrypt-devel

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.13.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.13.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.13.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.13.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.13.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 11 2023 Ray Strode <rstrode@redhat.com> - 23.13.9-1
- Update to 23.13.9
- Fix C99 compile error
  Resolves: #2185850

* Fri Mar 24 2023 Ray Strode <rstrode@redhat.com> - 23.11.69-2
- Fix delay during boot for some users
  Resolves: #2180768

* Wed Mar 15 2023 Ray Strode <rstrode@redhat.com> - 23.11.69-1
- Update to 23.11.69

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.08.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 26 2022 Kalev Lember <klember@redhat.com> - 22.08.8-2
- Rebuild

* Sat Aug 27 2022 Leigh Scott <leigh123linux@gmail.com> - 22.08.8-1
- Update to 22.08.8

* Tue Jul 26 2022 Tomas Popela <tpopela@redhat.com> - 0.6.55-11
- Fix the build with meson 0.60+

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.55-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.55-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.55-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Björn Esser <besser82@fedoraproject.org> - 0.6.55-7
+ accountsservice-0.6.55-7
- Add patch to use yescrypt for new user passwords, fixes rhbz#1976334

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.55-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Bastien Nocera <bnocera@redhat.com> - 0.6.55-5
+ accountsservice-0.6.55-5
- Own /usr/share/accountsservice

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.55-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Benjamin Berg <bberg@redhat.com> - 0.6.55-1
- Update to 0.6.55
  Resolves: #1755838

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Alexandru-Sever Horin <alex.sever.h@gmail.com> - 0.6.54-4
- Add patch from upstream to fix UID detection
  Resolves: #1646418

* Thu Jan 17 2019 Adam Williamson <awilliam@redhat.com> - 0.6.54-3
- Explicitly enable systemd support (#1576903) (Elliott Sales de Andrade)

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.6.54-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Sep 29 2018 Ray Strode <rstrode@redhat.com> - 0.6.54-1
- Update to 0.6.54

* Thu Sep 27 2018 Ray Strode <rstrode@redhat.com> - 0.6.53-1
- Update to 0.6.53

* Mon Sep 24 2018 Adam Williamson <awilliam@redhat.com> - 0.6.50-1
- Update to 0.6.50, plus a couple of backported patches
  Resolves: #1576903

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Ray Strode <rstrode@redhat.com> - 0.6.49-1
- Update to 0.6.49 (brown bag release)

* Thu May 10 2018 Ray Strode <rstrode@redhat.com> - 0.6.48-1
- Update to 0.6.48
  Resolves: #1575780

* Fri May 04 2018 Ray Strode <rstrode@redhat.com> - 0.6.47-2
- fix crash on user deletion
  Resolves: #1573550

* Tue Apr 24 2018 Ray Strode <rstrode@redhat.com> - 0.6.47-1
- Update to 0.6.47

* Sat Apr 21 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.46-1
- Update to 0.6.46
- Spec cleanup, use %%license

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.42-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.42-8
- Switch to %%ldconfig_scriptlets

* Thu Jan 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.42-7
- Fix systemd executions/requirements

* Wed Jan 24 2018 Ray Strode <rstrode@redhat.com> - 0.6.42-6
- Fix crash introduced by glibc/libxcrypt change
  https://fedoraproject.org/wiki/Changes/Replace_glibc_libcrypt_with_libxcrypt
  Resolves: #1538181

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.6.42-5
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 09 2016 Ray Strode <rstrode@redhat.com> - 0.6.42-1
- Update to 0.6.42
- Fixes systemd incompatibility

* Tue May 31 2016 Ray Strode <rstrode@redhat.com> - 0.6.40-4
- Don't create /root/.cache at startup
  Resolves: #1331926

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Ray Strode <rstrode@redhat.com> 0.6.40-1
- Update to 0.6.40

* Fri Oct 17 2014 Ray Strode <rstrode@redhat.com> 0.6.39-2
- More ListCachedUsers race fixes (this time with SSSD)
  Related: #1147504

* Thu Oct 16 2014 Ray Strode <rstrode@redhat.com> 0.6.39-1
- Update to 0.6.39
- Fixes ListCachedUsers race at startup

* Thu Sep 18 2014 Stef Walter <stefw@redhat.com> - 0.6.38-1
- Update to 0.6.38
- Fixes polkit policy rhbz#1094138
- Remove dbus-glib-devel dependency, accountsservice uses gdbus now

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.37-2
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.37-1
- Update to 0.6.37, drop upstreamed patches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Matthias Clasen <mclasen@redhat.com> - 0.6.35-4
- Consistently call userdel with -f

* Wed Nov 20 2013 Ray Strode <rstrode@redhat.com> 0.6.35-3
- Only treat users < 1000 as system users
- only use user heuristics on the range 500-1000

* Mon Nov 11 2013 Ray Strode <rstrode@redhat.com> 0.6.35-2
- pass --enable-user-heuristics which fedora needs so users
  with UIDs less than 1000 show up in the user list.

* Mon Oct 28 2013 Ray Strode <rstrode@redhat.com> 0.6.35-1
- Update to 0.6.35
  Related: #1013721

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Ray Strode <rstrode@redhat.com> 0.6.34-1
- Update to 0.6.34

* Tue Jun 11 2013 Matthias Clasen <mclasen@redhat.com> - 0.6.33-1
- Update to 0.6.33

* Tue May 14 2013 Matthias Clasen <mclasen@redhat.com> - 0.6.32-1
- Update to 0.6.32

* Thu Apr 18 2013 Matthias Clasen <mclasen@redhat.com> - 0.6.31-2
- Hardened build

* Tue Apr 16 2013 Matthias Clasen <mclasen@redhat.com> - 0.6.31-1
- Update to 0.6.31

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Richard Hughes <rhughes@redhat.com> - 0.6.30-1
- Update to 0.6.30

* Fri Nov 16 2012 Matthias Clasen <mclasen@redhat.com> - 0.6.26-1
- Update to 0.6.26

* Tue Oct  2 2012 Matthias Clasen <mclasen@redhat.com> - 0.6.25-2
- Update to 0.6.25
- Use systemd scriptlets (#856649)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.6.22-2
- Add ldconfig scriptlets to -libs.

* Thu Jun 28 2012 Ray Strode <rstrode@redhat.com> 0.6.22-1
- Update to 0.6.22.
- Fixes CVE-2012-2737 - local file disclosure
  Related:  #832532

* Thu May 30 2012 Matthias Clasen <mclasen@redhatcom> 0.6.21-1
- Update to 0.6.21

* Fri May 04 2012 Ray Strode <rstrode@redhat.com> 0.6.20-1
- Update to 0.6.20. Should fix user list.
  Related: #814690

* Thu May 03 2012 Ray Strode <rstrode@redhat.com> 0.6.19-1
- Update to 0.6.19
  Allows user deletion of logged in users
  Related: #814690

* Wed Apr 11 2012 Matthias Clasen <mclsaen@redhat.com> - 0.6.18-1
- Update to 0.6.18

* Tue Mar 27 2012 Ray Strode <rstrode@redhat.com> 0.6.17-1
- Update to latest release

* Sun Mar  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.15-4
- Fix unitdir with usrmove

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Matthias Clasen <mclasen@redhat.com> 0.6.15-2
- Make resetting user icons work
- Update to 0.6.15
- Fixes session chooser at login screen when logged into vt

* Wed Sep 21 2011 Ray Strode <rstrode@redhat.com> 0.6.14-2
- Fix wtmp loading so users coming from the network are
  remembered in the user list in subsequent boots

* Wed Sep 21 2011 Ray Strode <rstrode@redhat.com> 0.6.14-1
- Update to 0.6.14

* Sun Sep  4 2011 Matthias Clasen <mclasen@redhat.com> - 0.6.13-3
- Fix fast user switching

* Mon Aug 15 2011 Kalev Lember <kalevlember@gmail.com> - 0.6.13-2
- Rebuilt for rpm bug #728707

* Tue Jul 19 2011 Matthias Clasen <mclasen@redhat.com> - 0.6.13-1
- Update to 0.6.13
- Drop ConsoleKit dependency

* Mon Jun 06 2011 Ray Strode <rstrode@redhat.com> 0.6.12-1
- Update to latest release

* Wed May 18 2011 Matthias Clasen <mclasen@redhat.com> 0.6.11-1
- Update to 0.6.11

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Ray Strode <rstrode@redhat.com> 0.6.3-1
- Update to 0.6.3

* Thu Jan 27 2011 Matthias Clasen <mclasen@redhat.com> 0.6.2-1
- Update to 0.6.2

* Wed Jul 21 2010 Matthias Clasen <mclasen@redhat.com> 0.6.1-1
- Update to 0.6.1
- Install systemd unit file

* Mon Apr  5 2010 Matthias Clasen <mclasen@redhat.com> 0.6-2
- Always emit changed signal on icon change

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> 0.6-1
- Update to 0.6

* Mon Mar 22 2010 Matthias Clasen <mclasen@redhat.com> 0.5-1
- Update to 0.5

* Mon Feb 22 2010 Bastien Nocera <bnocera@redhat.com> 0.4-3
- Fix directory ownership

* Mon Feb 22 2010 Bastien Nocera <bnocera@redhat.com> 0.4-2
- Add missing directories to the filelist

* Fri Jan 29 2010 Matthias Clasen <mclasen@redhat.com> 0.4-1
- Initial packaging, based on work by Richard Hughes
