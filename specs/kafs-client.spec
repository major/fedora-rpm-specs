# % define buildid .local
%global libapivermajor 0
%global libapiversion %{libapivermajor}.1

Name:		kafs-client
Version:	0.4
Release:	14%{?dist}%{?buildid}
Summary:	The basic tools for kAFS and mounter for the AFS dynamic root
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://www.infradead.org/~dhowells/kafs/
Source0:	https://www.infradead.org/~dhowells/kafs/kafs-client-%{version}.tar.bz2

Requires: filesystem-afs
BuildRequires: krb5-devel
BuildRequires: keyutils-libs-devel
BuildRequires: openssl-devel
BuildRequires: gcc

#
# Need this for the upcall program to do DNS lookups.
#	/etc/kafs/client.conf
#
%global datadir %{_datarootdir}/kafs

# keyutils-1.6 request-key allows us to override AFSDB DNS lookups.
Requires: keyutils >= 1.6

BuildRequires: systemd-units
BuildRequires: make
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires: selinux-policy-base >= 3.7.19-5

%description
Provide basic AFS-compatible tools for kAFS and systemd scripts to mount the
dynamic root on /afs and preload the cell database.

%package libs
Summary: Library of routines for dealing with kAFS
Requires: %{name}%{?_isa} = %{version}-%{release}

%description libs
Provide a library of shareable routines for dealing with the kAFS
filesystem.  These provide things like configuration parsing and DNS lookups.

%package libs-devel
Summary: Library of routines for dealing with kAFS
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description libs-devel
Provide a library of shareable routines for dealing with the kAFS
filesystem.  These provide things like configuration parsing and DNS lookups.

#
# We generate a compatibility package that makes kafs look like OpenAFS, but it
# needs to be uninstalled be able to install OpenAFS or Auristor.
#
%package compat
Summary: AFS compatibility package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description compat
Compatibility package providing standard AFS names for tools such as
aklog.  This package must be uninstalled for kAFS to coexist with
another AFS implementation (such as OpenAFS).

%global _hardened_build 1
%global docdir %{_docdir}/kafs-client

%prep
%setup -q

%build
%make_build \
	ETCDIR=%{_sysconfdir} \
	BINDIR=%{_bindir} \
	SBINDIR=%{_sbindir} \
	DATADIR=%{datadir} \
	INCLUDEDIR=%{_includedir} \
	LIBDIR=%{_libdir} \
	LIBEXECDIR=%{_libexecdir} \
	MANDIR=%{_mandir} \
	CFLAGS="-Wall -Werror $RPM_OPT_FLAGS $RPM_LD_FLAGS $ARCH_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_datarootdir}

%make_install \
	ETCDIR=%{_sysconfdir} \
	BINDIR=%{_bindir} \
	SBINDIR=%{_sbindir} \
	DATADIR=%{datadir} \
	INCLUDEDIR=%{_includedir} \
	LIBDIR=%{_libdir} \
	LIBEXECDIR=%{_libexecdir} \
	MANDIR=%{_mandir} \
	CFLAGS="-Wall -Werror $RPM_OPT_FLAGS $RPM_LD_FLAGS $ARCH_OPT_FLAGS"

# Compat
ln -s aklog-kafs %{buildroot}/%{_bindir}/aklog

%ldconfig_scriptlets libs

%post
%systemd_post afs.mount

%preun
%systemd_preun afs.mount

%postun
%systemd_postun_with_restart afs.mount

%files
%doc README
%license LICENCE.GPL
%{_bindir}/aklog-kafs
%{_sbindir}/kafs-check-config
%{_unitdir}/*
%{_mandir}/man1/aklog-kafs.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%{_mandir}/man8/*.8*
%{_libexecdir}/kafs-preload
%{_libexecdir}/kafs-dns
%{_sysconfdir}/request-key.d/kafs_dns.conf

%files libs
%{_libdir}/libkafs_client.so.%{libapiversion}
%{_libdir}/libkafs_client.so.%{libapivermajor}
%{datadir}
%{_sysconfdir}/kafs
%config(noreplace) %{_sysconfdir}/kafs/client.conf
%config(noreplace) %{_sysconfdir}/kafs/client.d

%files libs-devel
%{_libdir}/libkafs_client.so
%{_includedir}/*

%files compat
%{_bindir}/aklog
%{_mandir}/man1/aklog.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 David Howells <dhowells@redhat.com> 0.4-1
- Use AF_ALG rather than OpenSSL's libcrypto.
- Move the aklog.1 manpage to the -compat rpm.

* Fri Jul 5 2019 David Howells <dhowells@redhat.com> 0.3-1
- Address Fedora packaging review comments [RH BZ 1724281].

* Tue Apr 16 2019 David Howells <dhowells@redhat.com> 0.2-1
- Improve aklog-kafs and its manpage.
- rpm: Depend on filesystem-afs for /afs dir installation.

* Fri Feb 9 2018 David Howells <dhowells@redhat.com> 0.1-1
- Initial commit
