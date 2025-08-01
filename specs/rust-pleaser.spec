# Generated by rust2rpm 23
%bcond_without check

%global crate pleaser

Name:           rust-pleaser
Version:        0.5.6
Release:        4%{?dist}
Summary:        Please, a polite regex-first sudo alternative

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/pleaser
Source:         %{crates_source}
Patch0:         pleaser-0.5.6.file.patch
# Manually created patch for downstream crate metadata changes
# * restrict dependencies on nix and syslog crates to compatible versions

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Please, a polite regex-first sudo alternative.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# GPL-3.0-or-later
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        GPL-3.0-or-later AND Apache-2.0 AND MIT AND Unicode-DFS-2016

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%doc please.ini.md
%doc please.md
%{_bindir}/please
%{_bindir}/pleaseedit
%{_mandir}/man1/please.1*
%{_mandir}/man5/please.ini.5*
%config(noreplace) /etc/pam.d/please
%config(noreplace) /etc/pam.d/pleaseedit
%{bash_completions_dir}/please
%zsh_completions_dir/_please

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/please.ini.md
%doc %{crate_instdir}/please.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

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
%{__install} -Dpm4755 -t %{buildroot}%{_bindir} target/release/please
%{__install} -Dpm4755 -t %{buildroot}%{_bindir} target/release/pleaseedit
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/please.1
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man5 man/please.ini.5
%{__install} -Dpm0644 -t %{buildroot}%{bash_completions_dir} completions/bash/please
%{__install} -Dpm0644 -t %{buildroot}%{zsh_completions_dir} completions/zsh/_please

mkdir -p $RPM_BUILD_ROOT/etc/pam.d
cat > $RPM_BUILD_ROOT/etc/pam.d/please << EOF
#%PAM-1.0
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    optional     pam_keyinit.so revoke
session    required     pam_limits.so
session    include      system-auth
EOF

mkdir -p $RPM_BUILD_ROOT/etc/pam.d
cat > $RPM_BUILD_ROOT/etc/pam.d/pleaseedit << EOF
#%PAM-1.0
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    optional     pam_keyinit.so revoke
session    required     pam_limits.so
session    include      system-auth
EOF

%if %{with check}
%check
# TODO: upstream to change test to be search for something more appropriate
%cargo_test -- --tests -- --skip test::test_search_bin_default_sbin
%endif

%changelog
* Thu Jul 31 2025 ed neville <ed@s5h.net> - 0.5.6-4
- Patching for nix

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 21 2024 ed neville <ed@s5h.net> - 0.5.6-1
- Switch to uzers

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Fabio Valentini <decathorpe@gmail.com> - 0.5.4-4
- Rebuild with Rust 1.78 to fix incomplete debuginfo and backtraces.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023  ed neville <ed@s5h.net> - 0.5.4-1
- Version bump

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-3
- Restrict dependencies on nix and syslog crates to compatible versions.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-1
- Update to version 0.5.3.
- Regenerate spec file with rust2rpm v23.
- Restore accidentally deleted changelog entries.
- Drop unnecessary patch for nix version compatibility.
- Update license tag for binary subpackage.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-4
- Rebuild with package notes

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Nov 23 21:34:08 GMT 2020 ed neville <ed@s5h.net> - 0.3.24-1
- Initial package
