%bcond check 1

Name:           hyfetch
Version:        2.0.5
Release:        %autorelease
Summary:        Customizable Linux System Information Script

License:        %{shrink:
    Apache-2.0 AND
    Apache-2.0 OR BSL-1.0 AND
    Apache-2.0 OR MIT AND
    Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT AND
    ISC AND
    LGPL-3.0-or-later AND
    MIT AND
    MIT OR Apache-2.0 AND
    MIT OR Apache-2.0 OR CC0-1.0 AND
    MPL-2.0 AND
    Unlicense OR MIT
}

URL:            https://github.com/hykilpikonna/hyfetch
Source0:        https://github.com/hykilpikonna/hyfetch/archive/%{version}/hyfetch-%{version}.tar.gz
Source1:        hyfetch-vendor-%{version}.tar.gz
Source2:        hyfetch-vendor-config-%{version}.toml
Patch0:         hyfetch-fix-metadata-auto.patch

BuildRequires:  cargo-rpm-macros

%description
HyFetch is a command line tool to display information about your
Linux system, such as amount of installed packages, OS and kernel
version, active GTK theme, CPU info, and used/available memory.
It is a fork of neofetch, and adds pride flag coloration to the OS logo.

%prep
%autosetup -n %{name}-%{version} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -pDm755 target/release/hyfetch %{buildroot}%{_bindir}/hyfetch
install -pDm644 docs/hyfetch.1 %{buildroot}%{_mandir}/man1/hyfetch.1
install -pDm644 hyfetch/scripts/autocomplete.bash %{buildroot}%{bash_completions_dir}/hyfetch
install -pDm644 hyfetch/scripts/autocomplete.zsh %{buildroot}%{zsh_completions_dir}/_hyfetch

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE.md
%license LICENSE.dependencies
%{_bindir}/hyfetch
%{_mandir}/man1/hyfetch.1*
%{bash_completions_dir}/hyfetch
%{zsh_completions_dir}/_hyfetch

%changelog
%autochangelog
