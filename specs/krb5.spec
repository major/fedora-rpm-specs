# Set this so that find-lang.sh will recognize the .po files.
%global gettext_domain mit-krb5
# Guess where the -libs subpackage's docs are going to go.
%define libsdocdir %{?_pkgdocdir:%(echo %{_pkgdocdir} | sed -e s,krb5,krb5-libs,g)}%{!?_pkgdocdir:%{_docdir}/%{name}-libs-%{version}}
# Figure out where the default ccache lives and how we set it.
%global configure_default_ccache_name 1
%global configured_default_ccache_name KEYRING:persistent:%%{uid}

%global krb5_release %{autorelease}

# This should be e.g. beta1 or %%nil
%global pre_release %nil
%if "x%{?pre_release}" != "x"
%global krb5_release %autorelease -p -e %pre_release
# Use for tarball
%global krb5_pre_release -%{pre_release}
%endif

%global krb5_version_major 1
%global krb5_version_minor 22
# For a release without a patch number set to %%nil
%global krb5_version_patch 2

%global krb5_version_major_minor %{krb5_version_major}.%{krb5_version_minor}
%global krb5_version %{krb5_version_major_minor}
%if "x%{?krb5_version_patch}" != "x"
%global krb5_version %{krb5_version_major_minor}.%{krb5_version_patch}
%endif

# Should be in form 5.0, 6.1, etc.
%global kdbversion 9.0

Summary: The Kerberos network authentication system
Name: krb5
Version: %{krb5_version}
Release: %{krb5_release}

# rharwood has trust path to signing key and verifies on check-in
Source0: https://web.mit.edu/kerberos/dist/krb5/%{krb5_version_major_minor}/krb5-%{krb5_version}%{?krb5_pre_release}.tar.gz
Source1: https://web.mit.edu/kerberos/dist/krb5/%{krb5_version_major_minor}/krb5-%{krb5_version}%{?krb5_pre_release}.tar.gz.asc

Source2: kprop.service
Source3: kadmin.service
Source4: krb5kdc.service
Source5: krb5.conf
Source6: kdc.conf
Source7: kadm5.acl
Source8: krb5kdc.sysconfig
Source9: kadmin.sysconfig
Source10: kprop.sysconfig
Source11: ksu.pamd
Source12: krb5kdc.logrotate
Source13: kadmind.logrotate
Source14: krb5-krb5kdc.conf
Source15: %{name}-tests

# FIXME Backport bug fixes to https://<url>/<repo>/<branch>
# This will give us CI and makes it easy to generate patchsets.
#
# Generate the patchset using:
#   git format-patch -l1 --stdout -N > krb5-1.22-redhat.patch
# Where N is the number of patches
Patch0:        krb5-1.22-redhat.patch

License: Brian-Gladman-2-Clause AND BSD-2-Clause AND (BSD-2-Clause OR GPL-2.0-or-later) AND BSD-2-Clause-first-lines AND BSD-3-Clause AND BSD-4-Clause AND CMU-Mach-nodoc AND FSFULLRWD AND HPND AND HPND-export2-US AND HPND-export-US AND HPND-export-US-acknowledgement AND HPND-export-US-modify AND ISC AND MIT AND MIT-CMU AND OLDAP-2.8 AND OpenVision
URL: https://web.mit.edu/kerberos/www/
BuildRequires: autoconf, bison, make, flex, gawk, gettext, pkgconfig, sed
BuildRequires: gcc, gcc-c++
BuildRequires: libcom_err-devel, libedit-devel, libss-devel
BuildRequires: gzip, ncurses-devel
BuildRequires: python3, python3-sphinx
BuildRequires: keyutils, keyutils-libs-devel >= 1.5.8
BuildRequires: libselinux-devel
BuildRequires: pam-devel
BuildRequires: systemd-units
BuildRequires: tcl-devel
BuildRequires: libverto-devel
BuildRequires: openldap-devel
BuildRequires: lmdb-devel
BuildRequires: perl-interpreter
BuildRequires: openssl-devel >= 1:3.0.0

# For autosetup
BuildRequires: git

# Enable compilation of optional tests
BuildRequires: resolv_wrapper
BuildRequires: libcmocka-devel
BuildRequires: opensc
BuildRequires: softhsm

%description
Kerberos V5 is a trusted-third-party network authentication system,
which can improve your network's security by eliminating the insecure
practice of sending passwords over the network in unencrypted form.

%package devel
Summary: Development files needed to compile Kerberos 5 programs
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libkadm5%{?_isa} = %{version}-%{release}
Requires: libcom_err-devel
Requires: keyutils-libs-devel, libselinux-devel
Requires: libverto-devel
Provides: krb5-kdb-devel-version = %{kdbversion}
# IPA wants ^ to be a separate symbol because they don't trust package
# managers to match -server and -devel in version.  Just go with it.

%description devel
Kerberos is a network authentication system. The krb5-devel package
contains the header files and libraries needed for compiling Kerberos
5 programs. If you want to develop Kerberos-aware programs, you need
to install this package.

%package libs
Summary: The non-admin shared libraries used by Kerberos 5
%if 0%{?fedora} > 35 || 0%{?rhel} >= 9
Requires: openssl-libs >= 1:3.0.0
%else
Requires: openssl-libs >= 1:1.1.1d-4
Requires: openssl-libs < 1:3.0.0
%endif
Requires: coreutils
Requires: keyutils-libs >= 1.5.8
Requires: /etc/crypto-policies/back-ends/krb5.config

%description libs
Kerberos is a network authentication system. The krb5-libs package
contains the shared libraries needed by Kerberos 5. If you are using
Kerberos, you need to install this package.

%package server
Summary: The KDC and related programs for Kerberos 5
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-pkinit%{?_isa} = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
# we drop files in its directory, but we don't want to own that directory
Requires: logrotate
# we specify /usr/share/dict/words (provided by words) as the default dict_file in kdc.conf
Requires: words
# for run-time, and for parts of the test suite
BuildRequires: libverto-module-base
Requires: libverto-module-base
Requires: libkadm5%{?_isa} = %{version}-%{release}
Provides: krb5-kdb-version = %{kdbversion}

%description server
Kerberos is a network authentication system. The krb5-server package
contains the programs that must be installed on a Kerberos 5 key
distribution center (KDC).  If you are installing a Kerberos 5 KDC,
you need to install this package (in other words, most people should
NOT install this package).

%package server-ldap
Summary: The LDAP storage plugin for the Kerberos 5 KDC
Requires: %{name}-server%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libkadm5%{?_isa} = %{version}-%{release}

%description server-ldap
Kerberos is a network authentication system. The krb5-server package
contains the programs that must be installed on a Kerberos 5 key
distribution center (KDC).  If you are installing a Kerberos 5 KDC,
and you wish to use a directory server to store the data for your
realm, you need to install this package.

%package workstation
Summary: Kerberos 5 programs for use on workstations
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-pkinit%{?_isa} = %{version}-%{release}
Requires: libkadm5%{?_isa} = %{version}-%{release}

%description workstation
Kerberos is a network authentication system. The krb5-workstation
package contains the basic Kerberos programs (kinit, klist, kdestroy,
kpasswd). If your network uses Kerberos, this package should be
installed on every workstation.

%package pkinit
Summary: The PKINIT module for Kerberos 5
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes: krb5-pkinit-openssl < %{version}-%{release}
Provides: krb5-pkinit-openssl = %{version}-%{release}

%description pkinit
Kerberos is a network authentication system. The krb5-pkinit
package contains the PKINIT plugin, which allows clients
to obtain initial credentials from a KDC using a private key and a
certificate.

%package xrealmauthz
Summary: Xrealmauthz policy module for Kerberos 5 KDC
Group: System Environment/Libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description xrealmauthz
Kerberos is a network authentication system. The krb5-xrealmauthz
package contains the xrealmauthz KDC plugin, which allows to configure
access rules to local realm for client principals from direct or
transitive cross-realms.

%package -n libkadm5
Summary: Kerberos 5 Administrative libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description -n libkadm5
Kerberos is a network authentication system. The libkadm5 package
contains only the libkadm5clnt and libkadm5serv shared objects. This
interface is not considered stable.

%package tests
Summary: Test sources for krb5 build

# Build dependencies
Requires: coreutils, gawk, sed
Requires: gcc-c++
Requires: gettext
Requires: libcom_err-devel
Requires: libselinux-devel
Requires: libss-devel
Requires: libverto-devel
Requires: lmdb-devel
Requires: openldap-devel
Requires: pam-devel
Requires: redhat-rpm-config
%if 0%{?fedora} > 35 || 0%{?rhel} >= 9
Requires: openssl-devel >= 1:3.0.0
%else
Requires: openssl-devel >= 1:1.1.1d-4
Requires: openssl-devel < 1:3.0.0
%endif

# Test dependencies
Requires: dejagnu
Requires: hostname
Requires: iproute
Requires: keyutils, keyutils-libs-devel >= 1.5.8
Requires: libcmocka-devel
Requires: libverto-module-base
Requires: logrotate
Requires: net-tools, rpcbind
Requires: perl-interpreter
Requires: procps-ng
Requires: python3-kdcproxy
Requires: resolv_wrapper
Requires: /etc/crypto-policies/back-ends/krb5.config
Requires: words
Requires: opensc
Requires: softhsm
Recommends: python3-pyrad

# Restore once openldap upstream tests are fixed
#Recommends: openldap-servers
#Recommends: openldap-clients

%description tests
FOR TESTING PURPOSE ONLY
Test sources for krb5 build, with pre-defined compilation parameters

%prep
%autosetup -S git_am -n %{name}-%{version}%{?dashpre}
ln NOTICE LICENSE

# Generate an FDS-compatible LDIF file.
inldif=src/plugins/kdb/ldap/libkdb_ldap/kerberos.ldif
cat > '60kerberos.ldif' << EOF
# This is a variation on kerberos.ldif which 389 Directory Server will like.
dn: cn=schema
EOF
grep -Eiv '(^$|^dn:|^changetype:|^add:)' $inldif >> 60kerberos.ldif
touch -r $inldif 60kerberos.ldif

# Rebuild the configure scripts.
pushd src
autoreconf -fiv
popd

# Mess with some of the default ports that we use for testing, so that multiple
# builds going on the same host don't step on each other.
cfg="src/util/k5test.py"
LONG_BIT=`getconf LONG_BIT`
PORT=`expr 61000 + $LONG_BIT - 48`
sed -i -e s,61000,`expr "$PORT" + 0`,g $cfg
PORT=`expr 1750 + $LONG_BIT - 48`
sed -i -e s,1750,`expr "$PORT" + 0`,g $cfg
sed -i -e s,1751,`expr "$PORT" + 1`,g $cfg
sed -i -e s,1752,`expr "$PORT" + 2`,g $cfg
PORT=`expr 8888 + $LONG_BIT - 48`
sed -i -e s,8888,`expr "$PORT" - 0`,g $cfg
sed -i -e s,8887,`expr "$PORT" - 1`,g $cfg
sed -i -e s,8886,`expr "$PORT" - 2`,g $cfg
PORT=`expr 7777 + $LONG_BIT - 48`
sed -i -e s,7777,`expr "$PORT" + 0`,g $cfg
sed -i -e s,7778,`expr "$PORT" + 1`,g $cfg

# Fix kadmind port hard-coded in tests
PORT=`expr 61000 + $LONG_BIT - 48`
sed -i -e \
    "s,params.kadmind_port = 61001;,params.kadmind_port = $((PORT + 1));," \
    src/lib/kadm5/t_kadm5.c


%build
# Go ahead and supply tcl info, because configure doesn't know how to find it.
source %{_libdir}/tclConfig.sh
pushd src

# This should be safe to remove once we have autoconf >= 2.70
export runstatedir=/run

# Work out the CFLAGS and CPPFLAGS which we intend to use.
INCLUDES=-I%{_includedir}/et
CFLAGS="`echo $RPM_OPT_FLAGS $DEFINES $INCLUDES -fPIC -fno-strict-aliasing -fstack-protector-all`"
CPPFLAGS="`echo $DEFINES $INCLUDES`"
%configure \
    CC="%{__cc}" \
    CFLAGS="$CFLAGS" \
    CPPFLAGS="$CPPFLAGS" \
    SS_LIB="-lss" \
    PKCS11_MODNAME="p11-kit-proxy.so" \
    --enable-shared \
    --runstatedir=/run \
    --localstatedir=%{_var}/kerberos \
    --disable-rpath \
    --without-krb5-config \
    --with-system-et \
    --with-system-ss \
    --enable-dns-for-realm \
    --with-ldap \
    --enable-pkinit \
    --with-crypto-impl=openssl \
    --with-tls-impl=openssl \
    --with-system-verto \
    --with-pam \
    --with-selinux \
    --with-lmdb \
    || (cat config.log; exit 1)

# Check we have required features enabled
for x in DNS_LOOKUP DNS_LOOKUP_REALM; do
    grep -q "#define KRB5_${x} 1" include/autoconf.h
done

# Sanity check the KDC_RUN_DIR.
pushd include
%make_build osconf.h
popd
configured_dir=`grep KDC_RUN_DIR include/osconf.h | awk '{print $NF}'`
configured_dir=`eval echo $configured_dir`
if test "$configured_dir" != /run/krb5kdc ; then
    echo Failed to configure KDC_RUN_DIR.
    exit 1
fi

%make_build
popd

# Build the docs.
make -C src/doc paths.py version.py
cp src/doc/paths.py doc/
install -d -m 0755 build-man build-html
sphinx-build -a -b man   -t pathsubs doc build-man
sphinx-build -a -b html  -t pathsubs doc build-html
rm -fr build-html/_sources

%install
# Sample KDC config files (bundled kdc.conf and kadm5.acl).
install -d -m 0755 %{buildroot}%{_var}/kerberos/krb5kdc
install -pm 600 %{SOURCE6} %{buildroot}%{_var}/kerberos/krb5kdc/
install -pm 600 %{SOURCE7} %{buildroot}%{_var}/kerberos/krb5kdc/

# Where per-user keytabs live by default.
install -d -m 0755 %{buildroot}%{_var}/kerberos/krb5/user

# Default configuration file for everything.
install -d -m 0755 %{buildroot}%{_sysconfdir}
install -pm 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/krb5.conf

# Default include on this directory
install -d -m 0755 %{buildroot}%{_sysconfdir}/krb5.conf.d
ln -sv %{_sysconfdir}/crypto-policies/back-ends/krb5.config %{buildroot}%{_sysconfdir}/krb5.conf.d/crypto-policies

# Parent of configuration file for list of loadable GSS mechs ("mechs").  This
# location is not relative to sysconfdir, but is hard-coded in g_initialize.c.
mkdir -m 755 -p %{buildroot}%{_sysconfdir}/gss
# Parent of groups of configuration files for a list of loadable GSS mechs
# ("mechs").  This location is not relative to sysconfdir, and is also
# hard-coded in g_initialize.c.
mkdir -m 755 -p %{buildroot}%{_sysconfdir}/gss/mech.d

# If the default configuration needs to start specifying a default cache
# location, add it now, then fixup the timestamp so that it looks the same.
%if 0%{?configure_default_ccache_name}
export DEFCCNAME="%{configured_default_ccache_name}"
awk '{print}
     /^#    default_realm/{print "    default_ccache_name =", ENVIRON["DEFCCNAME"]}' \
     %{SOURCE5} > %{buildroot}%{_sysconfdir}/krb5.conf
touch -r %{SOURCE5} %{buildroot}%{_sysconfdir}/krb5.conf
grep default_ccache_name %{buildroot}%{_sysconfdir}/krb5.conf
%endif

# Server init scripts (krb5kdc,kadmind,kpropd) and their sysconfig files.
install -d -m 0755 %{buildroot}%{_unitdir}
for unit in \
    %{SOURCE4}\
     %{SOURCE3} \
     %{SOURCE2} ; do
    # In the past, the init script was supposed to be named after the service
    # that the started daemon provided.  Changing their names is an
    # upgrade-time problem I'm in no hurry to deal with.
    install -pm 644 ${unit} %{buildroot}%{_unitdir}
done
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
install -pm 644 %{SOURCE14} %{buildroot}/%{_tmpfilesdir}/
install -d -m 0755 %{buildroot}/%{_localstatedir}/run/krb5kdc

install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
for sysconfig in %{SOURCE8} %{SOURCE9} %{SOURCE10} ; do
    install -pm 644 ${sysconfig} \
            %{buildroot}%{_sysconfdir}/sysconfig/`basename ${sysconfig} .sysconfig`
done

# logrotate configuration files
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d/
for logrotate in \
    %{SOURCE12} \
     %{SOURCE13} ; do
    install -pm 644 ${logrotate} \
            %{buildroot}%{_sysconfdir}/logrotate.d/`basename ${logrotate} .logrotate`
done

# PAM configuration files.
install -d -m 0755 %{buildroot}%{_sysconfdir}/pam.d/
for pam in %{SOURCE11} ; do
    install -pm 644 ${pam} \
            %{buildroot}%{_sysconfdir}/pam.d/`basename ${pam} .pamd`
done

# Plug-in directories.
install -pdm 755 %{buildroot}/%{_libdir}/krb5/plugins/preauth
install -pdm 755 %{buildroot}/%{_libdir}/krb5/plugins/kdb
install -pdm 755 %{buildroot}/%{_libdir}/krb5/plugins/authdata

# The rest of the binaries, headers, libraries, and docs.
%make_install -C src EXAMPLEDIR=%{libsdocdir}/examples

# Munge krb5-config yet again.  This is totally wrong for 64-bit, but chunks
# of the buildconf patch already conspire to strip out /usr/<anything> from the
# list of link flags, and it helps prevent file conflicts on multilib systems.
sed -r -i -e 's|^libdir=/usr/lib(64)?$|libdir=/usr/lib|g' %{buildroot}%{_bindir}/krb5-config

# Workaround krb5-config reading too much from LDFLAGS.
# https://bugzilla.redhat.com/show_bug.cgi?id=1997021
# https://bugzilla.redhat.com/show_bug.cgi?id=2048909
sed -i -r -e 's/^(LDFLAGS=).*/\1/' %{buildroot}%{_bindir}/krb5-config

# Install processed man pages.
for section in 1 5 8 ; do
    install -m 644 build-man/*.${section} \
            %{buildroot}/%{_mandir}/man${section}/
done

# I'm tired of warnings about these not having man pages
rm -- "%{buildroot}/%{_sbindir}/krb5-send-pr"
rm -- "%{buildroot}/%{_sbindir}/sim_server"
rm -- "%{buildroot}/%{_sbindir}/gss-server"
rm -- "%{buildroot}/%{_sbindir}/uuserver"
rm -- "%{buildroot}/%{_bindir}/sim_client"
rm -- "%{buildroot}/%{_bindir}/gss-client"
rm -- "%{buildroot}/%{_bindir}/uuclient"

# These files are already packaged elsewhere
rm -- "%{buildroot}/%{_docdir}/krb5-libs/examples/kdc.conf"
rm -- "%{buildroot}/%{_docdir}/krb5-libs/examples/krb5.conf"
rm -- "%{buildroot}/%{_docdir}/krb5-libs/examples/services.append"

# This is only needed for tests
rm -- "%{buildroot}/%{_libdir}/krb5/plugins/preauth/test.so"

# Generate tests launching script
sed -e 's/{{ name }}/%{name}/g' \
    -e 's/{{ version }}/%{krb5_version}/g' \
    -e 's/{{ release }}/%{krb5_release}/g' \
    -e 's/{{ arch }}/%{_arch}/g' \
    -i %{SOURCE15}
install -d -m 0755 %{buildroot}%{_libexecdir}
install -pm 755 %{SOURCE15} %{buildroot}%{_libexecdir}/%{name}-tests-%{_arch}

# Copy source files from build folder to system data folder
install -pdm 755 %{buildroot}%{_datarootdir}/%{name}-tests/%{_arch}
pushd src
cp -p --parents -t "%{buildroot}%{_datarootdir}/%{name}-tests/%{_arch}/" \
    $(find . -type f -exec file -i "{}" + \
          | sed -n \
                -e 's|^\./\([^:]\+\): \+text/.\+$|\1|p' \
                -e 's|^\./\([^:]\+\): \+application/x-pem-file.\+$|\1|p' \
                -e 's|^\./\([^:]\+\): \+application/json.\+$|\1|p' \
          | grep -Ev '~$')
popd

# Copy binary test files
install -pm 644 src/tests/pkinit-certs/*.p12 \
    "%{buildroot}%{_datarootdir}/%{name}-tests/%{_arch}/tests/pkinit-certs/"

# Unset executable bit if no shebang in script
for f in $(find "%{buildroot}%{_datarootdir}/%{name}-tests/%{_arch}/" -type f -executable)
do
    head -n1 "$f" | grep -Eq '^#!' || chmod a-x "$f"
done

%find_lang %{gettext_domain}

%ldconfig_scriptlets libs

%ldconfig_scriptlets server-ldap

%post server
%tmpfiles_create %{_tmpfilesdir}/krb5-krb5kdc.conf
%systemd_post krb5kdc.service kadmin.service kprop.service
# assert sanity.  A cleaner solution probably exists but it is opaque
/bin/systemctl daemon-reload
exit 0

%preun server
%systemd_preun krb5kdc.service kadmin.service kprop.service
exit 0

%postun server
%systemd_postun_with_restart krb5kdc.service kadmin.service kprop.service
exit 0

%ldconfig_scriptlets -n libkadm5

%files workstation
%doc src/config-files/services.append
%doc src/config-files/krb5.conf
%doc build-html/*

# Clients of the KDC, including tools you're likely to need if you're running
# app servers other than those built from this source package.
%{_bindir}/kdestroy
%{_mandir}/man1/kdestroy.1*
%{_bindir}/kinit
%{_mandir}/man1/kinit.1*
%{_bindir}/klist
%{_mandir}/man1/klist.1*
%{_bindir}/kpasswd
%{_mandir}/man1/kpasswd.1*
%{_bindir}/kswitch
%{_mandir}/man1/kswitch.1*

%{_bindir}/kvno
%{_mandir}/man1/kvno.1*
%{_bindir}/kadmin
%{_mandir}/man1/kadmin.1*
%{_bindir}/k5srvutil
%{_mandir}/man1/k5srvutil.1*
%{_bindir}/ktutil
%{_mandir}/man1/ktutil.1*

# Doesn't really fit anywhere else.
%attr(4755,root,root) %{_bindir}/ksu
%{_mandir}/man1/ksu.1*
%config(noreplace) %{_sysconfdir}/pam.d/ksu

%files server
%docdir %{_mandir}
%doc src/config-files/kdc.conf
%{_unitdir}/krb5kdc.service
%{_unitdir}/kadmin.service
%{_unitdir}/kprop.service
%{_tmpfilesdir}/krb5-krb5kdc.conf
%dir %{_localstatedir}/run/krb5kdc
%config(noreplace) %{_sysconfdir}/sysconfig/krb5kdc
%config(noreplace) %{_sysconfdir}/sysconfig/kadmin
%config(noreplace) %{_sysconfdir}/sysconfig/kprop
%config(noreplace) %{_sysconfdir}/logrotate.d/krb5kdc
%config(noreplace) %{_sysconfdir}/logrotate.d/kadmind

%dir %{_var}/kerberos
%dir %{_var}/kerberos/krb5kdc
%config(noreplace) %{_var}/kerberos/krb5kdc/kdc.conf
%config(noreplace) %{_var}/kerberos/krb5kdc/kadm5.acl

%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%dir %{_libdir}/krb5/plugins/preauth
%dir %{_libdir}/krb5/plugins/authdata
%{_libdir}/krb5/plugins/preauth/otp.so
%{_libdir}/krb5/plugins/kdb/db2.so
%{_libdir}/krb5/plugins/kdb/klmdb.so

# KDC binaries and configuration.
%{_mandir}/man5/kadm5.acl.5*
%{_mandir}/man5/kdc.conf.5*
%{_sbindir}/kadmin.local
%{_mandir}/man8/kadmin.local.8*
%{_sbindir}/kadmind
%{_mandir}/man8/kadmind.8*
%{_sbindir}/kdb5_util
%{_mandir}/man8/kdb5_util.8*
%{_sbindir}/kprop
%{_mandir}/man8/kprop.8*
%{_sbindir}/kpropd
%{_mandir}/man8/kpropd.8*
%{_sbindir}/kproplog
%{_mandir}/man8/kproplog.8*
%{_sbindir}/krb5kdc
%{_mandir}/man8/krb5kdc.8*

# This is here for people who want to test their server.  It was formerly also
# included in -devel.
%{_bindir}/sclient
%{_mandir}/man1/sclient.1*
%{_sbindir}/sserver
%{_mandir}/man8/sserver.8*

%files server-ldap
%docdir %{_mandir}
%doc src/plugins/kdb/ldap/libkdb_ldap/kerberos.ldif
%doc src/plugins/kdb/ldap/libkdb_ldap/kerberos.schema
%doc 60kerberos.ldif
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%{_libdir}/krb5/plugins/kdb/kldap.so
%{_libdir}/libkdb_ldap.so
%{_libdir}/libkdb_ldap.so.*
%{_mandir}/man8/kdb5_ldap_util.8.gz
%{_sbindir}/kdb5_ldap_util

%files libs -f %{gettext_domain}.lang
%doc README NOTICE
%{!?_licensedir:%global license %%doc}
%license LICENSE
%docdir %{_mandir}
# These are hard-coded, not-dependent-on-the-configure-script paths.
%dir %{_sysconfdir}/gss
%dir %{_sysconfdir}/gss/mech.d
%dir %{_sysconfdir}/krb5.conf.d
%config(noreplace) %{_sysconfdir}/krb5.conf
%config(noreplace,missingok) %{_sysconfdir}/krb5.conf.d/crypto-policies
%{_mandir}/man5/.k5identity.5*
%{_mandir}/man5/.k5login.5*
%{_mandir}/man5/k5identity.5*
%{_mandir}/man5/k5login.5*
%{_mandir}/man5/krb5.conf.5*
%{_mandir}/man7/kerberos.7*
%{_libdir}/libgssapi_krb5.so.*
%{_libdir}/libgssrpc.so.*
%{_libdir}/libk5crypto.so.*
%{_libdir}/libkdb5.so.*
%{_libdir}/libkrad.so.*
%{_libdir}/libkrb5.so.*
%{_libdir}/libkrb5support.so.*
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/*
%{_libdir}/krb5/plugins/tls/k5tls.so
%{_libdir}/krb5/plugins/preauth/spake.so
%dir %{_var}/kerberos
%dir %{_var}/kerberos/krb5
%dir %{_var}/kerberos/krb5/user

%files pkinit
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/preauth
%{_libdir}/krb5/plugins/preauth/pkinit.so

%files xrealmauthz
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdcpolicy
%{_libdir}/krb5/plugins/kdcpolicy/xrealmauthz.so

%files devel
%docdir %{_mandir}

%{_includedir}/gssapi.h
%{_includedir}/kdb.h
%{_includedir}/krad.h
%{_includedir}/krb5.h
%{_includedir}/profile.h
%{_includedir}/gssapi/
%{_includedir}/gssrpc/
%{_includedir}/kadm5/
%{_includedir}/krb5/
%{_libdir}/libgssapi_krb5.so
%{_libdir}/libgssrpc.so
%{_libdir}/libk5crypto.so
%{_libdir}/libkdb5.so
%{_libdir}/libkrad.so
%{_libdir}/libkrb5.so
%{_libdir}/libkrb5support.so
%{_libdir}/pkgconfig/gssrpc.pc
%{_libdir}/pkgconfig/kadm-client.pc
%{_libdir}/pkgconfig/kadm-server.pc
%{_libdir}/pkgconfig/kdb.pc
%{_libdir}/pkgconfig/krb5-gssapi.pc
%{_libdir}/pkgconfig/krb5.pc
%{_libdir}/pkgconfig/mit-krb5-gssapi.pc
%{_libdir}/pkgconfig/mit-krb5.pc

%{_bindir}/krb5-config
%{_mandir}/man1/krb5-config.1*

%files -n libkadm5
%{_libdir}/libkadm5clnt.so
%{_libdir}/libkadm5clnt_mit.so
%{_libdir}/libkadm5srv.so
%{_libdir}/libkadm5srv_mit.so
%{_libdir}/libkadm5clnt_mit.so.*
%{_libdir}/libkadm5srv_mit.so.*

%files tests
%{_libexecdir}/%{name}-tests-%{_arch}
%{_datarootdir}/%{name}-tests/%{_arch}

%changelog
%autochangelog
