# Building from fedora dependencies not possible
# Latest upstream rtnetlink frequently required
# sha2, zbus, zvariant are currently out of date

%global debug_package %{nil}

%global built_tag v1.4.0
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: netavark
Version: %{gen_version}
Release: %autorelease
License: ASL 2.0 and BSD and MIT
ExclusiveArch: %{rust_arches}
Summary: OCI network stack
URL: https://github.com/containers/%{name}
# Tarballs fetched from upstream's release page
Source0: %{url}/archive/%{built_tag}.tar.gz
Source1: %{url}/releases/download/%{built_tag}/%{name}-%{built_tag}-vendor.tar.gz
BuildRequires: cargo
%ifarch %{golang_arches}
BuildRequires: go-md2man
%endif
Recommends: aardvark-dns >= 1.2.0
Requires: (aardvark-dns >= 1.2.0 if fedora-release-identity-server)
Provides: container-network-stack = 2
BuildRequires: make
BuildRequires: rust-srpm-macros
BuildRequires: git-core
# Generated using:
# cargo tree --prefix none | awk '{print "Provides: bundled(crate("$1")) = "$2}' | sort | uniq
Provides: bundled(crate(aho-corasick)) = v0.7.18
Provides: bundled(crate(anyhow)) = v1.0.65
Provides: bundled(crate(async-broadcast)) = v0.4.0
Provides: bundled(crate(async-channel)) = v1.6.1
Provides: bundled(crate(async-executor)) = v1.4.1
Provides: bundled(crate(async-io)) = v1.7.0
Provides: bundled(crate(async-lock)) = v2.5.0
Provides: bundled(crate(async-recursion)) = v0.3.2
Provides: bundled(crate(async-task)) = v4.3.0
Provides: bundled(crate(async-trait)) = v0.1.56
Provides: bundled(crate(atty)) = v0.2.14
Provides: bundled(crate(autocfg)) = v1.1.0
Provides: bundled(crate(bitflags)) = v1.3.2
Provides: bundled(crate(block-buffer)) = v0.10.2
Provides: bundled(crate(byteorder)) = v1.4.3
Provides: bundled(crate(bytes)) = v1.1.0
Provides: bundled(crate(cache-padded)) = v1.2.0
Provides: bundled(crate(cfg-if)) = v1.0.0
Provides: bundled(crate(chrono)) = v0.4.22
Provides: bundled(crate(clap)) = v3.2.8
Provides: bundled(crate(clap_derive)) = v3.2.7
Provides: bundled(crate(clap_lex)) = v0.2.4
Provides: bundled(crate(concurrent-queue)) = v1.2.2
Provides: bundled(crate(cpufeatures)) = v0.2.2
Provides: bundled(crate(crypto-common)) = v0.1.5
Provides: bundled(crate(derivative)) = v2.2.0
Provides: bundled(crate(digest)) = v0.10.5
Provides: bundled(crate(dirs)) = v4.0.0
Provides: bundled(crate(dirs-sys)) = v0.3.7
Provides: bundled(crate(easy-parallel)) = v3.2.0
Provides: bundled(crate(enumflags2)) = v0.7.5
Provides: bundled(crate(enumflags2_derive)) = v0.7.4
Provides: bundled(crate(env_logger)) = v0.9.1
Provides: bundled(crate(event-listener)) = v2.5.2
Provides: bundled(crate(fastrand)) = v1.7.0
Provides: bundled(crate(form_urlencoded)) = v1.1.0
Provides: bundled(crate(fs2)) = v0.4.3
Provides: bundled(crate(futures)) = v0.3.24
Provides: bundled(crate(futures-channel)) = v0.3.24
Provides: bundled(crate(futures-core)) = v0.3.24
Provides: bundled(crate(futures-executor)) = v0.3.24
Provides: bundled(crate(futures-io)) = v0.3.24
Provides: bundled(crate(futures-lite)) = v1.12.0
Provides: bundled(crate(futures-macro)) = v0.3.24
Provides: bundled(crate(futures-sink)) = v0.3.24
Provides: bundled(crate(futures-task)) = v0.3.24
Provides: bundled(crate(futures-util)) = v0.3.24
Provides: bundled(crate(generic-array)) = v0.14.5
Provides: bundled(crate(getrandom)) = v0.2.7
Provides: bundled(crate(hashbrown)) = v0.12.2
Provides: bundled(crate(heck)) = v0.4.0
Provides: bundled(crate(hex)) = v0.4.3
Provides: bundled(crate(humantime)) = v2.1.0
Provides: bundled(crate(iana-time-zone)) = v0.1.46
Provides: bundled(crate(idna)) = v0.3.0
Provides: bundled(crate(indexmap)) = v1.9.1
Provides: bundled(crate(instant)) = v0.1.12
Provides: bundled(crate(ipnet)) = v2.5.0
Provides: bundled(crate(iptables)) = v0.5.0
Provides: bundled(crate(itoa)) = v1.0.2
Provides: bundled(crate(lazy_static)) = v1.4.0
Provides: bundled(crate(libc)) = v0.2.133
Provides: bundled(crate(lock_api)) = v0.4.7
Provides: bundled(crate(log)) = v0.4.17
Provides: bundled(crate(memchr)) = v2.5.0
Provides: bundled(crate(memoffset)) = v0.6.5
Provides: bundled(crate(mio)) = v0.8.4
Provides: bundled(crate(netavark)) = v1.2.0
Provides: bundled(crate(netlink-packet-core)) = v0.4.2
Provides: bundled(crate(netlink-packet-route)) = v0.13.0
Provides: bundled(crate(netlink-packet-utils)) = v0.5.1
Provides: bundled(crate(netlink-proto)) = v0.10.0
Provides: bundled(crate(netlink-sys)) = v0.8.3
Provides: bundled(crate(nix)) = v0.25.0
Provides: bundled(crate(num-integer)) = v0.1.45
Provides: bundled(crate(num-traits)) = v0.2.15
Provides: bundled(crate(num_cpus)) = v1.13.1
Provides: bundled(crate(once_cell)) = v1.13.0
Provides: bundled(crate(ordered-float)) = v2.10.0
Provides: bundled(crate(ordered-stream)) = v0.0.1
Provides: bundled(crate(os_str_bytes)) = v6.1.0
Provides: bundled(crate(parking)) = v2.0.0
Provides: bundled(crate(parking_lot)) = v0.12.1
Provides: bundled(crate(parking_lot_core)) = v0.9.3
Provides: bundled(crate(paste)) = v1.0.7
Provides: bundled(crate(percent-encoding)) = v2.2.0
Provides: bundled(crate(pin-project-lite)) = v0.2.9
Provides: bundled(crate(pin-utils)) = v0.1.0
Provides: bundled(crate(polling)) = v2.2.0
Provides: bundled(crate(ppv-lite86)) = v0.2.16
Provides: bundled(crate(proc-macro-crate)) = v1.1.3
Provides: bundled(crate(proc-macro-error)) = v1.0.4
Provides: bundled(crate(proc-macro-error-attr)) = v1.0.4
Provides: bundled(crate(proc-macro2)) = v1.0.40
Provides: bundled(crate(quote)) = v1.0.20
Provides: bundled(crate(rand)) = v0.8.5
Provides: bundled(crate(rand_chacha)) = v0.3.1
Provides: bundled(crate(rand_core)) = v0.6.3
Provides: bundled(crate(regex)) = v1.6.0
Provides: bundled(crate(regex-syntax)) = v0.6.27
Provides: bundled(crate(rtnetlink)) = v0.11.0
Provides: bundled(crate(ryu)) = v1.0.10
Provides: bundled(crate(same-file)) = v1.0.6
Provides: bundled(crate(scopeguard)) = v1.1.0
Provides: bundled(crate(serde)) = v1.0.144
Provides: bundled(crate(serde-value)) = v0.7.0
Provides: bundled(crate(serde_derive)) = v1.0.144
Provides: bundled(crate(serde_json)) = v1.0.85
Provides: bundled(crate(serde_repr)) = v0.1.8
Provides: bundled(crate(sha1)) = v0.6.1
Provides: bundled(crate(sha1_smol)) = v1.0.0
Provides: bundled(crate(sha2)) = v0.10.6
Provides: bundled(crate(signal-hook-registry)) = v1.4.0
Provides: bundled(crate(slab)) = v0.4.6
Provides: bundled(crate(smallvec)) = v1.9.0
Provides: bundled(crate(socket2)) = v0.4.4
Provides: bundled(crate(static_assertions)) = v1.1.0
Provides: bundled(crate(strsim)) = v0.10.0
Provides: bundled(crate(syn)) = v1.0.98
Provides: bundled(crate(sysctl)) = v0.5.2
Provides: bundled(crate(termcolor)) = v1.1.3
Provides: bundled(crate(textwrap)) = v0.15.0
Provides: bundled(crate(thiserror)) = v1.0.34
Provides: bundled(crate(thiserror-impl)) = v1.0.34
Provides: bundled(crate(time)) = v0.1.44
Provides: bundled(crate(tinyvec)) = v1.6.0
Provides: bundled(crate(tinyvec_macros)) = v0.1.0
Provides: bundled(crate(tokio)) = v1.21.1
Provides: bundled(crate(tokio-macros)) = v1.8.0
Provides: bundled(crate(toml)) = v0.5.9
Provides: bundled(crate(tracing)) = v0.1.35
Provides: bundled(crate(tracing-attributes)) = v0.1.22
Provides: bundled(crate(tracing-core)) = v0.1.28
Provides: bundled(crate(typenum)) = v1.15.0
Provides: bundled(crate(unicode-bidi)) = v0.3.8
Provides: bundled(crate(unicode-ident)) = v1.0.1
Provides: bundled(crate(unicode-normalization)) = v0.1.21
Provides: bundled(crate(url)) = v2.3.1
Provides: bundled(crate(version_check)) = v0.9.4
Provides: bundled(crate(waker-fn)) = v1.1.0
Provides: bundled(crate(walkdir)) = v2.3.2
Provides: bundled(crate(zbus)) = v2.3.2
Provides: bundled(crate(zbus_macros)) = v2.3.2
Provides: bundled(crate(zbus_names)) = v2.1.0
Provides: bundled(crate(zvariant)) = v3.4.1
Provides: bundled(crate(zvariant_derive)) = v3.4.1

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

[source.vendored-sources]
directory = "vendor"
EOF

%build
%{__make} build

%ifarch %{golang_arches}
cd docs
go-md2man -in %{name}.1.md -out %{name}.1
%endif

%install
%ifarch %{golang_arches}
%{__make} DESTDIR=%{buildroot} PREFIX=%{_prefix} install
%else
# no manpage, install only the binary
install -D -m0755 bin/netavark %{buildroot}%{_libexecdir}/podman/%{name}
%endif

%files
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/%{name}
%ifarch %{golang_arches}
%{_mandir}/man1/%{name}.1*
%endif

%changelog
%autochangelog
