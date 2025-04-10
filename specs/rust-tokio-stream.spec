# Generated by rust2rpm 27
# * tests can only be run in-tree
%bcond check 0
%global debug_package %{nil}

%global crate tokio-stream

Name:           rust-tokio-stream
Version:        0.1.17
Release:        %autorelease
Summary:        Utilities to work with Stream and tokio

License:        MIT
URL:            https://crates.io/crates/tokio-stream
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Utilities to work with `Stream` and `tokio`.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+fs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fs-devel %{_description}

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%files       -n %{name}+fs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+io-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+io-util-devel %{_description}

This package contains library source intended for building other packages which
use the "io-util" feature of the "%{crate}" crate.

%files       -n %{name}+io-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+net-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+net-devel %{_description}

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%files       -n %{name}+net-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+signal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+signal-devel %{_description}

This package contains library source intended for building other packages which
use the "signal" feature of the "%{crate}" crate.

%files       -n %{name}+signal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sync-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sync-devel %{_description}

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%files       -n %{name}+sync-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-util-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-util-devel
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
