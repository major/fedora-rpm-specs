%global username shellinabox

Name:           shellinabox
Version:        2.20
Release:        25%{?dist}
Summary:        Web based AJAX terminal emulator
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/%{name}/%{name}

Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        shellinaboxd.sysconfig
Source2:        shellinaboxd.service
Source3:        shellinaboxd.init

Patch0:         %{name}-ssh-options.patch
Patch1:         %{name}-gcc11.patch
Patch2: shellinabox-configure-c99.patch

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

Requires:       openssl
Requires(pre):  shadow-utils

%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:      systemd
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
%endif

%if 0%{?rhel} == 6
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(postun):   /sbin/service
%endif

%description
Shell In A Box implements a web server that can export arbitrary command line
tools to a web based terminal emulator. This emulator is accessible to any
JavaScript and CSS enabled web browser and does not require any additional
browser plugins.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
autoreconf -vif
%configure --disable-runtime-loading
make %{?_smp_mflags}
chmod 644 %{name}/*

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

install -p -m 755 -D shellinaboxd %{buildroot}%{_sbindir}/shellinaboxd
install -p -m 644 -D shellinaboxd.1 %{buildroot}%{_mandir}/man1/shellinaboxd.1
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/shellinaboxd
install -p -m 644 shellinabox/white-on-black.css %{buildroot}%{_datadir}/%{name}
install -p -m 644 shellinabox/color.css %{buildroot}%{_datadir}/%{name}
install -p -m 644 shellinabox/monochrome.css %{buildroot}%{_datadir}/%{name}

%if 0%{?fedora} || 0%{?rhel} >= 7

# Systemd unit files
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_unitdir}/shellinaboxd.service

%else

# Initscripts
install -p -m 755 -D %{SOURCE3} %{buildroot}%{_initrddir}/shellinaboxd

%endif

%pre
getent group %username >/dev/null || groupadd -r %username &>/dev/null || :
getent passwd %username >/dev/null || useradd -r -s /sbin/nologin \
    -d %{_sharedstatedir}/shellinabox -M -c 'Shellinabox' -g %username %username &>/dev/null || :
exit 0

%if 0%{?fedora} || 0%{?rhel} >= 7

%post
%systemd_post shellinaboxd.service

%preun
%systemd_preun shellinaboxd.service

%postun
%systemd_postun_with_restart shellinaboxd.service

%endif

%if 0%{?rhel} == 6

%post
/sbin/chkconfig --add shellinaboxd

%preun
if [ "$1" = 0 ]; then
        /sbin/service shellinaboxd stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del shellinaboxd
fi

%postun
if [ "$1" -ge "1" ]; then
        /sbin/service shellinaboxd condrestart >/dev/null 2>&1 || :
fi

%endif

%files
%{!?_licensedir:%global license %%doc}
%doc AUTHORS NEWS README README.Fedora
%doc shellinabox/styles.css shellinabox/print-styles.css
%doc shellinabox/shell_in_a_box.js
%config(noreplace) %{_sysconfdir}/sysconfig/shellinaboxd
%{_mandir}/man1/shellinaboxd.1.*
%{_datadir}/%{name}
%{_sbindir}/shellinaboxd
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_unitdir}/shellinaboxd.service
%else
%{_initrddir}/shellinaboxd
%endif
%attr(750,%{username},%{username}) %{_sharedstatedir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.20-24
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Florian Weimer <fweimer@redhat.com> - 2.20-20
- Port configure script to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.20-16
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.20-14
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Jeff Law <law@redhat.com> - 2.20-12
- Initialize sigset in configure test

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Simone Caronni <negativo17@gmail.com> - 2.20-5
- Disable SSHv1 options.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Simone Caronni <negativo17@gmail.com> - 2.20-2
- Remove support for RHEL/CentOS 5.

* Thu Mar 09 2017 Simone Caronni <negativo17@gmail.com> - 2.20-1
- Update to 2.20.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Simone Caronni <negativo17@gmail.com> - 2.19-1
- Update to 2.19. Fixes CVE-2015-8400 (#1287577).

* Mon Aug 31 2015 Simone Caronni <negativo17@gmail.com> - 2.18-1
- Update to 2.18.
- Remove upstreamed patches.

* Mon Aug 31 2015 Simone Caronni <negativo17@gmail.com> - 2.17-3
- Backport patch from upstream:
  https://github.com/shellinabox/shellinabox/pull/340

* Wed Aug 26 2015 Simone Caronni <negativo17@gmail.com> - 2.17-2
- Add license macro.
- Install files manually, as this simplifies installation of docs in versioned
  documentation dirs (CentOS/RHEL).

* Wed Aug 26 2015 Simone Caronni <negativo17@gmail.com> - 2.17-1
- Update for new GitHub packaging guidelines.
- Update source from new repository.
- Use make install target now that the source has it.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-29.git88822c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-28.git88822c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Simone Caronni <negativo17@gmail.com> - 2.14-27.git88822c1
- Add additional ssh option ProxyCommand=none (#1013974).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-26.git88822c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Simone Caronni <negativo17@gmail.com> - 2.14-25.git88822c1
- Add systemd to BuildRequires; not default on Fedora 20+.
- Remove Fedora 17 conditionals, distribution EOL.
- Remove systemd-sysv dependency as per new packaging guidelines.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-25.git88822c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Simone Caronni <negativo17@gmail.com> - 2.14-24.git88822c1
- Fix SSL support (#973058).
- SPEC file cleanup.

* Sat May 11 2013 Simone Caronni <negativo17@gmail.com> - 2.14-22.git88822c1
- Kill daemon by pid on EPEL (#962069).
- Change restart policy in service files and fix service dependencies.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-21.git88822c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Simone Caronni <negativo17@gmail.com> - 2.14-20.git88822c1
- Added define for RHEL 5 (rhbz#894903).
- Updated spec to new packaging guidelines for github sources.

* Wed Jan 09 2013 Simone Caronni <negativo17@gmail.com> - 2.14-19.git88822c1f
- Fix SysV init scripts.

* Wed Jan 09 2013 Simone Caronni <negativo17@gmail.com> - 2.14-18.git88822c1f
- Updated init script according to Fedora template (#893129)
  https://fedoraproject.org/wiki/Packaging:SysVInitScript?rd=Packaging/SysVInitScript

* Fri Dec 14 2012 Simone Caronni <negativo17@gmail.com> - 2.14-17.git88822c1f
- Fix the commit / dist tags order in the revision.

* Fri Dec 14 2012 Simone Caronni <negativo17@gmail.com> - 2.14-16.git88822c1f
- Move source from the original unmantained content to the github fork.

* Wed Oct 17 2012 Simone Caronni <negativo17@gmail.com> - 2.14-15
- Fix fedpkg checks. Requires fedpkg > 1.10:
  http://git.fedorahosted.org/cgit/fedpkg.git/commit/?id=11c46c06a3c9cc2f58d68aea964dd37dc028e349
- Change systemd requirements as per new package guidelines.

* Mon Oct 01 2012 Simone Caronni <negativo17@gmail.com> - 2.14-14
- Move user directory and data under /var/lib.

* Wed Sep 26 2012 Joel Young <jdy@cryregarder.com> - 2.14-13
- Fix variable expansions in init script and service file.

* Tue Sep 25 2012 Simone Caronni <negativo17@gmail.com> - 2.14-12
- Really add WorkingDirectory to service files.
- Remove postun user deletion leftovers.
- Add static files to be customized (as referenced by the man page) in the doc directory.

* Mon Sep 24 2012 Simone Caronni <negativo17@gmail.com> - 2.14-11
- Fix RHEL 5 rpm macro.

* Thu Sep 13 2012 Simone Caronni <negativo17@gmail.com> - 2.14-10
- Fixes from (Joel Young <jdy@cryregarder.com>):
    Install supplied css files.
    Set menu item to turn off ssl as disabled by default.
    Do not remove user on uninstall.
- Simplified spec file.
- Split options in the daemon config file.

* Wed Sep 12 2012 Simone Caronni <negativo17@gmail.com> - 2.14-9
- Added user/group and confined directory for certificates, based on work from Joel Young.

* Tue Sep 11 2012 Joel Young <jdy@cryregarder.com> - 2.14-8
- Fixed bug with firefox 15+ ignored key:
  http://code.google.com/p/shellinabox/issues/detail?id=202&q=key%20work

* Wed Sep 05 2012 Simone Caronni <negativo17@gmail.com> - 2.14-7
- Add Fedora 18 systemd macros.
- Remove isa'ed BuildRequires.

* Thu Aug 30 2012 Simone Caronni <negativo17@gmail.com> - 2.14-6
- Add nss-lookup.target requirement and Documentation tag in service file.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Simone Caronni <negativo17@gmail.com> - 2.14-4
- Move systemd-units BR to proper place.

* Tue May 29 2012 Simone Caronni <negativo17@gmail.com> - 2.14-3
- Spec file changes (changelog, formatting).
- Added license files to doc section.

* Wed May 09 2012 Simone Caronni <negativo17@gmail.com> - 2.14-2
- Tags for RHEL building.

* Wed May 09 2012 Simone Caronni <negativo17@gmail.com> - 2.14-1
- First build.
