%global	handlebars_git 36d52a2c199f50e3b636f4334b1daa8d2cdc3a5f
%global	mustache_git 83b0721610a4e11832e83df19c73ace3289972b9

Name:		php-zordius-lightncandy
Version:	1.2.6
Release:	9%{?dist}
Summary:	An extremely fast PHP implementation of handlebars and mustache

License:	MIT
URL:		https://github.com/zordius/lightncandy
Source0:	https://github.com/zordius/lightncandy/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Tests require data from third-party repositories
Source1:	https://github.com/jbboehr/handlebars-spec/archive/%{handlebars_git}.tar.gz#/%{name}-handlebars.tar.gz
Source2:	https://github.com/mustache/spec/archive/%{mustache_git}.tar.gz#/%{name}-mustache.tar.gz

BuildArch:	noarch

#BuildRequires:	php-phpunit-PHPUnit
BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 5.3.0
Requires:	php-pcre
Requires:	php-reflection
Requires:	php-spl

Provides:	php-composer(zordius/lightncandy) = %{version}

%description
An extremely fast PHP implementation of handlebars ( http://handlebarsjs.com/ )
and mustache ( http://mustache.github.io/ ).


%prep
%setup -qn lightncandy-%{version}
tar zxf %{SOURCE1}
cp -rp handlebars-spec-%{handlebars_git}/spec specs/handlebars/
tar zxf %{SOURCE2}
cp -rp spec-%{mustache_git}/specs specs/mustache/


%build
phpab --output src/autoload.php src


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/zordius/lightncandy
cp -p src/*.php %{buildroot}%{_datadir}/php/zordius/lightncandy


# Tests have been removed from upstream tarball
#check
#phpunit -v --filter test


%files
%license LICENSE.md
%doc HISTORY.md README.md UPGRADE.md
%{_datadir}/php/zordius


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Michael Cronenworth <mike@cchtml.com> - 1.2.6-1
- version update

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Michael Cronenworth <mike@cchtml.com> - 1.2.5-1
- version update

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-6
- Disabled tests

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Michael Cronenworth <mike@cchtml.com> - 0.23-1
- version update

* Fri Oct 09 2015 Michael Cronenworth <mike@cchtml.com> - 0.22-1
- Initial package

