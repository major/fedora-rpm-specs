%if %{?WITH_SELINUX:0}%{!?WITH_SELINUX:1}
%define WITH_SELINUX 1
%endif
%if %{?WITH_AUDIT:0}%{!?WITH_AUDIT:1}
%define WITH_AUDIT 1
%endif
Summary: An utility for setting or changing passwords using PAM
Name: passwd
Version: 0.80
Release: 15%{?dist}
License: BSD-3-Clause OR GPL-2.0-only
URL: https://pagure.io/passwd
Source: https://releases.pagure.org/passwd/passwd-%{version}.autotoolized.tar.bz2
Patch0: passwd-0.80-manpage.patch
Patch1: passwd-0.80-S-output.patch
Requires: pam >= 1.0.90, /etc/pam.d/system-auth
BuildRequires: make
%if %{WITH_SELINUX}
Requires: libselinux >= 2.1.6-3
BuildRequires: libselinux-devel >= 2.1.6-3
%endif
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/IJFYI5Q2BYZKIGDFS2WLOBDUSEGWHIKV/
BuildRequires: gcc
BuildRequires: glib2-devel, libuser-devel, pam-devel, libuser >= 0.53-1
BuildRequires: gettext, popt-devel
%if %{WITH_AUDIT}
BuildRequires: audit-libs-devel >= 2.4.5
Requires: audit-libs >= 2.4.5
%endif

%description
This package contains a system utility (passwd) which sets
or changes passwords, using PAM (Pluggable Authentication
Modules) library.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .manpage
%patch1 -p1 -b .S-output

%build
%configure \
%if %{WITH_SELINUX}
        --with-selinux \
%else
        --without-selinux \
%endif
%if %{WITH_AUDIT}
        --with-audit
%else
        --without-audit
%endif
make DEBUG= RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/
install -m 644 passwd.pamd $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/passwd
%find_lang %{name}
for dir in $(ls -1d $RPM_BUILD_ROOT%{_mandir}/{??,??_??}) ; do
    dir=$(echo $dir | sed -e "s|^$RPM_BUILD_ROOT||")
    lang=$(basename $dir)
    echo "%%lang($lang) $dir/man*/*" >> %{name}.lang
done


%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/pam.d/passwd
%attr(4755,root,root) %{_bindir}/passwd
%{_mandir}/man1/passwd.1*

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Jiri Kucera <jkucera@redhat.com> - 0.80-7
- fix inconsistencies in manpage
- fix incorrect -S output
  Resolves: #1612221, #1740166

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Jiri Kucera <jkucera@redhat.com> - 0.80-3
- passwd-0.80 relies on AUDIT_ACCT_LOCK and AUDIT_ACCT_UNLOCK that
  were introduced at audit-2.4.5

* Thu Apr 12 2018 Jiri Kucera <jkucera@redhat.com> - 0.80-2
- Removed autotools dependencies

* Thu Mar 29 2018 Jiri Kucera <jkucera@redhat.com> - 0.80-1
- Update to passwd-0.80
  Resolves: #1293929

* Thu Mar 29 2018 Jiri Kucera <jkucera@redhat.com> - 0.79-15
- Mercurial changeset ID changed to the corresponding Git
  changeset ID

* Wed Feb 21 2018 Jiri Kucera <jkucera@redhat.com> - 0.79-14
- Added missing gcc dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Miloslav Trmač <mitr@redhat.com> - 0.79-10
- Redirect URL: and Source: from fedorahosted.org to pagure.io
  Resolves: #1472576

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 2 2015 Miloslav Trmač <mitr@redhat.com> - 0.79-7
- Support passwords up to PAM_MAX_RESP_SIZE - 1 with --stdin
  Resolves: #1187105

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Tom Callaway <spot@fedoraproject.org> - 0.79-4
- fix license handling

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Miloslav Trmač <mitr@redhat.com> - 0.79-1
- Update to passwd-0.79
  Resolves: #926312, #948790

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.78.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec  4 2012 Miloslav Trmač <mitr@redhat.com> - 0.78.99-3
- Fix License:

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.78.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 27 2012 Tomas Mraz <tmraz@redhat.com> 0.78.99-1
- use better (auditable) libselinux calls for checking
  the access to passwd (#518268)
- add support for the -e option as seen on Debian passwd
- make the binary PIE and full RELRO (#784483)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.78-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Tomas Mraz <tmraz@redhat.com> 0.78-3
- add the postlogin substack to the PAM configuration (#665063)

* Fri Jul 16 2010 Tomas Mraz <tmraz@redhat.com> 0.78-1
- added japanese translation of the man page (#611692)
- updated translations

* Tue Apr  6 2010 Tomas Mraz <tmraz@redhat.com> 0.77-5
- first part of fix for pam_gnome_keyring prompting (#578624)
  needs support for use_authtok to be added to pam_gnome_keyring

* Thu Jan 28 2010 Tomas Mraz <tmraz@redhat.com> 0.77-4
- add COPYING and other things to doc
- correct the licence field

* Mon Sep 14 2009 Tomas Mraz <tmraz@redhat.com> 0.77-1
- updated translations
- improved manual page

* Wed Feb 11 2009 Tomas Mraz <tmraz@redhat.com> 0.76-1
- identify SHA-256 and SHA-512 password hashes (#484994)

* Tue Apr  8 2008 Tomas Mraz <tmraz@redhat.com> 0.75-2
- add optional pam_gnome_keyring module to passwd pam
  config (#441225)

* Wed Feb 20 2008 Tomas Mraz <tmraz@redhat.com> 0.75-1
- fix disabling SELinux and audit in spec (#433284)
- remove obsolete no.po (#332121)
- updated translations

* Tue Sep 25 2007 Tomas Mraz <tmraz@redhat.com> 0.74-5
- buildrequires popt-devel

* Wed Aug 22 2007 Tomas Mraz <tmraz@redhat.com> 0.74-4
- spec file cleanups

* Thu Apr  5 2007 Tomas Mraz <tmraz@redhat.com> 0.74-3
- use std buildroot, add dist tag (#226232)

* Tue Jan 30 2007 Tomas Mraz <tmraz@redhat.com> 0.74-2
- do not explicitly strip the binary

* Tue Dec 12 2006 Tomas Mraz <tmraz@redhat.com> 0.74-1
- minor fixes in error reporting
- localize messages (#204022)

* Mon Jul 17 2006 Tomas Mraz <tmraz@redhat.com> 0.73-1
- fixed broken logic from the last change (#196851)

* Fri Jul 14 2006 Tomas Mraz <tmraz@redhat.com> 0.72-1
- merged audit patch to upstream cvs
- improved passwd -S output (#170344)
- make passwd -d work with stripped down proc (#196851)
- corrected link to pam docs (#193084)
- spec file cleanups

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.71-3.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.71-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.71-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Steve Grubb <sgrubb@redhat.com> 0.71-3
- Adjust audit patch so it builds without libaudit

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Oct 25 2005 Steve Grubb <sgrubb@redhat.com> 0.71-2
- adjust audit communication to use common logging functions

* Fri Oct  7 2005 Tomas Mraz <tmraz@redhat.com> 0.71-1
- use include instead of pam_stack in pam config

* Fri Jun 17 2005 Tomas Mraz <tmraz@redhat.com> 0.70-1
- replace laus with audit
- auto* build changes

* Fri Jan 28 2005 Jindrich Novy <jnovy@redhat.com> 0.69-1
- spec file fixes
- add libuser >= 0.53-1 BuildPrereq (#139331)

* Tue Jan 25 2005 Dan Walsh <dwalsh@redhat.com>
- improve SELinux priv checking

* Mon Aug 23 2004 Jindrich Novy <jnovy@redhat.com>
- applied cleanup patch from Steve Grubb #120060
- fixed man page #115380
- added libselinux-devel to BuildPrereq #123750, #119416

* Thu Aug 19 2004 Jindrich Novy <jnovy@redhat.com> 0.68-10
- moved to 0.68-10 to fix problem with RHEL4-Alpha4 #129548
- updated GNU build scripts and file structure to recent style

* Wed Feb 4 2004 Dan Walsh <dwalsh@redhat.com> 0.68-8
- add check for enforcing mode

* Mon Jan 26 2004 Dan Walsh <dwalsh@redhat.com> 0.68-7
- fix is_selinux_enabled

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> 0.68-6
- turn off selinux

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> 0.68-5.sel
- Add SELinux support

* Mon Jul 28 2003 Dan Walsh <dwalsh@redhat.com> 0.68-4
- Add SELinux support

* Thu Feb 13 2003 Nalin Dahyabhai <nalin@redhat.com> 0.68-3
- add aging adjustment flags to passwd(1)'s synopsis, were just in the
  reference section before

* Mon Jan 27 2003 Nalin Dahyabhai <nalin@redhat.com> 0.68-2
- rebuild

* Mon Dec  9 2002 Nalin Dahyabhai <nalin@redhat.com> 0.68-1
- implement aging adjustments for pwdb

* Mon Nov 11 2002 Nalin Dahyabhai <nalin@redhat.com> 0.67-4
- modify default PAM configuration file to not specify directories, so that
  the same configuration can be used for all arches on multilib systems
- fix BuildPrereq on glib-devel to specify glib2-devel instead
- remove unpackaged files in %%install phase

* Tue May 28 2002 Nalin Dahyabhai <nalin@redhat.com> 0.67-3
- rebuild

* Mon May 20 2002 Nalin Dahyabhai <nalin@redhat.com> 0.67-2
- rebuild in new environment

* Wed Mar 13 2002 Nalin Dahyabhai <nalin@redhat.com> 0.67-1
- add the -i, -n, -w, and -x options to passwd

* Mon Mar 11 2002 Nalin Dahyabhai <nalin@redhat.com> 0.65-5
- rebuild

* Mon Feb 25 2002 Nalin Dahyabhai <nalin@redhat.com> 0.65-4
- rebuild

* Fri Feb 22 2002 Nalin Dahyabhai <nalin@redhat.com> 0.65-3
- rebuild

* Thu Jan 31 2002 Nalin Dahyabhai <nalin@redhat.com> 0.65-2
- rebuild to get dependencies right

* Tue Jan 29 2002 Nalin Dahyabhai <nalin@redhat.com> 0.65-1
- change dependency from pwdb to libuser

* Fri Jan 25 2002 Nalin Dahyabhai <nalin@redhat.com> 0.64.1-9
- rebuild

* Thu Aug 30 2001 Nalin Dahyabhai <nalin@redhat.com> 0.64.1-8
- man page fix (-r is the opposite of -l, not --stdin, which precedes it)
  from Felipe Gustavo de Almeida

* Mon Aug  6 2001 Nalin Dahyabhai <nalin@redhat.com> 0.64.1-7
- fix unguarded printf() (noted by Chris Evans)
- add missing build dependency on pwdb and pam-devel (#49550)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- move man pages to _mandir

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify PAM setup to use system-auth
- modify for building as non-root users

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- fix manpage links

* Fri Feb 04 2000 Nalin Dahyabhai <nalin@redhat.com>
- document --stdin in man page
- fix for gzipped man pages

* Sat Apr 10 1999 Cristian Gafton <gafton@redhat.com>
- first build from the new source code base.
