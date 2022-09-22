# lock_on_tmpfs: whether lock files are placed on tmpfs
%if !0%{?fedora}%{?rhel} || 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%bcond_without lock_on_tmpfs
%else
%bcond_with lock_on_tmpfs
%endif

%if !0%{?fedora}%{?rhel} || 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%bcond_without systemd_macros
%else
%bcond_with systemd_macros
%endif

%global _newconfigdir %{_sysconfdir}/uucp
%global _oldconfigdir %{_sysconfdir}/uucp/oldconfig
%global _varlogdir %{_localstatedir}/log/uucp
%global _varlockdir %{_localstatedir}/lock/uucp
%global _varspooldir %{_localstatedir}/spool

Summary: A set of utilities for operations between systems
Name: uucp
Version: 1.07
Release: 66%{?dist}
License: GPLv2+
Url: http://www.airs.com/ian/uucp.html
Source0: ftp://ftp.gnu.org/pub/gnu/uucp/uucp-%{version}.tar.gz
Source1: uucp.log
Source2: uucp@.service
Source3: uucp.socket
Source4: uuname.1
#Make the policy header better readable
Patch0: uucp-1.07-config.patch
Patch3: uucp-1.07-sigfpe.patch
#Use lockdev to create per-device lock(s) in /var/lock.
Patch6: uucp-1.07-lockdev.patch
#Fix to deny to use address in pipe ports.(thanks joery@dorchain.net)(#60771)
Patch8: uucp-1.06.1-pipe.patch
#fix truncation of values on 32b platforms where statvfs64
#is being called on a large file system (#153259)
Patch9: uucp-1.07-lfs.patch
#fix crashes with SIGFPE (#150978) (from Wolfgang Ocker)
Patch10: uucp-1.07-sigfpe2.patch
# Fix FTBFS for -Werror=format-security enablement
# ~> downstream, #1037372
Patch11: uucp-1.07-format.patch

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: lockdev-devel >= 1.0.0-14
BuildRequires: systemd-units
BuildRequires: texi2html

Requires(post): coreutils
Requires: cu
%if 0%{?fedora}%{?rhel} && (0%{?fedora} < 28 || 0%{?rhel} < 8)
Requires(preun): /sbin/install-info
Requires(post): /sbin/install-info
%endif
Requires: lockdev >= 1.0.0-14
Requires(pre): shadow-utils
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
The uucp command copies files between systems. Uucp is primarily used
by remote machines downloading and uploading email and news files to
local machines.

%package -n cu
Summary: call up another system

%description -n cu
The cu command is used to call up another system and act as a dial-in 
terminal (mostly on a serial line).
It can also do simple file transfers with no error checking.

cu is part of the UUCP source but has been split into its own package 
because it can be useful even if you do not do uucp. 

%prep
%setup -q
%patch0 -p1 -b .config
%patch3 -p1 -b .sigfpe
%patch6 -p1 -b .lockdev
%patch8 -p1 -b .pipe
%patch9 -p1 -b .lfs
%patch10 -p1 -b .sigfpe2
%patch11 -p1 -b .format

%build
# enable hardening because uucp contains setuid binaries
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 16 || 0%{?rhel} >= 7
%global _hardened_build 1
export CFLAGS="$RPM_OPT_FLAGS"
%else
# fake things
export CFLAGS="-fPIC $RPM_OPT_FLAGS"
export LDFLAGS="-pie"
%endif

autoreconf --verbose --force --install
export CFLAGS="$CFLAGS -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE"
%configure --with-newconfigdir=%{_newconfigdir} --with-oldconfigdir=%{_oldconfigdir}
make %{?_smp_mflags}

%install

%makeinstall install-info

gzip -9nf ${RPM_BUILD_ROOT}%{_infodir}/uucp*

mkdir -p ${RPM_BUILD_ROOT}%{_varlogdir}

mkdir -p ${RPM_BUILD_ROOT}%{_varspooldir}/uucp
mkdir -p ${RPM_BUILD_ROOT}%{_varspooldir}/uucppublic
mkdir -p ${RPM_BUILD_ROOT}%{_oldconfigdir}

mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/uucp
ln -sf ../../sbin/uucico ${RPM_BUILD_ROOT}%{_libdir}/uucp/uucico

mkdir -p ${RPM_BUILD_ROOT}/etc/logrotate.d
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}/etc/logrotate.d/uucp

mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_unitdir}
install -m644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_unitdir}

mkdir -p ${RPM_BUILD_ROOT}/%{_datadir}/uucp/contrib
install -p contrib/* ${RPM_BUILD_ROOT}/%{_datadir}/uucp/contrib/

install -m644 %{SOURCE4} ${RPM_BUILD_ROOT}%{_mandir}/man1

# Create ghost files
for n in Log Stats Debug; do
    touch ${RPM_BUILD_ROOT}%{_varlogdir}/$n
done

# the following is kind of gross, but it is effective
for i in dial passwd port dialcode sys call ; do
cat > ${RPM_BUILD_ROOT}%{_newconfigdir}/$i <<EOF
# This is an example of a $i file. This file is syntax compatible
# with Taylor UUCP (not HDB, not anything else). Please check uucp
# documentation if you are not sure how to configure Taylor UUCP config files.
# Edit the file as appropriate for your system, there are sample files
# in %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}/sample

# Everything after a '#' character is a comment.
EOF
done

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

# some more documentation
texi2html -monolithic uucp.texi

%if %{with lock_on_tmpfs}
mkdir -p ${RPM_BUILD_ROOT}%_tmpfilesdir
cat > ${RPM_BUILD_ROOT}%_tmpfilesdir/uucp.conf <<EOF
d %{_varlockdir} 0755 uucp uucp -
EOF
%endif

find "${RPM_BUILD_ROOT}%_datadir/uucp/contrib" -type f -exec chmod a-x {} +


%pre
getent group uucp >/dev/null || groupadd -g 14 -r uucp
if ! getent passwd uucp >/dev/null ; then
  if ! getent passwd 10 >/dev/null ; then
     useradd -r -u 10 -g uucp -d /var/spool/uucp  -c "Uucp user" uucp
  else
     useradd -r -g uucp -d /var/spool/uucp  -c "Uucp user" uucp
  fi
fi
exit 0


%post
%if %{with systemd_macros}
%systemd_post %{name}@.service
%else
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
if test $1 -eq 1; then
    %tmpfiles_create uucp.conf
fi

# Create initial log files so that logrotate doesn't complain
for n in Log Stats Debug; do
    [ -f %{_varlogdir}/$n ] || touch %{_varlogdir}/$n
    chown uucp:uucp %{_varlogdir}/$n
done
chmod 644 %{_varlogdir}/Log %{_varlogdir}/Stats
chmod 600 %{_varlogdir}/Debug

%if 0%{?fedora}%{?rhel} && (0%{?fedora} < 28 || 0%{?rhel} < 8)
/sbin/install-info %{_infodir}/uucp.info.gz %{_infodir}/dir || :
%endif

%preun
%if %{with systemd_macros}
%systemd_preun %{name}@.service
%else
if [ $1 -eq 0 ]; then
    #Package removal, not upgrade
    systemctl --no-reload disable %{name}@.service >/dev/null 2>&1 || :
    systemctl stop %{name}@.service >/dev/null 2>&1 || :
fi
%endif

%if 0%{?fedora}%{?rhel} && (0%{?fedora} < 28 || 0%{?rhel} < 8)
if [ $1 -eq 0 ]; then
    /sbin/install-info --del %{_infodir}/uucp.info.gz %{_infodir}/dir || :
fi
%endif

%postun
%if %{with systemd_macros}
%systemd_postun_with_restart %{name}@.service
%else
if [ $1 -ge 1 ]; then
        #Package upgrade, not uninstall
        systemctl try-restart %{name}@.service >/dev/null 2>&1
fi
%endif

%files
%doc README ChangeLog NEWS TODO
%doc sample uucp.html

%license COPYING

%attr(4555,uucp,uucp) %{_bindir}/uucp
%attr(0755,root,root) %{_bindir}/uulog
%attr(6555,uucp,uucp) %{_bindir}/uuname
%attr(0755,root,root) %{_bindir}/uupick
%attr(4555,uucp,uucp) %{_bindir}/uustat
%attr(0755,root,root) %{_bindir}/uuto
%attr(4555,uucp,uucp) %{_bindir}/uux

%attr(6555,uucp,uucp) %{_sbindir}/uucico
%attr(6555,uucp,uucp) %{_sbindir}/uuxqt
%attr(0755,root,root) %{_sbindir}/uuchk
%attr(0755,root,root) %{_sbindir}/uuconv
%attr(0755,root,root) %{_sbindir}/uusched

%attr(755,uucp,uucp) %dir %{_libdir}/uucp
%{_libdir}/uucp/uucico

%{_mandir}/man1/uucp.1*
%{_mandir}/man1/uuname.1*
%{_mandir}/man1/uustat.1*
%{_mandir}/man1/uux.1*
%{_mandir}/man8/uucico.8*
%{_mandir}/man8/uuxqt.8*

%{_infodir}/uucp.info*

%dir %{_datadir}/uucp
%{_datadir}/uucp/contrib

%attr(0755,uucp,uucp) %dir %{_varlogdir}
%attr(0644,uucp,uucp) %ghost %{_varlogdir}/Log
%attr(0644,uucp,uucp) %ghost %{_varlogdir}/Stats
%attr(0600,uucp,uucp) %ghost %{_varlogdir}/Debug

%ghost %attr(755,uucp,uucp) %dir %{_varlockdir}

%attr(775,uucp,uucp) %dir %{_varspooldir}/uucppublic

%config(noreplace) /etc/logrotate.d/uucp
%if %{with lock_on_tmpfs}
%_tmpfilesdir/uucp.conf
%endif
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.socket

%dir %{_newconfigdir}
%dir %{_oldconfigdir}
%attr(0640,root,uucp) %config(noreplace) %{_newconfigdir}/call
%config(noreplace) %{_newconfigdir}/dial
%config(noreplace) %{_newconfigdir}/dialcode
%attr(0640,root,uucp) %config(noreplace) %{_newconfigdir}/passwd
%config(noreplace) %{_newconfigdir}/port
%config(noreplace) %{_newconfigdir}/sys
%attr(755,uucp,uucp) /var/spool/uucp

%files -n cu
%doc README COPYING ChangeLog NEWS TODO
%attr(6555,uucp,uucp) %{_bindir}/cu
%{_mandir}/man1/cu.1*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.07-63
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Nils Philippsen <nils@tiptoe.de> - 1.07-56
- drop install-info scriptlets from Fedora 28 on

* Thu Feb 22 2018 Pavel Raiskup <praiskup@redhat.com> - 1.07-55
- drop executable bit contrib files (related to rhbz#1547805)

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 1.07-54
- reorder requirements
- remove empty %%clean section and obsolete %%defattr directive
- use %%license for COPYING
- require gcc for building

* Thu Feb 15 2018 Than Ngo <than@redhat.com> - - 1.07-53
- fixed FTBS

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.07-48
- Add cu BR to uucp pkg

* Fri Dec 23 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.07-47
- Split cu package

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Pavel Raiskup <praiskup@redhat.com> - 1.07-42
- lock file directory is %%ghost now (#1101325)
- remove uucp's ownership from non-suid binaries

* Mon Jan 20 2014 Pavel Raiskup <praiskup@redhat.com> - 1.07-41
- remove tetex BR, fix changelog dates

* Tue Dec 03 2013 Pavel Raiskup <praiskup@redhat.com> - 1.07-40
- pass string literal as format string for fprintf (#1037372)

* Sat Jul 27 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.07-39
- Honor %%{_pkgdocdir} where available.

* Wed Jul 03 2013 Ondrej Vasik <ovasik@redhat.com> - 1.07-38
- fix the typo in the uucp user creation (#980669)
- use soft static uid allocation

* Tue May 21 2013 Nils Philippsen <nils@redhat.com> - 1.07-37
- enable hardening because uucp contains setuid binaries (#965467)

* Sat May 11 2013 Ondrej Vasik <ovasik@redhat.com> - 1.07-36
- create /var/spool/uucp (previously in filesystem) (#961952)

* Wed Mar 20 2013 Ondrej Vasik <ovasik@redhat.com> - 1.07-35
- handle uucp (10:14) group in uucp (#918206)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 19 2012 Ondrej Vasik <ovasik@redhat.com> - 1.07-33
- ship uuname(1) manpage here instead of manpages

* Mon Aug 20 2012 Nils Philippsen <nils@redhat.com> - 1.07-32
- use spaces consistently
- default to lock on tmpfs if fedora/rhel not set
- use systemd macros from F-18/RHEL-7 on

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Nils Philippsen <nils@redhat.com> - 1.07-30
- move /etc/tmpfiles.d/uucp.conf to /usr/lib/tmpfiles.d

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 1.07-29
- rebuild for gcc 4.7

* Fri Nov 11 2011 Ondrej Vasik <ovasik@redhat.com> - 1.07-28
- drop ownership of /var/spool uucp (move to filesystem package
 as uucp is default system user) - #752885

* Fri Oct 21 2011 Ondrej Vasik <ovasik@redhat.com> - 1.07-27
- do not use baudboy.h, use lockdev instead (#747944)

* Tue Sep 13 2011 Ondrej Vasik <ovasik@redhat.com> - 1.07-26
- provide native systemd services (#737730)
- drop uucp.xinetd

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Nils Philippsen <nils@redhat.com> - 1.07-24
- add /etc/tmpfiles.d/uucp.conf to enable lock directory on tmpfs (#656714)
- use %%global instead of %%define

* Sat Apr 17 2010 Ondrej Vasik <ovasik@redhat.com> - 1.07-23
- fix uucico path in uucp.xinetd to work on 64 bit machines
  (#583179)

* Tue Dec 15 2009 Ondrej Vasik <ovasik@redhat.com> - 1.07-22
- move contrib dir from %%doc dir into /usr/share/uucp/

* Tue Dec 15 2009 Ondrej Vasik <ovasik@redhat.com> - 1.07-21
- Merge Review(#226521) - add _smp_mflags to make, remove implicit
  target, fix rpmlint warnings, commented patches, fix build root,
  use buildrequires/requires instead of prereq

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 25 2008 Ondrej Vasik <ovasik@redhat.com> 1.07-18
- remove uucp name from summary, generalize summary as there
  are other utilities in uucp set

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.07-17
- Autorebuild for GCC 4.3

* Wed Sep 19 2007 Radek Brich <rbrich@redhat.com> 1.07-16
- updated license tag

* Wed Apr 04 2007 Lukas Vrabel <lvrabel@redhat.com> 1.07-15
- fix crashes with SIGFPE (#150978) (from Wolfgang Ocker)

* Thu Jan 04 2007 Peter Vrabec <pvrabec@redhat.com> 1.07-14
- spec file improvements (#220534)

* Wed Jan 03 2007 Peter Vrabec <pvrabec@redhat.com> 1.07-13
- spec file improvements (#220534)

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 1.07-12
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.07-11.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.07-11.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Jul 15 2005 Peter Vrabec <pvrabec@redhat.com> 1.07-11
- use -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE together with RPM_OPT_FLAGS

* Thu Jul 14 2005 Peter Vrabec <pvrabec@redhat.com> 1.07-10
- revert fix from 1.07-9
- fix truncation of values on 32b platforms where statvfs64
  is being called on a large file system (#153259)

* Tue Apr 19 2005 Peter Vrabec <pvrabec@redhat.com> 1.07-9
- long long fsu_bavail in struct fs_usage

* Wed Mar 23 2005 Peter Vrabec <pvrabec@redhat.com> 1.07-8
- add texi2html to BuildRequires

* Wed Mar 16 2005 Peter Vrabec <pvrabec@redhat.com>
- include the default xinetd file

* Thu Feb 10 2005 Peter Vrabec <pvrabec@redhat.com>
- rebuilt

* Mon Oct 25 2004 Peter Vrabec <pvrabec@redhat.com>
- uucppublic change attr from 755 to 775 (#135335)

* Mon Oct 25 2004 Peter Vrabec <pvrabec@redhat.com>
- add dependencie tetex

* Thu Oct 14 2004 Peter Vrabec <pvrabec@redhat.com>
- fix spec file (#134328)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  8 2004 Jeff Johnson <jbj@jbj.org> 1.07-1
- upgrade to 1.07.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 12 2002 Jeff Johnson <jbj@redhat.com> 1.06.1-46
- rebuild from cvs.

* Sat Jul 20 2002 Akira TAGOH <tagoh@redhat.com> 1.06.1-45
- don't strip the binary.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 10 2002 Bill Huang <bhuang@redhat.com>
- Fix to deny to use address in pipe ports.(thanks joery@dorchain.net)(#60771)

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Feb  1 2002 Jeff Johnson <jbj@redhat.com>
- typo caused man8 pages to not be included (#54314).

* Fri Feb 1 2002 Bill Nottingham <notting@redhat.com>
- rebuild in new env. autoconf is fun!

* Mon Jan 28 2002 Jeff Johnson <jbj@redhat.com>
- filter all the long option aliases as well.

* Thu Jan 10 2002 Adrian Havill <havill@redhat.com>
- bumped version & rebuild for errata, changed spec "Copyright->License"

* Tue Sep  4 2001 Jeff Johnson <jbj@redhat.com>
- build against lockdev-1.0.0-14, with
- swap egid and gid for lockdev's access(2) device check (#52029).
- add (noreplace) to all config files.

* Tue Aug 28 2001 Jeff Johnson <jbj@redhta.com>
- move per-system lock to 755 uucp.uucp /var/lock/uucp directory.
- use baudboy.h to create per-device lock(s) in /var/lock.
- comment out compress/strip, rely on rpm brp-* scripts.
- check uuxqt arguments more carefully.

* Thu Aug  9 2001 Adrian Havill <havill@redhat.com>
- During build don't assume uid name == gid name (bug 14874)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Sat Jan  6 2001 Jeff Johnson <jbj@redhat.com>
- compile with owner=uucp.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun  2 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- map perms/owners into %%files to build as non-root.

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Sun Feb 13 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- change perms to be root:root for the config files and
  0640,root:uucp for config files containing passwords
- add patch from #6151 (division by zero, SIGFPE)
- make %%post work also for simple sh-versions

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages.

* Mon Aug 23 1999 Jeff Johnson <jbj@redhat.com>
- add notifempty/missingok to logrotate config file (#4138).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 19)

* Tue Dec 22 1998 Bill Nottingham <notting@redhat.com>
- expunge /usr/local/bin/perl reference in docs

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild
- added sample config files in /etc/uucp

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- added install-info support
- uses a build root

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- patched uureroute to find perl in /usr/bin instead of /usr/local/bin
- made log files ghosts

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Erik Troan <ewt@redhat.com>
- Brian Candler fixed /usr/lib/uucp/uucico symlink
- Added "create" entries to log file rotation configuration
- Touch log files on install if they don't already exist to allow proper
  rotation

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- symlinked /usr/sbin//uucico into /usr/lib/uucp
- (all of these changes are from Brian Candler <B.Candler@pobox.com>)
- sgid bit added on uucico so it can create lock files
- log files moved to /var/log/uucp/ owned by uucp (so uucico can create them)
- log rotation added
- uses /etc/uucp/oldconfig instead of /usr/lib/uucp for old config files
- package creates /etc/uucp and /etc/uucp/oldconfig directories
- man pages reference the correct locations for spool and config files

