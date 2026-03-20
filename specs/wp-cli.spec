%define name2 wp

Name:       wp-cli
Version:    2.12.0
Release:    1%{?dist}
Summary:    The command line interface for WordPress
License:    MIT
URL:        http://%{name}.org/
Source0:    https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.phar
Source1:    LICENSE
BuildArch:  noarch

%description
WP-CLI is the command-line interface for WordPress.
You can update plugins, configure multisite installations
and much more, without using a web browser.


%prep


%build


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name2}
cp -af %SOURCE1 LICENSE


%files
%license LICENSE
%{_bindir}/%{name2}


%changelog
* Wed Mar 18 2026 Jonathan Wright <jonathan@almalinux.org> - 2.12.0-1
- Update to 2.12.0

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 2.4.0-2
- update release.

* Fri Nov 22 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 2.4.0-1
- update to 2.4.0.

* Tue Aug 20 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 2.3.0-1
- update to 2.3.0.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 2.2.0-2
- include man
- change bindir wp-cli to wp

* Sat Jun 8 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 2.2.0-1
- update to 2.2.0.

* Sun Feb 24 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 2.1.0-1
- Initial package for Fedora, based on upstream SPEC file (dated Dec 2017).

