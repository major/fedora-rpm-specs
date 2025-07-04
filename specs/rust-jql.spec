# Generated by rust2rpm 27
%bcond check 1

%global crate jql

Name:           rust-jql
Version:        8.0.6
Release:        %autorelease
Summary:        JQL is a fast and simple command-line tool to manipulate JSON data

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/jql
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Jql - JSON Query Language - is a fast and simple command-line tool to
manipulate JSON data.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# EPL-2.0
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND EPL-2.0 AND MIT AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%doc README.md
%{_bindir}/jql

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

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
