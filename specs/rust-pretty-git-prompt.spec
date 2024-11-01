# Generated by rust2rpm 26
# * tests can only be run inside the upstream git repository:
#   https://github.com/tomastomecek/pretty-git-prompt/issues/35
%bcond_with check

%global crate pretty-git-prompt

Name:           rust-pretty-git-prompt
Version:        0.2.2
Release:        %autorelease
Summary:        Your current git repository information inside a beautiful shell prompt

License:        MIT
URL:            https://crates.io/crates/pretty-git-prompt
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump git2 dependency from 0.18 to 0.19
Patch:          pretty-git-prompt-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Your current git repository information inside a beautiful shell prompt.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND BSD-3-Clause AND GPL-2.0-only WITH GCC-exception-2.0 AND MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# Zlib OR Apache-2.0 OR MIT
License:        MIT AND BSD-3-Clause AND GPL-2.0-only WITH GCC-exception-2.0 AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/pretty-git-prompt

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
