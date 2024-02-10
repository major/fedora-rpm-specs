Version:        22

%global forgeurl https://github.com/neocturne/fastd
%forgemeta

Name:           fastd
Release:        %autorelease
Summary:        Fast and secure tunneling daemon

License:        BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{name}-tmpfiles.conf

BuildRequires:  gcc
BuildRequires:  meson
%if 0%{?rhel} < 8
BuildRequires:  python-sphinx
%else
BuildRequires:  python3-sphinx
%endif

BuildRequires:  bison
BuildRequires:  json-c-devel
BuildRequires:  libcap-devel
BuildRequires:  libmnl-devel
BuildRequires:  libsodium-devel
BuildRequires:  libuecc-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:     kmod(l2tp_core.ko)
Recommends:     kmod(l2tp_eth.ko)
Recommends:     kmod(l2tp_netlink.ko)
# Workaround for dnf pulling in kernel-debug-modules-extra over
# kernel-modules-extra to satisfy the kmod dependencies (rhbz#1192189)
Suggests:       kernel-modules-extra
%endif

%description
fastd is a secure tunneling daemon with some unique features:

 - Very small binary (about 100KB on OpenWRT in the default configuration,
   including all dependencies besides libc)
 - Exchangable crypto methods
 - Transport over UDP for simple usage behind NAT
 - Can run in 1:1 and 1:n scenarios
 - There are no server and client roles defined by the protocol, this is just
   defined by the usage.
 - Only one instance of the daemon is needed on each host to create a full mesh
   If no full mesh is established, a routing protocol is necessary to enable
   hosts that are not connected directly to reach each other

%prep
%forgeautosetup


%build
# These use special features on x86 and build may fail while trying to detect
# their presence on non-x86 builders
%ifnarch %{ix86} x86_64
  %meson \
    -Dcipher_salsa2012_xmm=disabled \
    -Dmac_ghash_pclmulqdq=disabled \
    -Dcipher_salsa20_xmm=disabled
%else
  %meson
%endif

%meson_build

# build documentation
pushd doc
  make text
popd


%install
%meson_install

install -Dpm 0644 doc/examples/fastd@.service %{buildroot}%{_unitdir}/%{name}@.service
install -Dpm 0644 doc/fastd.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -d %{buildroot}%{_sysconfdir}/%{name}

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -dm 0755 %{buildroot}/run/%{name}


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%doc README.md doc/build/text/*
%license COPYRIGHT
%dir %{_sysconfdir}/%{name}
%dir /run/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_unitdir}/%{name}@.service
%{_bindir}/%{name}
%{_tmpfilesdir}/%{name}.conf


%changelog
%autochangelog
