# Building from fedora dependencies not possible
# Latest upstream rtnetlink frequently required
# sha2, zbus, zvariant are currently out of date

%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global built_tag v1.6.0
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: netavark
Version: %{gen_version}
Release: %autorelease
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT
ExclusiveArch: %{golang_arches_future}
Summary: OCI network stack
URL: https://github.com/containers/%{name}
# Tarballs fetched from upstream's release page
Source0: %{url}/archive/%{built_tag}.tar.gz
Source1: %{url}/releases/download/%{built_tag}/%{name}-%{built_tag}-vendor.tar.gz
BuildRequires: cargo
BuildRequires: go-md2man
# aardvark-dns and %%{name} are usually released in sync
Recommends: aardvark-dns >= %{version}-1
Requires: (aardvark-dns >= %{version}-1 if fedora-release-identity-server)
Provides: container-network-stack = 2
BuildRequires: make
BuildRequires: protobuf-c
BuildRequires: protobuf-compiler
BuildRequires: rust-packaging
BuildRequires: rust-srpm-macros
BuildRequires: git-core
BuildRequires: systemd
BuildRequires: systemd-devel
# Generated using:
# cargo tree --prefix none | awk '{print "Provides: bundled(crate("$1")) = "$2}' | sort | uniq
Provides: bundled(crate(aho-corasick)) = v0.7.20
Provides: bundled(crate(anyhow)) = v1.0.70
Provides: bundled(crate(arrayvec)) = v0.7.2
Provides: bundled(crate(async-broadcast)) = v0.5.1
Provides: bundled(crate(async-channel)) = v1.8.0
Provides: bundled(crate(async-executor)) = v1.5.0
Provides: bundled(crate(async-fs)) = v1.6.0
Provides: bundled(crate(async-io)) = v1.12.0
Provides: bundled(crate(async-lock)) = v2.7.0
Provides: bundled(crate(async-recursion)) = v1.0.2
Provides: bundled(crate(async-task)) = v4.3.0
Provides: bundled(crate(async-trait)) = v0.1.68
Provides: bundled(crate(atomic-waker)) = v1.1.0
Provides: bundled(crate(atty)) = v0.2.14
Provides: bundled(crate(autocfg)) = v1.1.0
Provides: bundled(crate(axum)) = v0.6.12
Provides: bundled(crate(axum-core)) = v0.3.3
Provides: bundled(crate(base64)) = v0.21.0
Provides: bundled(crate(bitflags)) = v1.3.2
Provides: bundled(crate(block-buffer)) = v0.10.3
Provides: bundled(crate(blocking)) = v1.3.0
Provides: bundled(crate(byteorder)) = v1.4.3
Provides: bundled(crate(bytes)) = v1.4.0
Provides: bundled(crate(cfg-if)) = v1.0.0
Provides: bundled(crate(chrono)) = v0.4.24
Provides: bundled(crate(clap)) = v3.2.23
Provides: bundled(crate(clap_derive)) = v3.2.18
Provides: bundled(crate(clap_lex)) = v0.2.4
Provides: bundled(crate(concurrent-queue)) = v2.1.0
Provides: bundled(crate(cpufeatures)) = v0.2.5
Provides: bundled(crate(crossbeam-utils)) = v0.8.15
Provides: bundled(crate(crypto-common)) = v0.1.6
Provides: bundled(crate(data-encoding)) = v2.3.3
Provides: bundled(crate(derivative)) = v2.2.0
Provides: bundled(crate(dhcproto)) = v0.9.0
Provides: bundled(crate(dhcproto-macros)) = v0.1.0
Provides: bundled(crate(digest)) = v0.10.6
Provides: bundled(crate(dirs)) = v4.0.0
Provides: bundled(crate(dirs-sys)) = v0.3.7
Provides: bundled(crate(either)) = v1.8.1
Provides: bundled(crate(enum-as-inner)) = v0.5.1
Provides: bundled(crate(enumflags2)) = v0.7.5
Provides: bundled(crate(enumflags2_derive)) = v0.7.4
Provides: bundled(crate(env_logger)) = v0.10.0
Provides: bundled(crate(etherparse)) = v0.13.0
Provides: bundled(crate(ethtool)) = v0.2.4
Provides: bundled(crate(event-listener)) = v2.5.3
Provides: bundled(crate(fastrand)) = v1.9.0
Provides: bundled(crate(fixedbitset)) = v0.4.2
Provides: bundled(crate(fnv)) = v1.0.7
Provides: bundled(crate(form_urlencoded)) = v1.1.0
Provides: bundled(crate(fs2)) = v0.4.3
Provides: bundled(crate(futures)) = v0.3.26
Provides: bundled(crate(futures-channel)) = v0.3.28
Provides: bundled(crate(futures-core)) = v0.3.28
Provides: bundled(crate(futures-executor)) = v0.3.26
Provides: bundled(crate(futures-io)) = v0.3.28
Provides: bundled(crate(futures-lite)) = v1.12.0
Provides: bundled(crate(futures-macro)) = v0.3.28
Provides: bundled(crate(futures-sink)) = v0.3.28
Provides: bundled(crate(futures-task)) = v0.3.28
Provides: bundled(crate(futures-util)) = v0.3.28
Provides: bundled(crate(generic-array)) = v0.14.6
Provides: bundled(crate(genetlink)) = v0.2.4
Provides: bundled(crate(getrandom)) = v0.2.8
Provides: bundled(crate(h2)) = v0.3.16
Provides: bundled(crate(hashbrown)) = v0.12.3
Provides: bundled(crate(heck)) = v0.4.1
Provides: bundled(crate(hex)) = v0.4.3
Provides: bundled(crate(http)) = v0.2.9
Provides: bundled(crate(http-body)) = v0.4.5
Provides: bundled(crate(httparse)) = v1.8.0
Provides: bundled(crate(httpdate)) = v1.0.2
Provides: bundled(crate(humantime)) = v2.1.0
Provides: bundled(crate(hyper)) = v0.14.24
Provides: bundled(crate(hyper-timeout)) = v0.4.1
Provides: bundled(crate(iana-time-zone)) = v0.1.53
Provides: bundled(crate(idna)) = v0.2.3
Provides: bundled(crate(idna)) = v0.3.0
Provides: bundled(crate(indexmap)) = v1.9.2
Provides: bundled(crate(io-lifetimes)) = v1.0.5
Provides: bundled(crate(ipnet)) = v2.7.2
Provides: bundled(crate(iptables)) = v0.5.0
Provides: bundled(crate(is-terminal)) = v0.4.4
Provides: bundled(crate(itertools)) = v0.10.5
Provides: bundled(crate(itoa)) = v1.0.6
Provides: bundled(crate(lazy_static)) = v1.4.0
Provides: bundled(crate(libc)) = v0.2.140
Provides: bundled(crate(linux-raw-sys)) = v0.1.4
Provides: bundled(crate(log)) = v0.4.17
Provides: bundled(crate(macaddr)) = v1.0.1
Provides: bundled(crate(matches)) = v0.1.10
Provides: bundled(crate(matchit)) = v0.7.0
Provides: bundled(crate(memchr)) = v2.5.0
Provides: bundled(crate(memoffset)) = v0.7.1
Provides: bundled(crate(mime)) = v0.3.16
Provides: bundled(crate(mio)) = v0.8.6
Provides: bundled(crate(mozim)) = v0.2.2
Provides: bundled(crate(mptcp-pm)) = v0.1.2
Provides: bundled(crate(multimap)) = v0.8.3
Provides: bundled(crate(netavark)) = v1.6.0
Provides: bundled(crate(netlink-packet-core)) = v0.5.0
Provides: bundled(crate(netlink-packet-generic)) = v0.3.2
Provides: bundled(crate(netlink-packet-route)) = v0.15.0
Provides: bundled(crate(netlink-packet-utils)) = v0.5.2
Provides: bundled(crate(netlink-proto)) = v0.11.1
Provides: bundled(crate(netlink-sys)) = v0.8.5
Provides: bundled(crate(nispor)) = v1.2.10
Provides: bundled(crate(nix)) = v0.26.2
Provides: bundled(crate(num-integer)) = v0.1.45
Provides: bundled(crate(num-traits)) = v0.2.15
Provides: bundled(crate(num_cpus)) = v1.15.0
Provides: bundled(crate(once_cell)) = v1.17.1
Provides: bundled(crate(ordered-float)) = v2.10.0
Provides: bundled(crate(ordered-stream)) = v0.2.0
Provides: bundled(crate(os_str_bytes)) = v6.4.1
Provides: bundled(crate(parking)) = v2.0.0
Provides: bundled(crate(paste)) = v1.0.12
Provides: bundled(crate(percent-encoding)) = v2.2.0
Provides: bundled(crate(petgraph)) = v0.6.3
Provides: bundled(crate(pin-project)) = v1.0.12
Provides: bundled(crate(pin-project-internal)) = v1.0.12
Provides: bundled(crate(pin-project-lite)) = v0.2.9
Provides: bundled(crate(pin-utils)) = v0.1.0
Provides: bundled(crate(polling)) = v2.5.2
Provides: bundled(crate(ppv-lite86)) = v0.2.17
Provides: bundled(crate(prettyplease)) = v0.1.24
Provides: bundled(crate(proc-macro-crate)) = v1.3.1
Provides: bundled(crate(proc-macro-error)) = v1.0.4
Provides: bundled(crate(proc-macro-error-attr)) = v1.0.4
Provides: bundled(crate(proc-macro2)) = v1.0.53
Provides: bundled(crate(prost)) = v0.11.8
Provides: bundled(crate(prost-build)) = v0.11.8
Provides: bundled(crate(prost-derive)) = v0.11.8
Provides: bundled(crate(prost-types)) = v0.11.8
Provides: bundled(crate(quote)) = v1.0.26
Provides: bundled(crate(rand)) = v0.8.5
Provides: bundled(crate(rand_chacha)) = v0.3.1
Provides: bundled(crate(rand_core)) = v0.6.4
Provides: bundled(crate(regex)) = v1.7.1
Provides: bundled(crate(regex-syntax)) = v0.6.28
Provides: bundled(crate(rtnetlink)) = v0.12.0
Provides: bundled(crate(rustix)) = v0.36.9
Provides: bundled(crate(rustversion)) = v1.0.12
Provides: bundled(crate(ryu)) = v1.0.13
Provides: bundled(crate(same-file)) = v1.0.6
Provides: bundled(crate(serde)) = v1.0.159
Provides: bundled(crate(serde-value)) = v0.7.0
Provides: bundled(crate(serde_derive)) = v1.0.159
Provides: bundled(crate(serde_json)) = v1.0.95
Provides: bundled(crate(serde_repr)) = v0.1.11
Provides: bundled(crate(sha1)) = v0.10.5
Provides: bundled(crate(sha2)) = v0.10.6
Provides: bundled(crate(signal-hook-registry)) = v1.4.1
Provides: bundled(crate(slab)) = v0.4.8
Provides: bundled(crate(smallvec)) = v1.10.0
Provides: bundled(crate(socket2)) = v0.4.9
Provides: bundled(crate(static_assertions)) = v1.1.0
Provides: bundled(crate(strsim)) = v0.10.0
Provides: bundled(crate(syn)) = v2.0.12
Provides: bundled(crate(sync_wrapper)) = v0.1.2
Provides: bundled(crate(sysctl)) = v0.5.4
Provides: bundled(crate(tempfile)) = v3.4.0
Provides: bundled(crate(termcolor)) = v1.2.0
Provides: bundled(crate(textwrap)) = v0.16.0
Provides: bundled(crate(thiserror)) = v1.0.39
Provides: bundled(crate(thiserror-impl)) = v1.0.39
Provides: bundled(crate(tinyvec)) = v1.6.0
Provides: bundled(crate(tinyvec_macros)) = v0.1.1
Provides: bundled(crate(tokio)) = v1.27.0
Provides: bundled(crate(tokio-io-timeout)) = v1.2.0
Provides: bundled(crate(tokio-macros)) = v2.0.0
Provides: bundled(crate(tokio-stream)) = v0.1.12
Provides: bundled(crate(tokio-util)) = v0.7.7
Provides: bundled(crate(toml_datetime)) = v0.6.1
Provides: bundled(crate(toml_edit)) = v0.19.4
Provides: bundled(crate(tonic)) = v0.9.1
Provides: bundled(crate(tonic-build)) = v0.8.4
Provides: bundled(crate(tower)) = v0.4.13
Provides: bundled(crate(tower-layer)) = v0.3.2
Provides: bundled(crate(tower-service)) = v0.3.2
Provides: bundled(crate(tracing)) = v0.1.37
Provides: bundled(crate(tracing-attributes)) = v0.1.23
Provides: bundled(crate(tracing-core)) = v0.1.30
Provides: bundled(crate(trust-dns-proto)) = v0.22.0
Provides: bundled(crate(try-lock)) = v0.2.4
Provides: bundled(crate(typenum)) = v1.16.0
Provides: bundled(crate(unicode-bidi)) = v0.3.10
Provides: bundled(crate(unicode-ident)) = v1.0.8
Provides: bundled(crate(unicode-normalization)) = v0.1.22
Provides: bundled(crate(url)) = v2.3.1
Provides: bundled(crate(version_check)) = v0.9.4
Provides: bundled(crate(waker-fn)) = v1.1.0
Provides: bundled(crate(walkdir)) = v2.3.2
Provides: bundled(crate(want)) = v0.3.0
Provides: bundled(crate(which)) = v4.4.0
Provides: bundled(crate(winnow)) = v0.3.4
Provides: bundled(crate(zbus)) = v3.11.1
Provides: bundled(crate(zbus_macros)) = v3.11.1
Provides: bundled(crate(zbus_names)) = v2.5.0
Provides: bundled(crate(zvariant)) = v3.11.0
Provides: bundled(crate(zvariant_derive)) = v3.11.0
Provides: bundled(crate(zvariant_utils)) = v1.0.0

%description
%{summary}

Netavark is a rust based network stack for containers. It is being
designed to work with Podman but is also applicable for other OCI
container management applications.

Netavark is a tool for configuring networking for Linux containers.
Its features include:
* Configuration of container networks via JSON configuration file
* Creation and management of required network interfaces,
    including MACVLAN networks
* All required firewall configuration to perform NAT and port
    forwarding as required for containers
* Support for iptables and firewalld at present, with support
    for nftables planned in a future release
* Support for rootless containers
* Support for IPv4 and IPv6
* Support for container DNS resolution via aardvark-dns.

%prep
%autosetup -Sgit %{name}-%{built_tag_strip}
tar fx %{SOURCE1}
mkdir -p .cargo

cat >.cargo/config << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."https://github.com/containers/netavark-dhcp-proxy"]
git = "https://github.com/containers/netavark-dhcp-proxy"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%{__cargo} build --release
mkdir -p bin
cp target/release/%{name} bin/

cd docs
go-md2man -in %{name}.1.md -out %{name}.1

%install
%{__make} DESTDIR=%{buildroot} PREFIX=%{_prefix} install

%preun
%systemd_preun %{name}-dhcp-proxy.service

%postun
%systemd_postun %{name}-dhcp-proxy.service

%files
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/%{name}*
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}-dhcp-proxy.service
%{_unitdir}/%{name}-dhcp-proxy.socket

%changelog
%autochangelog
