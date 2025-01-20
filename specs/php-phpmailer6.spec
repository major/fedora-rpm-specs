# remirepo/fedora spec file for php-phpmailer6
#
# Copyright (c) 2017-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please preserve changelog entries
#
# Github
%global gh_commit    2f5c94fe7493efc213f643c23b1b1c249d40f47e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     PHPMailer
%global gh_project   PHPMailer
# Packagist
%global pk_vendor    phpmailer
%global pk_project   phpmailer
# Namespace
%global ns_vendor    PHPMailer
%global ns_project   PHPMailer
# don't change major version used in package name
%global major        6
%bcond_without       tests
%global php_home     %{_datadir}/php

Name:           php-%{pk_project}%{major}
Version:        6.9.3
Release:        2%{?dist}
Summary:        Full-featured email creation and transfer class for PHP

License:        LGPL-2.1-only
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
# Simple unit test for packaging
Source2:        PHPMailerRpmTest.php

# Fix path to match RPM installation layout
Patch0:         %{name}-layout.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-filter
BuildRequires:  php-hash
BuildRequires:  php-intl
BuildRequires:  php-mbstring
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-fedora-autoloader-devel
# From composer.json, "require-dev": {
#        "dealerdirect/phpcodesniffer-composer-installer": "^1.0",
#        "doctrine/annotations": "^1.236 || ^1.13.3",
#        "php-parallel-lint/php-console-highlighter": "^0.5.0",
#        "php-parallel-lint/php-parallel-lint": "^1.3.1",
#        "phpcompatibility/php-compatibility": "^9.3.5",
#        "roave/security-advisories": "dev-latest",
#        "squizlabs/php_codesniffer": "^3.7.2",
#        "yoast/phpunit-polyfills": "^1.0.4"
%global phpunit %{_bindir}/phpunit7
BuildRequires: (php-composer(yoast/phpunit-polyfills) >= 1.0.4 with php-composer(yoast/phpunit-polyfills) < 2)
BuildRequires:  %{phpunit}
BuildRequires:  %{_sbindir}/smtp-sink
%endif

# From composer.json, "require": {
#    "require": {
#        "php": ">=5.5.0",
#        "ext-ctype": "*",
#        "ext-filter": "*",
#        "ext-hash": "*"
Requires:       php(language) >= 5.5
Requires:       php-ctype
Requires:       php-filter
Requires:       php-hash
# from phpcompatinfo report on version 6.1.3
Requires:       php-date
Recommends:     php-imap
Requires:       php-intl
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-pcre
# From composer.json, "suggest": {
#        "ext-mbstring": "Needed to send email in multibyte encoding charset",
#        "greew/oauth2-azure-provider": "Needed for Microsoft Azure XOAUTH2 authentication",
#        "ext-openssl": "Needed for secure SMTP sending and DKIM signing",
#        "hayageek/oauth2-yahoo": "Needed for Yahoo XOAUTH2 authentication",
#        "league/oauth2-google": "Needed for Google XOAUTH2 authentication",
#        "psr/log": "For optional PSR-3 debug logging",
#        "thenetworg/oauth2-azure": "Needed for Microsoft XOAUTH2 authentication",
#        "symfony/polyfill-mbstring": "To support UTF-8 if the Mbstring PHP extension is not enabled (^1.2)"
Suggests:       php-composer(psr/log)
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
PHPMailer - A full-featured email creation and transfer class for PHP

Class Features
* Probably the world's most popular code for sending email from PHP!
* Used by many open-source projects:
  WordPress, Drupal, 1CRM, SugarCRM, Yii, Joomla! and many more
* Integrated SMTP support - send without a local mail server
* Send emails with multiple To, CC, BCC and Reply-to addresses
* Multipart/alternative emails for mail clients that do not read HTML email
* Add attachments, including inline
* Support for UTF-8 content and 8bit, base64, binary, and quoted-printable
  encodings
* SMTP authentication with LOGIN, PLAIN, CRAM-MD5 and XOAUTH2 mechanisms
  over SSL and SMTP+STARTTLS transports
* Validates email addresses automatically
* Protect against header injection attacks
* Error messages in 47 languages!
* DKIM and S/MIME signing support
* Compatible with PHP 5.5 and later
* Namespaced to prevent name clashes
* Much more!


Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm
find src -name \*.rpm -delete

cp %{SOURCE2} test/PHPMailerRpmTest.php

cat << 'EOF' | tee src/autoload.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('PHPMailer\\PHPMailer\\', __DIR__);
\Fedora\Autoloader\Dependencies::optional(array(
    '%{php_home}/Psr/Log/autoload.php',
));
EOF


%build
# Empty build section, most likely nothing required.


%install
mkdir -p        %{buildroot}/%{php_home}/%{ns_vendor}
cp -pr src      %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}
cp -pr language %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/language


%check
%if %{with tests}
: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
require_once '%{php_home}/Yoast/PHPUnitPolyfills/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('PHPMailer\\Test\\', dirname(__DIR__) . '/test');
EOF

sed -e '/colors/d;s/logging/nologging/' phpunit.xml.dist > phpunit.xml

: Start fake MTA and test environment
PORT=$(expr 2500 + %{?fedora}%{?rhel})
sed -e "s/2500/$PORT/" test/testbootstrap-dist.php > test/testbootstrap.php

mkdir -p build/logs
chmod +x test/fakesendmail.sh

pushd build
  smtp-sink -d "%%d.%%H.%%M.%%S" localhost:$PORT 1000 &>/dev/null &
  SMTPPID=$!
popd

: Run upstream test suite
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd  -d "sendmail_path=$PWD/test/fakesendmail.sh -t -i " \
      %{phpunit} --exclude slow,pop3,languages --verbose || ret=1
  fi
done

: Cleanup
kill $SMTPPID

exit $ret
%endif


%files
%license LICENSE
%license COMMITMENT
%doc *.md
%doc examples
%doc composer.json
%{php_home}/%{ns_vendor}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Remi Collet <remi@remirepo.net> - 6.9.3-1
- update to 6.9.3

* Wed Oct  9 2024 Remi Collet <remi@remirepo.net> - 6.9.2-1
- update to 6.9.2

* Fri Aug 30 2024 Remi Collet <remi@remirepo.net> - 6.9.1-6
- fix build dependency on yoast/phpunit-polyfills 1.0.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 30 2024 Remi Collet <remi@remirepo.net> - 6.9.1-4
- add missing dependency on php-fedora-autoloader

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 27 2023 Remi Collet <remi@remirepo.net> - 6.9.1-1
- update to 6.9.1

* Tue Aug 29 2023 Remi Collet <remi@remirepo.net> - 6.8.1-1
- update to 6.8.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar  6 2023 Remi Collet <remi@remirepo.net> - 6.8.0-1
- update to 6.8.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  8 2022 Remi Collet <remi@remirepo.net> - 6.7.1-1
- update to 6.7.1

* Mon Dec  5 2022 Remi Collet <remi@remirepo.net> - 6.7-1
- update to 6.7

* Mon Oct 10 2022 Remi Collet <remi@remirepo.net> - 6.6.5-1
- update to 6.6.5

* Tue Aug 30 2022 Remi Collet <remi@remirepo.net> - 6.6.4-1
- update to 6.6.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Remi Collet <remi@remirepo.net> - 6.6.3-1
- update to 6.6.3

* Tue Jun 14 2022 Remi Collet <remi@remirepo.net> - 6.6.2-1
- update to 6.6.2

* Mon Feb 28 2022 Remi Collet <remi@remirepo.net> - 6.6.0-1
- update to 6.6.0

* Thu Feb 17 2022 Remi Collet <remi@remirepo.net> - 6.5.4-1
- update to 6.5.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Remi Collet <remi@remirepo.net> - 6.5.3-1
- update to 6.5.3

* Wed Sep  1 2021 Remi Collet <remi@remirepo.net> - 6.5.1-1
- update to 6.5.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Remi Collet <remi@remirepo.net> - 6.5.0-1
- update to 6.5.0

* Mon May  3 2021 Remi Collet <remi@remirepo.net> - 6.4.1-1
- update to 6.4.1

* Thu Apr  1 2021 Remi Collet <remi@remirepo.net> - 6.4.0-1
- update to 6.4.0

* Wed Feb 24 2021 Remi Collet <remi@remirepo.net> - 6.3.0-1
- update to 6.3.0
- php-imap is optional

* Thu Nov 26 2020 Remi Collet <remi@remirepo.net> - 6.2.0-1
- update to 6.2.0
- add build dependency on yoast/phpunit-polyfills
- switch to phpunit7

* Sat Oct 10 2020 Remi Collet <remi@remirepo.net> - 6.1.8-1
- update to 6.1.8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Remi Collet <remi@remirepo.net> - 6.1.7-1
- update to 6.1.7

* Wed May 27 2020 Remi Collet <remi@remirepo.net> - 6.1.6-2
- update to 6.1.6

* Sat Mar 14 2020 Remi Collet <remi@remirepo.net> - 6.1.5-1
- update to 6.1.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Remi Collet <remi@remirepo.net> - 6.1.4-1
- update to 6.1.4

* Thu Nov 21 2019 Remi Collet <remi@remirepo.net> - 6.1.3-1
- update to 6.1.3

* Thu Nov 14 2019 Remi Collet <remi@remirepo.net> - 6.1.2-1
- update to 6.1.2

* Mon Sep 30 2019 Remi Collet <remi@remirepo.net> - 6.1.1-1
- update to 6.1.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb  4 2019 Remi Collet <remi@remirepo.net> - 6.0.7-1
- update to 6.0.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Remi Collet <remi@remirepo.net> - 6.0.6-1
- update to 6.0.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Remi Collet <remi@remirepo.net> - 6.0.5-1
- update to 6.0.5 (no change)

* Tue Mar 27 2018 Remi Collet <remi@remirepo.net> - 6.0.4-1
- update to 6.0.4
- add patch to fix lang_path with RPM layout

* Sun Jan  7 2018 Remi Collet <remi@remirepo.net> - 6.0.3-1
- Update to 6.0.3

* Fri Dec  1 2017 Remi Collet <remi@remirepo.net> - 6.0.2-1
- Update to 6.0.2

* Wed Nov 15 2017 Remi Collet <remi@remirepo.net> - 6.0.1-1
- initial rpm, version 6.0.1
- open https://github.com/PHPMailer/PHPMailer/issues/1243 for FSF address
