%define name2 wp

Name:       wp-cli
Version:    2.4.0
Release:    13%{?dist}
Summary:    The command line interface for WordPress
License:    MIT
URL:        http://%{name}.org/
Source0:    https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.phar
Source1:    LICENSE
Source2:    wp.1
BuildArch:  noarch

%description
WP-CLI is the command-line interface for WordPress.
You can update plugins, configure multisite installations
and much more, without using a web browser.

%prep
chmod +x %{SOURCE0}
{
    echo '.TH "WP" "1"'
    php %{SOURCE0} --help
} \
    | sed -e 's/^\([A-Z ]\+\)$/.SH "\1"/' \
    | sed -e 's/^  wp$/wp \\- The command line interface for WordPress/' \
> %{SOURCE2}

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name2}
cp -f %SOURCE1 LICENSE
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/


%files
%license LICENSE
%{_bindir}/%{name2}
%{_mandir}/man1/wp.1*

%changelog
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

