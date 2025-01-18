Name:		php-cssjanus
Version:	2.3.0
Release:	1%{?dist}
Summary:	Convert CSS stylesheets between left-to-right and right-to-left

License:	Apache-2.0
URL:		https://github.com/wikimedia/mediawiki-libs-php-cssjanus
Source0:	https://github.com/wikimedia/mediawiki-libs-php-cssjanus/archive/v%{version}.tar.gz#/mediawiki-libs-php-cssjanus-%{version}.tar.gz

BuildArch:	noarch

Requires:	php(language) >= 7.4.0
Requires:	php-pcre

Provides:	php-composer(cssjanus/cssjanus) = %{version}


%description
Convert CSS stylesheets between left-to-right and right-to-left.


%prep
%autosetup -n php-cssjanus-%{version}


%build


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/cssjanus
cp -p src/CSSJanus.php %{buildroot}%{_datadir}/php/cssjanus


%files
%license APACHE-LICENSE-2.0.txt
%doc README.md
%{_datadir}/php/cssjanus


%changelog
* Thu Jan 16 2025 Michael Cronenworth <mike@cchtml.com> - 2.3.0-1
- Update to 2.3.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 26 2023 Michael Cronenworth <mike@cchtml.com> - 2.1.1-1
- Version update

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Michael Cronenworth <mike@cchtml.com> - 2.1.0-1
- Version update

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 1.3.0-1
- Version update

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Michael Cronenworth <mike@cchtml.com> - 1.2.0-1
- Version update

* Mon Feb 13 2017 Michael Cronenworth <mike@cchtml.com> - 1.1.3-1
- Version update
- Add upstream patch for php 7.1 support

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 06 2015 Michael Cronenworth <mike@cchtml.com> - 1.1.2-1
- Version update

* Wed Sep 30 2015 Michael Cronenworth <mike@cchtml.com> - 1.1.1-1
- Initial package

