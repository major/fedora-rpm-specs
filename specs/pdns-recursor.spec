%ifarch %{ix86} armv7hl
%global _lto_cflags %{nil}
%endif

Name: pdns-recursor
Version: 5.2.0
Release: %autorelease
Summary: Modern, advanced and high performance recursing/non authoritative name server
License: GPL-2.0-only
URL: https://powerdns.com
Source0: https://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2
ExcludeArch: %{arm} %{ix86}

Provides: powerdns-recursor = %{version}-%{release}
BuildRequires: make
BuildRequires: boost-devel
BuildRequires: gcc-c++
%ifarch %{ix86} x86_64 aarch64
BuildRequires: luajit-devel
%else
BuildRequires: lua-devel
%endif
%ifarch ppc64le
BuildRequires: libatomic
%endif
BuildRequires: libcap-devel
BuildRequires: fstrm-devel
BuildRequires: openssl-devel
%if 0%{?fedora} >= 41
BuildRequires: openssl-devel-engine
%endif
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: protobuf-devel
BuildRequires: hostname
BuildRequires: libsodium-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: cargo-rpm-macros
BuildRequires: curl-devel

Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


Patch:         serde_yaml.patch


%description
PowerDNS Recursor is a non authoritative/recursing DNS server. Use this
package if you need a dns cache for your network.


%prep
%autosetup -n %{name}-%{version} -p1
cd settings/rust
%cargo_prep

%generate_buildrequires
cd settings/rust
%cargo_generate_buildrequires

%build
%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --with-libsodium \
    --enable-reproducible \
    --enable-dnstap \
    --enable-dns-over-tls \
%ifarch %{ix86} x86_64 aarch64
    --with-lua=luajit \
%else
    --with-lua \
%endif
    --with-socketdir=%{_rundir}

cd settings/rust
# needed because cargo_prep removes Cargo.lock but Makefile has no rule to make
# target 'Cargo.lock'
cargo generate-lockfile --offline
%make_build


%install
%make_install

%{__cp} %{buildroot}%{_sysconfdir}/%{name}/recursor.{yml-dist,conf}

# add directories for newly-observed-domains/unique-domain-response
install -p -d -m 0755 %{buildroot}/%{_sharedstatedir}/%{name}/nod
install -p -d -m 0755 %{buildroot}/%{_sharedstatedir}/%{name}/udr

# change user and group to pdns-recursor
sed -i \
    -e 's/# setuid=/setuid=pdns-recursor/' \
    -e 's/# setgid=/setgid=pdns-recursor/' \
    -e 's/# security-poll-suffix=secpoll\.powerdns\.com\./security-poll-suffix=/' \
    %{buildroot}%{_sysconfdir}/%{name}/recursor.conf


%pre
getent group pdns-recursor > /dev/null || groupadd -r pdns-recursor
getent passwd pdns-recursor > /dev/null || \
    useradd -r -g pdns-recursor -d / -s /sbin/nologin \
    -c "PowerDNS Recursor user" pdns-recursor
exit 0


%post
%systemd_post pdns-recursor.service


%preun
%systemd_preun pdns-recursor.service


%postun
%systemd_postun_with_restart pdns-recursor.service


%files
%{_bindir}/rec_control
%{_sbindir}/pdns_recursor
%{_mandir}/man1/pdns_recursor.1.gz
%{_mandir}/man1/rec_control.1.gz
%{_unitdir}/pdns-recursor.service
%{_unitdir}/pdns-recursor@.service
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/recursor.conf
# provide example yml config file. For new installs recursor.conf is the yaml
# because since recursor.yml takes precedence over recursor.conf we don't put
# it directly there
%config %{_sysconfdir}/%{name}/recursor.yml-dist
%dir %attr(0755,pdns-recursor,pdns-recursor) %{_sharedstatedir}/%{name}
%dir %attr(0755,pdns-recursor,pdns-recursor) %{_sharedstatedir}/%{name}/nod
%dir %attr(0755,pdns-recursor,pdns-recursor) %{_sharedstatedir}/%{name}/udr
%doc README
%license COPYING


%changelog
%autochangelog
