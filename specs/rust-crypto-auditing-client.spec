# Generated by rust2rpm 26
%bcond_without check

%global crate crypto-auditing-client

Name:           rust-crypto-auditing-client
Version:        0.2.3
Release:        %autorelease
Summary:        Event broker client for crypto-auditing project

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/crypto-auditing-client
Source:         %{crates_source}
Source1:	client.conf

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Event broker client for crypto-auditing project.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Upstream license specification: GPL-3.0-or-later
#
# The build dependencies have the following licenses:
#
#   (MIT OR Apache-2.0) AND Unicode-DFS-2016
#   Apache-2.0 OR BSL-1.0
#   Apache-2.0 OR MIT
#   GPL-3.0-or-later
#   MIT
#   MIT OR Apache-2.0
#   Unlicense OR MIT
#
License:        GPL-3.0-or-later AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND MIT AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown
Requires:       crypto-auditing-agent

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/crypto-auditing-client
%config(noreplace) %{_sysconfdir}/crypto-auditing/client.conf
%dir %{_sysconfdir}/crypto-auditing/

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/crypto-auditing
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/crypto-auditing

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
