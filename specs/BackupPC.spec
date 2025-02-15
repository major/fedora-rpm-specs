%global _hardened_build 1

# tmpfiles.d & systemd not supported in RHEL < 7
%if 0%{?fedora} || 0%{?rhel} >= 7
%global _with_tmpfilesd 1
%global _with_systemd 1
%endif

%global _updatedb_conf /etc/updatedb.conf

Name:           BackupPC
Version:        4.4.0
Release:        19%{?dist}
Summary:        High-performance backup system

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://backuppc.github.io/backuppc/index.html
Source0:        https://github.com/backuppc/backuppc/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        BackupPC.htaccess
Source2:        BackupPC.logrotate
Source3:        README.setup
#A C wrapper to use since perl-suidperl is no longer provided
Source4:        BackupPC_Admin.c
Source5:        backuppc.service
Source6:        BackupPC.tmpfiles
Source7:        README.RHEL
Source8:        apache.users

Patch0:         BackupPC-4.1.3-docfix.patch
# Fixes https://bugzilla.redhat.com/show_bug.cgi?id=2091514
Patch1:         https://github.com/backuppc/backuppc/commit/2c9270b9b849b2c86ae6301dd722c97757bc9256.patch

BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl(BackupPC::XS) >= 0.53
BuildRequires:  perl(CGI)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Listing)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
%if 0%{?_with_systemd}
BuildRequires:  systemd
%endif

# Unbundled libraries
Requires:       perl(Net::FTP::AutoReconnect)
Requires:       perl(Net::FTP::RetrHandle)

Requires:       bzip2
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       webserver
Recommends:     httpd
%else
Requires:       httpd
%endif
Requires:       iputils
Requires:       openssh-clients
%if ! 0%{?el6}
Requires:       par2cmdline
%endif
Requires:       rrdtool
Requires:       rsync-bpc >= 3.0.9.6
Requires:       perl(BackupPC::XS) >= 0.53
Requires:       perl-Time-modules
Requires:       samba-client
Requires:       %{_sbindir}/sendmail

%if 0%{?_with_systemd}
Requires(post): shadow-utils
%{?systemd_requires}
%else
Requires(preun): initscripts chkconfig
Requires(post): initscripts chkconfig shadow-utils
Requires(postun): initscripts
%endif

Requires:       policycoreutils
BuildRequires:  selinux-policy-devel checkpolicy
BuildRequires: make
Provides:       backuppc = %{version}-%{release}


%description
BackupPC is a high-performance, enterprise-grade system for backing up Linux
and WinXX and Mac OS X PCs and laptops to a server's disk. BackupPC is highly
configurable and easy to install and maintain.

NOTE: Proper configuration is required after install, see README.setup for more
information.


%prep
%autosetup -p1

for f in ChangeLog; do
  iconv -f ISO-8859-1 -t UTF-8 $f > $f.utf && mv $f.utf $f
done

cp %{SOURCE3} .
cp %{SOURCE7} .
cp %{SOURCE4} .

mkdir selinux
pushd selinux

cat >%{name}.te <<EOF
policy_module(%{name},0.0.6)
require {
        type httpd_t, var_lib_t, var_log_t;
        class sock_file { write };
        type unconfined_service_t;
        class unix_stream_socket { connectto };
        type ssh_exec_t, ping_exec_t, sendmail_exec_t;
        class file { getattr };
        type var_run_t;
        class sock_file { getattr };
        type httpd_log_t;
        class file { open };
        class dir { read };
}

allow httpd_t var_run_t:sock_file write;
allow httpd_t var_lib_t:file write;
allow httpd_t unconfined_service_t:unix_stream_socket connectto;
allow httpd_t ping_exec_t:file getattr;
allow httpd_t sendmail_exec_t:file getattr;
allow httpd_t ssh_exec_t:file getattr;
allow httpd_t var_run_t:sock_file getattr;
allow httpd_t httpd_log_t:file open;
allow httpd_t httpd_log_t:dir read;
EOF

cat >%{name}.fc <<EOF
%{_sysconfdir}/%{name}(/.*)?            gen_context(system_u:object_r:httpd_sys_script_rw_t,s0)
%{_sysconfdir}/%{name}/LOCK             gen_context(system_u:object_r:httpd_lock_t,s0)
%{_localstatedir}/run/%{name}(/.*)?     gen_context(system_u:object_r:var_run_t,s0)
%{_localstatedir}/lib/%{name}(/.*)?     gen_context(system_u:object_r:httpd_var_lib_t,s0)
%{_localstatedir}/log/%{name}(/.*)?     gen_context(system_u:object_r:httpd_log_t,s0)
EOF
popd

# attempt to unbundle as much as possible
for m in Net/FTP; do
  rm -rf lib/$m
  sed -i "\@lib/$m@d" configure.pl 
done

# Create a sysusers.d config file
cat >backuppc.sysusers.conf <<EOF
u backuppc - - %{_localstatedir}/lib/%{name} -
EOF


%build
# Build C wrapper
gcc -o BackupPC_Admin BackupPC_Admin.c %{optflags}

# SElinux 
pushd selinux
make -f %{_datadir}/selinux/devel/Makefile
popd


%install
%{__perl} configure.pl \
        --batch \
        --backuppc-user=backuppc \
        --dest-dir %{buildroot} \
        --config-dir %{_sysconfdir}/%{name}/ \
        --config-override CgiURL=\"http://localhost/%{name}\" \
        --config-override ClientNameAlias=undef \
        --config-override NmbLookupPath=\"%{_bindir}/nmblookup\" \
        --config-override ParPath=\"%{_bindir}/par2\" \
        --config-override PingPath=\"%{_bindir}/ping\" \
        --config-override Ping6Path=\"%{_sbindir}/ping6\" \
        --config-override RrdToolPath=\"%{_bindir}/rrdtool\" \
        --config-override RsyncBackupPCPath=\"%{_bindir}/rsync_bpc\" \
        --config-override RsyncClientPath=\"%{_bindir}/rsync\" \
        --config-override SendmailPath=\"%{_sbindir}/sendmail\" \
        --config-override SmbClientPath=\"%{_bindir}/smbclient\" \
        --config-override SshPath=\"%{_bindir}/ssh\" \
        --config-override TarClientPath=\"%{_bindir}/gtar\" \
        --config-override XferMethod=\"rsync\" \
        --cgi-dir %{_libexecdir}/%{name} \
        --data-dir %{_localstatedir}/lib/%{name}/ \
        --hostname localhost \
        --html-dir %{_datadir}/%{name}/html/ \
        --html-dir-url /%{name}/images \
        --install-dir %{_datadir}/%{name} \
        --log-dir %{_localstatedir}/log/%{name} \
        --no-set-perms \
        --uid-ignore

# Make bin files executable
chmod +x %{buildroot}%{_datadir}/%{name}/bin/*

%if 0%{?_with_tmpfilesd}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -p -m 0644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%else
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
%endif

%if 0%{?_with_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/
%else
mkdir -p %{buildroot}%{_initrddir}
install -p -m 0755 systemd/src/init.d/linux-backuppc %{buildroot}%{_initrddir}/backuppc
%endif

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/pc

install -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -m 0644 %{SOURCE8} \
    %{buildroot}%{_sysconfdir}/%{name}/

# perl-suidperl is no longer avaialable, we use a C wrapper
mkdir -p %{buildroot}%{_datadir}/%{name}/sbin
mv %{buildroot}%{_libexecdir}/%{name}/BackupPC_Admin \
   %{buildroot}%{_datadir}/%{name}/sbin/BackupPC_Admin
install -pm 0755 BackupPC_Admin %{buildroot}%{_libexecdir}/%{name}/

# SElinux 
mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{name}
install -m 0644 selinux/%{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{name}/%{name}.pp

install -m0644 -D backuppc.sysusers.conf %{buildroot}%{_sysusersdir}/backuppc.conf



%preun
%if 0%{?_with_systemd}
%systemd_preun backuppc.service
%else
if [ $1 = 0 ]; then
  # Package removal, not upgrade
  service backuppc stop > /dev/null 2>&1 || :
  chkconfig --del backuppc || :
fi
%endif

%post
(
     # Install/update Selinux policy
     semodule -i %{_datadir}/selinux/packages/%{name}/%{name}.pp
     # files created by app
     restorecon -R %{_sysconfdir}/%{name}
     restorecon -R %{_localstatedir}/log/%{name}
) &>/dev/null

%if 0%{?_with_systemd}
%systemd_post backuppc.service
%else
if [ $1 -eq 1 ]; then
  # initial installation
  chkconfig --add backuppc || :
fi
%{_sbindir}/usermod -a -G backuppc apache || :
%endif

# add BackupPC backup directories to PRUNEPATHS in locate database
if [ -w %{_updatedb_conf} ]; then
  grep ^PRUNEPATHS %{_updatedb_conf} | grep %{_localstatedir}/lib/%{name} > /dev/null
  if [ $? -eq 1 ]; then
    sed -i '\@PRUNEPATHS@s@"$@ '%{_localstatedir}/lib/%{name}'"@' %{_updatedb_conf}
  fi
fi
:

%postun
# clear out any BackupPC configuration in apache
service httpd condrestart > /dev/null 2>&1 || :

if [ $1 -eq 0 ]; then
  # uninstall
  # Remove the SElinux policy.
  semodule -r %{name} &> /dev/null || :
  # remove BackupPC backup directories from PRUNEPATHS in locate database
  if [ -w %{_updatedb_conf} ]; then
    sed -i '\@PRUNEPATHS@s@[ ]*'%{_localstatedir}/lib/%{name}'@@' %{_updatedb_conf} || :
  fi
fi

%systemd_postun_with_restart backuppc.service


%files
%doc README.md README.setup README.RHEL ChangeLog doc/*
%license LICENSE
%dir %attr(-,backuppc,backuppc) %{_localstatedir}/log/%{name} 
%dir %attr(-,backuppc,apache) %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %attr(-,backuppc,apache) %{_sysconfdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/sbin
%{_datadir}/%{name}/[^s]*
%attr(750,backuppc,apache) %{_datadir}/%{name}/sbin/BackupPC_Admin

%if 0%{?_with_tmpfilesd}
%{_tmpfilesdir}/%{name}.conf
%else
%dir %attr(0775,root,backuppc) %{_localstatedir}/run/%{name} 
%endif

%if 0%{?_with_systemd}
%{_unitdir}/backuppc.service
%else
%attr(0755,root,root) %{_initrddir}/backuppc
%endif

%attr(4750,backuppc,apache) %{_libexecdir}/%{name}/BackupPC_Admin
%attr(-,backuppc,root) %{_localstatedir}/lib/%{name}/
%{_datadir}/selinux/packages/%{name}/%{name}.pp
%{_sysusersdir}/backuppc.conf


%changelog
* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.4.0-19
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.4.0-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 25 2024 Orion Poplawski <orion@nwra.com> - 4.4.0-14
- Create and own /etc/BackupPC/pc

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Richard Shaw <hobbes1069@gmail.com> - 4.4.0-8
- Add patch to fix #2091514 where saving a configuration change in the web UI
  would replace {} with () in the config file.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.4.0-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Richard Shaw <hobbes1069@gmail.com> - 4.4.0-1
- Update to 4.4.0.

* Wed Mar 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.3.2-3
- Add perl dependencies needed for build
- Remove duplicities from run-requires

* Thu Mar 12 2020 Richard Shaw <hobbes1069@gmail.com> - 4.3.2-2
- Add patch to allow prevention of backups being deleted.
- Add apache.users config file to control permissions and update related SETUP
  documentation.
- Fix PID file to be created in /run instead of /var/run.

* Tue Feb 18 2020 Richard Shaw <hobbes1069@gmail.com> - 4.3.2-1
- Update to 4.3.2.
- Update SELinux permissions, fixes RHBZ#1791369.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Richard Shaw <hobbes1069@gmail.com> - 4.3.1-3
- Add selinux context for /var/lib/BackupPC to stop AVCs with LOCK files.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Richard Shaw <hobbes1069@gmail.com> - 4.3.1-1
- Update to 4.3.1.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Richard Shaw <hobbes1069@gmail.com> - 4.3.0-1
- Update to 4.3.0.

* Mon Nov 05 2018 Orion Poplawski <orion@nwra.com> - 4.2.1-4
- Add reload support to systemd service file

* Thu Oct 11 2018 Richard Shaw <hobbes1069@gmail.com> - 4.2.1-3
- Revert accidental change to log dir permissions.
- Don't package /run dir when using tmpfiles.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 07 2018 Richard Shaw <hobbes1069@gmail.com> - 4.2.1-1
- Update to 4.2.1.

* Mon Apr  9 2018 Richard Shaw <hobbes1069@gmail.com> - 4.2.0-1
- Update to 4.2.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec  4 2017 Richard Shaw <hobbes1069@gmail.com> - 4.1.5-1
- Update to latest upstream release.

* Sat Nov 25 2017 Richard Shaw <hobbes1069@gmail.com> - 4.1.4-1
- Update to latest upstream release.

* Thu Nov 09 2017 Richard Shaw <hobbes1069@gmail.com> - 4.1.3-4.1
- Add patch to set lib location correctly in BackupPC_zipCreate.pl

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul  4 2017 Richard Shaw <hobbes1069@gmail.com> - 4.1.3-2
- Change requirement from the sendmail package to the sendmail binary
  which is also provided by the default MTA, postfix.

* Sun Jun  4 2017 Richard Shaw <hobbes1069@gmail.com> - 4.1.3-1
- Update to latest upstream release.

* Sun May 28 2017 Richard Shaw <hobbes1069@gmail.com> - 4.1.2-2
- Change permissions on config files to be in the apache group.
- Update systemd service file to start httpd automatically.

* Tue May  2 2017 Richard Shaw <hobbes1069@gmail.com> - 4.1.2-1
- Update to latest upstream release, 4.1.2.

* Thu Mar 30 2017 Richard Shaw <hobbes1069@gmail.com> - 4.1.1-1
- Update to latest upstream release, 4.1.1.

* Sat Mar 25 2017 Richard Shaw <hobbes1069@gmail.com> - 4.1.0-1
- Update to latest upstream release, 4.1.0.

* Thu Mar  9 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.0-1
- Update to latest upstream release, 4.0.0.

* Wed Mar  1 2017 Ville Skyttä <ville.skytta@iki.fi> - 3.3.1-9
- Move tmpfiles.d config to %%{_tmpfilesdir}
- Install LICENSE as %%license

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Benjamin Lefoul <lef@fedoraproject.org> - 3.3.1-7
- Perl unescaped braces (BZ 1259481)

* Tue Oct 18 2016 Benjamin Lefoul <lef@fedoraproject.org> - 3.3.1-6
- Some IPv6 support (BZ 1385630)

* Fri Jul 15 2016 Benjamin Lefoul <lef@fedoraproject.org> - 3.3.1-5
- Deprecation of defined(@array) in perl

* Wed Jun 29 2016 Benjamin Lefoul <lef@fedoraproject.org> - 3.3.1-4
- Support for systemd and tmpfiles for RHEL >= 7

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 14 2015 Bernard Johnson <bjohnson@symetrix.com> - 3.3.1-1
- v 3.3.1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Bernard Johnson <bjohnson@symetrix.com> 3.3.0-2
- fix typo in README.RHEL
- enable PIE build (bz #965523)
- add patch that causes getpwnam to return only uid to fix selinux denials
  (bz #827854)
- add local-fs.target and remote-fs.target to startup dependency (bz #959309)

* Fri Feb 21 2014 Johan Cwiklinski <johan AT x-tnd DOT be> 3.3.0-1
- Last upstream release
- Remove no longer needeed patches
- Fix incorrect-fsf-address to reduce rpmlint output

* Fri Feb 21 2014 Bernard Johnson <bjohnson@symetrix.com> - 3.3.0-1
- v 3.3.0
- fixed typos

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.2.1-14
- Perl 5.18 rebuild

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.2.1-13
- Add build dependency on Pod::Usage (#913855).
- Fix bogus dates in %%changelog.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Bernard Johnson <bjohnson@symetrix.com> 3.2.1-11
- Missing backuppc.service file after upgrade to 3.2.1-10 causes service to
  exit at start (bz #896626)

* Mon Dec 24 2012 Bernard Johnson <bjohnson@symetrix.com> 3.2.1-10
- cleanup build macros for Fedora
- fix deprecated qw messages (partial fix for bz #755076)
- CVE-2011-5081 BackupPC: XSS flaw in RestoreFile.pm
  (bz #795017, #795018, #795019)
- Broken configuration for httpd 2.4 (bz #871353)

* Sun Dec  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.1-9
- Fix FTBFS on F-18+

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 22 2012 Bernard Johnson <bjohnson@symetrix.com> - 3.2.1-7
- change %%{_sharedstatedir} to %%{_localstatedir}/lib as these expand
  differently on EL (bz #767719)
- fix XSS vulnerability (bz #749846, bz #749847, bz #749848) CVE-2011-3361
- additional documentation about enabling correct channels in RHEL to resolve
  all dependencies (bz #749627)
- fix bug with missing tmpfiles.d directory
- add perl(Digest::MD5) to list of build and install dependencies

* Wed Sep 21 2011 Bernard Johnson <bjohnson@symetrix.com> - 3.2.1-6
- fix postun scriptlet error (bz #736946)
- make postun scriptlet more coherent
- change selinux context on log files to httpd_log_t and allow access
  to them (bz #730704)

* Fri Aug 12 2011 Bernard Johnson <bjohnson@symetrix.com> - 3.2.1-4
- change macro conditionals to include tmpfiles.d support starting at
  Fedora 15 (bz #730053)
- change install lines to preserve timestamps

* Fri Jul 08 2011 Bernard Johnson <bjohnson@symetrix.com> - 3.2.1-1
- v 3.2.1
- add lower case script URL alias for typing impaired
- cleanup selinux macros
- spec cleanup
- make samba dependency on actual files required to EL5 can use samba-client
  or samba3x-client (bz #667479)
- unbundle perl(Net::FTP::AutoReconnect) and perl(Net::FTP::RetrHandle)
- remove old patch that is no longer needed
- attempt to make sure $Conf{TopDir} is listed in updatedb PRUNEPATHS,
  otherwise at least generate a warning on statup (bz #554491)
- move sockets to /var/run (bz #719499)
- add support for systemd starting at F16 (bz #699441)
- patch to move pid dir under /var/run
- unbundle Net::FTP::*
- add support for tmpfiles.d

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 02 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-16
- perl-suidperl is no longer available (fix bug #611009)

* Fri Jul 09 2010 Mike McGrath <mmcgrath@redhat.com> 3.1.0-14.1
- Rebuilding to fix perl-suidperl broken dep

* Mon May 17 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-14
- Fix for bug #592762

* Sun Feb 28 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-12
- Add "::1" to the apache config file for default allowed adresses
- Fix a typo in the apache config file

* Sun Jan 17 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-11
- Really fix selinux labelling backup directory (bug #525948)

* Fri Jan 15 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-10
- Fix selinux labelling backup directory (bug #525948)

* Fri Sep 25 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-9
- Fix security bug (bug #518412)

* Wed Sep 23 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-8
- Rebuild with latest SELinux policy (bug #524630)

* Fri Sep 18 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-7
- Fix SELinux policy module for UserEmailInfo.pl file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-5
- Fix TopDir change (bug #473944)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-3
- using /dev/null with SELinux policy to avoid broken pipe errors (bug #432149)

* Sat Apr 05 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-2
- correcting nologin path

* Thu Nov 29 2007 Johan Cwiklinski <johan AT x-tnd DOT be> 3.1.0-1
- New upstream version
- Added samba-client as a dependency
- Added readme.fedora
- Changed CGI admin path in default config file

* Fri Sep 21 2007 Johan Cwiklinski <johan AT x-tnd DOT be> 3.0.0-3
- Fixed SELinux policy module

* Wed Sep 12 2007 Johan Cwiklinski <johan AT x-tnd DOT be> 3.0.0-2
- Added SELinux policy module

* Tue Jan 30 2007 Johan Cwiklinski <johan AT x-tnd DOT be> 3.0.0-1
- Rebuild RPM for v 3.0.0

* Sat Aug 26 2006 Mike McGrath <imlinux@gmail.com> 2.1.2-7
- Release bump for rebuild

* Tue Jul 25 2006 Mike McGrath <imlinux@gmail.com> 2.1.2-6
- One more config change

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 2.1.2-5
- Added upstream patch for better support for rsync

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 2.1.2-4
- Properly marking config files as such

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 2.1.2-3
- Changes to defaults in config.pl
- Added Requires: rsync

* Fri Jul 21 2006 Mike McGrath <imlinux@gmail.com> 2.1.2-2
- Added requires: perl(File::RsyncP)

* Tue Jul 18 2006 Mike McGrath <imlinux@gmail.com> 2.1.2-1
- Initial Fedora Packaging
