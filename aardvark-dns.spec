# trust-dns-{client,server} not available
# using vendored deps

# debuginfo doesn't work yet
%global debug_package %{nil}

%global built_tag_strip 1.1.0

Name: aardvark-dns
Version: 1.1.0
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: ASL-2.0+
Release: 0%{?dist}
%else
License: ASL 2.0 and BSD and MIT
Release: %autorelease
ExclusiveArch: %{rust_arches}
%endif
Summary: Authoritative DNS server for A/AAAA container records
URL: https://github.com/containers/%{name}
Source0: %{url}/archive/v%{built_tag_strip}.tar.gz
Source1: %{url}/releases/download/v%{built_tag_strip}/%{name}-v%{built_tag_strip}-vendor.tar.gz
BuildRequires: cargo
%if "%{_vendor}" == "debbuild"
BuildRequires: git
%else
BuildRequires: git-core
BuildRequires: make
BuildRequires: rust-srpm-macros
# cargo tree --prefix none | awk '{print "Provides: bundled(crate("$1")) = "$2}' | sort | uniq
Provides: bundled(crate(aardvark-dns)) = v1.0.3
Provides: bundled(crate(aho-corasick)) = v0.7.18
Provides: bundled(crate(anyhow)) = v1.0.57
Provides: bundled(crate(async-broadcast)) = v0.4.0
Provides: bundled(crate(async-trait)) = v0.1.53
Provides: bundled(crate(atty)) = v0.2.14
Provides: bundled(crate(autocfg)) = v1.1.0
Provides: bundled(crate(bitflags)) = v1.3.2
Provides: bundled(crate(bytes)) = v1.1.0
Provides: bundled(crate(cfg-if)) = v1.0.0
Provides: bundled(crate(chrono)) = v0.4.19
Provides: bundled(crate(clap)) = v3.1.15
Provides: bundled(crate(clap_derive)) = v3.1.7
Provides: bundled(crate(clap_lex)) = v0.2.0
Provides: bundled(crate(data-encoding)) = v2.3.2
Provides: bundled(crate(easy-parallel)) = v3.2.0
Provides: bundled(crate(endian-type)) = v0.1.2
Provides: bundled(crate(enum-as-inner)) = v0.4.0
Provides: bundled(crate(env_logger)) = v0.9.0
Provides: bundled(crate(error-chain)) = v0.12.4
Provides: bundled(crate(event-listener)) = v2.5.2
Provides: bundled(crate(form_urlencoded)) = v1.0.1
Provides: bundled(crate(futures-channel)) = v0.3.21
Provides: bundled(crate(futures-core)) = v0.3.21
Provides: bundled(crate(futures-executor)) = v0.3.21
Provides: bundled(crate(futures-io)) = v0.3.21
Provides: bundled(crate(futures-macro)) = v0.3.21
Provides: bundled(crate(futures-task)) = v0.3.21
Provides: bundled(crate(futures-util)) = v0.3.21
Provides: bundled(crate(getrandom)) = v0.2.6
Provides: bundled(crate(hashbrown)) = v0.11.2
Provides: bundled(crate(heck)) = v0.4.0
Provides: bundled(crate(hostname)) = v0.3.1
Provides: bundled(crate(humantime)) = v2.1.0
Provides: bundled(crate(idna)) = v0.2.3
Provides: bundled(crate(indexmap)) = v1.8.1
Provides: bundled(crate(instant)) = v0.1.12
Provides: bundled(crate(ipnet)) = v2.5.0
Provides: bundled(crate(itoa)) = v1.0.1
Provides: bundled(crate(lazy_static)) = v1.4.0
Provides: bundled(crate(libc)) = v0.2.125
Provides: bundled(crate(lock_api)) = v0.4.7
Provides: bundled(crate(log)) = v0.4.17
Provides: bundled(crate(match_cfg)) = v0.1.0
Provides: bundled(crate(matches)) = v0.1.9
Provides: bundled(crate(memchr)) = v2.5.0
Provides: bundled(crate(mio)) = v0.8.2
Provides: bundled(crate(nibble_vec)) = v0.1.0
Provides: bundled(crate(num-integer)) = v0.1.45
Provides: bundled(crate(num-traits)) = v0.2.15
Provides: bundled(crate(num_cpus)) = v1.13.1
Provides: bundled(crate(num_threads)) = v0.1.6
Provides: bundled(crate(once_cell)) = v1.10.0
Provides: bundled(crate(os_str_bytes)) = v6.0.0
Provides: bundled(crate(parking_lot)) = v0.12.0
Provides: bundled(crate(parking_lot_core)) = v0.9.3
Provides: bundled(crate(percent-encoding)) = v2.1.0
Provides: bundled(crate(pin-project-lite)) = v0.2.9
Provides: bundled(crate(pin-utils)) = v0.1.0
Provides: bundled(crate(ppv-lite86)) = v0.2.16
Provides: bundled(crate(proc-macro-error)) = v1.0.4
Provides: bundled(crate(proc-macro-error-attr)) = v1.0.4
Provides: bundled(crate(proc-macro2)) = v1.0.37
Provides: bundled(crate(quick-error)) = v1.2.3
Provides: bundled(crate(quote)) = v1.0.18
Provides: bundled(crate(radix_trie)) = v0.2.1
Provides: bundled(crate(rand)) = v0.8.5
Provides: bundled(crate(rand_chacha)) = v0.3.1
Provides: bundled(crate(rand_core)) = v0.6.3
Provides: bundled(crate(regex)) = v1.5.5
Provides: bundled(crate(regex-syntax)) = v0.6.25
Provides: bundled(crate(resolv-conf)) = v0.7.0
Provides: bundled(crate(scopeguard)) = v1.1.0
Provides: bundled(crate(serde)) = v1.0.137
Provides: bundled(crate(serde_derive)) = v1.0.137
Provides: bundled(crate(signal-hook)) = v0.3.13
Provides: bundled(crate(signal-hook-registry)) = v1.4.0
Provides: bundled(crate(slab)) = v0.4.6
Provides: bundled(crate(smallvec)) = v1.8.0
Provides: bundled(crate(socket2)) = v0.4.4
Provides: bundled(crate(strsim)) = v0.10.0
Provides: bundled(crate(syn)) = v1.0.92
Provides: bundled(crate(syslog)) = v6.0.1
Provides: bundled(crate(termcolor)) = v1.1.3
Provides: bundled(crate(textwrap)) = v0.15.0
Provides: bundled(crate(thiserror)) = v1.0.31
Provides: bundled(crate(thiserror-impl)) = v1.0.31
Provides: bundled(crate(time)) = v0.3.9
Provides: bundled(crate(tinyvec)) = v1.6.0
Provides: bundled(crate(tinyvec_macros)) = v0.1.0
Provides: bundled(crate(tokio)) = v1.18.1
Provides: bundled(crate(tokio-macros)) = v1.7.0
Provides: bundled(crate(toml)) = v0.5.9
Provides: bundled(crate(trust-dns-client)) = v0.21.2
Provides: bundled(crate(trust-dns-proto)) = v0.21.2
Provides: bundled(crate(trust-dns-server)) = v0.21.2
Provides: bundled(crate(unicode-bidi)) = v0.3.8
Provides: bundled(crate(unicode-normalization)) = v0.1.19
Provides: bundled(crate(unicode-xid)) = v0.2.3
Provides: bundled(crate(url)) = v2.2.2
Provides: bundled(crate(version_check)) = v0.9.4
%endif

%description
%{summary}

Forwards other request to configured resolvers.
Read more about configuration in `src/backend/mod.rs`.

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

%install
%{__make} DESTDIR=%{buildroot} PREFIX=%{_prefix} install

%files
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/%{name}

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
