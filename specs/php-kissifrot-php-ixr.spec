%global author   kissifrot
%global project  php-ixr
Name: php-%{author}-%{project}

Version: 1.8.4
Release: 2%{?dist}

Summary: XML-RPC library for PHP
License: BSD

URL: https://github.com/%{author}/%{project}

# Starting with v1.8.4, upstrean marked tests
# as excluded from auto-generated tarballs.
Source0: %{name}-%{version}.zip

# Script to clone git repo (will include the tests!)
# and zip it up
Source1: makesrc.sh

BuildArch: noarch

%global with_tests 1

BuildRequires: php(language) >= 5.4.0
BuildRequires: php-fedora-autoloader-devel

%if 0%{with_tests}
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-xml
BuildRequires: phpunit8
%endif

Requires: php-composer(fedora/autoloader)

Requires: php(language) >= 5.4.0
Requires: php-curl
Requires: php-date
Requires: php-pcre
Requires: php-xml

Provides: php-composer(%{author}/%{project}) = %{version}

# Use a PSR-0 compatible directory hierarchy
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgauthordir %{phpdir}/%{author}
%global pkgdir %{pkgauthordir}/IXR


%description
PHP-IXR is an XML-RPC library designed primarily for ease of use.
It incorporates both client and server classes, and is designed to hide
as much of the workings of XML-RPC from the user as possible. A key feature
of the library is automatic type conversion from PHP types to XML-RPC types
and vice versa. This should enable developers to write web services
with very little knowledge of the underlying XML-RPC standard.

However, don't be fooled by it's simple surface. The library includes
a wide variety of additional XML-RPC specifications and has
all of the features required for serious web service implementations.

Autoloader: %{pkgdir}/autoload.php


%prep
%autosetup -p1

# Remove tests from composer.json autoload list
sed -e '/"IXR\\\\tests\\\\":/d' -i composer.json


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
%license LICENSE.txt
%doc composer.json
%doc README.md
%{pkgauthordir}/


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Mar 24 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.8.4-1
- Update to v1.8.4

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-8.20220717git4a17452
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-7.20220717git4a17452
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-6.20220717git4a17452
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-5.20220717git4a17452
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4.20220717git4a17452
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3.20220717git4a17452
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.8.3-2.20220717git4a17452
- Add missing dependencies (as reported by phpcompatinfo)
- Make package directory hierarchy PSR-0 compatible
- Make test suite optional

* Mon Sep 19 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.8.3-1.20220717git4a17452
- Initial packaging
