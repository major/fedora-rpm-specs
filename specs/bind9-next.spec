#
# Red Hat BIND9 package .spec file
#
# vim:expandtab ts=2:

# bcond_without is built by default, unless --without X is passed
# bcond_with is built only when --with X is passed to build
%bcond_with    SYSTEMTEST
# Allow net configuration using sudo when SYSTEMTEST is enabled
%bcond_without SUDO
%bcond_without GSSTSIG
%bcond_without JSON
# New MaxMind GeoLite support
%bcond_without GEOIP2
# Disabled temporarily until kyua is fixed on rawhide, bug #1926779
%bcond_without UNITTEST
# Do not set CI environment, include more unit tests, even less stable
%bcond_with    UNITTEST_ALL
%bcond_without DNSTAP
%bcond_without LMDB
%bcond_without DOC
%bcond_with    TSAN
%bcond_without DTRACE
%bcond_with    OPENSSL_ENGINE
%bcond         JEMALLOC  0%{?fedora}

%{?!bind_uid:  %global bind_uid  25}
%{?!bind_gid:  %global bind_gid  25}
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global        bind_dir          /var/named
%global        chroot_prefix     %{bind_dir}/chroot
%global        chroot_create_directories /dev /run/named %{_localstatedir}/{log,named,tmp} \\\
                                         %{_sysconfdir}/{crypto-policies/back-ends,pki/dnssec-keys,pki/tls,named} \\\
                                         %{_libdir}/bind %{_libdir}/named %{_datadir}/{GeoIP,dns-root-data} /proc/sys/net/ipv4

%global forgeurl0 https://gitlab.isc.org/isc-projects/bind9

# libisc-nosym requires to be linked with unresolved symbols
# When libisc-nosym linking is fixed, it can be defined to 1
# Visit https://bugzilla.redhat.com/show_bug.cgi?id=1540300
%undefine _strict_symbol_defs_build

# Upstream package name
%global upname bind
# Provide only bind-utils on f37+, it has better behaviour
%define upname_compat() \
%if "%{name}" != "%{upname}" \
Provides: %1 = %{version}-%{release} \
Conflicts: %1 \
%endif

Summary:  The Berkeley Internet Name Domain (BIND) DNS (Domain Name System) server
Name:     bind9-next
License:  MPL-2.0 AND ISC AND BSD-3-clause AND MIT AND BSD-2-clause
#
Version:  9.21.17
Release:  %autorelease
Epoch:    32
Url:      https://www.isc.org/downloads/bind/
VCS:      git:%{forgeurl0}
#
Source0:  https://downloads.isc.org/isc/bind9/%{version}/%{upname}-%{version}.tar.xz
Source1:  named.sysconfig
Source2:  https://downloads.isc.org/isc/bind9/%{version}/%{upname}-%{version}.tar.xz.asc
Source3:  named.logrotate
Source4:  https://www.isc.org/docs/isc-keyblock.asc
Source16: named.conf
Source18: named.localhost
Source19: named.loopback
Source20: named.empty
Source23: named.rfc1912.zones
Source25: named.conf.sample
Source27: named-mkroot.sh
Source35: bind.tmpfiles.d
Source37: named.service
Source38: named-chroot.service
Source41: setup-named-chroot.sh
Source42: generate-rndc-key.sh
Source43: named.rwtab
Source44: named-chroot-setup.service
Source46: named-setup-rndc.service
Source48: setup-named-softhsm.sh
Source49: named-chroot.files

# Common patches
# Red Hat specific documentation is not relevant to upstream
Patch1: bind-9.16-redhat_doc.patch
# https://gitlab.isc.org/isc-projects/bind9/-/issues/5328
# avoid often fails on i386, unsupported upstream
Patch4: bind-9.21-unittest-qpdb-i386.patch

%{?systemd_ordering}
Requires:       coreutils
Requires(post): shadow-utils
Requires(post): glibc-common
Requires(post): grep
Requires:       dns-root-data
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:     %{name}-utils %{name}-dnssec-utils
%upname_compat %{upname}
Obsoletes:      %{name}-pkcs11 < 32:9.18.4-2
Conflicts:      bind-dyndb-ldap

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  libtool
BuildRequires:  meson >= 1.3.0
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  libcap-devel
BuildRequires:  libidn2-devel
BuildRequires:  libxml2-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  selinux-policy
BuildRequires:  findutils
BuildRequires:  sed
BuildRequires:  libnghttp2-devel
BuildRequires:  userspace-rcu-devel
BuildRequires:  pkgconfig(libedit)
BuildRequires:  dns-root-data
# Compress the changelog
BuildRequires:  gzip
%if %{with JEMALLOC}
BuildRequires:  jemalloc-devel
%endif
%if ! 0%{?rhel}
BuildRequires:  gpgverify
%endif
BuildRequires:  libuv-devel
%if %{with OPENSSL_ENGINE}
BuildRequires:  openssl-devel-engine
%endif
%if %{with UNITTEST}
# make unit dependencies
BuildRequires:  libcmocka-devel
# Ensure we have lscpu
BuildRequires:  util-linux
# Catch failing unittests coredumps
BuildRequires:  gdb
BuildRequires:  xz
%endif
%if %{with UNITTEST} || %{with SYSTEMTEST}
BuildRequires:  softhsm
%endif
%if %{with SYSTEMTEST}
# bin/tests/system dependencies
BuildRequires:  perl(Net::DNS) perl(Net::DNS::Nameserver) perl(Time::HiRes) perl(Getopt::Long)
BuildRequires:  perl(English)
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-dns
# manual configuration requires this tool
BuildRequires:  iproute
BuildRequires:  python3-jinja2
%if %{with SUDO}
BuildRequires:  libcap sudo
%endif
%endif
%if %{with GSSTSIG}
BuildRequires:  krb5-devel
%endif
%if %{with LMDB}
BuildRequires:  lmdb-devel
%endif
%if %{with JSON}
BuildRequires:  json-c-devel
%endif
%if %{with GEOIP2}
BuildRequires:  libmaxminddb-devel
%endif
%if %{with DNSTAP}
BuildRequires:  fstrm-devel protobuf-c-devel
%endif
# Needed to regenerate dig.1 manpage
%if %{with DOC}
BuildRequires:  python3-sphinx python3-sphinx_rtd_theme
BuildRequires:  doxygen
%endif
%if %{with TSAN}
BuildRequires: libtsan
%endif
%if %{with DTRACE}
# https://gitlab.isc.org/isc-projects/bind9/-/issues/4041
BuildRequires:  systemtap
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace
%endif

%description
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.

%package libs
Summary: Libraries used by the BIND DNS packages
Provides: %{name}-license = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-license < 32:9.21.11-5
Provides: %{name}-libs-lite = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-libs-lite < 32:9.16.13
Obsoletes: %{name}-pkcs11-libs < 32:9.18.4-2

%description libs
Contains heavyweight version of BIND suite libraries used by both named DNS
server and utilities in %{name}-utils package.

%package utils
Summary: Utilities for querying DNS name servers
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
# For compatibility with Debian package
Provides: dnsutils = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-pkcs11-utils < 32:9.18.4-2
%upname_compat %{upname}-utils

%description utils
Bind-utils contains a collection of utilities for querying DNS (Domain
Name System) name servers to find out information about Internet
hosts. These tools will provide you with the IP addresses for given
host names, as well as other information about registered domains and
network addresses.

You should install %{name}-utils if you need to get information from DNS name
servers.

%package dnssec-utils
Summary: DNSSEC keys and zones management utilities
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: %{name}-utils
Obsoletes: python3-%{name} < 32:9.18.0
Obsoletes: %{name}-dnssec-doc < 32:9.18.4-2
%upname_compat %{upname}-dnssec-utils

%description dnssec-utils
%{name}-dnssec-utils contains a collection of utilities for editing
DNSSEC keys and BIND zone files. These tools provide generation,
revocation and verification of keys and DNSSEC signatures in zone files.

You should install %{name}-dnssec-utils if you need to sign a DNS zone
or maintain keys for it.

%package devel
Summary:  Header files and libraries needed for bind-dyndb-ldap
Provides: %{name}-lite-devel = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-lite-devel < 32:9.16.6-3
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: openssl-devel%{?_isa} libxml2-devel%{?_isa}
Requires: libcap-devel%{?_isa}
%upname_compat %{upname}-devel
%if %{with GSSTSIG}
Requires: krb5-devel%{?_isa}
%endif
%if %{with LMDB}
Requires: lmdb-devel%{?_isa}
%endif
%if %{with JSON}
Requires:  json-c-devel%{?_isa}
%endif
%if %{with DNSTAP}
Requires:  fstrm-devel%{?_isa} protobuf-c-devel%{?_isa}
%endif
%if %{with GEOIP2}
Requires:  libmaxminddb-devel%{?_isa}
%endif

%description devel
The %{name}-devel package contains full version of the header files and libraries
required for building bind-dyndb-ldap. Upstream no longer supports nor recommends
bind libraries for third party applications.

%package chroot
Summary:        A chroot runtime environment for the ISC BIND DNS server, named(8)
Prefix:         %{chroot_prefix}
# grep is required due to setup-named-chroot.sh script
Requires:       grep
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description chroot
This package contains a tree of files which can be used as a
chroot(2) jail for the named(8) program from the BIND package.
Based on the code from Jan "Yenya" Kasprzak <kas@fi.muni.cz>


%if %{with DOC}
%package doc
Summary:   BIND 9 Administrator Reference Manual
Requires:  python3-sphinx_rtd_theme
BuildArch: noarch

%description doc
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.

This package contains BIND 9 Administrator Reference Manual
in HTML and PDF format.
%end

%endif

%prep
%if ! 0%{?rhel} || 0%{?rhel} > 10
# RHEL does not (again?) support this verification
%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE2}' --data='%{SOURCE0}'
%endif
%autosetup -n %{upname}-%{version} -p1

:;

# Create a sysusers.d config file
cat >bind9-next.sysusers.conf <<EOF
g named %{bind_gid}
u named %{bind_uid} 'Named' /var/named -
EOF

# get rid of rpath issues
sed -e '/install_rpath:/ d' -i meson.build


%build

# normal and pkcs11 unit tests
%define unit_prepare_build() \
  find lib -name 'K*.key' -exec cp -uv '{}' "%{1}/{}" ';' \
  find lib -name 'testdata' -type d -exec cp -Tav '{}' "%{1}/{}" ';' \
  find lib -name 'testkeys' -type d -exec cp -Tav '{}' "%{1}/{}" ';' \

%define systemtest_prepare_build() \
  cp -Tuav bin/tests "%{1}/bin/tests/" \

%if %{with OPENSSL_ENGINE}
CPPFLAGS="$CPPFLAGS -DOPENSSL_API_COMPAT=10100"
%else
CPPFLAGS="$CPPFLAGS -DOPENSSL_NO_ENGINE=1"
%endif
%if %{with TSAN}
  CFLAGS+=" -O1 -fsanitize=thread -fPIE -pie"
%endif
export CFLAGS CPPFLAGS
export STD_CDEFINES="$CPPFLAGS"

#sed -i -e \
#'s/([bind_VERSION_EXTRA],\s*\([^)]*\))/([bind_VERSION_EXTRA], \1-RH)/' \
#configure.ac

install -p -m 0755 %{SOURCE27} ./named-mkroot.sh # create named.root.key
./named-mkroot.sh
[ -f named.root.key ]


LIBDIR_SUFFIX=
export LIBDIR_SUFFIX

%meson \
  --includedir=%{_includedir}/bind9 \
  -Didn=enabled \
  -Dfuzzing=disabled \
%if %{without DTRACE}
  -Dtracing=disabled \
%endif
%if %{with GEOIP2}
  -Dgeoip=enabled \
%endif
%if %{with GSSTSIG}
  -Dgssapi=enabled \
%endif
%if %{with LMDB}
  -Dlmdb=enabled \
%else
  -Dlmdb=disabled \
%endif
%if %{with JSON}
  -Dstats-json=enabled \
%endif
%if %{with DNSTAP}
  -Ddnstap=enabled \
%endif
%if %{with UNITTEST}
  -Dcmocka=enabled \
%endif
%if %{with DOC}
  -Ddoc=enabled \
%endif
%if %{without JEMALLOC}
  -Djemalloc=disabled \
%endif
;
%if %{with DNSTAP}
  pushd lib
  SRCLIB="../../../lib"
  (cd dns && ln -s ${SRCLIB}/dns/dnstap.proto)
  popd
%endif

%meson_build

%if %{with DOC}
  %meson_build man arm arm-epub
%endif
%if %{with SYSTEMTEST}
  %meson_build system-test-dependencies
%endif

# Compress changelog by default
gzip doc/changelog/changelog-*.rst

#unit_prepare_build build
#systemtest_prepare_build build

%check
# reduce test loops (from default 100) for isc/{mutex/spinlock/rwlock}
# to allow rwlock(isc_rwlock_benchmark) to finish within the 300 seconds
# timeout limit on platforms (riscv64,s390x) where it is slow
# TODO: find out why it is slow
export ISC_BENCHMARK_LOOPS=20
%if %{with UNITTEST} || %{with SYSTEMTEST}
  # Tests require initialization of pkcs11 token
  eval "$(bash %{SOURCE48} -A "`pwd`/softhsm-tokens")"
%endif

%if %{with TSAN}
export TSAN_OPTIONS="log_exe_name=true log_path=ThreadSanitizer exitcode=0"
%endif

# We produce it runtime. Check it has valid syntax.
LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${RPM_BUILD_ROOT}%{_libdir}" \
  ${RPM_BUILD_ROOT}%{_bindir}/named-checkconf ${RPM_BUILD_ROOT}%{_sysconfdir}/named.root.key

%if %{with UNITTEST}
  CPUS=$(lscpu -p=cpu,core | grep -v '^#' | wc -l)
  THREADS="$CPUS"
  COREPATTERN="$(cat /proc/sys/kernel/core_pattern)"
%if %{without UNITTEST_ALL}
  export CI=true
%endif
  if [ "$CPUS" -gt 16 ]; then
    ORIGFILES=$(ulimit -n)
    THREADS=16
    # https://gitlab.isc.org/isc-projects/bind9/-/issues/5328
    export ISC_TASK_WORKERS="$THREADS"
    ulimit -n 8092 || : # Requires on some machines with many cores
  fi
  e=0
  %meson_test --num-processes ${THREADS} || e=$?

  if [ "$e" -ne 0 ]; then
    echo "ERROR: test failed. Aborting."
    exit $e;
  fi;
  [ "$CPUS" -gt 16 ] && ulimit -n $ORIGFILES || :
## End of UNITTEST
%endif

%if %{with SYSTEMTEST}
# Runs system test if ip addresses are already configured
# or it is able to configure them
  SUDO=
  pushd bin/tests/system/
  if perl ./testsock.pl
  then
    CONFIGURED=already
  else
    %if %{with SUDO}
      if [ -x /usr/sbin/capsh ] && ! /usr/sbin/capsh --has-p=cap_net_admin; then
        echo "Not running as privileged user, using sudo"
        SUDO=sudo
      fi
    %endif

    CONFIGURED=
    $SUDO sh ./ifconfig.sh up
    perl ./testsock.pl && CONFIGURED=build
  fi
  popd

  if [ -n "$CONFIGURED" ]
  then
    pushd bin/tests/system
    export CI_SYSTEM=yes # allow running tests as root
    chown -R ${USER} . # Can be unknown user
    e=0
    pytest -n ${THREADS} --capture=tee-sys || e=$?
    [ "$CONFIGURED" = build ] && $SUDO sh ./ifconfig.sh down
    if [ "$e" -ne 0 ]; then
      echo "ERROR: failed running 'pytest' in system tests. Aborting."
      ls -1 "$(pwd)"/*_tmp_*
      for TMPTEST in *_tmp_*
      do
        echo "# $TMPTEST"
        cat $TMPTEST/pytest.log.txt
      done
      exit $e;
    fi;
    popd
  else
    echo 'SKIPPED: tests require root, CAP_NET_ADMIN or already configured test addresses.'
  fi
%endif
:

%install
# Build directory hierarchy
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/{bind,named}
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/named/{slaves,data,dynamic}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/{man1,man5,man8}
mkdir -p ${RPM_BUILD_ROOT}/run/named
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/log

#chroot
for D in %{chroot_create_directories}
do
  mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}${D}
done

# create symlink as it is on real filesystem
pushd ${RPM_BUILD_ROOT}/%{chroot_prefix}/var
ln -s ../run run
popd

# these are required to prevent them being erased during upgrade of previous
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}%{_sysconfdir}/named.conf
#end chroot

%meson_install

# Remove unwanted files
rm -f ${RPM_BUILD_ROOT}/etc/bind.keys

# Systemd unit files
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -pm 644 %{SOURCE37} ${RPM_BUILD_ROOT}%{_unitdir}
install -pm 644 %{SOURCE38} ${RPM_BUILD_ROOT}%{_unitdir}
install -pm 644 %{SOURCE44} ${RPM_BUILD_ROOT}%{_unitdir}
install -pm 644 %{SOURCE46} ${RPM_BUILD_ROOT}%{_unitdir}

mkdir -p ${RPM_BUILD_ROOT}%{_libexecdir}
install -pm 755 %{SOURCE41} ${RPM_BUILD_ROOT}%{_libexecdir}/setup-named-chroot.sh
install -pm 755 %{SOURCE42} ${RPM_BUILD_ROOT}%{_libexecdir}/generate-rndc-key.sh

install -pm 755 %{SOURCE48} ${RPM_BUILD_ROOT}%{_libexecdir}/setup-named-softhsm.sh

install -pm 644 %SOURCE3 ${RPM_BUILD_ROOT}/etc/logrotate.d/named
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -pm 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/named
install -pm 644 %{SOURCE49} ${RPM_BUILD_ROOT}%{_sysconfdir}/named-chroot.files

%if "%{_sbindir}" != "%{_bindir}"
  ln -s ../bin/{named-checkconf,named-checkzone,named-compilezone} %{buildroot}%{_sbindir}/
%endif

# Remove libtool .la files:
find ${RPM_BUILD_ROOT}/%{_libdir} -name '*.la' -exec '/bin/rm' '-f' '{}' ';';

# 9.16.4 installs even manual pages for tools not generated
%if %{without DNSTAP}
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/dnstap-read.1* || true
%endif
%if %{without LMDB}
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man8/named-nzd2nzf.8* || true
%endif

pushd ${RPM_BUILD_ROOT}%{_mandir}/man8
ln -s ddns-confgen.8.gz tsig-keygen.8.gz
popd
pushd ${RPM_BUILD_ROOT}%{_mandir}/man1
ln -s named-checkzone.1.gz named-compilezone.1.gz
popd

%if %{with DOC}
mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}
pushd %{_vpath_builddir}
cp -a arm/ ${RPM_BUILD_ROOT}%{_pkgdocdir}/html/
#rm -rf ${RPM_BUILD_ROOT}%{_pkgdocdir}/html/.{buildinfo,doctrees}
# Backward compatible link to 9.11 documentation
(cd ${RPM_BUILD_ROOT}%{_pkgdocdir} && ln -s html/index.html Bv9ARM.html)
# Share static data from original sphinx package
for DIR in %{python3_sitelib}/sphinx_rtd_theme/static/*
do
  BASE=$(basename -- "$DIR")
  BINDTHEMEDIR="${RPM_BUILD_ROOT}%{_pkgdocdir}/html/_static/$BASE"
  if [ -d "$BINDTHEMEDIR" ]; then
    rm -rf "$BINDTHEMEDIR"
    ln -sr "${RPM_BUILD_ROOT}${DIR}" "$BINDTHEMEDIR"
  fi
done
cp -p arm-epub/Bv9ARM.epub ${RPM_BUILD_ROOT}%{_pkgdocdir}
popd
cp -p doc/changelog/changelog-history.rst* doc/notes/notes-*.rst* \
      ${RPM_BUILD_ROOT}%{_pkgdocdir}
%endif

# Ghost config files:
touch ${RPM_BUILD_ROOT}%{_localstatedir}/log/named.log

# configuration files:
install -m 640 %{SOURCE16} ${RPM_BUILD_ROOT}%{_sysconfdir}/named.conf
touch ${RPM_BUILD_ROOT}%{_sysconfdir}/rndc.{key,conf}
install -m 644 -p named.root.key ${RPM_BUILD_ROOT}%{_sysconfdir}/named.root.key
ln -s "%{_datadir}/dns-root-data/root.key" ${RPM_BUILD_ROOT}%{_sysconfdir}/trusted-key.key
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/named

# data files:
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/named
ln -s "%{_datadir}/dns-root-data/root.hints" ${RPM_BUILD_ROOT}%{_localstatedir}/named/named.ca
install -m 640 %{SOURCE18} ${RPM_BUILD_ROOT}%{_localstatedir}/named/named.localhost
install -m 640 %{SOURCE19} ${RPM_BUILD_ROOT}%{_localstatedir}/named/named.loopback
install -m 640 %{SOURCE20} ${RPM_BUILD_ROOT}%{_localstatedir}/named/named.empty
install -m 640 %{SOURCE23} ${RPM_BUILD_ROOT}%{_sysconfdir}/named.rfc1912.zones

# sample bind configuration files for %%doc:
mkdir -p sample/etc sample/var/named/{data,slaves}
install -m 644 %{SOURCE25} sample/etc/named.conf
# Copy default configuration to %%doc to make it usable from system-config-bind
install -m 644 %{SOURCE16} named.conf.default
install -m 644 %{SOURCE23} sample/etc/named.rfc1912.zones
install -m 644 %{SOURCE18} %{SOURCE19} %{SOURCE20}  sample/var/named
ln -s "%{_datadir}/dns-root-data/root.hints" sample/var/named/named.ca
for f in my.internal.zone.db slaves/my.slave.internal.zone.db slaves/my.ddns.internal.zone.db my.external.zone.db; do 
  echo '@ in soa localhost. root 1 3H 15M 1W 1D
  ns localhost.' > sample/var/named/$f; 
done
:;

mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
install -m 644 %{SOURCE35} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/named.conf

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d
install -m 644 %{SOURCE43} ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d/named

install -m0644 -D bind9-next.sysusers.conf %{buildroot}%{_sysusersdir}/bind9-next.conf

%post
%?ldconfig
if [ "$1" -eq 1 ]; then
  # Initial installation
  [ -x /sbin/restorecon ] && /sbin/restorecon /etc/rndc.* /etc/named.* >/dev/null 2>&1 ;
  # rndc.key has to have correct perms and ownership, CVE-2007-6283
  [ -e /etc/rndc.key ] && chown root:named /etc/rndc.key
  [ -e /etc/rndc.key ] && chmod 0640 /etc/rndc.key
else
  # Upgrade, use invalid shell
  if getent passwd named | grep ':/bin/false$' >/dev/null; then
    /sbin/usermod -s /sbin/nologin named
  fi
  # Checkconf will parse out comments
  if /usr/bin/named-checkconf -p /etc/named.conf 2>/dev/null | grep -q named.iscdlv.key
  then
    echo "Replacing obsolete named.iscdlv.key with named.root.key..."
    if cp -Rf --preserve=all --remove-destination /etc/named.conf /etc/named.conf.rpmbackup; then
      sed -e 's/named\.iscdlv\.key/named.root.key/' \
        /etc/named.conf.rpmbackup > /etc/named.conf || \
      mv /etc/named.conf.rpmbackup /etc/named.conf
    fi
  fi
fi
%systemd_post named.service
:;

%preun
# Package removal, not upgrade
%systemd_preun named.service

%postun
%?ldconfig
# Package upgrade, not uninstall
%systemd_postun_with_restart named.service

# Fix permissions on existing device files on upgrade
%define chroot_fix_devices() \
if [ $1 -gt 1 ]; then \
  for DEV in "%{1}/dev"/{null,random,zero}; do \
    if [ -e "$DEV" -a "$(/bin/stat --printf="%G %a" "$DEV")" = "root 644" ]; \
    then \
      /bin/chmod 0664 "$DEV" \
      /bin/chgrp named "$DEV" \
    fi \
  done \
fi

%triggerun -- bind < 32:9.9.0-0.6.rc1
/sbin/chkconfig --del named >/dev/null 2>&1 || :
/bin/systemctl try-restart named.service >/dev/null 2>&1 || :

%triggerpostun -- bind < 32:9.18.4-2, selinux-policy, policycoreutils
if [ -x %{_sbindir}/selinuxenabled ] && [ -x %{_sbindir}/getsebool ] && [ -x %{_sbindir}/setsebool ] \
   && %{_sbindir}/selinuxenabled && [ -x %{_sbindir}/named ]; then
  # Return master zones after upgrade from selinux_booleans version
  WRITEBOOL="$(LC_ALL=C %{_sbindir}/getsebool named_write_master_zones)"
  if [ "echo ${WRITEBOOL#named_write_master_zones --> }" = "off" ]; then
    echo "Restoring new sebool default of named_write_master_zones..."
    %{_sbindir}/setsebool -P named_write_master_zones=1 || :
  fi
fi

%ldconfig_scriptlets libs

%post chroot
%systemd_post named-chroot.service
%chroot_fix_devices %{chroot_prefix}
:;

%posttrans chroot
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon %{chroot_prefix}/dev/* > /dev/null 2>&1;
fi;

%preun chroot
# wait for stop of both named-chroot and named-chroot-setup services
# on uninstall
%systemd_preun named-chroot.service named-chroot-setup.service
:;

%postun chroot
# Package upgrade, not uninstall
%systemd_postun_with_restart named-chroot.service


%files
# TODO: Move from lib/bind to lib/named, as used by upstream
# FIXME: current build targets filters into %%_libdir/bind again?
%dir %{_libdir}/bind
%{_libdir}/bind/filter*.so
%{_libdir}/bind/synthrecord.so
%dir %{_libdir}/named
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sysconfig/named
%config(noreplace) %attr(0644,root,named) %{_sysconfdir}/named.root.key
%config(noreplace) %{_sysconfdir}/logrotate.d/named
%{_tmpfilesdir}/named.conf
%{_sysusersdir}/bind9-next.conf
%{_sysconfdir}/rwtab.d/named
%{_unitdir}/named.service
%{_unitdir}/named-setup-rndc.service
%{_bindir}/named-journalprint
%{_bindir}/named-checkconf
%{_bindir}/named-rrchecker
%{_bindir}/named-makejournal
%{_bindir}/mdig
%{_sbindir}/named
%{_sbindir}/rndc*
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/named-checkconf
%endif
%{_libexecdir}/generate-rndc-key.sh
%{_libexecdir}/setup-named-softhsm.sh
%{_mandir}/man1/mdig.1*
%{_mandir}/man1/named-rrchecker.1*
%{_mandir}/man5/named.conf.5*
%{_mandir}/man5/rndc.conf.5*
%{_mandir}/man8/rndc.8*
%{_mandir}/man8/named.8*
%{_mandir}/man1/named-checkconf.1*
%{_mandir}/man8/rndc-confgen.8*
%{_mandir}/man1/named-journalprint.1*
%{_mandir}/man1/named-makejournal.1*
%{_mandir}/man8/filter-*.8*
%doc README.md named.conf.default
%doc doc/changelog/changelog-9.*.rst*
%doc sample/

# Hide configuration
%defattr(0640,root,named,0750)
%dir %{_sysconfdir}/named
%config(noreplace) %verify(not link) %{_sysconfdir}/named.conf
%config(noreplace) %verify(not link) %{_sysconfdir}/named.rfc1912.zones
%defattr(0660,root,named,01770)
%dir %{_localstatedir}/named
%defattr(0660,named,named,0770)
%dir %{_localstatedir}/named/slaves
%dir %{_localstatedir}/named/data
%dir %{_localstatedir}/named/dynamic
%ghost %{_localstatedir}/log/named.log
%defattr(0640,root,named,0750)
%config %verify(not link) %{_localstatedir}/named/named.ca
%config %verify(not link) %{_localstatedir}/named/named.localhost
%config %verify(not link) %{_localstatedir}/named/named.loopback
%config %verify(not link) %{_localstatedir}/named/named.empty
%ghost %config(noreplace) %{_sysconfdir}/rndc.key
# ^- rndc.key now created on first install only if it does not exist
%ghost %config(noreplace) %{_sysconfdir}/rndc.conf
# ^- The default rndc.conf which uses rndc.key is in named's default internal config -
#    so rndc.conf is not necessary.
%defattr(-,named,named,-)
%dir /run/named

%files libs
%{_libdir}/libisccc-%{version}*.so
%{_libdir}/libns-%{version}*.so
%{_libdir}/libdns-%{version}*.so
%{_libdir}/libisc-%{version}*.so
%{_libdir}/libisccfg-%{version}*.so
%{!?_licensedir:%global license %%doc}
%license COPYRIGHT

%files utils
%{_bindir}/dig
%{_bindir}/delv
%{_bindir}/host
%{_bindir}/nslookup
%{_bindir}/nsupdate
%{_bindir}/arpaname
%{_sbindir}/ddns-confgen
%{_sbindir}/tsig-keygen
%{_bindir}/nsec3hash
%{_bindir}/named-checkzone
%{_bindir}/named-compilezone
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/named-checkzone
%{_sbindir}/named-compilezone
%endif
%if %{with DNSTAP}
%{_bindir}/dnstap-read
%{_mandir}/man1/dnstap-read.1*
%endif
%if %{with LMDB}
%{_bindir}/named-nzd2nzf
%{_mandir}/man1/named-nzd2nzf.1*
%endif
%{_mandir}/man1/host.1*
%{_mandir}/man1/nsupdate.1*
%{_mandir}/man1/dig.1*
%{_mandir}/man1/delv.1*
%{_mandir}/man1/nslookup.1*
%{_mandir}/man1/arpaname.1*
%{_mandir}/man8/ddns-confgen.8*
%{_mandir}/man8/tsig-keygen.8*
%{_mandir}/man1/nsec3hash.1*
%{_mandir}/man1/named-checkzone.1*
%{_mandir}/man1/named-compilezone.1*
%{_sysconfdir}/trusted-key.key

%files dnssec-utils
%{_bindir}/dnssec*
%{_mandir}/man1/dnssec*.1*

%if 0
# TODO: remove devel subpackage or create custom installation part
%files devel
%{_libdir}/libisccc.so
%{_libdir}/libns.so
%{_libdir}/libdns.so
%{_libdir}/libisc.so
%{_libdir}/libisccfg.so
%dir %{_includedir}/bind9
%{_includedir}/bind9/isccc
%{_includedir}/bind9/ns
%{_includedir}/bind9/dns
%{_includedir}/bind9/dst
%{_includedir}/bind9/irs
%{_includedir}/bind9/isc
%{_includedir}/bind9/isccfg
%endif

%files chroot
%config(noreplace) %{_sysconfdir}/named-chroot.files
%{_unitdir}/named-chroot.service
%{_unitdir}/named-chroot-setup.service
%{_libexecdir}/setup-named-chroot.sh
%defattr(0664,root,named,-)
%ghost %dev(c,1,3) %verify(not mtime) %{chroot_prefix}/dev/null
%ghost %dev(c,1,8) %verify(not mtime) %{chroot_prefix}/dev/random
%ghost %dev(c,1,9) %verify(not mtime) %{chroot_prefix}/dev/urandom
%ghost %dev(c,1,5) %verify(not mtime) %{chroot_prefix}/dev/zero
%defattr(0640,root,named,0750)
%dir %{chroot_prefix}
%dir %{chroot_prefix}/dev
%dir %{chroot_prefix}%{_sysconfdir}
%dir %{chroot_prefix}%{_sysconfdir}/named
%dir %{chroot_prefix}%{_sysconfdir}/pki
%dir %{chroot_prefix}%{_sysconfdir}/pki/dnssec-keys
%dir %{chroot_prefix}%{_sysconfdir}/pki/tls
%dir %{chroot_prefix}%{_sysconfdir}/crypto-policies
%dir %{chroot_prefix}%{_sysconfdir}/crypto-policies/back-ends
%dir %{chroot_prefix}%{_localstatedir}
%dir %{chroot_prefix}/run
%ghost %config(noreplace) %{chroot_prefix}%{_sysconfdir}/named.conf
%defattr(-,root,root,-)
%dir %{chroot_prefix}/usr
%dir %{chroot_prefix}/%{_libdir}
%dir %{chroot_prefix}/%{_libdir}/bind
%dir %{chroot_prefix}/%{_datadir}
%dir %{chroot_prefix}/%{_datadir}/GeoIP
%{chroot_prefix}/proc
%defattr(0660,root,named,01770)
%dir %{chroot_prefix}%{_localstatedir}/named
%defattr(0660,named,named,0770)
%dir %{chroot_prefix}%{_localstatedir}/tmp
%dir %{chroot_prefix}%{_localstatedir}/log
%defattr(-,named,named,-)
%dir %{chroot_prefix}/run/named
%{chroot_prefix}%{_localstatedir}/run

%if %{with DOC}
%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/Bv9ARM.html
%doc %{_pkgdocdir}/Bv9ARM.epub
%doc %{_pkgdocdir}/changelog-history.rst*
%doc %{_pkgdocdir}/notes-*.rst*
%license COPYRIGHT
%endif

%changelog
%autochangelog
