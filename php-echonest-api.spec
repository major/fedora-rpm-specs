%global commit 662d62a7df1247515572bf517e14b795714e0824
%global short_commit %(echo %{commit} | cut -c 1-8)

Name:       php-echonest-api
Version:    0
Release:    0.17.20131228git.%{short_commit}%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    PHP classes for the Echo Nest API
URL:        https://github.com/Afterster/php-echonest-api
Source0:    %{url}/archive/%{commit}.tar.gz
Source1:    autoload.php

BuildRequires: php-phpunit-PHPUnit   

Requires:      php(language) >= 5.2.0
Requires:      php-curl
Requires:      php-date
Requires:      php-json
Requires:      php-spl
Requires:      php-xml


%description
A simple, Object Oriented API wrapper for the EchoNest Api written with PHP5.
This library is modeled after the php-github-api library built by ornicar.


%prep
%setup -q -n %{name}-%{commit}

echo $(ls ..)

chmod a-x LICENSE
chmod a-x README.md

# https://github.com/Afterster/php-echonest-api/pull/1
find . -name "*.php" | xargs chmod 0644


%install
install -d -p -m 0755 %{buildroot}/%{_datadir}/php

cp -a -r lib/EchoNest %{buildroot}/%{_datadir}/php/

install -p -m 0644 %{S:1} %{buildroot}/%{_datadir}/php/EchoNest


%check
phpunit --bootstrap=%{buildroot}/%{_datadir}/php/EchoNest/autoload.php


%files
%license LICENSE
%doc README.md
%{_datadir}/php/EchoNest


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20131228git.662d62a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0-0.3.20131228git.662d62a7
- Add the commit date into the release.
- Remove the execute bit on php files.
- Do not require php virtual provides by version.

* Sat Jan 14 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0-0.2.git.662d62a7
- Depend on php(language) instead of php.
- Use the full commit reference.
- Require needed php components explicitly.
- Included a simple autoload.php file.
- Run the tests against the installed library.

* Sun Jan 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0-0.1.git.662d62a7
- Initial release.
