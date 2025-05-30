# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate cursive

Name:           rust-cursive0.20
Version:        0.20.0
Release:        %autorelease
Summary:        TUI (Text User Interface) library focused on ease-of-use

License:        MIT
URL:            https://crates.io/crates/cursive
Source:         %{crates_source}
# * License text linked in https://github.com/gyscos/cursive/pull/702
Source1:        https://github.com/gyscos/cursive/raw/main/LICENSE
# Manually created patch for downstream crate metadata changes
# * drop unused markdown support with outdated dependencies
Patch:          cursive-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A TUI (Text User Interface) library focused on ease-of-use.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/Readme.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crossterm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crossterm-devel %{_description}

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%files       -n %{name}+crossterm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crossterm-backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crossterm-backend-devel %{_description}

This package contains library source intended for building other packages which
use the "crossterm-backend" feature of the "%{crate}" crate.

%files       -n %{name}+crossterm-backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+doc-cfg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+doc-cfg-devel %{_description}

This package contains library source intended for building other packages which
use the "doc-cfg" feature of the "%{crate}" crate.

%files       -n %{name}+doc-cfg-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+maplit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+maplit-devel %{_description}

This package contains library source intended for building other packages which
use the "maplit" feature of the "%{crate}" crate.

%files       -n %{name}+maplit-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ncurses-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ncurses-devel %{_description}

This package contains library source intended for building other packages which
use the "ncurses" feature of the "%{crate}" crate.

%files       -n %{name}+ncurses-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ncurses-backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ncurses-backend-devel %{_description}

This package contains library source intended for building other packages which
use the "ncurses-backend" feature of the "%{crate}" crate.

%files       -n %{name}+ncurses-backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pancurses-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pancurses-devel %{_description}

This package contains library source intended for building other packages which
use the "pancurses" feature of the "%{crate}" crate.

%files       -n %{name}+pancurses-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pancurses-backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pancurses-backend-devel %{_description}

This package contains library source intended for building other packages which
use the "pancurses-backend" feature of the "%{crate}" crate.

%files       -n %{name}+pancurses-backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+term_size-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+term_size-devel %{_description}

This package contains library source intended for building other packages which
use the "term_size" feature of the "%{crate}" crate.

%files       -n %{name}+term_size-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+termion-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+termion-devel %{_description}

This package contains library source intended for building other packages which
use the "termion" feature of the "%{crate}" crate.

%files       -n %{name}+termion-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+termion-backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+termion-backend-devel %{_description}

This package contains library source intended for building other packages which
use the "termion-backend" feature of the "%{crate}" crate.

%files       -n %{name}+termion-backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+toml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+toml-devel %{_description}

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%files       -n %{name}+toml-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable_scroll-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable_scroll-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable_scroll" feature of the "%{crate}" crate.

%files       -n %{name}+unstable_scroll-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
cp -pav %{SOURCE1} .

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
