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
Release: %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
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
Patch12: uucp-configure-c99.patch
# Fix FTBFS due to incompatible types
Patch13: uucp-1.07-fix-types.patch

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
%patch -P0 -p1 -b .config
%patch -P3 -p1 -b .sigfpe
%patch -P6 -p1 -b .lockdev
%patch -P8 -p1 -b .pipe
%patch -P9 -p1 -b .lfs
%patch -P10 -p1 -b .sigfpe2
%patch -P11 -p1 -b .format
%patch -P12 -p1 -b .configure-c99
%patch -P13 -p1 -b .fix-types

# Create a sysusers.d config file
cat >uucp.sysusers.conf <<EOF
g uucp 14
u uucp 10 'Uucp user' /var/spool/uucp -
EOF

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

install -m0644 -D uucp.sysusers.conf %{buildroot}%{_sysusersdir}/uucp.conf

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
%{_sysusersdir}/uucp.conf

%files -n cu
%doc README COPYING ChangeLog NEWS TODO
%attr(6555,uucp,uucp) %{_bindir}/cu
%{_mandir}/man1/cu.1*

%changelog
%autochangelog
