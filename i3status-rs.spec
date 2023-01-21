%bcond_without check
%global __cargo_skip_build 0

Name:           i3status-rs
Version:        0.13.1
Release:        9%{?dist}
Summary:        Feature-rich and resource-friendly replacement for i3status, written in Rust

# Upstream license specification: GPLv3
# Install all deps (without check), grab their licenses and make it simple
# * 0BSD
# * ASL 2.0
# * ASL 2.0 or Boost
# * ASL 2.0 or MIT
# * ISC
# * MIT
# * MIT or ASL 2.0
# * (MIT or ASL 2.0) and BSD
# * (MIT or ASL 2.0) and Public Domain
# * Unlicense or MIT
License:        GPLv3 and 0BSD and ASL 2.0 and ISC and MIT and BSD and Public Domain
URL:            https://github.com/greshake/i3status-rust
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
Recommends:     fontawesome-fonts
Enhances:       i3
Enhances:       sway

%description
i3status-rs is a feature-rich and resource-friendly replacement for i3status,
written in pure Rust. It provides a way to display "blocks" of system
information (time, battery status, volume, etc) on the i3 bar. It is also
compatible with sway.

%prep
%autosetup -n i3status-rust-%{version_no_tilde} -p1
# Upstream bumps deps every release
sed -i -e '/maildir/s/0.3/0.4/' -e '/nix/s/0.16.0/0.17/' Cargo.toml
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

%files
%license LICENSE
%doc README.md NEWS.md CONTRIBUTING.md blocks.md example_config.toml example_icon.toml example_theme.toml themes.md
%{_bindir}/i3status-rs

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:26:06 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.13.1-4
- Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.13.1-2
- Update dependencies

* Fri Feb 21 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Mon Feb 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.0-1
- Update to 0.13.0
- Drop example config file in favour of upstream examples

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-6
- Rename to i3status-rs

* Wed Dec 18 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.12.0-5
- Use Enhances instead of Suggests

* Tue Dec 17 00:00:00 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.12.0-4
- Fix license
- Bump inotify to "0.8.0"

* Thu Dec 12 18:35:09 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.12.0-3
- Update to 0.12.0

* Tue Nov 05 18:51:24 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11.0-1
- Initial package
