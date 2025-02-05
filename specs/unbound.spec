%{?!with_python2:     %global with_python2     0}
%{?!with_python3:     %global with_python3     1}
%{?!with_munin:       %global with_munin       1}
%bcond_without dnstap
%bcond_without systemd
%bcond_without doh
%if 0%{?rhel} && ! 0%{?epel}
%bcond_with redis
%else
%bcond_without redis
%endif

%global forgeurl0 https://github.com/NLnetLabs/unbound
%global downloads https://nlnetlabs.nl/downloads
%global _hardened_build 1

#global extra_version rc1

%if 0%{with_python2}
%global python_primary %{__python2}
%endif

%if 0%{with_python3}
%global python_primary %{__python3}
%endif

%if 0%{?rhel}
%global with_munin   0

%if 0%{?rhel} <= 7
%global with_python3 0
%else
%global with_python2 0
%endif
%endif

Summary: Validating, recursive, and caching DNS(SEC) resolver
Name: unbound
Version: 1.22.0
Release: %autorelease %{?extra_version:-e %{extra_version}}
License: BSD-3-Clause
Url: https://nlnetlabs.nl/projects/unbound/
VCS: git:%{forgeurl0}
Source: %{downloads}/%{name}/%{name}-%{version}%{?extra_version}.tar.gz
Source1: unbound.service
Source3: unbound.munin
Source4: unbound_munin_
Source5: root.key
Source7: unbound-keygen.service
Source8: tmpfiles-unbound.conf
Source9: example.com.key
Source10: example.com.conf
Source11: block-example.com.conf
Source12: https://data.iana.org/root-anchors/icannbundle.pem
Source13: root.anchor
Source14: unbound.sysconfig
Source15: unbound-anchor.timer
Source16: unbound-munin.README
Source17: unbound-anchor.service
Source18: %{downloads}/%{name}/%{name}-%{version}%{?extra_version}.tar.gz.asc
# source: https://nlnetlabs.nl/people/
Source19: https://keys.openpgp.org/pks/lookup?op=get&search=0x9F6F1C2D7E045F8D#/wouter.nlnetlabs.nl.key
Source20: unbound.sysusers
Source21: remote-control.conf
Source22: https://nlnetlabs.nl/downloads/keys/Yorgos.asc
Source23: unbound-as112-networks.conf
Source24: unbound-local-root.conf
Source25: openssl-sha1.conf
Source26: remote-control-include.conf
Source27: fedora-defaults.conf
Source28: module-setup.sh
Source29: unbound-initrd.conf

# Downstream configuration changes
Patch1:   unbound-fedora-config.patch

BuildRequires: gcc, make
BuildRequires: openssl-devel
BuildRequires: libevent-devel expat-devel
BuildRequires: pkgconfig

# Required for configure regeneration
BuildRequires: automake autoconf libtool
BuildRequires: autoconf-archive
# Regenerate config parser too
BuildRequires: bison flex byacc

%if 0%{?fedora}
BuildRequires: gnupg2
%endif
%if 0%{with_python2}
BuildRequires: python2-devel swig
%endif
%if 0%{with_python3}
BuildRequires: python3-devel swig
%endif
%if %{with dnstap}
BuildRequires: fstrm-devel protobuf-c-devel
%endif
%if %{with systemd}
BuildRequires: systemd-devel
%endif
%if %{with doh}
BuildRequires: libnghttp2-devel
%endif
%if %{with redis}
BuildRequires: hiredis-devel
%endif
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 9
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd
%endif

# Needed because /usr/sbin/unbound links unbound libs staticly
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-anchor%{?_isa} = %{version}-%{release}
Recommends: %{name}-utils%{?_isa} = %{version}-%{release}
# unbound-keygen.service requires it, bug #2116790
Requires: openssl

%description
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

The C implementation of Unbound is developed and maintained by NLnet
Labs. It is based on ideas and algorithms taken from a java prototype
developed by Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also
DNSSEC (secure DNS) validation and stub-resolvers (that do not run
as a server, but are linked into an application) are easily possible.

%if %{with_munin}
%package munin
Summary: Plugin for the munin / munin-node monitoring package
Requires: munin-node
Requires: %{name} = %{version}-%{release}, bc
BuildArch: noarch

%description munin
Plugin for the munin / munin-node monitoring package
%endif

%package devel
Summary: Development package that includes the unbound header files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}, openssl-devel
Requires: pkgconfig

%description devel
The devel package contains the unbound library and the include files

%package libs
Summary: Libraries used by the unbound server and client applications
Recommends: %{name}-anchor
%{?sysusers_requires_compat}
%if ! 0%{with_python2}
# Make explicit conflict with no longer provided python package
Obsoletes: python2-unbound < 1.9.3
%endif

%description libs
Contains libraries used by the unbound server and client applications.

%package anchor
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Summary: DNSSEC trust anchor maintaining tool

%description anchor
Contains tool maintaining trust anchor using RFC 5011 key rollover algorithm.

%package utils
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Summary: Unbound DNS lookup utilities

%description utils
Contains tools for making DNS queries. Can make queries to DNS servers
also over TLS connection or validate DNSSEC signatures. Similar to
bind-utils.

%if 0%{with_python2}
%package -n python2-unbound
%{?python_provide:%python_provide python2-unbound}
Summary: Python 2 modules and extensions for unbound
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: unbound-python = %{version}-%{release}
Obsoletes: unbound-python < %{version}-%{release}

%description -n python2-unbound
Python 2 modules and extensions for unbound
%endif

%if 0%{with_python3}
%package -n python3-unbound
Summary: Python 3 modules and extensions for unbound
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if ! 0%{with_python2}
# Make explicit conflict with no longer provided python package
Conflicts: python2-unbound < 1.9.3
%endif

%description -n python3-unbound
Python 3 modules and extensions for unbound
%endif

%package dracut
Summary: Unbound dracut module
Requires: dracut%{?_isa}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description dracut
Unbound dracut module allowing use of Unbound for name resolution
in initramfs.

%prep
%if 0%{?fedora}
%{gpgverify} --keyring='%{SOURCE19}' --signature='%{SOURCE18}' --data='%{SOURCE0}'
%endif
%global pkgname %{name}-%{version}%{?extra_version}

%if 0%{with_python2} && 0%{with_python3}
%global python_primary %{__python3}
%global dir_secondary %{pkgname}_python2
%global python_secondary %{__python2}
%endif

%autosetup -N -n %{pkgname}

# patches go here
%autopatch -p1

%if 0%{?rhel} > 8
  # SHA-1 breaks some tests. Disable just some tests because of that.
  # This got broken in ELN
  ls testdata/*.rpl
  for TEST in autotrust_init_fail autotrust_init_failsig; do
    mv testdata/${TEST}.rpl{,-disabled} 
  done
%endif

%if 0%{with_python2} && 0%{with_python3}
  cp -a . %{dir_secondary}
%endif

%build
# ./configure script common arguments
%global configure_args --with-libevent --with-pthreads --with-ssl \\\
            --disable-rpath --disable-static \\\
            --enable-relro-now --enable-pie \\\
            --enable-subnet --enable-ipsecmod \\\
            --with-conf-file=%{_sysconfdir}/%{name}/unbound.conf \\\
            --with-share-dir=%{_datadir}/%{name} \\\
            --with-pidfile=%{_rundir}/%{name}/%{name}.pid \\\
            --enable-sha2 --disable-gost --enable-ecdsa \\\
            --with-rootkey-file=%{_sharedstatedir}/%{name}/root.key \\\
            --with-username=unbound \\\
            --enable-linux-ip-local-port-range \\\
            --with-dynlibmodule \\\
#

# always regenerate configure
rm -f config.h.in aclocal.m4 configure ltmain.sh
rm -f {ax_pthread,ax_swig_python}.m4
cp -p %{_datadir}/aclocal/{ax_pthread,ax_swig_python}.m4 .
# ensure bison is used to generate fresh parser
rm -f util/configparser.{c,h} util/configlexer.c

autoreconf -fiv

%configure  \
%if 0%{?python_primary:1}
            --with-pythonmodule --with-pyunbound PYTHON=%{python_primary} \
%endif
%if %{with dnstap}
            --enable-dnstap \
%endif
%if %{with systemd}
            --enable-systemd \
%endif
%if %{with doh}
            --with-libnghttp2 \
%endif
%if %{with redis}
            --with-libhiredis \
            --enable-cachedb \
%endif
            %{configure_args}

%make_build
%make_build streamtcp

%if 0%{?python_secondary:1}
pushd %{dir_secondary}
%configure  \
            --with-pythonmodule --with-pyunbound PYTHON=%{python_secondary} \
%if %{with dnstap}
            --enable-dnstap \
%endif
%if %{with systemd}
            --enable-systemd \
%endif
            %{configure_args}

%make_build
popd
%endif


%install
install -p -m 0644 %{SOURCE16} .

%if 0%{?python_secondary:1}
# install first secondary build. It will be overwritten by primary
pushd %{dir_secondary}
%make_install unbound-event-install
popd
%endif

%make_install unbound-event-install
install -m 0755 streamtcp %{buildroot}%{_sbindir}/unbound-streamtcp
install -p -m 0644 doc/example.conf %{buildroot}%{_sysconfdir}/unbound/unbound.conf

install -d -m 0755 %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/unbound.service
install -p -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/unbound-keygen.service
install -p -m 0644 %{SOURCE15} %{buildroot}%{_unitdir}/unbound-anchor.timer
install -p -m 0644 %{SOURCE17} %{buildroot}%{_unitdir}/unbound-anchor.service
install -p -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/unbound
install -p -m 0644 %{SOURCE14} %{buildroot}%{_sysconfdir}/sysconfig/unbound
install -p -D -m 0644 %{SOURCE20} %{buildroot}%{_sysusersdir}/%{name}.conf
%if %{with_munin}
# Install munin plugin and its softlinks
install -d -m 0755 %{buildroot}%{_sysconfdir}/munin/plugin-conf.d
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/unbound
install -d -m 0755 %{buildroot}%{_datadir}/munin/plugins/
install -p -m 0755 %{SOURCE4} %{buildroot}%{_datadir}/munin/plugins/unbound
for plugin in unbound_munin_hits unbound_munin_queue unbound_munin_memory unbound_munin_by_type unbound_munin_by_class unbound_munin_by_opcode unbound_munin_by_rcode unbound_munin_by_flags unbound_munin_histogram; do
    ln -s unbound %{buildroot}%{_datadir}/munin/plugins/$plugin
done
%endif

# install streamtcp man page
install -m 0644 testcode/streamtcp.1 %{buildroot}/%{_mandir}/man1/unbound-streamtcp.1
install -D -m 0644 contrib/libunbound.pc %{buildroot}/%{_libdir}/pkgconfig/libunbound.pc

# Install tmpfiles.d config
install -d -m 0755 %{buildroot}%{_tmpfilesdir} %{buildroot}%{_sharedstatedir}/unbound
install -m 0644 %{SOURCE8} %{buildroot}%{_tmpfilesdir}/unbound.conf

# install root - we keep a copy of the root key in old location,
# in case user has changed the configuration and we wouldn't update it there
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/unbound/
install -m 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/unbound/dnssec-root.key
# make initial key static
pushd %{buildroot}%{_sharedstatedir}/unbound
  KEYPATH=$(realpath --relative-to="%{buildroot}%{_sharedstatedir}/unbound" "%{buildroot}%{_sysconfdir}/unbound/dnssec-root.key")
  ln -s "$KEYPATH" root.key
popd

# remove static library from install (fedora packaging guidelines)
rm %{buildroot}%{_libdir}/*.la


%if 0%{with_python2}
rm %{buildroot}%{python2_sitearch}/*.la
%endif

%if 0%{with_python3}
rm %{buildroot}%{python3_sitearch}/*.la
%endif

mkdir -p %{buildroot}%{_rundir}/unbound

# Install directories for easier config file drop in

mkdir -p %{buildroot}%{_sysconfdir}/unbound/{keys.d,conf.d,local.d}
install -p -m 0644 %{SOURCE9} %{buildroot}%{_sysconfdir}/unbound/keys.d/
install -p -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/unbound/conf.d/
install -p -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/unbound/local.d/
install -p -m 0644 %{SOURCE26} %{buildroot}%{_sysconfdir}/unbound/conf.d/remote-control.conf
install -p -m 0644 %{SOURCE25} %{buildroot}%{_sysconfdir}/unbound/openssl-sha1.conf

mkdir -p %{buildroot}%{_datadir}/%{name}/conf.d
install -p -m 0644 %{SOURCE21} %{buildroot}%{_datadir}/%{name}/conf.d/
install -p -m 0644 %{SOURCE23} %{buildroot}%{_datadir}/%{name}/conf.d/
install -p -m 0644 %{SOURCE24} %{buildroot}%{_datadir}/%{name}/conf.d/
install -p -m 0644 %{SOURCE27} %{buildroot}%{_datadir}/%{name}/

# Link unbound-control-setup.8 manpage to unbound-control.8
echo ".so man8/unbound-control.8" > %{buildroot}/%{_mandir}/man8/unbound-control-setup.8

# install dracut module
mkdir -p %{buildroot}%{_prefix}/lib/dracut/modules.d/99unbound

install -p -m 0755 %{SOURCE28} %{buildroot}%{_prefix}/lib/dracut/modules.d/99unbound
install -p -m 0644 %{SOURCE29} %{buildroot}%{_prefix}/lib/dracut/modules.d/99unbound

%pre libs
%sysusers_create_compat %{SOURCE20}

%post
%systemd_post unbound.service
%systemd_post unbound-keygen.service

%post anchor
%systemd_post unbound-anchor.service unbound-anchor.timer
# start the timer only if installing the package to prevent starting it, if it was stopped on purpose
if [ "$1" -eq 1 ]; then
    # the Unit is in presets, but would be started after reboot
    /bin/systemctl start unbound-anchor.timer >/dev/null 2>&1 || :
fi

%preun
%systemd_preun unbound.service
%systemd_preun unbound-keygen.service

%preun anchor
%systemd_preun unbound-anchor.service unbound-anchor.timer

%postun
%systemd_postun_with_restart unbound.service
%systemd_postun unbound-keygen.service

%postun anchor
%systemd_postun_with_restart unbound-anchor.service unbound-anchor.timer

%check
export OPENSSL_CONF="%{buildroot}%{_sysconfdir}/unbound/openssl-sha1.conf"
make check

%if 0%{?python_secondary:1}
pushd %{dir_secondary}
make check
popd
%endif


%files
%doc doc/CREDITS doc/FEATURES
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-keygen.service
%attr(0755,unbound,unbound) %dir %{_rundir}/%{name}
%attr(0644,root,root) %{_tmpfilesdir}/unbound.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/unbound.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/openssl-sha1.conf
%dir %attr(0755,root,unbound) %{_sysconfdir}/%{name}/keys.d
%attr(0644,root,unbound) %config(noreplace) %{_sysconfdir}/%{name}/keys.d/*.key
%dir %attr(0755,root,unbound) %{_sysconfdir}/%{name}/conf.d
%attr(0644,root,unbound) %config(noreplace) %{_sysconfdir}/%{name}/conf.d/*.conf
%dir %attr(0755,root,unbound) %{_sysconfdir}/%{name}/local.d
%attr(0644,root,unbound) %config(noreplace) %{_sysconfdir}/%{name}/local.d/*.conf
%ghost %attr(0640,root,unbound) %{_sysconfdir}/%{name}/unbound_control.pem
%ghost %attr(0640,root,unbound) %{_sysconfdir}/%{name}/unbound_control.key
%ghost %attr(0640,root,unbound) %{_sysconfdir}/%{name}/unbound_server.pem
%ghost %attr(0640,root,unbound) %{_sysconfdir}/%{name}/unbound_server.key
%{_sbindir}/unbound
%{_sbindir}/unbound-checkconf
%{_sbindir}/unbound-control
%{_sbindir}/unbound-control-setup
%{_datadir}/%{name}/
%{_mandir}/man5/*
%exclude %{_mandir}/man8/unbound-anchor*
%{_mandir}/man8/*

%if 0%{with_python2}
%files -n python2-unbound
%license pythonmod/LICENSE
%{python2_sitearch}/*
%doc libunbound/python/examples/*
%doc pythonmod/examples/*
%endif

%if 0%{with_python3}
%files -n python3-unbound
%license pythonmod/LICENSE
%{python3_sitearch}/*
%doc libunbound/python/examples/*
%doc pythonmod/examples/*
%endif

%if 0%{with_munin}
%files munin
%doc unbound-munin.README
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/unbound
%{_datadir}/munin/plugins/unbound*
%endif

%files devel
%{_libdir}/libunbound.so
%{_includedir}/unbound.h
%{_includedir}/unbound-event.h
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc

%files libs
%doc doc/README
%license doc/LICENSE
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%{_sysusersdir}/%{name}.conf
%{_libdir}/libunbound.so.8*
%dir %attr(0755,unbound,unbound) %{_sharedstatedir}/%{name}
%config(noreplace) %verify(not link user group) %{_sharedstatedir}/%{name}/root.key
# just left for backwards compat with user changed unbound.conf files - format is different!
%attr(0644,root,root) %config %{_sysconfdir}/%{name}/root.key
%attr(0644,root,root) %config %{_sysconfdir}/%{name}/dnssec-root.key

%files anchor
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/unbound-anchor
%{_mandir}/man8/unbound-anchor*
# icannbundle and root.key(s) should be replaced from package
# intentionally not using noreplace
%config %{_sysconfdir}/%{name}/icannbundle.pem
%{_unitdir}/unbound-anchor.timer
%{_unitdir}/unbound-anchor.service

%files utils
%{_sbindir}/unbound-host
%{_sbindir}/unbound-streamtcp
%{_mandir}/man1/unbound-*

%files dracut
%{_prefix}/lib/dracut/modules.d/99unbound

%changelog
%autochangelog
