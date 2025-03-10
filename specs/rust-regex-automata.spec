# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate regex-automata

Name:           rust-regex-automata
Version:        0.4.9
Release:        %autorelease
Summary:        Automata construction and matching using regular expressions

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/regex-automata
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Automata construction and matching using regular expressions.}

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
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dfa-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dfa-devel %{_description}

This package contains library source intended for building other packages which
use the "dfa" feature of the "%{crate}" crate.

%files       -n %{name}+dfa-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dfa-build-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dfa-build-devel %{_description}

This package contains library source intended for building other packages which
use the "dfa-build" feature of the "%{crate}" crate.

%files       -n %{name}+dfa-build-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dfa-onepass-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dfa-onepass-devel %{_description}

This package contains library source intended for building other packages which
use the "dfa-onepass" feature of the "%{crate}" crate.

%files       -n %{name}+dfa-onepass-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dfa-search-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dfa-search-devel %{_description}

This package contains library source intended for building other packages which
use the "dfa-search" feature of the "%{crate}" crate.

%files       -n %{name}+dfa-search-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hybrid-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hybrid-devel %{_description}

This package contains library source intended for building other packages which
use the "hybrid" feature of the "%{crate}" crate.

%files       -n %{name}+hybrid-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+internal-instrument-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+internal-instrument-devel %{_description}

This package contains library source intended for building other packages which
use the "internal-instrument" feature of the "%{crate}" crate.

%files       -n %{name}+internal-instrument-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+internal-instrument-pikevm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+internal-instrument-pikevm-devel %{_description}

This package contains library source intended for building other packages which
use the "internal-instrument-pikevm" feature of the "%{crate}" crate.

%files       -n %{name}+internal-instrument-pikevm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+logging-devel %{_description}

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%files       -n %{name}+logging-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+meta-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+meta-devel %{_description}

This package contains library source intended for building other packages which
use the "meta" feature of the "%{crate}" crate.

%files       -n %{name}+meta-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nfa-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nfa-devel %{_description}

This package contains library source intended for building other packages which
use the "nfa" feature of the "%{crate}" crate.

%files       -n %{name}+nfa-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nfa-backtrack-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nfa-backtrack-devel %{_description}

This package contains library source intended for building other packages which
use the "nfa-backtrack" feature of the "%{crate}" crate.

%files       -n %{name}+nfa-backtrack-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nfa-pikevm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nfa-pikevm-devel %{_description}

This package contains library source intended for building other packages which
use the "nfa-pikevm" feature of the "%{crate}" crate.

%files       -n %{name}+nfa-pikevm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nfa-thompson-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nfa-thompson-devel %{_description}

This package contains library source intended for building other packages which
use the "nfa-thompson" feature of the "%{crate}" crate.

%files       -n %{name}+nfa-thompson-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+perf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-devel %{_description}

This package contains library source intended for building other packages which
use the "perf" feature of the "%{crate}" crate.

%files       -n %{name}+perf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+perf-inline-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-inline-devel %{_description}

This package contains library source intended for building other packages which
use the "perf-inline" feature of the "%{crate}" crate.

%files       -n %{name}+perf-inline-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+perf-literal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-literal-devel %{_description}

This package contains library source intended for building other packages which
use the "perf-literal" feature of the "%{crate}" crate.

%files       -n %{name}+perf-literal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+perf-literal-multisubstring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-literal-multisubstring-devel %{_description}

This package contains library source intended for building other packages which
use the "perf-literal-multisubstring" feature of the "%{crate}" crate.

%files       -n %{name}+perf-literal-multisubstring-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+perf-literal-substring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-literal-substring-devel %{_description}

This package contains library source intended for building other packages which
use the "perf-literal-substring" feature of the "%{crate}" crate.

%files       -n %{name}+perf-literal-substring-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+syntax-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+syntax-devel %{_description}

This package contains library source intended for building other packages which
use the "syntax" feature of the "%{crate}" crate.

%files       -n %{name}+syntax-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-age-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-age-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-age" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-age-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-bool-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-bool-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-bool" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-bool-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-case-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-case-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-case" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-case-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-gencat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-gencat-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-gencat" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-gencat-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-perl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-perl-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-perl" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-perl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-script-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-script-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-script" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-script-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-segment-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-segment-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-segment" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-segment-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-word-boundary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-word-boundary-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-word-boundary" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-word-boundary-devel
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
# * integration tests can only be run in-tree
# * skip one doctest that fails depending on Rust version and architecture:
#   https://github.com/rust-lang/regex/issues/1230
%cargo_test -- --lib
%cargo_test -- --doc -- --skip nfa::thompson::compiler::Config::nfa_size_limit
%endif

%changelog
%autochangelog
