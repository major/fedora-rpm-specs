Summary: A wiki engine
Name: mediawiki
Version: 1.43.0
Release: 1%{?dist}
License: GPL-2.0-or-later
URL: https://www.mediawiki.org/
Source0: https://releases.wikimedia.org/mediawiki/1.43/%{name}-%{version}.tar.gz
Source1: https://releases.wikimedia.org/mediawiki/1.43/%{name}-%{version}.tar.gz.sig
Source2: mediawiki.conf
Source3: README.RPM
Source4: mw-createinstance.in
Source5: mw-updateallinstances.in

BuildArch: noarch

BuildRequires: djvulibre
BuildRequires: perl-generators
BuildRequires: php-cli
BuildRequires: php-gd
BuildRequires: php-intl
BuildRequires: php-pdo
#BuildRequires: php-phpunit-PHPUnit
BuildRequires: php-theseer-autoload
BuildRequires: php-composer(cssjanus/cssjanus) >= 2.3.0
BuildRequires: php-composer(liuggio/statsd-php-client) >= 1.0.18
BuildRequires: php-composer(oojs/oojs-ui) >= 0.51.2
BuildRequires: php-composer(psr/log) >= 1.1.4
BuildRequires: php-composer(wikimedia/assert) >= 0.5.1
BuildRequires: php-composer(wikimedia/cdb) >= 3.0.0
BuildRequires: php-composer(wikimedia/utfnormal) >= 4.0.0
BuildRequires: php-composer(zordius/lightncandy) >= 1.2.6
BuildRequires: php-pear(Mail) >= 2.0.0
BuildRequires: php-pear(Mail_Mime) >= 1.10.12
BuildRequires: php-pear(Net_SMTP) >= 1.12.1
BuildRequires: php-pear(Net_Socket) >= 1.2.2
BuildRequires: python3-devel

Requires: httpd-filesystem
Requires: php(httpd)
Requires: php(language) >= 7.4.3
Requires: php-gd
Requires: php-xml
Requires: diffutils
Recommends: ImageMagick
Requires: php-composer(cssjanus/cssjanus) >= 2.3.0
Requires: php-composer(liuggio/statsd-php-client) >= 1.0.18
Requires: php-composer(oojs/oojs-ui) >= 0.51.2
Requires: php-composer(psr/log) >= 1.1.4
Requires: php-composer(wikimedia/assert) >= 0.5.1
Requires: php-composer(wikimedia/cdb) >= 3.0.0
Requires: php-composer(wikimedia/utfnormal) >= 4.0.0
Requires: php-composer(zordius/lightncandy) >= 1.2.6
Requires: php-pear(Mail) >= 2.0.0
Requires: php-pear(Mail_Mime) >= 1.10.12
Requires: php-pear(Net_SMTP) >= 1.12.1
Requires: php-pear(Net_Socket) >= 1.2.2

# Update script call command-line php
Requires(post): php-cli

Obsoletes: php-mediawiki-at-ease <= 1.1.0
Obsoletes: php-wikimedia-ip-set <= 3.1.0
Obsoletes: php-wikimedia-avro <= 1.9.0

Provides: bundled(php-christian-riesen-base32) = 1.6.0
Provides: bundled(php-composer-semver) = 3.4.3
Provides: bundled(php-guzzlehttp-guzzle) = 7.9.2
Provides: bundled(php-guzzlehttp-promises) = 2.0.4
Provides: bundled(php-guzzlehttp-psr7) = 2.7.0
Provides: bundled(php-jakobo-hotp-php) = 2.0.0
Provides: bundled(php-justinrainbow-json-schema) = 5.3.0
Provides: bundled(php-monolog-monolog) = 2.9.3
Provides: bundled(php-pear-console_getopt) = 1.4.3
Provides: bundled(php-pear-Net_URL2) = 2.2.2
Provides: bundled(php-pear-pear-core-minimal) = 1.10.15
Provides: bundled(php-pear-pear_exception) = 1.0.2
Provides: bundled(php-psr-container) = 1.1.2
Provides: bundled(php-psr-http-client) = 1.0.3
Provides: bundled(php-psr-http-factory) = 1.1.0
Provides: bundled(php-psr-http-message) = 1.1
Provides: bundled(php-ralouphie-getallheaders) = 3.0.3
Provides: bundled(php-symfony-deprecation-contracts) = 2.5.3
Provides: bundled(php-symfony-polyfill-php80) = 1.31.0
Provides: bundled(php-symfony-polyfill-php81) = 1.31.0
Provides: bundled(php-symfony-polyfill-php82) = 1.31.0
Provides: bundled(php-symfony-polyfill-php83) = 1.31.0
Provides: bundled(php-symfony-yaml) = 5.4.45
Provides: bundled(php-wikimedia-at-ease) = 3.0.0
Provides: bundled(php-wikimedia-common-passwords) = 0.5.0
Provides: bundled(php-wikimedia-composer-merge-plugin) = 2.1.0
Provides: bundled(php-wikimedia-equivset) = 1.7.0
Provides: bundled(php-wikimedia-timestamp) = 4.1.1
Provides: bundled(php-wikimedia-base-convert) = 2.0.2
Provides: bundled(php-wikimedia-bcp-47-code) = 2.0.0
Provides: bundled(php-wikimedia-cldr-plural-rule-parser) = 2.0.0
Provides: bundled(php-wikimedia-composer-merge-plugin) = 2.0.1
Provides: bundled(php-wikimedia-html-formatter) = 4.1.0
Provides: bundled(php-wikimedia-ip-utils) = 5.0.0
Provides: bundled(php-wikimedia-json-codec) = 3.0.3
Provides: bundled(php-wikimedia-langconv) = 0.4.2
Provides: bundled(php-wikimedia-less.php) = 5.1.2
Provides: bundled(php-wikimedia-minify) = 2.8.0
Provides: bundled(php-wikimedia-normalized-exception) = 2.0.0
Provides: bundled(php-wikimedia-object-factory) = 5.0.1
Provides: bundled(php-wikimedia-parsoid) = 0.20.1
Provides: bundled(php-wikimedia-php-session-serializer) = 3.0.0
Provides: bundled(php-wikimedia-purtle) = 2.0.0
Provides: bundled(php-wikimedia-relpath) = 4.0.1
Provides: bundled(php-wikimedia-remex-html) = 4.1.1
Provides: bundled(php-wikimedia-request-timeout) = 2.0.0
Provides: bundled(php-wikimedia-running-stat) = 2.1.0
Provides: bundled(php-wikimedia-scoped-callback) = 5.0.0
Provides: bundled(php-wikimedia-services) = 4.0.0
Provides: bundled(php-wikimedia-shellbox) = 4.1.1
Provides: bundled(php-wikimedia-timestamp) = 4.1.1
Provides: bundled(php-wikimedia-wait-condition-loop) = 2.0.2
Provides: bundled(php-wikimedia-wrappedstring) = 4.0.1
Provides: bundled(php-wikimedia-xmp-reader) = 0.9.4
Provides: bundled(php-wikimedia-zest-css) = 3.0.1


%description
MediaWiki is the software used for Wikipedia and the other Wikimedia
Foundation websites. Compared to other wikis, it has an excellent
range of features and support for high-traffic websites using multiple
servers

This package supports wiki farms. Read the instructions for creating wiki
instances under %{_pkgdocdir}/README.RPM.
Remember to remove the config dir after completing the configuration.


%prep
%autosetup
# Remove extension as it ships a bundled lua binary
rm -rf extensions/Scribunto
# Remove bundled PHP libraries in order to use system versions
rm -rf vendor/composer/*php
rm -rf vendor/composer/*json
rm -rf vendor/composer/LICENSE
rm -rf vendor/cssjanus
rm -rf vendor/liuggio
rm -rf vendor/oojs
#rm -rf vendor/oyejorge
rm -rf vendor/pear/mail
rm -rf vendor/pear/mail_mime
rm -rf vendor/pear/mail_mime-decode
rm -rf vendor/psr/log
rm -rf vendor/wikimedia/assert
rm -rf vendor/wikimedia/avro
rm -rf vendor/wikimedia/cdb
rm -rf vendor/wikimedia/composer-merge-plugin
rm -rf vendor/wikimedia/ip-set
rm -rf vendor/wikimedia/utfnormal
rm -rf vendor/zordius
ln -s %{_datadir}/php/cssjanus vendor/cssjanus-shared
ln -s %{_datadir}/php/Liuggio vendor/liuggio-shared
ln -s %{_datadir}/php/OOUI vendor/oojs-shared
#ln -s %%{_datadir}/php/lessphp vendor/oyejorge-shared
ln -s %{_datadir}/pear/Mail vendor/pear/mail-shared
ln -s %{_datadir}/php/Psr vendor/psr-shared
ln -s %{_datadir}/php/Wikimedia vendor/wikimedia/assert-shared
ln -s %{_datadir}/php/avro vendor/wikimedia/avro-shared
ln -s %{_datadir}/php/Cdb vendor/wikimedia/cdb-shared
ln -s %{_datadir}/php/IPSet vendor/wikimedia/ip-set-shared
ln -s %{_datadir}/php/UtfNormal vendor/wikimedia/utfnormal-shared
ln -s %{_datadir}/php/zordius vendor/zordius-shared
# Fix up Python shebangs
%py3_shebang_fix \
  maintenance/language/zhtable/Makefile.py \
  extensions/ConfirmEdit/captcha.py \
  extensions/SyntaxHighlight_GeSHi/pygments/create_pygmentize_bundle

%build
%{_bindir}/php -d memory_limit=1G %{_bindir}/phpab --follow --tolerant --output vendor/autoload.php vendor
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/at-ease/src/AtEase.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/base-convert/src/Functions.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/html-formatter/src/HtmlFormatter.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/php-session-serializer/src/PhpSessionSerializer.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/timestamp/src/defines.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/relpath/src/RelPath.php';" >> vendor/autoload.php


%install
# move away the documentation to the final folder.
cp -p %{SOURCE3} .

# now copy the rest to the buildroot.
mkdir -p %{buildroot}%{_datadir}/mediawiki
cp -a * %{buildroot}%{_datadir}/mediawiki/

# remove unneeded parts
rm -fr %{buildroot}%{_datadir}/mediawiki/{t,test,tests}
rm -fr %{buildroot}%{_datadir}/mediawiki/includes/zhtable
find %{buildroot}%{_datadir}/mediawiki/ \
  \( -name .htaccess -or -name \*.cmi \) \
  | xargs -r rm
rm -fr %{buildroot}%{_datadir}/mediawiki/maintenance/hhvm/

# fix permissions
find %{buildroot}%{_datadir}/mediawiki -name \*.pl | xargs -r chmod +x
chmod +x %{buildroot}%{_datadir}/mediawiki/maintenance/storage/make-blobs
chmod +x %{buildroot}%{_datadir}/mediawiki/extensions/ConfirmEdit/captcha.py

# remove version control/patch files
find %{buildroot} -name .svnignore | xargs -r rm
find %{buildroot} -name \*.commoncode | xargs -r rm
find %{buildroot} -name .gitreview | xargs -r rm
find %{buildroot} -name .jshintignore | xargs -r rm
find %{buildroot} -name .jshintrc | xargs -r rm

# placeholder for a default instance
mkdir -p %{buildroot}/var/www/wiki

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -p -m 0644 %{SOURCE2} \
  %{buildroot}%{_sysconfdir}/httpd/conf.d/mediawiki.conf

# tools for keeping mediawiki instances current
mkdir -p %{buildroot}%{_sbindir}
sed -e's,@datadir@,%{_datadir},g' -e's,@sysconfdir@,%{_sysconfdir},g' \
  < %{SOURCE4} > %{buildroot}%{_sbindir}/mw-createinstance
sed -e's,@datadir@,%{_datadir},g' -e's,@sysconfdir@,%{_sysconfdir},g' \
  < %{SOURCE5} > %{buildroot}%{_sbindir}/mw-updateallinstances
chmod 0755 %{buildroot}%{_sbindir}/mw-*
mkdir %{buildroot}%{_sysconfdir}/mediawiki
echo /var/www/wiki > %{buildroot}%{_sysconfdir}/mediawiki/instances


%check
php maintenance/install.php \
    --dbtype sqlite \
    --dbname mediawiki-test \
    --dbpath /tmp \
    --pass test123456 \
    Test test
cd tests/phpunit
# Database tests currently fail on the 1.26 release series
# https://phabricator.wikimedia.org/T122301
# KafkaHandlerTest tests now fail in 1.26.3
#make database
# Some tests now fail on the 1.27 release series.
#FLAGS="--exclude-group Broken,ParserFuzz,Destructive,Database,Stub,default" make phpunit


%post
%{_sbindir}/mw-updateallinstances >> /var/log/mediawiki-updates.log 2>&1 || :


%files
%doc FAQ HISTORY README.md README.RPM RELEASE-NOTES-1.43 UPGRADE CREDITS docs
%license COPYING
%{_datadir}/mediawiki
/var/www/wiki
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mediawiki.conf
%dir %{_sysconfdir}/mediawiki
%config(noreplace) %{_sysconfdir}/mediawiki/instances
%{_sbindir}/mw-createinstance
%{_sbindir}/mw-updateallinstances


%changelog
* Thu Jan 16 2025 Michael Cronenworth <mike@cchtml.com> - 1.43.0-1
- Update to 1.43.0

* Mon Dec 09 2024 Orion Poplawski <orion@nwra.com> - 1.41.1-3
- Use run.php for maintenance scripts (rhbz#2330978)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 03 2024 Michael Cronenworth <mike@cchtml.com> - 1.41.1-1
- Update to 1.41.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Michael Cronenworth <mike@cchtml.com> - 1.40.0-1
- Update to 1.40.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.39.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 01 2023 Michael Cronenworth <mike@cchtml.com> - 1.39.3-1
- Update to 1.39.3

* Sun Feb 26 2023 Michael Cronenworth <mike@cchtml.com> - 1.39.2-1
- Update to 1.39.2
- https://www.mediawiki.org/wiki/Release_notes/1.39#MediaWiki_1.39.2
- Change ImageMagick to a weak dependency

* Sun Feb 26 2023 Orion Poplawski <orion@nwra.com> - 1.39.1-3
- Add <Directory> tags for skins in apache httpd config (bz#2171908)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.39.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Michael Cronenworth <mike@cchtml.com> - 1.39.1-1
- Update to 1.39.1
- https://www.mediawiki.org/wiki/Release_notes/1.39#MediaWiki_1.39.1

* Tue Nov 01 2022 Michael Cronenworth <mike@cchtml.com> - 1.38.4-1
- Update to 1.38.4

* Thu Sep 01 2022 Michael Cronenworth <mike@cchtml.com> - 1.38.2-1
- Update to 1.38.2
- https://www.mediawiki.org/wiki/Release_notes/1.38#MediaWiki_1.38.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Michael Cronenworth <mike@cchtml.com> - 1.38.1-1
- Update to 1.38.1
- https://www.mediawiki.org/wiki/Release_notes/1.38#MediaWiki_1.38.1

* Sat Mar 12 2022 Orion Poplawski <orion@nwra.com> - 1.37.1-3
- Avoid dangling symlinks in mw-createinstane, install rest.php

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Michael Cronenworth <mike@cchtml.com> - 1.37.1-1
- Update to 1.37.1
- https://www.mediawiki.org/wiki/Release_notes/1.37#MediaWiki_1.37.1

* Mon Oct 04 2021 Michael Cronenworth <mike@cchtml.com> - 1.36.2-1
- Update to 1.36.2
- https://www.mediawiki.org/wiki/Release_notes/1.36#MediaWiki_1.36.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Michael Cronenworth <mike@cchtml.com> - 1.36.0-1
- Update to 1.36.0
- https://www.mediawiki.org/wiki/Release_notes/1.36

* Mon Apr 12 2021 Michael Cronenworth <mike@cchtml.com> - 1.35.2-1
- Update to 1.35.2
- https://lists.wikimedia.org/pipermail/mediawiki-announce/2021-April/000272.html

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Michael Cronenworth <mike@cchtml.com> - 1.35.1-1
- Update to 1.35.1
- https://lists.wikimedia.org/pipermail/mediawiki-announce/2020-December/000268.html

* Wed Dec 02 2020 Michael Cronenworth <mike@cchtml.com> - 1.35.0-1
- Update to 1.35.0
- https://lists.wikimedia.org/pipermail/mediawiki-announce/2020-September/000263.html

* Fri Sep 25 2020 Michael Cronenworth <mike@cchtml.com> - 1.34.4-1
- Update to 1.34.4
- https://lists.wikimedia.org/pipermail/mediawiki-announce/2020-September/000262.html

* Thu Sep 24 2020 Michael Cronenworth <mike@cchtml.com> - 1.34.3-1
- Update to 1.34.3
- https://lists.wikimedia.org/pipermail/mediawiki-announce/2020-September/000260.html

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Michael Cronenworth <mike@cchtml.com> - 1.34.2-1
- Update to 1.34.2
- https://lists.wikimedia.org/pipermail/mediawiki-announce/2020-June/000252.html

* Thu Mar 26 2020 Michael Cronenworth <mike@cchtml.com> - 1.34.1-1
- Update to 1.34.1
- https://lists.wikimedia.org/pipermail/mediawiki-announce/2020-June/000252.html

* Thu Mar 05 2020 Michael Cronenworth <mike@cchtml.com> - 1.34.0-1
- Update to 1.34.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Michael Cronenworth <mike@cchtml.com> - 1.33.1-1
- Update to 1.33.1

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 1.33.0-2
- Change python support from 2 to 3 (RHBZ#1738080)

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 1.33.0-1
- Update to 1.33.0
- https://lists.wikimedia.org/pipermail/mediawiki-announce/2019-July/000235.html

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Michael Cronenworth <mike@cchtml.com> - 1.32.2-1
- Update to 1.32.2
- https://lists.wikimedia.org/pipermail/mediawiki-announce/2019-June/000230.html

* Wed May 01 2019 Michael Cronenworth <mike@cchtml.com> - 1.32.1-1
- Update to 1.32.1
- https://www.mediawiki.org/wiki/MediaWiki_1.32

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Michael Cronenworth <mike@cchtml.com> - 1.29.3-1
- Update to 1.29.3
- https://www.mediawiki.org/wiki/Release_notes/1.29#MediaWiki_1.29.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Michael Cronenworth <mike@cchtml.com> - 1.29.2-2
- Add links to new libraries (rhbz#1515022)

* Thu Nov 16 2017 Michael Cronenworth <mike@cchtml.com> - 1.29.2-1
- Update to 1.29.2

* Mon Sep 18 2017 Michael Cronenworth <mike@cchtml.com> - 1.29.1-1
- Update to 1.29.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Michael Cronenworth <mike@cchtml.com> - 1.29.0-1
- Update to 1.29.0

* Mon May 01 2017 Michael Cronenworth <mike@cchtml.com> - 1.28.2-1
- Update to 1.28.2
- https://www.mediawiki.org/wiki/Release_notes/1.28#MediaWiki_1.28.2

* Fri Apr 07 2017 Michael Cronenworth <mike@cchtml.com> - 1.28.1-2
- Remove hhvm pieces

* Thu Apr 06 2017 Michael Cronenworth <mike@cchtml.com> - 1.28.1-1
- Update to 1.28.1
- https://www.mediawiki.org/wiki/Release_notes/1.28#MediaWiki_1.28.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Michael Cronenworth <mike@cchtml.com> - 1.28.0-1
- Update to 1.28.0
- https://www.mediawiki.org/wiki/MediaWiki_1.28

* Mon Nov 28 2016 Michael Cronenworth <mike@cchtml.com> - 1.27.1-2
- Add relpath to autoloader. (rhbz#1398171)

* Sun Aug 28 2016 Michael Cronenworth <mike@cchtml.com> - 1.27.1-1
- Update to 1.27.1
- https://www.mediawiki.org/wiki/MediaWiki_1.27

* Wed Jun 29 2016 Michael Cronenworth <mike@cchtml.com> - 1.26.3-2
- PHP 7 rebuild

* Fri Jun 24 2016 Michael Cronenworth <mike@cchtml.com> - 1.26.3-1
- Update to 1.26.3
- https://www.mediawiki.org/wiki/Release_notes/1.26#MediaWiki_1.26.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Michael Cronenworth <mike@cchtml.com> - 1.26.2-1
- Update to 1.26.2
- https://www.mediawiki.org/wiki/Release_notes/1.26#MediaWiki_1.26.2

* Sun Nov 29 2015 Michael Cronenworth <mike@cchtml.com> - 1.26.0-1
- Update to 1.26.0
- https://www.mediawiki.org/wiki/Release_notes/1.26#MediaWiki_1.26.0

* Wed Oct 21 2015 Michael Cronenworth <mike@cchtml.com> - 1.25.3-1
- Update to 1.25.3
- https://www.mediawiki.org/wiki/Release_notes/1.25#MediaWiki_1.25.3

* Wed Aug 19 2015 Michael Cronenworth <mike@cchtml.com> - 1.25.2-2
- Rename shared library directories to not confict with old bundled names

* Tue Aug 18 2015 Michael Cronenworth <mike@cchtml.com> - 1.25.2-1
- Update to 1.25.2
- https://www.mediawiki.org/wiki/Release_notes/1.25#MediaWiki_1.25.2

* Wed Jun 24 2015 Michael Cronenworth <mike@cchtml.com> - 1.25.1-3
- Temp workaround for RHBZ#1230630
- Enable tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Michael Cronenworth <mike@cchtml.com> - 1.25.1-1
- Update to 1.25.1
- http://www.mediawiki.org/wiki/MediaWiki_1.25

* Thu May 21 2015 Michael Cronenworth <mike@cchtml.com> - 1.24.2-2
- Less restrictive requires on webserver and php engine (rhbz#1223712)

* Wed Apr 01 2015 Michael Cronenworth <mike@cchtml.com> - 1.24.2-1
- Update to 1.24.2
- (bug T85848, bug T71210) SECURITY: Don't parse XMP blocks that contain XML entities, to prevent various DoS attacks.
- (bug T85848) SECURITY: Don't allow directly calling Xml::isWellFormed, to reduce likelihood of DoS.
- (bug T88310) SECURITY: Always expand xml entities when checking SVG's.
- (bug T73394) SECURITY: Escape > in Html::expandAttributes to prevent XSS.
- (bug T85855) SECURITY: Don't execute another user's CSS or JS on preview.
- (bug T64685) SECURITY: Allow setting maximal password length to prevent DoS when using PBKDF2.
- (bug T85349, bug T85850, bug T86711) SECURITY: Multiple issues fixed in SVG filtering to prevent XSS and protect viewer's privacy.
- Fix case of SpecialAllPages/SpecialAllMessages in SpecialPageFactory to fix loading these special pages when $wgAutoloadAttemptLowercase is false.
- (bug T70087) Fix Special:ActiveUsers page for installations using PostgreSQL.
- (bug T76254) Fix deleting of pages with PostgreSQL. Requires a schema change and running update.php to fix.

* Thu Dec 18 2014 Michael Cronenworth <mike@cchtml.com> - 1.24.1-1
- Update to 1.24.1
- (bug T76686) [SECURITY] thumb.php outputs wikitext message as raw HTML, which could lead to xss. Permission to edit MediaWiki namespace is required to exploit this.
- (bug T77028) [SECURITY] Malicious site can bypass CORS restrictions in $wgCrossSiteAJAXdomains in API calls if it only included an allowed domain as part of its name.
- (bug T74222) The original patch for T74222 was reverted as unnecessary.
- Fixed a couple of entries in RELEASE-NOTES-1.24.
- (bug T76168) OutputPage: Add accessors for some protected properties.
- (bug T74834) Make 1.24 branch directly installable under PostgreSQL.

* Fri Nov 28 2014 Michael Cronenworth <mike@cchtml.com> - 1.24.0-1
- Update to 1.24.0
- Release notes: http://www.mediawiki.org/wiki/Release_notes/1.24

* Mon Nov 03 2014 Michael Cronenworth <mike@cchtml.com> - 1.23.6-1
- Update to 1.23.6
- (bug 67440) Allow classes to be registered properly from installer
- (bug 72274) Job queue not running (HTTP 411) due to missing Content-Length: header

* Thu Oct 02 2014 Michael Cronenworth <mike@cchtml.com> - 1.23.5-1
- Update to 1.23.5
- CVE-2014-7295 (bug 70672) SECURITY: OutputPage: Remove separation of css and js module
  allowance.

* Fri Sep 26 2014 Michael Cronenworth <mike@cchtml.com> - 1.23.4-1
- Update to 1.23.4
- (bug 69008) SECURITY: Enhance CSS filtering in SVG files. Filter <style> elements; normalize style
  elements and attributes before filtering; add checks for attributes that contain css; add unit tests
  for html5sec and reported bugs.
- (bug 65998) Make MySQLi work with non-standard socket.
- (bug 66986) GlobalVarConfig shouldn't throw exceptions for null-valued config settings.

* Thu Aug 28 2014 Michael Cronenworth <mike@cchtml.com> - 1.23.3-1
- Update to 1.23.3
- (bug 68501) Correctly handle incorrect namespace in cleanupTitles.php.
- (bug 64970) Fix support for blobs on DatabaseOracle::update.
- (bug 66574) Display MediaWiki:Loginprompt on the login page.
- (bug 67870) wfShellExec() cuts off stdout at multiples of 8192 bytes.
- (bug 60629) Handle invalid language code gracefully in 
  Language::fetchLanguageNames.
- (bug 62017) Restore the number of rows shown on Special:Watchlist.
- Check for boolean false result from database query in SqlBagOStuff.

* Thu Jul 31 2014 Michael Cronenworth <mike@cchtml.com> - 1.23.2-1
- Update to 1.23.2
- (bug 68187) SECURITY: Prepend jsonp callback with comment.
- (bug 66608) SECURITY: Fix for XSS issue in bug 66608: Generate the URL used for loading 
  a new page in Javascript,instead of relying on the URL in the link that has been clicked.
- (bug 65778) SECURITY: Copy prevent-clickjacking between OutputPage and ParserOutput.
- (bug 68313) Preferences: Turn stubthreshold back into a combo box.
- (bug 65214) Fix initSiteStats.php maintenance script.
- (bug 67594) Special:ActiveUsers: Fix to work with PostgreSQL.

* Wed Jun 25 2014 Michael Cronenworth <mike@cchtml.com> - 1.23.1-1
- Update to 1.23.1
- (bug 65839) SECURITY: Prevent external resources in SVG files.
- (bug 67025) Special:Watchlist: Don't try to render empty row.
- (bug 66922) Don't allow some E_NOTICE messages to end up in the LocalSettings.php.
- (bug 66467) FileBackend: Avoid using popen() when "parallelize" is disabled.
- (bug 66428) MimeMagic: Don't seek before BOF. This has weird side effects
  like only extracting the tail of the file partially or not at all.
- (bug 66182) Removed -x flag on some php files.

* Tue Jun 10 2014 Michael Cronenworth <mike@cchtml.com> - 1.23.0-1
- Update to 1.23.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Michael Cronenworth <mike@cchtml.com> - 1.22.7-1
- Update to 1.22.7
- (bug 65501) SECURITY: Don't parse usernames as wikitext on Special:PasswordReset.
- (bug 36356) Add space between two feed links.
- (bug 63269) Email notifications were not correctly handling the
  [[MediaWiki:Helppage]] message being set to a full URL. This is a regression
  from the 1.22.5 point release, which made the default value for it a URL.
  If you customized [[MediaWiki:Enotif body]] (the text of email notifications),
  you'll need to edit it locally to include the URL via the new variable
  $HELPPAGE instead of the parser functions fullurl and canonicalurl; otherwise
  you don't have to do anything.
- Add missing uploadstash.us_props for PostgreSQL.
- (bug 56047) Fixed stream wrapper in PhpHttpRequest.

* Fri Apr 25 2014 Michael Cronenworth <mike@cchtml.com> - 1.22.6-1
- Update to 1.22.6
- (bug 63251) (CVE-2014-2853) SECURITY: Escape sortKey in pageInfo.

* Fri Mar 28 2014 Michael Cronenworth <mike@cchtml.com> - 1.22.5-1
- Update to 1.22.5
- (bug 62497) SECURITY: Add CSRF token on Special:ChangePassword.
- (bug 62467) Set a title for the context during import on the cli.
- Fix custom local MediaWiki:Helppage values.
- mediawiki.js: Fix documentation breakage.
- (bug 58153) Make MySQLi work with non standard port.
- (bug 53887) Reintroduced a link to help pages in the default sidebar, that any sysop can customize by editing MediaWiki:Sidebar locally.
- (bug 53888) Corrected a regression in 1.22 which introduced red links on the login page. If you previously installed 1.22.x and have created a local page to make the red link blue, write its title as in MediaWiki:helplogin-url if you didn't already. Otherwise, you don't need to do anything, but you can translate the help page at https://www.mediawiki.org/wiki/Help:Logging_in .

* Sat Mar 15 2014 Michael Cronenworth <mike@cchtml.com> - 1.22.4-1
- Update to 1.22.4
- 1.22 branch now requires php-pecl-jsonc

* Sat Mar 01 2014 Michael Cronenworth <mike@cchtml.com> - 1.22.3-1
- Update to 1.22.3
- (bug 60771) SECURITY: Disallow uploading SVG files using non-whitelisted namespaces. Also disallow iframe elements. User will get an error including the namespace name if they use a non- whitelisted namespace.
- (bug 61346) SECURITY: Make token comparison use constant time. It seems like our token comparison would be vulnerable to timing attacks. This will take constant time.
- (bug 61362) SECURITY: API: Don't find links in the middle of api.php links.
- (bug 53710) Add sequence support for upsert in DatabaseOracle in the same way as in selectInsert
- (bug 60231, bug 58719) Various fixes to job running code in Wiki.php: Make it async on Windows. Fixed possible "invalid filename" errors on Windows. Redirect output to dev/null to avoid hanging PHP.
- (bug 60083) Correct sequence name for fresh Postgres installation. Spotted by gebhkla
- (bug 60531) Avoid variable naming conflicts in DatabasePostgres::selectSQLText. Spotted by gebhkla
- (bug 60094) Fix rebuildall.php fatal error with PostgreSQL.
- (bug 43817) Add error handling if descriptionmsg isn't defined for extension.
- (bug 60543) Special:PrefixIndex omits stripprefix=1 for "Next page" link.

* Tue Jan 28 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.22.2-1
- Update to 1.22.2
- (bug 60339) (CVE-2014-1610) SECURITY: Reported RCE in djvu thumbnailing
- (bug 58253) Check for very old PCRE versions in installer and updater
- (bug 60054) Make WikiPage::$mPreparedEdit public

* Tue Jan 14 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.22.1-1
- Update to 1.22.1
- (bug 57550) (CVE-2013-6452) SECURITY: Disallow stylesheets in SVG Uploads
- (bug 58088) (CVE-2013-6451) SECURITY: Don't normalize U+FF3C to \ in CSS Checks
- (bug 58472) (CVE-2013-6454) SECURITY: Disallow -o-link in styles
- (bug 58553) (CVE-2013-6453) SECURITY: Return error on invalid XML for SVG Uploads
- (bug 58699) (CVE-2013-6472) SECURITY: Fix RevDel log entry information leaks
- (bug 58178) Restore compatibility with curl < 7.16.2.
- (bug 56931) Updated the plural rules to CLDR 24. They are in new format which is detailed in UTS 35 Rev 33. The PHP parser and evaluator as well as the JavaScript evaluator were updated to support the new format. Plural rules for some languages have changed, most notably Russian. Affected software messages have been updated and marked for review at translatewiki.net. This change is backported from the development branch of MediaWiki 1.23.
- (bug 58434) The broken installer for database backend Oracle was fixed.
- (bug 58167) The web installer no longer throws an exception when PHP is compiled without support for MySQL yet with support for another DBMS.
- (bug 58640) Fixed a compatibility issue with PCRE 8.34 that caused pages to appear blank or with missing text.
- (bug 47055) Changed FOR UPDATE handling in Postgresql
- (bug 57026) Avoid extra parsing in prepareContentForEdit()

* Mon Dec 09 2013 Michael Cronenworth <mike@cchtml.com> - 1.22.0-1
- New upstream release.

* Tue Nov 19 2013 Michael Cronenworth <mike@cchtml.com> - 1.21.3-1
- New upstream release.

* Sat Oct 05 2013 Michael Cronenworth <mike@cchtml.com> - 1.21.2-2
- Packaging fixes. (#1006110, #1007377)

* Thu Sep 05 2013 Michael Cronenworth <mike@cchtml.com> - 1.21.2-1
- New upstream release.

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.21.1-6
- Perl 5.18 rebuild

* Sat Jul 27 2013 Michael Cronenworth <mike@cchtml.com> - 1.21.1-5
- Update mw-createinstance
- Support for UnversionedDocdirs

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.21.1-4
- Perl 5.18 rebuild

* Wed Jul 10 2013 Michael Cronenworth <mike@cchtml.com> - 1.21.1-3
- Fix Obsoletes

* Tue Jul 09 2013 Michael Cronenworth <mike@cchtml.com> - 1.21.1-2
- Provide/Obsolete now included extensions (#967811)

* Mon Jun 03 2013 Michael Cronenworth <mike@cchtml.com> - 1.21.1-1
- New upstream release.

* Tue May 28 2013 Michael Cronenworth <mike@cchtml.com> - 1.21.0-1
- New upstream release.

* Tue May 07 2013 Michael Cronenworth <mike@cchtml.com> - 1.20.5-1
- New upstream release.
- Obsolete mediawiki116 package.

* Wed Apr 17 2013 Michael Cronenworth <mike@cchtml.com> - 1.20.4-1
- New upstream release.

* Thu Apr 11 2013 Michael Cronenworth <mike@cchtml.com> - 1.20.3-3
- Update mw-* scripts. (#926899)

* Tue Mar 12 2013 Michael Cronenworth <mike@cchtml.com> - 1.20.3-2
- Update mw-createinstance for new access points.

* Mon Mar  4 2013 Michael Cronenworth <mike@cchtml.com> - 1.20.3-1
- New upstream release.

* Thu Feb 28 2013 Michael Cronenworth <mike@cchtml.com> - 1.20.2-2
- Fix upgrade path.

* Wed Feb 27 2013 Michael Cronenworth <mike@cchtml.com> - 1.20.2-1
- New upstream release.

* Wed Feb 27 2013 Michael Cronenworth <mike@cchtml.com> - 1.19.3-1
- New upstream release.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.5-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.5-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.5-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May  8 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.16.5-59
- Update to 1.16.5.

* Fri Apr 22 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.16.4-58
- texvc was being accidentially wiped out before packaging it.

* Sat Apr 16 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.16.4-57
- Update to 1.16.4.

* Sun Apr  3 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.16.2-56
- Update to 1.16.2.
- Fixes RH bugs #614065, #644325, #682281, #662402
- Enable suggestions while typing in search boxes by default.
- Add some basic mediawiki management scripts.

* Fri Sep 10 2010 Nick Bebout <nb@fedoraproject.org> - 1.15.4-55
- Mark mediawiki.conf as config(noreplace) (RH bug #614396).

* Mon Jul  5 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.15.4-54
- Update to 1.5.14 (Fixes CVE-2010-1647 CVE-2010-1648).
- Change BR php to php-common (RH bug #549822).

* Wed Apr  7 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.15.3-53
- Update to 1.15.3 (Fixes login CSRF vulnerability).

* Wed Mar 31 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.15.2-51
- Update to 1.15.2 (Fixes CSS validation issue and data leakage
  vulnerability).

* Fri Jul 24 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.15.1-50
- Add a README.RPM and a sample apache mediawiki.conf file.

* Thu Jul 23 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.15.1-49
- All (runtime) dependencies from mediawiki need to move to
  mediawiki-nomath.

* Mon Jul 13 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.15.1-48
- Update to 1.15.1 (Fixes XSS vulnerability).

* Sat Jul 11 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.15.0-47
- Fix api.php breakage.

* Sat Jun 13 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.15.0-46
- Update to 1.15.0.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Sat Feb 28 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.14.0-45
- Update to 1.14.0.

* Sun Feb 22 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.13.4-44
- Split package up, so some users can decide to not install math
  support (results in smaller installs), see RH bug #485447.

* Wed Feb 18 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.13.4-43
- Update to 1.13.4, closes RH bug #485728.

* Tue Dec 23 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.13.3-42
- Update to 1.13.3, closes RH bug #476621 (CVE-2008-5249,
  CVE-2008-5250, CVE-2008-5252 and CVE-2008-5687, CVE-2008-5688)

* Sun Oct  5 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.13.2-41
- Update to 1.13.2.

* Sun Aug 24 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.13.0-40
- Use consistently Patch0 and %%patch0.

* Sat Aug 16 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.13.0-39
- Update to 1.13.0.

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.10.4-40
- fix license tag

* Tue Mar  4 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.10.4-38
- Update to 1.10.4.

* Sun Feb 17 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.10.3-37
- Update to 1.10.3.
- Fixes CVE-2008-0460 (bug #430286).

* Wed May  9 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.10.0-35
- Update to 1.10.0.

* Thu Feb 22 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.9.3-34
- Update to 1.9.4.

* Mon Feb  5 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.9.2-33
- Update to 1.9.2.

* Fri Feb  2 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.9.1-32
- Fix permissions.
- Remove some parts not needed at runtime anymore.

* Thu Feb  1 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.9.1-31
- Update to 1.9.1.

* Sat Oct 14 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.8.2-28
- Update to 1.8.2.

* Wed Oct 11 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.8.1-27
- Update to 1.8.1.
- Update to 1.8.0.

* Mon Jul 10 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.7.1.

* Wed Jun  7 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.6.7.

* Fri May 26 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.6.6.

* Thu Apr 13 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.6.3.

* Sat Apr  8 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.6.2.

* Fri Apr  7 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.6.1.

* Mon Apr  3 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5.8.

* Thu Mar  2 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5.7.

* Thu Jan 19 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5.6.

* Fri Jan  6 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5.5.

* Sun Dec  4 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5.3.

* Fri Nov  4 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5.2.

* Mon Oct 31 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5.1.

* Thu Oct  6 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5.0.

* Fri Sep  2 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5rc4.

* Sun Jul 31 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5beta4.

* Fri Jul  8 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5beta3.

* Tue Jul  5 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.5beta2.

* Sun Jul  3 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.

