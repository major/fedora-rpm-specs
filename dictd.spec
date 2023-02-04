%if 0%{?rhel} > 6 || 0%{?fedora} >= 16
%bcond_with         fedora
%bcond_without      systemd
%else
%bcond_without      fedora
%bcond_with         systemd
%endif
%global _hardened_build 1
# Do no change username -- hardcoded in dictd.c
%global username    dictd
%global homedir     %{_datadir}/dict/dictd
%global selinux_variants mls targeted
%define libmaaVersion 1.3.2

Summary:   DICT protocol (RFC 2229) server and command-line client
Name:      dictd
Version:   1.12.1
Release:   33%{?dist}
License:   GPL+ and zlib and MIT
Source0:   http://downloads.sourceforge.net/dict/%{name}-%{version}.tar.gz
Source1:   dictd.service
Source2:   libmaa-%{libmaaVersion}.tar.gz
Source3:   dictd2.te
Source4:   dictd.init
Patch0:    dictd-1.12.1-unused-return.patch
Patch1:    dictd-1.12.1-maa-bufsize.patch
Patch2:    dictd-c99.patch
URL:       http://www.dict.org/

BuildRequires:  flex bison libtool libtool-ltdl-devel byacc
BuildRequires:  libdbi-devel, zlib-devel, gawk, gcc
%if %{with systemd}
BuildRequires:  systemd
%endif
BuildRequires:	checkpolicy, selinux-policy-devel
BuildRequires: make
# , /usr/share/selinux/devel/policyhelp
Requires(pre):  shadow-utils

%description
Command-line client for the DICT protocol.  The Dictionary Server
Protocol (DICT) is a TCP transaction based query/response protocol that
allows a client to access dictionary definitions from a set of natural
language dictionary databases.

%package server
Summary: Server for the Dictionary Server Protocol (DICT)
%if %{with systemd}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%else
Requires(post):  chkconfig
Requires(preun): chkconfig
Requires(postun): initscripts
%endif
%if "%{_selinux_policy_version}" != ""
Requires:       selinux-policy >= %{_selinux_policy_version}
%endif

%description server
A server for the DICT protocol. You need to install dictd-usable databases
before you can use this server. Those can be found p.e. at
ftp://ftp.dict.org/pub/dict/pre/
More information can be found in the INSTALL file in this package.

%prep
%setup -q
tar xzf %{SOURCE2}
mv libmaa-%{libmaaVersion} libmaa
%patch0 -p1
%patch1 -p1
%patch2 -p1
mkdir SELinux
cp -p %{SOURCE3} SELinux

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export LDFLAGS="%{?__global_ldflags}" CPPFLAGS="$RPM_OPT_FLAGS -fPIC"
pushd libmaa
# Required for aarch64 support:
%configure
make %{?_smp_mflags}
popd

cd SELinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv dictd2.pp dictd2.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -

export LDFLAGS="%{?__global_ldflags} -Llibmaa/.libs" CPPFLAGS="-Ilibmaa $RPM_OPT_FLAGS -fPIC"
%configure --enable-dictorg --disable-plugin
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{homedir}
%if %{with systemd}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/dictd.service
%else
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install -m 755 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/dictd
%endif

cat <<EOF > $RPM_BUILD_ROOT/%{_sysconfdir}/dictd.conf
global {
    #syslog
    #syslog_facility daemon
}

# Add database definitions here...

# We stop the search here
database_exit

# Add hidden database definitions here...

EOF

for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 SELinux/dictd2.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/dictd2.pp
done


%post server
%if %{with systemd}
%systemd_post dictd.service
%else
if [ $1 = 1 ]; then
   /sbin/chkconfig --add dictd
fi
%endif

%preun server
%if %{with systemd}
%systemd_preun dictd.service
%else
if [ $1 = 0 ]; then
   # Stop the service (otherwise userdel will fail)
   /etc/rc.d/init.d/dictd stop &>/dev/null || :
   /sbin/chkconfig --del dictd
fi
%endif

%postun server
%if %{with systemd}
%systemd_postun_with_restart dictd.service
%else
if [ $1 -ge 1 ] ; then
   /sbin/service dictd condrestart > /dev/null 2>&1 || :
fi
%endif

%pre
getent group %{username} >/dev/null || groupadd -r %{username}
getent passwd %{username} >/dev/null || \
    useradd -r -g %{username} -d %{homedir} -s /sbin/nologin \
    -c "dictd dictionary server" %{username}
exit 0

%files
%doc ANNOUNCE COPYING ChangeLog README doc/rfc2229.txt doc/security.doc
%doc examples/dict1.conf
%{_bindir}/dict
%{_mandir}/man1/dict.1*


%files server
%doc ANNOUNCE COPYING INSTALL ChangeLog README doc/rfc2229.txt doc/security.doc
%doc examples/dictd*
%exclude %{_mandir}/man1/dict.1*
%exclude %{_bindir}/dict
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man?/*
%if %{with systemd}
%attr(0644,root,root) %{_unitdir}/dictd.service
%else
%{_sysconfdir}/rc.d/init.d/*
%endif
%{homedir}
%config(noreplace) %{_sysconfdir}/dictd.conf
%doc SELinux
%{_datadir}/selinux/*/dictd2.pp

%changelog
* Thu Feb 02 2023 Florian Weimer <fweimer@redhat.com> - 1.12.1-33
- Fix C99 compatibility issues in lexer/parser integration

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.12.1-28
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 1.12.1-22
- Clean up SELinux module sources

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Matěj Cepl <mcepl@redhat.com> - 1.12.1-20
- Don't confuse systemd service file with the old initd script (#1444555)

* Wed Feb 21 2018 Karsten Hopp <karsten@redhat.com> - 1.12.1-19
- Buildrequire gcc

* Tue Feb 13 2018 Karsten Hopp <karsten@redhat.com> - 1.12.1-18
- drop requirement policyhelp
- enlarge buffer in log.c

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 05 2017 Matěj Cepl <mcepl@redhat.com> - 1.12.1-14
- Add conditionals to build on EPEL-6 (#1116553)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 24 2016 Karsten Hopp <karsten@redhat.com> - 1.12.1-12
- solve uid 52 conflict with puppet package. use dynamic uid allocation
  (rhbz#1337978)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Karsten Hopp <karsten@redhat.com> 1.12.1-9
- fix dictd.service permissions (rhbz#1192228)
- drop unused /etc/sysconfig/dictd (rhbz#1165413)
- add SELinux policies (rhbz#1148302)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.12.1-7
- %%configure macro updates config.guess/sub for new arches (aarch64/ppc64le)
- Update systemd scriptlets to latest standard
- General cleanups

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Karsten Hopp <karsten@redhat.com> 1.12.1-5
- used hardened build flag to enable PIE (rhbz 955198)

* Mon Aug 05 2013 Karsten Hopp <karsten@redhat.com> 1.12.1-3
- add BR: systemd-units for the _unitdir macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Karsten Hopp <karsten@redhat.com> 1.12.1-1
- update to 1.12.1
- add support for aarch64 (#925252)

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 1.12.0-6
- Migrate from fedora-usermgmt to guideline scriptlets.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Jon Ciesla <limburgher@gmail.com> - 1.12.0-3
- Migrate to systemd, BZ 772085.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 04 2011 Karsten Hopp <karsten@redhat.com> 1.12.0-1
- update to version 1.12.0
- split into server and client packages
- add most of Oron Peled's <oron@actcom.co.il> changes from
  https://bugzilla.redhat.com/attachment.cgi?id=381332
  - The daemon now runs as 'dictd' user. This user is added/remove
    during install/uninstall.
  - Create and own a default configuration file
  - By default listen only on 127.0.0.1 (secure by default)
  - Default directory for dictionaries (datadir) is
    now /usr/share/dict/dictd and not /usr/share
  - Add the examples directory to the documentation

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Karsten Hopp <karsten@redhat.com> 1.11.0-3
- add disttag

* Thu Jan 22 2009 Karsten Hopp <karsten@redhat.com> 1.11.0-2
- add postun script (#225694)
- fix file permissions (defattr)

* Wed Jan 14 2009 Karsten Hopp <karsten@redhat.com> 1.11.0-1
- update

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.10.11-3
- fix license tag

* Wed May 07 2008 Karsten Hopp <karsten@redhat.com> 1.10.11-2
- update to 1.10.11

* Tue Apr 01 2008 Karsten Hopp <karsten@redhat.com> 1.10.10-1
- fix typo (#281981)
- update

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.10.9-2
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Karsten Hopp <karsten@redhat.com> 1.10.9-1
- new upstream version

* Wed Aug 22 2007 Karsten Hopp <karsten@redhat.com> 1.9.15-11
- update license tag and rebuild

* Mon Aug 13 2007 Karsten Hopp <karsten@redhat.com> 1.9.15-10
- add LSB stuff (#246910)

* Wed Feb 21 2007 Karsten Hopp <karsten@redhat.com> 1.9.15-9
- misc. merge review fixes

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.9.15-8.1
- rebuild

* Mon May 22 2006 Karsten Hopp <karsten@redhat.de> 1.9.15-8
- buildrequires zlib-devel

* Thu May 18 2006 Karsten Hopp <karsten@redhat.de> 1.9.15-7
- Buildrequires: libdbi-devel

* Mon Feb 20 2006 Karsten Hopp <karsten@redhat.de> 1.9.15-6
- BuildRequires: byacc

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.9.15-5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.9.15-5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 02 2006 Karsten Hopp <karsten@redhat.de> 1.9.15-5
- add BuildRequires libtool-ltdl-devel (#176505)

* Tue Dec 20 2005 Karsten Hopp <karsten@redhat.de> 1.9.15-4
- consult dict.org if no server is specified on the commandline
  (#176038)

* Mon Dec 12 2005 Karsten Hopp <karsten@redhat.de> 1.9.15-3
- rebuild with gcc-4.1

* Tue Jul 12 2005 Karsten Hopp <karsten@redhat.de> 1.9.15-2
- Buildrequires libtool (ltdl.h)

* Wed Jul 06 2005 Karsten Hopp <karsten@redhat.de> 1.9.15-1
- update to dictd-1.9.15
- drop gcc34 patch

* Mon May 02 2005 Karsten Hopp <karsten@redhat.de> 1.9.7-9
- use _bindir / _sysconfdir macros

* Sat Apr 02 2005 Florian La Roche <laroche@redhat.com>
- /etc/init.d -> /etc/rc.d/init.d


* Thu Mar 10 2005 Bill Nottingham <notting@redhat.com> 1.9.7-7
- prereq chkconfig

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 1.9.7-6
- build with gcc-4

* Tue Jan 25 2005 Karsten Hopp <karsten@redhat.de> 1.9.7-5
- don't install config file, leave it to the dictionary packages to
  populate it. (#135920)

* Mon Oct 04 2004 Karsten Hopp <karsten@redhat.de> 1.9.7-4
- add initscript

* Sat Jun 19 2004 Karsten Hopp <karsten@redhat.de> 1.9.7-3
- fix build with gcc34

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 02 2004 Karsten Hopp <karsten@redhat.de> 1.9.7-1
- update

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- build on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Mar 26 2000 Philip Copeland <bryce@redhat.com> 1.5.5-1
- initial rpm version
