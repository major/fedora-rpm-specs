Name:          php-smarty-gettext
Summary:       Gettext support for Smarty
Version:       1.7.0
Release:       6%{?dist}
License:       LGPL-2.1-or-later
URL:           https://github.com/smarty-gettext/smarty-gettext

Source0:       %{url}/archive/%{version}/smarty-gettext-%{version}.tar.gz
Source1:       make_smarty_gettext_tarball.sh

BuildArch:     noarch

BuildRequires: php(language) >= 5.3
BuildRequires: php-fedora-autoloader-devel
# Tests
%if 0%{?fedora}
BuildRequires: phpunit9
BuildRequires: gettext
# Not packaged
#BuildRequires: php-azatoth-php-pgettext
BuildRequires: glibc-langpack-pl
BuildRequires: glibc-langpack-et
BuildRequires: glibc-langpack-en
BuildRequires: php-Smarty
BuildRequires: php-pcre
%endif
Requires:      php(language) >= 5.3
Requires:      php-Smarty
Requires:      php-gettext

Provides:      php-composer(smarty-gettext/smarty-gettext) = %{version}


%description
smarty-gettext provides gettext (i18n) support for Smarty, the popular PHP
templating engine, to implement an NLS (Native Language Support) API which can
be used to internationalize and translate your PHP applications.


%prep
%setup -q -n smarty-gettext-%{version}
%if 0%{?fedora}
# Adapt for recent phpunit
sed -i -e 's/public static function setUpBeforeClass() {/public static function setUpBeforeClass():void {/' \
 tests/TestCase.php \
 tests/ParserTest.php
%endif


%build
# Nothing to build


%install
# Generate autoloader
phpab --template fedora --output smarty-gettext-autoload.php . tests
# Install Smarty
install -d -m 0755 %{buildroot}%{_datadir}/php/Smarty/plugins/
install -p -m 0644 \
  block.t.php \
  function.locale.php \
  smarty-gettext-autoload.php \
  %{buildroot}%{_datadir}/php/Smarty/plugins/


%check
%if 0%{?fedora}
ls -lh
mkdir -p vendor
cat > vendor/autoload.php << EOF
<?php
require_once "/usr/share/php/Smarty/autoload.php";
require_once "block.t.php";
require_once "function.locale.php";
require_once "tests/TestCase.php";
?>
EOF
# Drop for now, it needs php-azatoth-php-pgettext
rm tests/MsgctxtTest.php
phpunit9 \
  --verbose \
  --do-not-cache-result \
  --testdox \
  tests
%endif


%files
%license COPYING
%doc AUTHORS CHANGELOG.md README.md
%{_datadir}/php/Smarty/plugins/smarty-gettext-autoload.php
%{_datadir}/php/Smarty/plugins/block.t.php
%{_datadir}/php/Smarty/plugins/function.locale.php


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 16 2023 Xavier Bachelot <xavier@bachelot.org> - 1.7.0-2
- Provide autoloader
- Run test suite

* Mon Jul 17 2023 Xavier Bachelot <xavier@bachelot.org> - 1.7.0-1
- Initial package
