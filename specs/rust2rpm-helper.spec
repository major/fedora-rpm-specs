%bcond check 1

%global crate rust2rpm-helper

Name:           rust2rpm-helper
Version:        0.1.9
Release:        %autorelease
Summary:        Helper program for rust2rpm

SourceLicense:  MIT
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        MIT AND Apache-2.0 AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://codeberg.org/rust2rpm/rust2rpm-helper
Source:         %{url}/archive/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26

%description
Helper program for rust2rpm.

%prep
%autosetup -n %{name} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dpm 0755 target/rpm/rust2rpm-helper -t %{buildroot}/%{_bindir}/

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc README.md
%{_bindir}/rust2rpm-helper

%changelog
%autochangelog
