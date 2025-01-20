Name:		php-email-address-validation
Summary:	PHP class for validating email addresses
License:	BSD-2-Clause

Version:	2.0.1
Release:	14%{?dist}

%global repo_owner	aziraphale
%global repo_name	email-address-validator
URL:		https://github.com/%{repo_owner}/%{repo_name}
Source0:	%{URL}/archive/%{version}/%{repo_name}-%{version}.tar.gz

Patch0:	0000-update-tests-for-phpunit10.patch

BuildArch:	noarch

BuildRequires:	php-composer(phpunit/phpunit) >= 10
BuildRequires:	php-composer(phpunit/phpunit) < 11

Requires:	php-common
Requires:	php-pcre

Provides:	php-composer(aziraphale/email-address-validator) = %{version}


%description
This PHP class is used to check email addresses for technical validity.


%prep
%autosetup -n %{repo_name}-%{version} -p1
# Replace \r\n endlines with \n
sed -i 's/\r$//g' ./EmailAddressValidator.php tests/EmailAddressValidatorTest.php


%build
# nothing to do here


%install
install -m 755 -d %{buildroot}%{_datadir}/php/%{name}
install -m 644 -p EmailAddressValidator.php %{buildroot}%{_datadir}/php/%{name}/


%check
phpunit10 --bootstrap %{buildroot}%{_datadir}/php/%{name}/EmailAddressValidator.php


%files
%doc tests/
%doc composer.json
%{_datadir}/php/%{name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.1-13
- Explicitly call "phpunit10" instead of "phpunit" in tests

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.1-11
- Fix FTBFS - update tests for PHPUnit10
- Migrate License tag to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.1-5
- Drop "Requires: php"

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.1-1
- Switch main source to a fork (composer: aziraphale/email-address-validator)
- Run the test suite during %%check

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 11 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.3.20090910svn
- Add php dependency

* Thu Sep 10 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.2.20090910svn
- Improved description
- Add comments to indicate source generation.
- Add php-common dependency

* Thu Aug 06 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.1.20090806svn
- Initial package
