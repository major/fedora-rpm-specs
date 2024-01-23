%global github_owner    bantuXorg
%global github_name     php-ini-get-wrapper
%global github_version  1.0.1
%global github_commit   4770c7feab370c62e23db4f31c112b7c6d90aee2
%global packagist_owner bantu
%global packagist_name  ini-get-wrapper
%global psr4_namespace  bantu
%global psr4_prefix     %{psr4_namespace}/IniGetWrapper

# phpci: uses namespaces
%global php_min_ver    5.3.0

Name:          php-%{packagist_owner}-%{packagist_name}
Version:       %{github_version}
Release:       18%{?dist}
Summary:       Convenience wrapper around PHP's ini_get() function

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
# Must use commit-based not tag-based github tarball:
# https://fedoraproject.org/wiki/Packaging:SourceURL#Github
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{_bindir}/phpunit
BuildRequires: %{_bindir}/phpab

Requires:      php(language) >= %{php_min_ver}

Provides:       php-composer(%{packagist_owner}/%{packagist_name}) = %{version}

%description
Convenience wrapper around ini_get().


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
# use PSR-0 layout relative to _datadir/php
mkdir -p %{buildroot}%{_datadir}/php/%{psr4_prefix}
cp -pr src/* %{buildroot}%{_datadir}/php/%{psr4_prefix}


%check
# roll our own loader to run tests
%{_bindir}/phpab --output bootstrap.php --exclude *Test.php --basedir . src tests

# run tests
%{_bindir}/phpunit --bootstrap bootstrap.php


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md composer.json
%{_datadir}/php/%{psr4_namespace}


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 12 2014 Adam Williamson <awilliam@redhat.com> - 1.0.1-1
- initial package
