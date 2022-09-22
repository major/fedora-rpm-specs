%global composer_vendor   openpsa
%global composer_project  universalfeedcreator
Name: php-%{composer_vendor}-%{composer_project}

Version: 1.8.4.1
Release: 2%{?dist}

Summary: RSS and Atom feed generator
License: LGPLv2+

%global repo_owner  flack
%global repo_name   UniversalFeedCreator
URL: https://github.com/%{repo_owner}/%{repo_name}
Source0: %{URL}/archive/v%{version}/%{repo_name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-simplexml

BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-fedora-autoloader-devel

Requires: php-date
Requires: php-pcre
Requires: php-simplexml

Requires: php-composer(fedora/autoloader)

# Composer
Provides: php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgdir %{phpdir}/%{composer_vendor}-%{composer_project}


%description
RSS and Atom feed generator. Supported formats: RSS0.91, RSS1.0, RSS2.0,
PIE0.1 (deprecated), MBOX, OPML, ATOM, ATOM0.3, HTML, JS, PHP.

Autoloader: %{pkgdir}/autoload.php


%prep
%setup -q -n %{repo_name}-%{version}


%build
# Create autoloader
phpab \
	--template fedora \
	--output autoload.php \
	--basedir lib/ \
	./composer.json
echo 'require_once __DIR__ . "/constants.php";' >> autoload.php
cat autoload.php


%install
install -d -m 755 %{buildroot}%{phpdir}
cp -a lib %{buildroot}%{pkgdir}

cp autoload.php %{buildroot}%{pkgdir}/autoload.php


%check
phpunit --verbose --bootstrap %{buildroot}%{pkgdir}/autoload.php


%files
%doc *.md
%doc composer.json
%license LICENSE
%{pkgdir}/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 13 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.8.4.1-1
- Update to v1.8.4.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Artur Iwicki <fedora@svgames.pl> - 1.8.3.2-3
- Simplify autoloader generation

* Fri Aug 21 2020 Artur Iwicki <fedora@svgames.pl> - 1.8.3.2-2
- Add Requires: for PHP extensions needed by the package
- Put files inside pkgdir/ instead of pkgdir/lib/

* Wed Jul 29 2020 Artur Iwicki <fedora@svgames.pl> - 1.8.3.2-1
- Initial packaging
