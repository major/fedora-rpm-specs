# Generated by rust2rpm 27
# * missing dev-dependencies: unic-emoji-char ^0.9
%bcond check 0
%global debug_package %{nil}

%global crate textwrap

Name:           rust-textwrap
Version:        0.16.2
Release:        %autorelease
Summary:        Library for word wrapping, indenting, and dedenting strings

License:        MIT
URL:            https://crates.io/crates/textwrap
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Library for word wrapping, indenting, and dedenting strings. Has
optional support for Unicode and emojis as well as machine hyphenation.}

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

%package     -n %{name}+smawk-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+smawk-devel %{_description}

This package contains library source intended for building other packages which
use the "smawk" feature of the "%{crate}" crate.

%files       -n %{name}+smawk-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+terminal_size-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+terminal_size-devel %{_description}

This package contains library source intended for building other packages which
use the "terminal_size" feature of the "%{crate}" crate.

%files       -n %{name}+terminal_size-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-linebreak-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-linebreak-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-linebreak" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-linebreak-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-width-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-width-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-width" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-width-devel
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
