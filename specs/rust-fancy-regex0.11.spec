# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate fancy-regex

Name:           rust-fancy-regex0.11
Version:        0.11.0
Release:        %autorelease
Summary:        An implementation of regexes, supporting a relatively rich set of features

License:        MIT
URL:            https://crates.io/crates/fancy-regex
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
Patch:          fancy-regex-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
An implementation of regexes, supporting a relatively rich set of
features, including backreferences and look-around.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/AUTHORS
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/PERFORMANCE.md
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

%package     -n %{name}+perf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-devel %{_description}

This package contains library source intended for building other packages which
use the "perf" feature of the "%{crate}" crate.

%files       -n %{name}+perf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+perf-cache-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-cache-devel %{_description}

This package contains library source intended for building other packages which
use the "perf-cache" feature of the "%{crate}" crate.

%files       -n %{name}+perf-cache-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+perf-dfa-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-dfa-devel %{_description}

This package contains library source intended for building other packages which
use the "perf-dfa" feature of the "%{crate}" crate.

%files       -n %{name}+perf-dfa-devel
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

%package     -n %{name}+track_caller-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+track_caller-devel %{_description}

This package contains library source intended for building other packages which
use the "track_caller" feature of the "%{crate}" crate.

%files       -n %{name}+track_caller-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-devel
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
