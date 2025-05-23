# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate binascii

Name:           rust-binascii
Version:        0.1.4
Release:        %autorelease
Summary:        Useful no-std binascii operations including base64, base32 and base16

License:        MIT
URL:            https://crates.io/crates/binascii
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Useful no-std binascii operations including base64, base32 and base16
(hex).}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
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

%package     -n %{name}+decode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+decode-devel %{_description}

This package contains library source intended for building other packages which
use the "decode" feature of the "%{crate}" crate.

%files       -n %{name}+decode-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+encode-devel %{_description}

This package contains library source intended for building other packages which
use the "encode" feature of the "%{crate}" crate.

%files       -n %{name}+encode-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
