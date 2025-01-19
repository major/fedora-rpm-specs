Summary: PAM module for use with SSH keys and ssh-agent
Name: pam_ssh
Version: 2.3
Release: 19%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://sourceforge.net/projects/pam-ssh/
Source0: http://downloads.sourceforge.net/pam-ssh/pam_ssh-%{version}.tar.xz
BuildRequires: make
BuildRequires: pam-devel, openssh-clients, openssl-devel, libtool
BuildRequires: systemd-units
Requires: openssh-clients
Conflicts: selinux-policy-targeted < 3.0.8-55
Patch0: pam_ssh-2.3-rundir.patch
Patch1: pam_ssh-2.3-inexistent_directory.patch


%description
This PAM module provides single sign-on behavior for UNIX using SSH keys. 
Users are authenticated by decrypting their SSH private keys with the 
password provided. In the first PAM login session phase, an ssh-agent 
process is started and keys are added. The same agent is used for the
following PAM sessions. In any case the appropriate environment variables
are set in the session phase.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

# re-run autoconf utils to libtoolize properly
autoreconf -f -si


%build
CFLAGS="$RPM_OPT_FLAGS -fcommon"
%configure  --with-pam-dir=/%{_lib}/security/
make clean

#  only needed symbols should be exported
cat >>pam_ssh.sym <<EOF
pam_sm_acct_mgmt
pam_sm_authenticate
pam_sm_chauthtok
pam_sm_close_session
pam_sm_open_session
pam_sm_setcred
EOF

make %{?_smp_mflags} LDFLAGS='-export-symbols pam_ssh.sym'


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.la

install -d $RPM_BUILD_ROOT%{_tmpfilesdir}
cat <<EOF >$RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
D %{_rundir}/pam_ssh 0755 root root -
EOF

install -d -m 755 $RPM_BUILD_ROOT%{_rundir}/pam_ssh



%files
/%{_lib}/security/*.so
%dir %{_rundir}/pam_ssh
%{_tmpfilesdir}/%{name}.conf
%doc AUTHORS NEWS README ChangeLog TODO
%license COPYING
%{_mandir}/*/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.3-10
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb  8 2021 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.3-8
- Use /run instead of /var/run (#1926099)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.3-6
- Use /run instead of /var/run (#1892535)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
- Use gcc -fcommon flag to build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May  7 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.3-2
- fix inexistent .ssh subdir checking (Alexi Dimitriadis <adimitriadis@noggin.com.au>, #1707257)
- no more need to build with compat-openssl-1.0

* Wed Mar 13 2019 Dmitry Butskoy <Dmitry@Butskoy.name> - 2.3-1
- Upgrade to 2.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Ville Skyttä <ville.skytta@iki.fi> - 1.98-7
- Move tmpfiles.d config to %%{_tmpfilesdir}
- Install COPYING as %%license

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.98-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.98-1
- Update to 1.98

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct  6 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.97-9
- No more ghost /var/run/pam_ssh

* Mon Oct  3 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.97-8
- Use tmpfiles.d for /var/run pre-creation to avoid SELinux issues (#742274)

* Tue Jun  7 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.97-7
- Drop root group privileges properly before executing ssh-agent (#711170)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.97-5
- export only pam_sm_* symbols from the module
  (else it could cause cross linking when used under sshd daemon)

* Mon Dec 13 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.97-4
- auto-create state dir under /var/run (#656657)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.97-3
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.97-1
- update to 1.97
- drop no more needed patches
- specfile cleanup
- run autoreconf to re-libtoolize properly

* Thu Mar 26 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.92-10
- Always use standard "Password:" prompt for the first password's inquire
  in a PAM chain (#492153)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Manuel "lonely wolf" Wolfshant <wolfy@nobugconsulting.ro> 1.92-8.1
- rebuild for newer openssl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.92-8
- Autorebuild for GCC 4.3

* Thu Dec 27 2007 Patrice Dumas <pertusus@free.fr> 1.92-7
- keep timestamps

* Mon Dec 10 2007 Patrice Dumas <pertusus@free.fr> 1.92-6
- remove selinux policy module support, since it is in main selinux
- Conflicts: selinux-policy-targeted < 3.0.8-55 since it seems to be 
  the first package with included selinux policy

* Mon Dec 10 2007 Patrice Dumas <pertusus@free.fr> 1.92-5
- correct a typo in selinux %%postun script

* Thu Nov 15 2007 Martin Ebourne <martin@zepler.org> - 1.92-3
- Added SELinux policy module

* Thu Aug 23 2007 Patrice Dumas <pertusus@free.fr> 1.92-2
- update to 1.92
- Fix #253959, CVE-2007-0844

* Sun Sep 10 2006 Patrice Dumas <pertusus@free.fr> 1.91-15
- rebuild for FC6

* Fri Feb 17 2006 Patrice Dumas <pertusus@free.fr> - 1.91-14
- rebuild for fc5

* Thu Dec 22 2005 Patrice Dumas <pertusus@free.fr> - 1.91-13
- add patch to include syslog.h

* Sun Nov 13 2005 <pertusus@free.fr> 1.91-11
- add patch to include openssl/md5.h 

* Sun Nov 13 2005 <pertusus@free.fr> 1.91-10
- rebuild against new openssl

* Fri Sep  2 2005 <pertusus@free.fr> 1.91-9
- bump release

* Fri Aug 26 2005 <pertusus@free.fr> 1.91-8
- add --with-pam-dir switch for ./configure

* Wed Aug 17 2005 <pertusus@free.fr> 1.91-7
- remove openssh from BuildRequires (Dmitry)
- remove pam from Requires, it is picked up automatically

* Tue Aug 16 2005 <pertusus@free.fr> 1.91-6
- new summary from me and Dmirty
- use Dmitry modified patch1 to let user see the informations in 
  /var/run/pam_ssh/ (modified at my request)
- document the agent environment information files location in
  the man page

* Mon Aug 15 2005 Patrice Dumas <pertusus@free.fr> 1.91-5
- remove gcc-g++ from BuildRequires. Merge description with 
  Dmitry description

* Mon Aug 15 2005 Dmitry Butskoy <Dmitry@Butskoy.name> 1.91-3
- Allow standalone session module (patch0)
- Move runtime state files from ~/.ssh/agent-<hostname>* to
  /var/run/pam_ssh/<user>* . This is an easy way to provide properly
  cleanups after system crash. (patch1)

* Mon Aug 15 2005 Patrice Dumas <pertusus@free.fr> 1.91-2
- correct URL, use upstream source, add COPYING to %%doc

* Sat Apr 01 2004 Patrice Dumas <pertusus@free.fr> 1.91-1
- update source

* Mon Mar 15 2004 Patrice Dumas <pertusus@free.fr> 1.9-0.fdr.1
- Use fedora-newrpmspec to update the spec file

* Fri Aug 16 2002 Dumas Patrice <pertusus@free.fr>
- Initial build.
