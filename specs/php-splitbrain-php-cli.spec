%global author   splitbrain
%global project  php-cli
Name: php-%{author}-%{project}

Version: 1.3.1
Release: 2%{?dist}

Summary: PHP library to build command line tools 
License: MIT

URL: http://splitbrain.github.io/php-cli/
Source0: https://github.com/%{author}/%{project}/archive/%{version}/%{project}-%{version}.tar.gz

BuildArch: noarch

%global with_tests 1

BuildRequires: php(language) >= 8.0.0
BuildRequires: php-fedora-autoloader-devel

%if 0%{?with_tests}
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: phpunit8
%endif

Requires: php(language) >= 8.0.0
Requires: php-pcre

Requires: php-composer(fedora/autoloader)

Provides: php-composer(%{author}/%{project}) = %{version}

# Use a PSR-0 compatible directory hierarchy
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgauthordir %{phpdir}/%{author}
%global pkgdir %{pkgauthordir}/phpcli


%description
PHP-CLI is a simple library that helps with creating nice looking
command line scripts. It takes care of option parsing, help page generation,
automatic width adjustment and colored output.

It is lightweight and has no 3rd party dependencies.
Note: this is for non-interactive scripts only.
It has no readline or similar support.

Autoloader: %{pkgdir}/autoload.php


%prep
%setup -q -n %{project}-%{version}


%build
# Create autoloader
phpab \
	--template fedora \
	--output autoload.php \
	--basedir src/ \
	./composer.json
cat autoload.php


%install
install -d -m 755 %{buildroot}%{pkgauthordir}
cp -a src %{buildroot}%{pkgdir}

cp autoload.php %{buildroot}%{pkgdir}/autoload.php


%if 0%{?with_tests}
%check
phpunit8 --verbose --bootstrap %{buildroot}%{pkgdir}/autoload.php
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md examples/
%{pkgauthordir}/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 01 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.3.1-1
- Update to v1.3.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 24 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.1-1
- Update to v1.2.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.0-2
- Add missing dependencies (as reported by phpcompatinfo)
- Make package directory hierarchy PSR-0 compatible
- Make test suite optional

* Thu Sep 15 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.0-1
- Initial packaging
