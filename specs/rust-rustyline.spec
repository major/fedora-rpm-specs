# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate rustyline

Name:           rust-rustyline
Version:        13.0.0
Release:        %autorelease
Summary:        Readline implementation based on Antirez's Linenoise

License:        MIT
URL:            https://crates.io/crates/rustyline
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          rustyline-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * relax rusqlite dependency from ^0.30 to >=0.28,<0.31
# * drop rusqlite/bundled feature for statically linking sqlite
Patch:          rustyline-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Rustyline, a readline implementation based on Antirez's Linenoise.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/Ansi.md
%doc %{crate_instdir}/BUGS.md
%doc %{crate_instdir}/CustomBinding.md
%doc %{crate_instdir}/Features.md
%doc %{crate_instdir}/History.md
%doc %{crate_instdir}/Incremental.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/TODO.md
%doc %{crate_instdir}/linenoise.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+case_insensitive_history_search-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+case_insensitive_history_search-devel %{_description}

This package contains library source intended for building other packages which
use the "case_insensitive_history_search" feature of the "%{crate}" crate.

%files       -n %{name}+case_insensitive_history_search-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+custom-bindings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+custom-bindings-devel %{_description}

This package contains library source intended for building other packages which
use the "custom-bindings" feature of the "%{crate}" crate.

%files       -n %{name}+custom-bindings-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fd-lock-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fd-lock-devel %{_description}

This package contains library source intended for building other packages which
use the "fd-lock" feature of the "%{crate}" crate.

%files       -n %{name}+fd-lock-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+home-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+home-devel %{_description}

This package contains library source intended for building other packages which
use the "home" feature of the "%{crate}" crate.

%files       -n %{name}+home-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+radix_trie-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+radix_trie-devel %{_description}

This package contains library source intended for building other packages which
use the "radix_trie" feature of the "%{crate}" crate.

%files       -n %{name}+radix_trie-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rusqlite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rusqlite-devel %{_description}

This package contains library source intended for building other packages which
use the "rusqlite" feature of the "%{crate}" crate.

%files       -n %{name}+rusqlite-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustyline-derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustyline-derive-devel %{_description}

This package contains library source intended for building other packages which
use the "rustyline-derive" feature of the "%{crate}" crate.

%files       -n %{name}+rustyline-derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+signal-hook-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+signal-hook-devel %{_description}

This package contains library source intended for building other packages which
use the "signal-hook" feature of the "%{crate}" crate.

%files       -n %{name}+signal-hook-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+skim-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+skim-devel %{_description}

This package contains library source intended for building other packages which
use the "skim" feature of the "%{crate}" crate.

%files       -n %{name}+skim-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+termios-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+termios-devel %{_description}

This package contains library source intended for building other packages which
use the "termios" feature of the "%{crate}" crate.

%files       -n %{name}+termios-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-dirs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-dirs-devel %{_description}

This package contains library source intended for building other packages which
use the "with-dirs" feature of the "%{crate}" crate.

%files       -n %{name}+with-dirs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-file-history-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-file-history-devel %{_description}

This package contains library source intended for building other packages which
use the "with-file-history" feature of the "%{crate}" crate.

%files       -n %{name}+with-file-history-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-fuzzy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-fuzzy-devel %{_description}

This package contains library source intended for building other packages which
use the "with-fuzzy" feature of the "%{crate}" crate.

%files       -n %{name}+with-fuzzy-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-sqlite-history-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-sqlite-history-devel %{_description}

This package contains library source intended for building other packages which
use the "with-sqlite-history" feature of the "%{crate}" crate.

%files       -n %{name}+with-sqlite-history-devel
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
# * skip test for exact struct size that fails on 32-bit architectures:
#   https://github.com/kkawakam/rustyline/issues/740
%cargo_test -- -- --exact --skip binding::test::size_of_event
%endif

%changelog
%autochangelog
