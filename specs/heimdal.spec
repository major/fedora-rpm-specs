%global _hardened_build 1
%global prefix %{_libdir}/%{name}
%global exec_prefix %{_exec_prefix}/lib/%{name}

Name: heimdal
Version: 7.8.0
Release: %autorelease
Summary: A Kerberos 5 implementation without export restrictions
# Tracked at https://github.com/abstrm/heimdal/blob/heimdal-7.8.0-spdx/doc/copyright.texi
License: BSD-2-Clause AND BSD-3-Clause AND HPND-export-US AND HPND-export2-US AND LicenseRef-Fedora-Public-Domain
URL: http://www.heimdal.software/heimdal
Source0:  https://github.com/%{name}/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source3:  %{name}.sysconfig
Source4:  %{name}.sh
Source5:  %{name}.csh
Source9:  krb5.conf.sample
Source10: %{name}.logrotate
Source11: %{name}-bashrc
Source25: %{name}-kdc.conf
Source26: %{name}-kdc.service
Source27: %{name}-ipropd-master.service
Source28: %{name}-ipropd-slave.service
Source29: %{name}-kadmind.service
Source30: %{name}-kpasswdd.service
Source31: %{name}-ipropd-slave-wrapper

# klist, kswitch, and kvno are symlinks to "heimtools", and this utility needs
# to know how to interpret the "heimdal-" prefixes.
Patch1: heimdal-1.6.0-c25f45a-rename-commands.patch
Patch4: heimdal-7.7.0-configure.patch
Patch5: heimdal-7.7.0-58c8ad96-py3.patch
Patch6: heimdal-configure-c99.patch
Patch7: heimdal-7.8.0-1b57b62d-ac272.patch
Patch8: heimdal-7.8.0-e93a1357-slapdtest.patch

BuildRequires:  gettext
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libedit-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
#Required for tests/ldap
%if (0%{?rhel})
# but not available on RHEL 8
%else
BuildRequires:  openldap-servers
%endif
BuildRequires:  pam-devel
BuildRequires:  perl(JSON)
BuildRequires:  sqlite-devel
BuildRequires:  texinfo
BuildRequires:  libcom_err-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libdb-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  python3
BuildRequires:  groff-base
BuildRequires: systemd-units
BuildRequires: make
BuildRequires: libxcrypt-devel

# Bundled libtommath (https://bugzilla.redhat.com/1118462)
Provides: bundled(libtommath) = 0.42.0

%description
Kerberos 5 is a network authentication and single sign-on system.
Heimdal is a free Kerberos 5 implementation without export restrictions
written from the spec (rfc1510 and successors) including advanced features
like thread safety, IPv6, master-slave replication of Kerberos Key
Distribution Center server and support for ticket delegation (S4U2Self,
S4U2Proxy).
This package can coexist with MIT Kerberos 5 packages. Hesiod is disabled
by default since it is deemed too big a security risk by the packager.

%package    workstation
Summary:    Heimdal kerberos programs for use on workstations

%description workstation
This package contains Heimdal Kerberos 5 programs and utilities for
use on workstations (kinit, klist, kdestroy, kpasswd)

%package server
Summary:  Heimdal kerberos server
Requires: logrotate
Requires(preun): systemd
Requires(postun): systemd
Requires(post): systemd
Provides: heimdal-kdc = %{version}-%{release}
Obsoletes: heimdal-kdc < 1.5

%description server
This package contains the master Heimdal kerberos Key Distribution
Center (KDC), admin interface server (admind) and master-slave
synchronisation daemons. Install this package if you intend to
set up Kerberos server.

%package libs
Summary: Heimdal kerberos shared libraries
Requires(post): info
Requires(preun): info

%description libs
This package contains shared libraries required by several of the other
Heimdal packages.

%package devel
Summary:  Header and other development files for Heimdal kerberos

%description devel
Contains files needed to compile and link software using the Heimdal
kerberos headers/libraries.

%package static
Summary:  Static libraries for Heimdal kerberos
Requires: %{name}-devel = %{version}-%{release}

%description static
Contains files needed to statically link software using the Heimdal
kerberos headers/libraries.

%package path
Summary: Heimdal kerberos PATH manipulation
Requires: %{name}-libs
# For /etc/profile.d
Requires: setup

%description path
This package prepends the Heimdal binary directory to the beginning of
PATH.

%prep
%setup -q
%patch -P1 -p1 -b .cmds
%patch -P4 -p1 -b .config
%patch -P5 -p1 -b .2to3
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1

for f in lib/*/*.py; do
    sed -i "$f" -re 's,^#!/usr/(local/|)bin/python,#!/usr/bin/python3,'
done

# FIXME check-slapd fails
for f in tests/Makefile.{in,am}; do sed -i $f -re 's, ldap , ,'; done

./autogen.sh

%build
%ifarch i386
%global build_fix "-march=i686"
%else
%global build_fix ""
%endif
autoreconf -ivf
%configure \
        --prefix=%{_prefix} \
        --includedir=%{_includedir}/%{name} \
        --libdir=%{prefix}/lib \
        --enable-static \
        --enable-shared \
        --enable-pthread-support \
        --without-x \
        --without-hesiod \
        --with-ipv6 \
        --enable-kcm \
        --enable-pk-init \
        --with-openldap=%{_prefix} \
        --with-sqlite3=%{_prefix} \
        --with-libedit=%{_prefix} \
        LIBS="-ltermcap" \
        CFLAGS="-fPIC %{optflags} %{build_fix}"
%make_build -C include krb5-types.h
%make_build
%make_build -C doc html

# po/localefiles is not in the tarball, which causes install to fail
touch po/localefiles
%make_build -C po mo

%check
%make_build -j1 check

%install
%make_install
# install the init files
# install systemd service files
mkdir -p %{buildroot}%{_unitdir}
pushd %{buildroot}%{_unitdir}
  install -p -D -m 644 %{SOURCE26} heimdal-kdc.service
  install -p -D -m 644 %{SOURCE27} heimdal-ipropd-master.service
  install -p -D -m 644 %{SOURCE28} heimdal-ipropd-slave.service
  install -p -D -m 644 %{SOURCE29} heimdal-kadmind.service
  install -p -D -m 644 %{SOURCE30} heimdal-kpasswdd.service
popd
install -p -D -m 755 %{SOURCE31} %{buildroot}%{_libexecdir}/ipropd-slave-wrapper
install -p -D -m 644 %{SOURCE3}  %{buildroot}%{_sysconfdir}/sysconfig/heimdal
install -p -D -m 644 %{SOURCE4}  %{buildroot}%{_sysconfdir}/profile.d/heimdal.sh
install -p -D -m 644 %{SOURCE5}  %{buildroot}%{_sysconfdir}/profile.d/heimdal.csh
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/logrotate.d/heimdal
mkdir -p %{buildroot}%{_localstatedir}/heimdal/
install -p -D -m 755 %{SOURCE25}  %{buildroot}%{_sysconfdir}/heimdal-kdc.conf
ln -s %{_sysconfdir}/heimdal-kdc.conf %{buildroot}%{_localstatedir}/heimdal/kdc.conf
echo "# see man heimdal-kadmind(8)" > %{buildroot}%{_sysconfdir}/heimdal-kadmind.acl
ln -s %{_sysconfdir}/heimdal-kadmind.acl %{buildroot}%{_localstatedir}/heimdal/kadmind.acl
touch    %{buildroot}%{_sysconfdir}/heimdal-slaves
ln -s %{_sysconfdir}/heimdal-slaves %{buildroot}%{_localstatedir}/heimdal/slaves
install -d -m 700 %{buildroot}%{_localstatedir}/log/heimdal
install -d -m 755 %{buildroot}/%{_pkgdocdir}
install -p -D -m 644 LICENSE    %{buildroot}/%{_pkgdocdir}/LICENSE
install -p -D -m 644 %{SOURCE9} %{buildroot}/%{_pkgdocdir}/krb5.conf.sample
install -p -D -m 644 %{SOURCE11} %{buildroot}/%{_pkgdocdir}/bashrc
rm -rf %{buildroot}%{_infodir}/dir
# NOTICE: no support for X11
rm -f %{buildroot}%{_mandir}/man1/kx.1*
rm -f %{buildroot}%{_mandir}/man1/rxtelnet.1*
rm -f %{buildroot}%{_mandir}/man1/rxterm.1*
rm -f %{buildroot}%{_mandir}/man1/tenletxr.1*
rm -f %{buildroot}%{_mandir}/man1/xnlock.1*
rm -f %{buildroot}%{_mandir}/man8/kxd.8*
# Remove CAT files, they are not needed
rm -rf %{buildroot}%{_mandir}/cat*
# Remove libtool archives
find %{buildroot} -type f -name '*.la' -exec rm -f {} ';'

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
cat >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf << EOF
%{prefix}/lib
EOF

mkdir -p %{buildroot}%{exec_prefix}/bin
mkdir -p %{buildroot}%{_mandir}/%{name}/man{1,5,8}

# rename clashes with other pkgs from <app> to heimdal-<app>
for prog in kadmin kadmind kdestroy kinit klist kpasswd krb5-config ktutil su pagsh compile_et
do
   if [ -e %{buildroot}%{_bindir}/${prog} ]; then
     mv %{buildroot}%{_bindir}/{,%{name}-}${prog}
     ln -s %{_bindir}/%{name}-${prog} %{buildroot}%{exec_prefix}/bin/${prog}
   elif [ -e %{buildroot}%{_sbindir}/${prog} ]; then
     mv %{buildroot}%{_sbindir}/{,%{name}-}${prog}
     ln -s %{_sbindir}/%{name}-${prog} %{buildroot}%{exec_prefix}/bin/${prog}
   elif [ -e %{buildroot}%{_libexecdir}/${prog} ]; then
     mv %{buildroot}%{_libexecdir}/{,%{name}-}${prog}
   fi

   if [ -e %{buildroot}%{_mandir}/man1/${prog}.1 ]; then
     mv %{buildroot}%{_mandir}/man1/{,%{name}-}${prog}.1
   elif [ -e %{buildroot}%{_mandir}/man8/${prog}.8 ]; then
     mv %{buildroot}%{_mandir}/man8/{,%{name}-}${prog}.8
   fi
done

# If we have the prefixed name in one pkg we want it in all.
mv %{buildroot}%{_bindir}/{,%{name}-}kswitch
ln -s %{_bindir}/%{name}-kswitch %{buildroot}%{exec_prefix}/bin/kswitch
mv %{buildroot}%{_mandir}/man1/{,%{name}-}kswitch.1

ln -s %{name}-kinit %{buildroot}%{_bindir}/kauth

mv %{buildroot}%{_mandir}/man5/{,%{name}-}krb5.conf.5

rm %{buildroot}%{_mandir}/man5/qop.5
ln -s mech.5.gz %{buildroot}%{_mandir}/man5/qop.5.gz

sha256sum %{buildroot}%{_mandir}/man3/*.3 | sort >man3hash
firsthash="X"; firstname="X"
while read hash path; do
    name="${path##*/}"
    if [ "$hash" != "$firsthash" ]; then
        firsthash="$hash"
        firstname="${path##*/}"
    else
        rm "$path"
        ln -s "$firstname".gz "$path".gz
    fi
done <man3hash
rm man3hash

%find_lang %{name} --all-name

%post server
%systemd_post heimdal-kdc.service
%systemd_post heimdal-ipropd-master.service
%systemd_post heimdal-ipropd-slave.service
%systemd_post heimdal-kadmind.service
%systemd_post heimdal-kpasswdd.service

%preun server
%systemd_preun heimdal-kdc.service
%systemd_preun heimdal-ipropd-master.service
%systemd_preun heimdal-ipropd-slave.service
%systemd_preun heimdal-kadmind.service
%systemd_preun heimdal-kpasswdd.service

%postun server
%systemd_postun_with_restart heimdal-kdc.service
%systemd_postun_with_restart heimdal-ipropd-master.service
%systemd_postun_with_restart heimdal-ipropd-slave.service
%systemd_postun_with_restart heimdal-kadmind.service
%systemd_postun_with_restart heimdal-kpasswdd.service

%files libs -f %{name}.lang
%dir %{exec_prefix}
%dir %{exec_prefix}/bin
%dir %{prefix}
%dir %{prefix}/lib
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%{prefix}/lib/lib*.so.*
%{prefix}/lib/windc.so.*
%{_infodir}/heimdal.info*
%{_infodir}/hx509.info*
%{_mandir}/man5/%{name}-krb5.conf.5*
%{_mandir}/man5/qop.5*
%{_mandir}/man5/mech.5*
%{_mandir}/man8/kerberos.8*
%{_prefix}/bin/string2key
%{_mandir}/man8/string2key.8*
%{_libexecdir}/kdigest
%{_mandir}/man8/kdigest.8*
%{_prefix}/bin/verify_krb5_conf
%{_mandir}/man8/verify_krb5_conf.8*
%{_libexecdir}/digest-service
%doc %{_pkgdocdir}
%license LICENSE

%files server
%{_unitdir}/*.service
%{_sysconfdir}/logrotate.d/heimdal
%config(noreplace) %{_sysconfdir}/sysconfig/heimdal
%dir %attr(700,root,root) %{_localstatedir}/heimdal
%dir %attr(700,root,root) %{_localstatedir}/log/heimdal
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/heimdal-kdc.conf
%config(noreplace) %{_localstatedir}/heimdal/kdc.conf
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/heimdal-kadmind.acl
%config(noreplace) %{_localstatedir}/heimdal/kadmind.acl
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/heimdal-slaves
%config(noreplace) %{_localstatedir}/heimdal/slaves
%{_libexecdir}/hprop
%{_mandir}/man8/hprop.8*
%{_libexecdir}/hpropd
%{_mandir}/man8/hpropd.8*
%{_mandir}/man8/iprop.8*
%{_sbindir}/iprop-log
%{_mandir}/man8/iprop-log.8*
%{_libexecdir}/ipropd-master
%{_mandir}/man8/ipropd-master.8*
%{_libexecdir}/ipropd-slave
%{_mandir}/man8/ipropd-slave.8*
%{_libexecdir}/ipropd-slave-wrapper
%{_libexecdir}/%{name}-kadmind
%{_mandir}/man8/%{name}-kadmind.8*
%{_libexecdir}/kdc
%{_mandir}/man8/kdc.8*
%{_libexecdir}/kpasswdd
%{_mandir}/man8/kpasswdd.8*
%{_sbindir}/kstash
%{_mandir}/man8/kstash.8*

%files workstation
%{_prefix}/bin/afslog
%{_mandir}/man1/afslog.1*
%{_prefix}/bin/bsearch
%{_mandir}/man1/bsearch.1*
%{_prefix}/bin/%{name}-pagsh
%{exec_prefix}/bin/pagsh
%{_mandir}/man1/%{name}-pagsh.1*
%{_prefix}/bin/gsstool
%{_prefix}/bin/heimtools
%{_prefix}/bin/hxtool
%{_prefix}/bin/idn-lookup
%{_prefix}/bin/%{name}-kdestroy
%{exec_prefix}/bin/kdestroy
%{_mandir}/man1/%{name}-kdestroy.1*
%{_prefix}/bin/kf
%{_mandir}/man1/kf.1*
%{_prefix}/bin/kgetcred
%{_mandir}/man1/kgetcred.1*
%{_libexecdir}/kimpersonate
%{_mandir}/man8/kimpersonate.8*
%{_prefix}/bin/%{name}-kinit
%{exec_prefix}/bin/kinit
%{_prefix}/bin/kauth
%{_mandir}/man1/%{name}-kinit.1*
%{_prefix}/bin/%{name}-klist
%{exec_prefix}/bin/klist
%{_mandir}/man1/%{name}-klist.1*
%{_prefix}/bin/%{name}-kpasswd
%{exec_prefix}/bin/kpasswd
%{_mandir}/man1/%{name}-kpasswd.1*
%{_prefix}/bin/heimdal-kswitch
%{exec_prefix}/bin/kswitch
%{_mandir}/man1/heimdal-kswitch.1*
%{_prefix}/bin/otp
%{_mandir}/man1/otp.1*
%{_prefix}/bin/otpprint
%{_mandir}/man1/otpprint.1*
%{_bindir}/%{name}-kadmin
%{exec_prefix}/bin/kadmin
%{_mandir}/man1/%{name}-kadmin.1*
%{_libexecdir}/kcm
%{_mandir}/man8/kcm.8*
%{_libexecdir}/kfd
%{_mandir}/man8/kfd.8*
%{_bindir}/%{name}-ktutil
%{exec_prefix}/bin/ktutil
%{_mandir}/man1/%{name}-ktutil.1*
# NOTICE: no support for X11
#%%{_libexecdir}/kxd
#%%{_mandir}/man8/kxd.8*
#%%{_mandir}/cat8/kxd.8*
%attr(04550,root,root) %{_prefix}/bin/%{name}-su
%{exec_prefix}/bin/su
%{_mandir}/man1/%{name}-su.1*

%files devel
%dir %{_libexecdir}/%{name}
%{_bindir}/%{name}-krb5-config
%{exec_prefix}/bin/krb5-config
%{_mandir}/man1/%{name}-krb5-config.1*
%{_includedir}/*
%{prefix}/lib/lib*.so
%{prefix}/lib/windc.so
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_libexecdir}/%{name}/asn1_compile
%{_libexecdir}/%{name}/asn1_print
%{_libexecdir}/%{name}/slc
%{prefix}/lib/pkgconfig/*.pc

%files static
%{prefix}/lib/lib*.a
%{prefix}/lib/windc.a

%files path
%{_sysconfdir}/profile.d/%{name}.sh
%{_sysconfdir}/profile.d/%{name}.csh

%changelog
%autochangelog
