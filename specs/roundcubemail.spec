#
# Fedora spec file for roundcubemail
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%bcond_with  internet

# support for apache / nginx / php-fpm
%global with_phpfpm 1
%global upstream_version     1.6.9
#global upstream_prever      rc

%global roundcubedir %{_datadir}/roundcubemail
%global _logdir /var/log  
Name: roundcubemail
Version:  %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:  2%{?dist}
Summary: Round Cube Webmail is a browser-based multilingual IMAP client

# Since 0.8 beta, the main code has been GPLv3+ with exceptions and
# skins CC-BY-SA.
# Plugins are a mix of GPLv3+ and GPLv2. The Enigma plugin contains a
# copy of php-Pear-Crypt-GPG (not yet packaged for Fedora), which is
# LGPLv2+. The jqueryui plugin contains the entire jQuery UI framework
# for the use of roundcube plugins: it is licensed as MIT or GPLv2.
# The program/js/tiny_mce directory contains an entire copy of TinyMCE
# which is LGPLv2+.
# https://github.com/pear/Crypt_GPG
# http://jqueryui.com/
# http://www.tinymce.com/
License: GPL-3.0-or-later AND GPL-2.0-only AND LGPL-2.0-or-later AND CC-BY-SA-3.0 AND MIT AND BSD-2-Clause AND BSD-3-Clause AND PHP-3.01
URL: http://www.roundcube.net
Source0: https://github.com/roundcube/roundcubemail/releases/download/%{upstream_version}%{?upstream_prever:-%{upstream_prever}}/roundcubemail-%{upstream_version}%{?upstream_prever:-%{upstream_prever}}-complete.tar.gz
Source8: https://github.com/roundcube/roundcubemail/releases/download/%{upstream_version}%{?upstream_prever:-%{upstream_prever}}/roundcubemail-%{upstream_version}%{?upstream_prever:-%{upstream_prever}}-complete.tar.gz.asc
Source9: https://roundcube.net/download/pubkey.asc

Source1: roundcubemail.httpd
Source3: roundcubemail.nginx
Source2: roundcubemail.logrotate
Source4: roundcubemail-README-rpm.txt
# Simple script to dump name, version and licenses of bundled libraries
Source5: roundcubemail-bundled.php

# Non-upstreamable: Adjusts config path to Fedora policy
Patch1: roundcubemail-1.6-confpath.patch


BuildArch: noarch
BuildRequires: gnupg2
BuildRequires: php(language) >= 7.3
# For test
BuildRequires: php-cli

%if %{with_phpfpm}
Requires:  webserver
Requires:  nginx-filesystem
Requires:  httpd-filesystem
Requires:  php(httpd)
%else
Requires: httpd
Requires: mod_php
%endif
Requires: php(language) >= 7.3
Requires: php-ctype
Requires: php-curl
Requires: php-date
Requires: php-dom
Requires: php-fileinfo
Requires: php-filter
Requires: php-gd
Requires: php-hash
Requires: php-iconv
Requires: php-intl
Requires: php-json
Requires: php-ldap
Requires: php-libxml
Requires: php-mbstring
Requires: php-openssl
Requires: php-pcre
Requires: php-pdo
Requires: php-posix
Requires: php-reflection
Requires: php-session
Requires: php-simplexml
Requires: php-sockets
Requires: php-spl
Requires: php-tokenizer
# mailcap for /etc/mime.types
Requires: mailcap
# EXIF images
Requires: php-exif
# ZIP download plugin
Requires: php-zip

# Optional deps
# Upload progress (shock!)
Suggests:   php-uploadprogress
# Crypto
Suggests:   php-sodium
# Spell check
Recommends: php-enchant
Suggests:   php-pspell
# Caching
Suggests:   php-apcu
Suggests:   php-memcache
Suggests:   php-memcached
Suggests:   php-redis
# Gearman support
Suggests:   php-gearman
# Authent
Suggests:   php-krb5
Suggests:   php-pam

# Bundled JS libraries
# see https://github.com/roundcube/roundcubemail/blob/master/jsdeps.json
# License Apache-2.0
Provides: bundled(js-lessjs) = 3.13.0
# License GPLv3
Provides: bundled(js-publickey) = 0e011cb1
# License LGPL
Provides: bundled(js-openpgp) = 5.0.0
Provides: bundled(js-tinymce) = 5.8.2
# License MIT
Provides: bundled(js-bootstrap) = 4.5.3
Provides: bundled(js-codemirror) = 5.58.3
Provides: bundled(js-jquery) = 3.5.1
Provides: bundled(js-jstimezonedetect) = 1.0.7
# License Unkown
Provides: bundled(js-tinymce-langs) = 5.8.2

# Bundled PHP libraries
# see vendor/composer/installed.json
# License BSD
Provides: bundled(php-pear-auth-sasl) = v1.1.0
# License BSD-2-Clause
Provides: bundled(php-bacon-bacon-qr-code) = 2.0.8
Provides: bundled(php-dasprid-enum) = 1.0.6
Provides: bundled(php-pear-console-getopt) = v1.4.3
Provides: bundled(php-pear-net-sieve) = 1.4.7
Provides: bundled(php-pear-net-smtp) = 1.10.1
Provides: bundled(php-pear-pear-exception) = v1.0.2
# License BSD-3-Clause
Provides: bundled(php-pear-mail-mime) = 1.10.12
Provides: bundled(php-pear-pear-core-minimal) = v1.10.15
# License GPL-2.0
Provides: bundled(php-roundcube-rtf-html-php) = v2.2
# License GPL-3.0+
Provides: bundled(php-kolab-net-ldap3) = v1.1.5
# License GPL-3.0-or-later
Provides: bundled(php-roundcube-plugin-installer) = 0.3.8
# License LGPL-2.1
Provides: bundled(php-pear-crypt-gpg) = v1.6.9
# License LGPL-3.0
Provides: bundled(php-pear-net-ldap2) = v2.3.0
# License MIT
Provides: bundled(php-guzzlehttp-guzzle) = 7.9.2
Provides: bundled(php-guzzlehttp-promises) = 2.0.3
Provides: bundled(php-guzzlehttp-psr7) = 2.7.0
Provides: bundled(php-masterminds-html5) = 2.7.6
Provides: bundled(php-pear-console-commandline) = v1.2.6
Provides: bundled(php-psr-http-client) = 1.0.3
Provides: bundled(php-psr-http-factory) = 1.1.0
Provides: bundled(php-psr-http-message) = 2.0
Provides: bundled(php-ralouphie-getallheaders) = 3.0.3
Provides: bundled(php-symfony-deprecation-contracts) = v2.5.3
# License PHP License
Provides: bundled(php-pear-net-socket) = v1.2.2


%description
RoundCube Webmail is a browser-based multilingual IMAP client
with an application-like user interface. It provides full
functionality you expect from an e-mail client, including MIME
support, address book, folder manipulation, message searching
and spell checking. RoundCube Webmail is written in PHP and 
requires a database: MySQL, PostgreSQL and SQLite are known to
work. The user interface is fully skinnable using XHTML and
CSS 2.


%prep
%{?gpgverify: %{gpgverify} --keyring=%{SOURCE9} --signature=%{SOURCE8} --data=%{SOURCE0}}

%setup -q -n roundcubemail-%{upstream_version}%{?upstream_prever:-%{upstream_prever}}
%patch -P1 -p1 -b .rpm

: PHP bundled libraries
php %{SOURCE5} vendor/composer/installed.json

%if %{with internet}
: JS bundled libraries
php %{SOURCE5} https://raw.githubusercontent.com/roundcube/roundcubemail/%{upstream_version}%{?upstream_prever:-%{upstream_prever}}/jsdeps.json
%endif

# fix permissions and remove any .htaccess files
find . -type f -print | xargs chmod a-x
find . -name \.htaccess -delete -print

# drop file from patch
find . -type f -name '*.orig' -o -name '*.rpm' -exec rm {} \; -print

# Wipe bbcode plugin from bundled TinyMCE to make doubleplus sure we cannot
# be vulnerable to CVE-2012-4230, unaddressed upstream
echo "CVE-2012-4230: removing tinymce bbcode plugin, check path if this fails."
test -d program/js/*mce/plugins/bbcode && rm -rf program/js/*mce/plugins/bbcode || exit 1


%build
# Nothing


%install
install -d %{buildroot}%{roundcubedir}
cp -pr * %{buildroot}%{roundcubedir}

# Apache with mod_php or php-fpm
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

%if %{with_phpfpm}
# Nginx with php-fpm
install -Dpm 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/nginx/default.d/%{name}.conf
%endif

mkdir -p %{buildroot}%{_sysconfdir}/roundcubemail
install -pDm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/roundcubemail

# Log files
mkdir -p %{buildroot}/var/log/roundcubemail
# Temp files
mkdir -p %{buildroot}/var/lib/roundcubemail/temp
# GPG keys
mkdir -p %{buildroot}/var/lib/roundcubemail/enigma

cp -pr %SOURCE4 README-rpm.txt

# create empty files for ghost to not remove OLD config (0.9.x)
touch %{buildroot}%{_sysconfdir}/roundcubemail/db.inc.php
touch %{buildroot}%{_sysconfdir}/roundcubemail/main.inc.php
# create empty files for ghost for the NEW config
touch %{buildroot}%{_sysconfdir}/roundcubemail/config.inc.php

# keep any other config files too
mv %{buildroot}%{roundcubedir}/config/* %{buildroot}%{_sysconfdir}/roundcubemail/

# Also move plugins configuration file samples
pushd %{buildroot}%{roundcubedir}/plugins
for plug in $(ls); do
  if [ -f $plug/config.inc.php.dist ]; then
    mv $plug/config.inc.php.dist %{buildroot}%{_sysconfdir}/roundcubemail/$plug.inc.php.dist
  fi
  if [ -d $plug/tests ]; then
    rm -r $plug/tests
  fi
done
popd

# clean up the buildroot
rm -r %{buildroot}%{roundcubedir}/{config,logs,temp}
rm -r %{buildroot}%{roundcubedir}/{CHANGELOG.md,INSTALL,LICENSE,README.md,UPGRADING}
rm    %{buildroot}%{roundcubedir}/composer.json-dist


%check
: Check our autoloader for needed classes
php -r '
require "%{buildroot}%{roundcubedir}/vendor/autoload.php";
$cl = [ "Auth_SASL", "Crypt_GPG", "Mail_mime", "Net_LDAP2", "Masterminds\\HTML5", "GuzzleHttp\\Client",
        "Net_LDAP3", "Net_Sieve", "Net_SMTP", "PEAR" , "BaconQrCode\\Writer", "RtfHtmlPhp\\Document" ];
$ret = 0;
foreach ($cl as $c) {
  if (class_exists($c)) {
    echo "$c ok\n";
  } else {
    echo("$c is missing\n");
    $ret = 1;
  }
}
exit($ret);
'

%pre
# Drop some old config options to ensure new defaults are used
if [ -f %{_sysconfdir}/%{name}/main.inc.php ]; then
  sed -e "/'temp_dir'/d" \
      -e "/'mime_types'/d" \
      -e "/'log_dir'/d" \
      -i %{_sysconfdir}/%{name}/main.inc.php
fi


%files
%license LICENSE
%doc CHANGELOG.md INSTALL README.md UPGRADING README-rpm.txt
%doc composer.json-dist
%{roundcubedir}
%dir %{_sysconfdir}/%{name}
# OLD config files from previous version
%ghost %attr(0640,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/db.inc.php
%ghost %attr(0640,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/main.inc.php
# NEW config file
%ghost %attr(0640,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/config.inc.php
# Default upstream values, overwritten on update
%attr(0640,root,apache) %{_sysconfdir}/%{name}/mimetypes.php
%attr(0640,root,apache) %{_sysconfdir}/%{name}/defaults.inc.php
%attr(0640,root,apache) %{_sysconfdir}/%{name}/config.inc.php.sample
%attr(0640,root,apache) %{_sysconfdir}/%{name}/*.inc.php.dist
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%if %{with_phpfpm}
%config(noreplace) %{_sysconfdir}/nginx/default.d/%{name}.conf
%endif
%attr(0770,root,apache) %dir /var/log/roundcubemail
%attr(0770,root,apache) %dir /var/lib/roundcubemail
%attr(0770,root,apache) %dir /var/lib/roundcubemail/temp
%attr(0770,root,apache) %dir /var/lib/roundcubemail/enigma
%config(noreplace) %{_sysconfdir}/logrotate.d/roundcubemail


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Remi Collet <remi@remirepo.net> - 1.6.9-1
- update to 1.6.9

* Mon Aug  5 2024 Remi Collet <remi@remirepo.net> - 1.6.8-1
- update to 1.6.8

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 20 2024 Remi Collet <remi@remirepo.net> - 1.6.7-1
- update to 1.6.7

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Remi Collet <remi@remirepo.net> - 1.6.6-1
- update to 1.6.6

* Mon Nov  6 2023 Remi Collet <remi@remirepo.net> - 1.6.5-1
- update to 1.6.5

* Mon Oct 16 2023 Remi Collet <remi@remirepo.net> - 1.6.4-1
- update to 1.6.4

* Fri Sep 15 2023 Remi Collet <remi@remirepo.net> - 1.6.3-1
- update to 1.6.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul  2 2023 Remi Collet <remi@remirepo.net> - 1.6.2-1
- update to 1.6.2

* Tue Jan 24 2023 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1
- use SPDX license id

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug  3 2022 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6~rc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Remi Collet <remi@remirepo.net> - 1.6~rc-1
- update to 1.6-rc
- drop patch merged upstream

* Mon Mar  7 2022 Remi Collet <remi@remirepo.net> - 1.6~beta-1
- update to 1.6-beta
- raise dependency on PHP 7.3
- add patch to keep use default_host and smtp_server
  from https://github.com/roundcube/roundcubemail/pull/8467

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2

* Fri Dec  3 2021 Remi Collet <remi@remirepo.net> - 1.5.1-2
- update to 1.5.1
- use all PHP bundled libraries

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5~rc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul  5 2021 Remi Collet <remi@remirepo.net> - 1.5~rc-1
- update to 1.5-rc
- raise dependency on pear/net_smtp 1.10
- raise dependency on pear/net_sieve 1.4.5

* Thu Apr 22 2021 Remi Collet <remi@remirepo.net> - 1.5~beta-1
- update to 1.5-beta
- drop dependency on pear/net_idna2
- raise dependency on pear/net_smtp 1.9
- raise dependency on masterminds/html5 2.7
- add dependency on guzzlehttp/guzzle
- switch from mkopinsky/zxcvbn-php to bjeavons/zxcvbn-php

* Tue Feb  9 2021 Remi Collet <remi@remirepo.net> - 1.4.11-1
- update to 1.4.11

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 2021 Remi Collet <remi@remirepo.net> - 1.4.10-1
- update to 1.4.10

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 1.4.9-1
- update to 1.4.9

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 1.4.8-1
- update to 1.4.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul  6 2020 Remi Collet <remi@remirepo.net> - 1.4.7-1
- update to 1.4.7

* Mon Jun  8 2020 Remi Collet <remi@remirepo.net> - 1.4.6-1
- update to 1.4.6

* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 1.4.5-1
- update to 1.4.5
- fix logrotate configuration file permissions

* Thu Apr 30 2020 Remi Collet <remi@remirepo.net> - 1.4.4-1
- update to 1.4.4

* Thu Feb 20 2020 Remi Collet <remi@remirepo.net> - 1.4.3-1
- update to 1.4.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 1.4.2-1
- update to 1.4.2

* Fri Nov 22 2019 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 1.4.0-1
- Update to 1.4.0

* Tue Sep 17 2019 Remi Collet <remi@remirepo.net> - 1.4~rc2-1
- Update to 1.4-rc2
- raise dependency on masterminds/html5 2.5.0
- raise dependency on kolab/net_ldap3 1.1.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.2.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  1 2019 Remi Collet <remi@remirepo.net> - 1.4~rc1-1
- Update to 1.4-rc1
- raise dependency on pear/net_smtp 1.8.1
- drop dependency on pear/net_socket
- add weak dependency on mkopinsky/zxcvbn-php

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.1.beta.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  2 2018 Remi Collet <remi@remirepo.net> - 1.4-0.1.beta
- rebuild

* Mon Sep 17 2018 Remi Collet <remi@remirepo.net> - 1.4~beta-1
- Update to 1.4-beta
- raise dependency on pear/net_sieve 1.4.3
- raise dependency on kolab/net_ldap3 1.0.6
- add dependency on masterminds/html5

* Wed Aug 01 2018 Kevin Fenzi <kevin@scrye.com> - 1.3.7-1
- Update to 1.3.7. Fixes bug #1609445

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Remi Collet <remi@remirepo.net> - 1.3.6-1
- Update to 1.3.6

* Fri Mar 16 2018 Remi Collet <remi@remirepo.net> - 1.3.5-1
- Update to 1.3.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Remi Collet <remi@remirepo.net> - 1.3.4-1
- Update to 1.3.4
- fix missing .log suffix #1520132

* Thu Nov  9 2017 Remi Collet <remi@remirepo.net> - 1.3.3-1
- Update to 1.3.3

* Tue Oct 31 2017 Kevin Fenzi <kevin@scrye.com> - 1.3.2-1
- Update to 1.3.2. Fixes bug #1508242

* Tue Sep  5 2017 Remi Collet <remi@remirepo.net> - 1.3.1-1
- Update to 1.3.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Remi Collet <remi@remirepo.net> - 1.3.0-2
- update to 1.3.0
- open https://github.com/roundcube/roundcubemail/pull/5820 - PHP 7
- add dependency on endroid/qrcode
- raise dependency on Net_Socket 1.2.1
- raise dependency on Auth_SASL 1.1.0
- raise dependency on Net_IDNA2 0.2.0
- raise dependency on Crypt_GPG 1.6.0
- switch from roundcube/net_sieve to pear/Net_Sieve
- switch to fedora/autoloader
- add weak dependencies for optional components
- use upstream complete archive for JS libraries
- add a minimal %%check for our autoloader

* Fri Apr 28 2017 Remi Collet <remi@remirepo.net> - 1.2.5-1
- update to 1.2.5

* Sat Mar 11 2017 Remi Collet <remi@fedoraproject.org> - 1.2.4-1
- update to 1.2.4
- don't install plugin test suites

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- update to 1.2.3

* Thu Sep 29 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Sun Jul 31 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-3
- use /var/lib/roundcubemail/temp for temporary files
- add /var/lib/roundcubemail/enigma for GPG keys storage
- move plugins configuration samples in /etc/roundcubemail
- fix permission adjustments required for encryption support #1347332

* Wed Jul 27 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Fri May 27 2016 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0
- add dependency on Crypt_GPG   >= 1.4.1
- raise dependency on Net_LDAP2 >= 2.2.0
- raise dependency on Mail_Mime >= 1.10.0
- replace dependency on pear/Net_Sieve by roundcube/net_sieve >= 1.5.0

* Thu Apr 21 2016 Remi Collet <remi@fedoraproject.org> - 1.1.5-1
- update to 1.1.5
- sources from github
- add dependency on Net_Socket >= 1.0.12

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Remi Collet <remi@fedoraproject.org> - 1.1.4-2
- update to 1.1.4
- raise dependency on Net_SMTP 1.7.1
- add .log suffix to all log files, and rotate all #1269164
- more secure permissions on /var/log and /var/lib #1269155

* Tue Sep 15 2015 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- update to 1.1.3
- raise dependencies on Mail_Mime 1.9.0, Net_Sieve 1.3.4,
  Net_SMTP 1.6.3
- drop dependency on Mail_mimeDecode
- add explicit license spec file headers (MIT per FPCA)

* Wed Jul  8 2015 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- update to 1.1.2 for CVE-2015-5381 CVE-2015-5382 CVE-2015-5383

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Robert Scheck <robert@fedoraproject.org> - 1.1.1-2
- switch run-time requirement from php-mcrypt to php-openssl

* Fri Mar 20 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Wed Mar  4 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-2
- add optional dependencies for LDAP management on
  Net_LDAP2 and Net_LDAP3

* Mon Feb 16 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- provide Nginx configuration (Fedora >= 21)
- use %%license

* Thu Feb 05 2015 Jon Ciesla <limburgher@gmail.com> - 1.0.5-1
- Fix for security issues.

* Sat Dec 20 2014 Adam Williamson <awilliam@redhat.com> - 1.0.4-2
- drop tinymce bbcode plugin for safety (CVE-2012-4230)

* Sat Dec 20 2014 Adam Williamson <awilliam@redhat.com> - 1.0.4-1
- new release 1.0.4 (security update)

* Tue Oct 14 2014 Adam Williamson <awilliam@redhat.com> - 1.0.3-1
- update to 1.0.3
- drop small chunk of confpath.patch that got done upstream

* Mon Jul 21 2014 Adam Williamson <awilliam@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Robert Scheck <robert@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu May  8 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- Update to 1.0.0
- provide the installer
- cleanup some config options from previous version
- requires mailcap for /etc/mime.types
- explicitly requires all needed extensions

* Tue Oct 22 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.5-1
- Fix for CVE-2013-6172, BZ 1021735, 1021965.

* Mon Sep 09 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.4-1
- 0.9.4
- Change httpd dep to webserver, BZ 1005696.

* Fri Aug 23 2013 Adam Williamson <awilliam@redhat.com> - 0.9.3-2
- patch tinymce to cope elegantly with Flash binary being removed

* Fri Aug 23 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.3-1
- Fix two XSS vulnerabilities:
- http://trac.roundcube.net/ticket/1489251

* Fri Aug 16 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.2-3
- Drop precompiled flash.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Adam Williamson <awilliam@redhat.com> - 0.9.2-1
- latest upstream
- correct License field, add comment on complex licensing case

* Wed May 01 2013 Adam Williamson <awilliam@redhat.com> - 0.9.0-1
- latest upstream
- drop MDB2 dependencies, add php-pdo dependency (upstream now using
  pdo not MDB2)
- drop the update.sh script as it requires the installer framework we
  don't ship
- update the Fedora README for changes to sqlite and update process
- drop strict.patch, upstream actually merged it years ago, just in
  a slightly different format, and we kept dumbly diffing it
- drop references to obsolete patches (all merged upstream long ago)

* Thu Mar 28 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.6-1
- Latest upstream, fixes local file inclusion via web UI
- modification of certain config options.

* Fri Feb 08 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.5-1
- Latest upstream, CVE-2012-6121.

* Mon Dec 03 2012 Remi Collet <remi@fedoraproject.org> - 0.8.4-2
- requires php-fileinfo instead of php-pecl-Fileinfo

* Mon Nov 19 2012 Jon Ciesla <limburgher@gmail.com> - 0.8.4-1
- Latest upstream.

* Mon Oct 29 2012 Remi Collet <remi@fedoraproject.org> - 0.8.2-3
- fix configuration for httpd 2.4 (#871123)

* Sun Oct 28 2012 Remi Collet <remi@fedoraproject.org> - 0.8.2-2
- add fix for latest MDB2 (#870933)

* Wed Oct 10 2012 Jon Ciesla <limburgher@gmail.com> - 0.8.2-1
- Latest upstream.

* Thu Aug 30 2012 Adam Williamson <awilliam@redhat.com> - 0.8.1-2
- correct stray parenthesis in strict patch

* Mon Aug 20 2012 Jon Ciesla <limburgher@gmail.com> - 0.8.1-1
- Latest upstream.
- Updated strict patch.
- XSS patch upstreamed.

* Mon Aug 20 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.3-1
- 0.7.3, patch for XSS in signature issue, BZ 849616, 849617.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.2-2
- Rediffed strict patch.

* Mon Mar 12 2012 Adam Williamson <awilliam@redhat.com> - 0.7.2-1
- new upstream release 0.7.2

* Thu Feb 16 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.1-2
- Fix logrotate, BZ 789552.
- Modify error logging for strict, BZ 789576.

* Wed Feb  1 2012 Adam Williamson <awilliam@redhat.com> - 0.7.1-1
- new upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Adam Williamson <awilliam@redhat.com> - 0.7-1
- new upstream release
- drop all patches except confpath.patch:
    + html2text.patch and all CVE fixes were merged upstream
    + pg-mdb2.patch no longer necessary as all currently supported
      Fedora releases have a php-pear-MDB2-Driver-pgsql package new
      enough to work with this option

* Fri Oct 07 2011 Jon Ciesla <limb@jcomserv.net> = 0.6-1
- New upstream.

* Tue Sep 06 2011 Jon Ciesla <limb@jcomserv.net> = 0.5.4-1
- New upstream, fixes multiple security issues.

* Tue Jul 05 2011 Jon Ciesla <limb@jcomserv.net> = 0.5.3-1
- New upstream.

* Tue May 17 2011 Jon Ciesla <limb@jcomserv.net> = 0.5.2-1
- New upstream.

* Thu Feb 10 2011 Jon Ciesla <limb@jcomserv.net> = 0.5.1-1
- New upstream.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Jon Ciesla <limb@jcomserv.net> = 0.4.2-1
- New upstream.

* Mon Oct 04 2010 Jon Ciesla <limb@jcomserv.net> = 0.4.1-1
- New upstream.

* Mon Feb 01 2010 Jon Ciesla <limb@jcomserv.net> = 0.3.1-2
- Patch to fix CVE-2010-0464, BZ 560143.

* Mon Nov 30 2009 Jon Ciesla <limb@jcomserv.net> = 0.3.1-1
- New upstream.

* Thu Oct 22 2009 Jon Ciesla <limb@jcomserv.net> = 0.3-2
- Macro fix, BZ530037.

* Wed Sep 23 2009 Jon Ciesla <limb@jcomserv.net> = 0.3-1
- New upstream.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Jon Ciesla <limb@jcomserv.net> = 0.2.2-2
- Incorporated Chris Eveleigh's config changes to fix mimetype bug, BZ 511857.

* Wed Jul 01 2009 Jon Ciesla <limb@jcomserv.net> = 0.2.2-1
- New upstream.

* Fri Apr 10 2009 Jon Ciesla <limb@jcomserv.net> = 0.2.1-1
- New upstream.

* Mon Mar 30 2009 Jon Ciesla <limb@jcomserv.net> = 0.2-9.stable
- Patch for PG until php-pear-MDB2 hits 1.5.0 stable. BZ 489505.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8.stable
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Jon Ciesla <limb@jcomserv.net> = 0.2-7.stable
- Patch for CVE-2009-0413, BZ 484052.

* Mon Jan 05 2009 Jon Ciesla <limb@jcomserv.net> = 0.2-6.stable
- New upstream.
- Dropped two most recent patches, applied upstream.

* Wed Dec 17 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-5.beta
- Security fix, BZ 476830.

* Fri Dec 12 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-4.beta
- Security fix, BZ 476223.

* Thu Oct 09 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-3.beta
- New upstream.

* Mon Jun 16 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-2.alpha
- osx files removed upstream.

* Mon Jun 16 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-1.alpha
- Fixed php-xml, php-mbstring Requires.  BZ 451652.
- Removing osx files, will be pulled from next upstream release.

* Fri Jun 13 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-0.alpha
- Update to 0.2-alpha, security fixes for BZ 423271. 
- mysql update and pear patches applied upstream.
- Patched config paths.

* Fri Apr 18 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-5
- Added php-pecl-Fileinfo Reqires. BZ 442728.

* Wed Apr 16 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-4
- Added mcrypt, MDB2 Requires.  BZ 442728.

* Thu Apr 10 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-3
- Patch to fix PEAR path issue, drop symlinks.

* Thu Apr 10 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-2
- Drop %%pre script that was breaking pear packages.

* Wed Apr 09 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-1
- New upstream release.
- Added patch to fix mysql update.

* Tue Mar 18 2008 Jon Ciesla <limb@jcomserv.net> = 0.1-1
- Updgrade to 0.1 final, -dep.
- Added new mimeDecode dep.

* Mon Feb 04 2008 Jon Ciesla <limb@jcomserv.net> = 0.1-0.10rc2.1
- Changed to upstream -dep tarball, GPL-compliant.

* Fri Feb 01 2008 Jon Ciesla <limb@jcomserv.net> = 0.1-0.9rc2.1
- re-removed PEAR components that slipped back in after rc1.

* Fri Oct 26 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.8rc2
- Upgrade to 0.1-rc2

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.7rc1.1
- License tag correction.

* Tue Jul 03 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.6rc1.1
- New upstream release, all GPL, all current languages included.

* Mon May 14 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.5.beta2.2
- Fixed source timestamps, added Russian langpack.
- Added logpath fix to main.inc.php
- Fixed logrotate filename.

* Fri May 11 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.4.beta2.2
- Cleanup/elegantization of spec, .conf.

* Thu May 10 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.3.beta2.2
- Fixed bad chars in script.

* Thu May 10 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.2.beta2.2
- Added all langpacks.

* Thu May 10 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.1.beta2.2
- Versioning fix.

* Wed May 09 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-beta2.3
- Fixed generation of DES.
- Cleanup re patch.

* Mon May 07 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-beta2.2.3
- Removed duplicate docs.
- Moved SQL to doc.
- Fixed perms on log dir, sysconfdir.
- Fixed Requires.  
- Fixed config.
- Fixed changelog spacing.
  
* Fri May 04 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-beta2.2.2
- Created new source tarball with PEAR code removed. Added script for creation.

* Tue Feb 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-beta2.2.1
- Excluded Portions from PEAR, included as dependancies
- Fixed log/temp issues, including logrotate

* Tue Jan 30 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-beta2.2
- Initial packaging.
