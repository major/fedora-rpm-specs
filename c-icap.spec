%global     full_version C_ICAP_%{version}

Name:       c-icap
Version:    0.6.0
Release:    1%{?dist}
Summary:    An implementation of an ICAP server
License:    LGPL-2.1-or-later and GPL-2.0-or-later
URL:        http://%{name}.sourceforge.net/

Source0:    https://github.com/%{name}/%{name}-server/archive/%{full_version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    %{name}.logrotate
Source3:    %{name}.tmpfiles.conf
Source4:    %{name}.service

# Adjust some paths to standard Fedora/EPEL ones:
Patch0:     %{name}-conf.in.patch
# Avoid useless linking to libdb in Perl library:
Patch1:     %{name}-libdb-path.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  brotli-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libatomic
BuildRequires:  libtool
BuildRequires:  lmdb-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel

Requires:       logrotate
Requires(pre):  shadow-utils

%description
C-icap is an implementation of an ICAP server. It can be used with HTTP proxies
that support the ICAP protocol to implement content adaptation and filtering
services. Most of the commercial HTTP proxies must support the ICAP protocol,
the open source Squid 3.x proxy server supports it too.

%package devel
Summary:     Development tools for %{name}
Requires:    %{name}-libs%{?_isa} = %{version}-%{release}
Requires:    zlib-devel

%description devel
The c-icap-devel package contains the static libraries and header files for
developing software using c-icap.

%package libs
Summary:    Libraries used by %{name}

%description libs
The c-icap-libs package contains all runtime libraries used by c-icap and the
utilities.

%package perl
Summary:    The Perl handler for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description perl
The c-icap-perl package contains the Perl handler for c-icap.

%prep
%autosetup -p1 -n c-icap-server-%{full_version}

# See RECONF
echo "master-%{shortcommit0}" > VERSION.m4
autoreconf -vif

%build
# Do not explicitly link to libdb which is only brought in as a Perl dependency and not directly used
sed -i 's/$Config{libs}//' configure.ac

%configure \
  --sysconfdir=%{_sysconfdir}/%{name} \
  --enable-shared \
  --disable-static \
  --enable-ipv6 \
  --enable-large-files \
  --enable-lib-compat \
  --without-bdb \
  --with-brotli \
  --with-ldap \
  --with-lmdb \
  --with-openssl \
  --with-perl \
  --with-zlib

%make_build

%check
pushd tests
./test_allocators
./test_arrays
./test_atomics
./test_atomics_cplusplus
./test_base64
# Requires input:
#./test_body
./test_cache
# Requires input:
#./test_filetype
./test_headers
./test_lists
./test_md5
./test_ops
./test_shared_locking
# Requires input:
#./test_tables
popd

%install
%make_install

find %{buildroot} -name "*.la" -delete

mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_datadir}/c_icap/{contrib,templates}/
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}/
mkdir -p %{buildroot}/run/%{name}/

mv -f %{buildroot}%{_bindir}/%{name} %{buildroot}%{_sbindir}/

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service

# Do not add default configuration files
rm -f %{buildroot}%{_sysconfdir}/%{name}/*.default

# Let rpm pick up the docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null ||
    useradd -r -g %{name} -d /run/%{name} -s /sbin/nologin \
    -c "C-ICAP Service user" %{name}
exit 0

%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%if 0%{?rhel} == 7
%ldconfig_scriptlets libs
%endif

%files
%license COPYING
%doc AUTHORS README TODO
%doc contrib/*.pl
%attr(750,root,%{name}) %dir %{_sysconfdir}/%{name}
%attr(640,root,%{name}) %config(noreplace) %{_sysconfdir}/%{name}/*.conf
%attr(640,root,%{name}) %config(noreplace) %{_sysconfdir}/%{name}/*.magic
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0755,%{name},%{name}) %dir /run/%{name}/
%{_bindir}/%{name}-client
%{_bindir}/%{name}-mklmdb
%{_bindir}/%{name}-stretch
%{_sbindir}/%{name}
%{_datadir}/c_icap
%dir %{_libdir}/c_icap
%{_libdir}/c_icap/dnsbl_tables.so
%{_libdir}/c_icap/ldap_module.so
%{_libdir}/c_icap/lmdb_tables.so
%{_libdir}/c_icap/shared_cache.so
%{_libdir}/c_icap/srv_echo.so
%{_libdir}/c_icap/srv_ex206.so
%{_libdir}/c_icap/sys_logger.so
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}-client.8*
# Removed as BDB support is not enabled:
%exclude %{_mandir}/man8/%{name}-mkbdb.8*
%{_mandir}/man8/%{name}-mklmdb.8*
%{_mandir}/man8/%{name}-stretch.8*
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%attr(750,%{name},%{name}) %dir %{_localstatedir}/log/%{name}

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-libicapapi-config
%{_includedir}/c_icap
%{_libdir}/libicapapi.so
%{_mandir}/man8/%{name}-config.8*
%{_mandir}/man8/%{name}-libicapapi-config.8*

%files libs
%license COPYING
%{_libdir}/libicapapi.so.*

%files perl
%{_libdir}/c_icap/perl_handler.so

%changelog
* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 0.6.0-1
- Update to final 0.6.0 release.

* Sun Sep 10 2023 Simone Caronni <negativo17@gmail.com> - 0.5.11-16.20230905git49b6801
- Update to latest snapshot.

* Wed Aug 23 2023 Simone Caronni <negativo17@gmail.com> - 0.5.11-15.20230621git7a7b929
- Do not fork process in systemd unit.

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.11-14.20230621git7a7b929
- Perl 5.38 rebuild

* Thu Jun 22 2023 Simone Caronni <negativo17@gmail.com> - 0.5.11-13.20230621git7a7b929
- Update to latest snapshot, fixes build on non-x86_64 architectures and el7.

* Mon Jun 12 2023 Simone Caronni <negativo17@gmail.com> - 0.5.11-12.20230403git1238524
- Adjust C++ compiler flags on non-x86_64 architectures so tests build fine.
- Remove unused sysconfig file.

* Wed May 24 2023 Simone Caronni <negativo17@gmail.com> - 0.5.11-11.20230403git1238524
- Update to latest snapshot.
- Switch to PCRE 2.

* Fri Mar 31 2023 Simone Caronni <negativo17@gmail.com> - 0.5.11-10.20230319git2e36bb8
- Update to latest snapshot.

* Fri Feb 24 2023 Simone Caronni <negativo17@gmail.com> - 0.5.11-9.20230220gitc5f2103
- Update to latest snapshot.
- Adjust tmpfiles creation.

* Fri Feb 10 2023 Simone Caronni <negativo17@gmail.com> - 0.5.11-8.20230129git5b8fcd9
- Update to latest snapshot.
- Enable LMDB.
- Enabled more tests.

* Wed Jan 04 2023 Simone Caronni <negativo17@gmail.com> - 0.5.10-7
- Review fixes: drop bundled Berkeley DB and disable DB support, adjust Perl
  requirements, add tests, adjust licenses.

* Mon Aug 22 2022 Simone Caronni <negativo17@gmail.com> - 0.5.10-6
- Bundle Berkely DB 5.3.28.
- Merge ldap subpackage into main package (minimal dependencies).

* Sun Aug 21 2022 Simone Caronni <negativo17@gmail.com> - 0.5.10-5
- Review fixes.

* Sat Aug 20 2022 Simone Caronni <negativo17@gmail.com> - 0.5.10-4
- Initial import.
