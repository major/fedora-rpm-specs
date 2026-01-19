%global composer_vendor  php81_bc
%global composer_project strftime

Name: php-%{composer_vendor}-%{composer_project}

Version: 0.7.6
Release: 2%{?dist}

Summary: Backwards-compatible strftime() implementation
License: MIT

%global git_owner alphp
%global git_repo  strftime

URL: https://github.com/%{git_owner}/%{git_repo}
Source0: %{URL}/archive/%{version}/%{git_repo}-%{version}.tar.gz

BuildArch: noarch

%global with_tests 1

%if 0%{with_tests}
BuildRequires: php(language) >= 7.1.0
BuildRequires: php-intl

BuildRequires: phpunit10
%endif

Requires: php(language) >= 7.1.0
Requires: php-intl

Provides: php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%global pkgdir %{_datadir}/php/PHP81_BC


%description
The strftime() function has been marked as deprecated in PHP 8.1. This package
provides a locale-formatted strftime() implementation using IntlDateFormatter,
for projects seeking an easy, backwards-compatible solution.


%prep
%autosetup -p1 -n %{git_repo}-%{version}


%build
# Nothing to do here


%install
install -d -m 755 %{buildroot}%{pkgdir}
install -p src/php-8.1-strftime.php -m 644 %{buildroot}%{pkgdir}/strftime.php


%if 0%{with_tests}
%check
cat > ./bootstrap.php <<'EOF'
<?php
require '%{buildroot}%{pkgdir}/strftime.php';

function test_autoloader($className) {
	if(str_starts_with($className, 'PHP81_BC\\Tests\\')) {
		$className = substr($className, 15);
		$className = str_replace('\\', '/', $className);
		include(__DIR__ . '/tests/' . $className . '.php');
	}
}
spl_autoload_register('test_autoloader');
EOF

phpunit10 --bootstrap bootstrap.php
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%{pkgdir}


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu May 15 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.6-1
- Initial packaging
