# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate gix

Name:           rust-gix
Version:        0.70.0
Release:        %autorelease
Summary:        Interact with git repositories just like git would

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Interact with git repositories just like git would.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-network-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-network-client-devel %{_description}

This package contains library source intended for building other packages which
use the "async-network-client" feature of the "%{crate}" crate.

%files       -n %{name}+async-network-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-network-client-async-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-network-client-async-std-devel %{_description}

This package contains library source intended for building other packages which
use the "async-network-client-async-std" feature of the "%{crate}" crate.

%files       -n %{name}+async-network-client-async-std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-std-devel %{_description}

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%files       -n %{name}+async-std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+attributes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+attributes-devel %{_description}

This package contains library source intended for building other packages which
use the "attributes" feature of the "%{crate}" crate.

%files       -n %{name}+attributes-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+basic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+basic-devel %{_description}

This package contains library source intended for building other packages which
use the "basic" feature of the "%{crate}" crate.

%files       -n %{name}+basic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blame-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blame-devel %{_description}

This package contains library source intended for building other packages which
use the "blame" feature of the "%{crate}" crate.

%files       -n %{name}+blame-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blob-diff-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blob-diff-devel %{_description}

This package contains library source intended for building other packages which
use the "blob-diff" feature of the "%{crate}" crate.

%files       -n %{name}+blob-diff-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-http-transport-curl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-http-transport-curl-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking-http-transport-curl" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-http-transport-curl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-http-transport-reqwest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-http-transport-reqwest-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking-http-transport-reqwest" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-http-transport-reqwest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-http-transport-reqwest-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-http-transport-reqwest-native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking-http-transport-reqwest-native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-http-transport-reqwest-native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-http-transport-reqwest-rust-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-http-transport-reqwest-rust-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking-http-transport-reqwest-rust-tls" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-http-transport-reqwest-rust-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-http-transport-reqwest-rust-tls-trust-dns-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-http-transport-reqwest-rust-tls-trust-dns-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking-http-transport-reqwest-rust-tls-trust-dns" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-http-transport-reqwest-rust-tls-trust-dns-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-network-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-network-client-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking-network-client" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-network-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cache-efficiency-debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cache-efficiency-debug-devel %{_description}

This package contains library source intended for building other packages which
use the "cache-efficiency-debug" feature of the "%{crate}" crate.

%files       -n %{name}+cache-efficiency-debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+comfort-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+comfort-devel %{_description}

This package contains library source intended for building other packages which
use the "comfort" feature of the "%{crate}" crate.

%files       -n %{name}+comfort-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+command-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+command-devel %{_description}

This package contains library source intended for building other packages which
use the "command" feature of the "%{crate}" crate.

%files       -n %{name}+command-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+credentials-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+credentials-devel %{_description}

This package contains library source intended for building other packages which
use the "credentials" feature of the "%{crate}" crate.

%files       -n %{name}+credentials-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dirwalk-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dirwalk-devel %{_description}

This package contains library source intended for building other packages which
use the "dirwalk" feature of the "%{crate}" crate.

%files       -n %{name}+dirwalk-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+document-features-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+document-features-devel %{_description}

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%files       -n %{name}+document-features-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+excludes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+excludes-devel %{_description}

This package contains library source intended for building other packages which
use the "excludes" feature of the "%{crate}" crate.

%files       -n %{name}+excludes-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+extras-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extras-devel %{_description}

This package contains library source intended for building other packages which
use the "extras" feature of the "%{crate}" crate.

%files       -n %{name}+extras-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fast-sha1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fast-sha1-devel %{_description}

This package contains library source intended for building other packages which
use the "fast-sha1" feature of the "%{crate}" crate.

%files       -n %{name}+fast-sha1-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gix-archive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gix-archive-devel %{_description}

This package contains library source intended for building other packages which
use the "gix-archive" feature of the "%{crate}" crate.

%files       -n %{name}+gix-archive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gix-status-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gix-status-devel %{_description}

This package contains library source intended for building other packages which
use the "gix-status" feature of the "%{crate}" crate.

%files       -n %{name}+gix-status-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gix-worktree-stream-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gix-worktree-stream-devel %{_description}

This package contains library source intended for building other packages which
use the "gix-worktree-stream" feature of the "%{crate}" crate.

%files       -n %{name}+gix-worktree-stream-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hp-tempfile-registry-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hp-tempfile-registry-devel %{_description}

This package contains library source intended for building other packages which
use the "hp-tempfile-registry" feature of the "%{crate}" crate.

%files       -n %{name}+hp-tempfile-registry-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+index-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+index-devel %{_description}

This package contains library source intended for building other packages which
use the "index" feature of the "%{crate}" crate.

%files       -n %{name}+index-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+interrupt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+interrupt-devel %{_description}

This package contains library source intended for building other packages which
use the "interrupt" feature of the "%{crate}" crate.

%files       -n %{name}+interrupt-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mailmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mailmap-devel %{_description}

This package contains library source intended for building other packages which
use the "mailmap" feature of the "%{crate}" crate.

%files       -n %{name}+mailmap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max-control-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max-control-devel %{_description}

This package contains library source intended for building other packages which
use the "max-control" feature of the "%{crate}" crate.

%files       -n %{name}+max-control-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max-performance-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max-performance-devel %{_description}

This package contains library source intended for building other packages which
use the "max-performance" feature of the "%{crate}" crate.

%files       -n %{name}+max-performance-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max-performance-safe-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max-performance-safe-devel %{_description}

This package contains library source intended for building other packages which
use the "max-performance-safe" feature of the "%{crate}" crate.

%files       -n %{name}+max-performance-safe-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+merge-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+merge-devel %{_description}

This package contains library source intended for building other packages which
use the "merge" feature of the "%{crate}" crate.

%files       -n %{name}+merge-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+need-more-recent-msrv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+need-more-recent-msrv-devel %{_description}

This package contains library source intended for building other packages which
use the "need-more-recent-msrv" feature of the "%{crate}" crate.

%files       -n %{name}+need-more-recent-msrv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pack-cache-lru-dynamic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pack-cache-lru-dynamic-devel %{_description}

This package contains library source intended for building other packages which
use the "pack-cache-lru-dynamic" feature of the "%{crate}" crate.

%files       -n %{name}+pack-cache-lru-dynamic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pack-cache-lru-static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pack-cache-lru-static-devel %{_description}

This package contains library source intended for building other packages which
use the "pack-cache-lru-static" feature of the "%{crate}" crate.

%files       -n %{name}+pack-cache-lru-static-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+parallel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parallel-devel %{_description}

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%files       -n %{name}+parallel-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+parallel-walkdir-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parallel-walkdir-devel %{_description}

This package contains library source intended for building other packages which
use the "parallel-walkdir" feature of the "%{crate}" crate.

%files       -n %{name}+parallel-walkdir-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prodash-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prodash-devel %{_description}

This package contains library source intended for building other packages which
use the "prodash" feature of the "%{crate}" crate.

%files       -n %{name}+prodash-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+progress-tree-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+progress-tree-devel %{_description}

This package contains library source intended for building other packages which
use the "progress-tree" feature of the "%{crate}" crate.

%files       -n %{name}+progress-tree-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+revision-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+revision-devel %{_description}

This package contains library source intended for building other packages which
use the "revision" feature of the "%{crate}" crate.

%files       -n %{name}+revision-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+revparse-regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+revparse-regex-devel %{_description}

This package contains library source intended for building other packages which
use the "revparse-regex" feature of the "%{crate}" crate.

%files       -n %{name}+revparse-regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+status-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+status-devel %{_description}

This package contains library source intended for building other packages which
use the "status" feature of the "%{crate}" crate.

%files       -n %{name}+status-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tracing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-devel %{_description}

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%files       -n %{name}+tracing-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tracing-detail-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-detail-devel %{_description}

This package contains library source intended for building other packages which
use the "tracing-detail" feature of the "%{crate}" crate.

%files       -n %{name}+tracing-detail-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tree-editor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tree-editor-devel %{_description}

This package contains library source intended for building other packages which
use the "tree-editor" feature of the "%{crate}" crate.

%files       -n %{name}+tree-editor-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+verbose-object-parsing-errors-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+verbose-object-parsing-errors-devel %{_description}

This package contains library source intended for building other packages which
use the "verbose-object-parsing-errors" feature of the "%{crate}" crate.

%files       -n %{name}+verbose-object-parsing-errors-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+worktree-archive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+worktree-archive-devel %{_description}

This package contains library source intended for building other packages which
use the "worktree-archive" feature of the "%{crate}" crate.

%files       -n %{name}+worktree-archive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+worktree-mutation-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+worktree-mutation-devel %{_description}

This package contains library source intended for building other packages which
use the "worktree-mutation" feature of the "%{crate}" crate.

%files       -n %{name}+worktree-mutation-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+worktree-stream-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+worktree-stream-devel %{_description}

This package contains library source intended for building other packages which
use the "worktree-stream" feature of the "%{crate}" crate.

%files       -n %{name}+worktree-stream-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zlib-ng-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zlib-ng-devel %{_description}

This package contains library source intended for building other packages which
use the "zlib-ng" feature of the "%{crate}" crate.

%files       -n %{name}+zlib-ng-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zlib-stock-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zlib-stock-devel %{_description}

This package contains library source intended for building other packages which
use the "zlib-stock" feature of the "%{crate}" crate.

%files       -n %{name}+zlib-stock-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
