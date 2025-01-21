# Fedora spec file for wordpress
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global wp_content %{_datadir}/wordpress/wp-content

%global upstream_version 6.7.1
#global upstream_prever  RC5
#global upstream_lower   rc5

Summary:    Blog tool and publishing platform
URL:        https://wordpress.org/
Name:       wordpress
Version:    %{upstream_version}%{?upstream_prever:~%upstream_lower}
Release:    2%{?dist}
# Wordpress     is GPL-2.0-or-later
# php-simplepie is BSD-3-Clause
# php-getid3    is LGPL-3.0-or-later (or some others)
# php-mailer    is LGPL-2.1-only
License:    GPL-2.0-or-later AND BSD-3-Clause AND LGPL-3.0-or-later AND LGPL-2.1-only

Source0:    https://wordpress.org/%{name}-%{upstream_version}%{?upstream_prever:-%{upstream_prever}}.tar.gz
Source1:    wordpress-httpd-conf
Source2:    README.fedora.wordpress
Source3:    README.fedora.wordpress-mu
Source4:    wordpress-nginx-conf
# To minify JS assets
Source5:    wordpress-minify.php

# Patch out copyrighted text of Hello, Dolly
# (and replace it with Free Software Song)
Patch0: wordpress-5.2-hello.patch
# Drop swfupload: not built from source, not reasonably possible to do
Patch2: wordpress-6.4-no_swfupload.patch
# Adjust tinymce's media plugin not to use its SWF plugin. This changes
# 'p.getParam("flash_video_player_url",u.convertUrl(u.url+"/moxieplayer.swf"))'
# to 'false'
Patch3: wordpress-5.1-tinymce_noflash.patch
# We drop the SWF files from mediaelement
Patch4: wordpress-5.6-mediaelement_no_swf.patch
# RPM configuration:
# Path to installation
# Disable auto-updater
Patch5: wordpress-5.4-config.patch
# RPM are readonly
# disable version check and updated
# change DISALLOW_FILE_MODS default value to true
# ignore WP_AUTO_UPDATE_CORE (always false)
Patch6: wordpress-5.8-noupdate.patch
# Debian patch for jshint
Patch8: wordpress-5.1-remove-jshint-refs.patch


BuildArch: noarch
BuildRequires: php-cli
BuildRequires: php-patchwork-jsqueeze
BuildRequires: php(language) >= 7.2

Requires: webserver
Requires: php(httpd)
Suggests: httpd
# For directory ownership
Requires: httpd-filesystem
Requires: nginx-filesystem
Requires: php(language) >= 7.2
Requires: php-sodium
Requires: php-ctype
Requires: php-filter
Requires: php-mysqli

# From phpcompatinfo report for version 4.5.3
Requires: php-curl
Requires: php-date
Requires: php-dom
Requires: php-exif
Requires: php-fileinfo
Requires: php-gd
Requires: php-gettext
Requires: php-hash
Requires: php-iconv
Requires: php-intl
Requires: php-json
Requires: php-libxml
Requires: php-mbstring
Requires: php-openssl
Requires: php-pcre
Requires: php-simplexml
Requires: php-spl
Requires: php-xml
Requires: php-xmlreader
Requires: php-zip
Requires: php-zlib
Requires: httpd
# Unbundled
Requires: ca-certificates
# Bundled
# grep "SIMPLEPIE_VERSION'" wordpress/wp-includes/class-simplepie.php
Provides: bundled(php-simplepie) = 1.8.0
# grep ' VERSION '  wordpress/wp-includes/ID3/getid3.php
Provides: bundled(php-getid3) = 1.9.23
# grep ' VERSION ' wordpress/wp-includes/PHPMailer/PHPMailer.php
Provides: bundled(php-phpmailer)  = 6.9.2
Provides: wordpress-mu = %{version}-%{release}
Obsoletes: wordpress-mu < 2.9.3


%description
Wordpress is an online publishing / weblog package that makes it very easy,
almost trivial, to get information out to people on the web.

Important information in %{_pkgdocdir}/README.fedora


%prep
%setup -q -n wordpress

# swfupload can just die in its entirety
rm -rf wp-includes/js/swfupload

# remove .htaccess, protected by httpd config file
rm wp-content/plugins/akismet/.htaccess

# only for PHP < 7.0 without random_int
rm -rf wp-includes/random_compat
# only for PHP < 7.2 without sodium_crypto_box
rm -rf wp-includes/sodium_compat

%patch -P0 -p1 -b .dolly
%patch -P2 -p1
%patch -P3 -p1
# Adjust mediaelement not to use its SWF
%patch -P4 -p1
%patch -P8 -p1

# We patch .js files, so minify them
php %{SOURCE5} \
  wp-includes/js/tinymce/plugins/media/plugin.js \
  wp-includes/js/tinymce/plugins/media/plugin.min.js
php %{SOURCE5} \
  wp-includes/js/mediaelement/mediaelement-and-player.js \
  wp-includes/js/mediaelement/mediaelement-and-player.min.js
php %{SOURCE5} \
  wp-includes/js/mediaelement/mediaelement.js \
  wp-includes/js/mediaelement/mediaelement.min.js

# Re-Generated the archive
arc=wp-includes/js/tinymce/wp-tinymce.js
grep "^// Source" $arc | while read a b c
do
  if [ -f $c ]; then
    echo -e "\n$a $b $c"
    cat $c
  else
    exit 1
  fi
done >$arc.tmp
if [ -s $arc.tmp ]; then
  gzip -c $arc > $arc.gz
  ls -l $arc*
  mv $arc.tmp $arc
else
  exit 1
fi

# Create RPM configuration
sed -e 's/\r//' wp-config-sample.php >wp-config.php
%patch -P5 -p1
%patch -P6 -p1

# fix file encoding
sed -i -e 's/\r//' license.txt

: Bundled library versions
grep ' VERSION '  wp-includes/SimplePie/src/SimplePie.php
grep ' VERSION '  wp-includes/ID3/getid3.php
grep ' VERSION '  wp-includes/PHPMailer/PHPMailer.php


%build

%install
# Apache configuration
install -m 0644 -D -p %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/wordpress.conf

install -m 0644 -D -p %{SOURCE4} ${RPM_BUILD_ROOT}%{_sysconfdir}/nginx/default.d/wordpress.conf

# Application
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/wordpress
cp -pr * ${RPM_BUILD_ROOT}%{_datadir}/wordpress

# Configuration
install -m 0644 -D wp-config.php ${RPM_BUILD_ROOT}%{_sysconfdir}/wordpress/wp-config.php
/bin/ln -sf ../../../etc/wordpress/wp-config.php ${RPM_BUILD_ROOT}%{_datadir}/wordpress/wp-config.php

/bin/cp %{SOURCE2} ./README.fedora
/bin/cp %{SOURCE3} ./README.fedora-multiuser

# Create additional wp-content directories so we can own them
install -d ${RPM_BUILD_ROOT}%{wp_content}/{plugins,themes,upgrade,uploads}

# Remove empty files to make rpmlint happy
find ${RPM_BUILD_ROOT} -type f -empty -exec rm -vf {} \;
# These are docs, remove them from here, docify them later
rm -f ${RPM_BUILD_ROOT}%{_datadir}/wordpress/{license.txt,readme.html}

# Remove bundled ca-bundle.crt
rm ${RPM_BUILD_ROOT}%{_datadir}/wordpress/wp-includes/certificates/ca-bundle.crt
ln -s %{_sysconfdir}/pki/tls/certs/ca-bundle.crt \
   ${RPM_BUILD_ROOT}%{_datadir}/wordpress/wp-includes/certificates/ca-bundle.crt

# Remove backup copies of patches
find ${RPM_BUILD_ROOT} \( -name \*.dolly -o -name \*.rhbz522897 -o -name \*.orig \) \
    -print -delete


%pretrans -p <lua>
-- Remove link to system library
path = "%{_datadir}/wordpress/wp-includes/PHPMailer"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end


%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/wordpress.conf
%config(noreplace) %{_sysconfdir}/nginx/default.d/wordpress.conf
%dir %{_datadir}/wordpress
%{_datadir}/wordpress/wp-admin
%{_datadir}/wordpress/wp-includes
%{_datadir}/wordpress/index.php
%dir %{wp_content}/
%{wp_content}/index.php
%dir %attr(2775,apache,ftp) %{wp_content}/plugins
%dir %attr(2775,apache,ftp) %{wp_content}/themes
%dir %attr(2775,apache,ftp) %{wp_content}/upgrade
%dir %attr(2775,apache,ftp) %{wp_content}/uploads
%{wp_content}/plugins/*
%{wp_content}/themes/*
%{!?_licensedir:%global license %%doc}
%license license.txt
%doc readme.html
%doc README.fedora
%doc README.fedora-multiuser
%{_datadir}/wordpress/wp-*.php
%attr(750,root,apache) %dir               %{_sysconfdir}/wordpress
%attr(640,root,apache) %config(noreplace) %{_sysconfdir}/wordpress/wp-config.php
%{_datadir}/wordpress/xmlrpc.php


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 22 2024 Remi Collet <remi@remirepo.net> - 6.7.1-1
- WordPress 6.7.1 Maintenance Release

* Wed Nov 13 2024 Remi Collet <remi@remirepo.net> - 6.7-1
- WordPress 6.7 “Rollins”

* Wed Sep 11 2024 Remi Collet <remi@remirepo.net> - 6.6.2-1
- WordPress 6.6.2 Maintenance Release

* Wed Jul 24 2024 Remi Collet <remi@remirepo.net> - 6.6.1-1
- WordPress 6.6.1 Maintenance Release

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Remi Collet <remi@remirepo.net> - 6.6-1
- WordPress 6.6 “Dorsey”

* Tue Jul  2 2024 Remi Collet <remi@remirepo.net> - 6.5.5-1
- WordPress 6.4.2 Maintenance & Security Release

* Thu Jun  6 2024 Remi Collet <remi@remirepo.net> - 6.5.4-1
- WordPress 6.5.4 Maintenance Release

* Mon May 13 2024 Remi Collet <remi@remirepo.net> - 6.5.3-1
- WordPress 6.5.3 Maintenance Release

* Wed Apr 10 2024 Remi Collet <remi@remirepo.net> - 6.5.2-1
- WordPress 6.5.2 Maintenance and Security Release

* Wed Apr  3 2024 Remi Collet <remi@remirepo.net> - 6.5-1
- WordPress 6.5 “Regina”

* Thu Feb  1 2024 Remi Collet <remi@remirepo.net> - 6.4.3-1
- WordPress 6.4.3 Maintenance & Security Release

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec  7 2023 Remi Collet <remi@remirepo.net> - 6.4.2-1
- WordPress 6.4.2 Maintenance & Security Release

* Thu Nov  9 2023 Remi Collet <remi@remirepo.net> - 6.4.1-1
- WordPress 6.4.1 Maintenance Release

* Wed Nov  8 2023 Remi Collet <remi@remirepo.net> - 6.4-1
- WordPress 6.4 “Shirley”

* Mon Oct 16 2023 Remi Collet <remi@remirepo.net> - 6.3.2-1
- WordPress 6.3.2 – Maintenance and Security release

* Thu Aug 31 2023 Remi Collet <remi@remirepo.net> - 6.3.1-1
* WordPress 6.3.1 Maintenance Release

* Sun Aug 20 2023 Remi Collet <remi@remirepo.net> - 6.3-1
- WordPress 6.3 “Lionel”

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 21 2023 Remi Collet <remi@remirepo.net> - 6.2.2-1
- WordPress 6.2.2 Security Release

* Wed May 17 2023 Remi Collet <remi@remirepo.net> - 6.2.1-1
- WordPress 6.2.1 Maintenance & Security Release

* Thu Mar 30 2023 Remi Collet <remi@remirepo.net> - 6.2-1
- WordPress 6.2 “Dolphy”
- use SPDX license IDs

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Remi Collet <remi@remirepo.net> - 6.1.1-1
- WordPress 6.1.1 Maintenance Release

* Wed Nov  2 2022 Remi Collet <remi@remirepo.net> - 6.1-1
- WordPress 6.1 “Misha”

* Tue Oct 18 2022 Remi Collet <remi@remirepo.net> - 6.0.3-1
- WordPress 6.0.3 Security Release

* Thu Sep  8 2022 Remi Collet <remi@remirepo.net> - 6.0.2-1
- WordPress 6.0.2 Security and Maintenance Release

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Remi Collet <remi@remirepo.net> - 6.0.1-1
- WordPress 6.0.1 Maintenance Release

* Wed May 25 2022 Remi Collet <remi@remirepo.net> - 6.0-1
- WordPress 6.0 “Arturo”

* Wed Apr  6 2022 Remi Collet <remi@remirepo.net> - 5.9.3-1
- WordPress 5.9.3 Maintenance Release

* Fri Mar 11 2022 Remi Collet <remi@remirepo.net> - 5.9.2-1
- WordPress 5.9.2 Security & Maintenance Release

* Wed Feb 23 2022 Remi Collet <remi@remirepo.net> - 5.9.1-1
- WordPress 5.9.1 Maintenance Release

* Wed Jan 26 2022 Remi Collet <remi@remirepo.net> - 5.9-1
- WordPress 5.9 Josephine

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan  7 2022 Remi Collet <remi@remirepo.net> - 5.8.3-1
- WordPress 5.8.3 Security Release

* Tue Dec  7 2021 Remi Collet <remi@remirepo.net> - 5.8.2-2
- use bundled libraries

* Thu Nov 11 2021 Remi Collet <remi@remirepo.net> - 5.8.2-1
- WordPress 5.8.2 Security and Maintenance Release

* Thu Sep  9 2021 Remi Collet <remi@remirepo.net> - 5.8.1-1
- WordPress 5.8.1 Security and Maintenance Release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Remi Collet <remi@remirepo.net> - 5.8-1
- WordPress 5.8 Tatum

* Thu May 13 2021 Remi Collet <remi@remirepo.net> - 5.7.2-1
- WordPress 5.7.2 Security Release

* Thu Apr 15 2021 Remi Collet <remi@remirepo.net> - 5.7.1-1
- WordPress 5.7.1 Security and Maintenance Release

* Wed Mar 10 2021 Remi Collet <remi@remirepo.net> - 5.7-1
- WordPress 5.7 “Esperanza”

* Tue Feb 23 2021 Remi Collet <remi@remirepo.net> - 5.6.2-1
- WordPress 5.6.2 Maintenance Release

* Fri Feb  5 2021 Remi Collet <remi@remirepo.net> - 5.6.1-1
- WordPress 5.6.1 Maintenance Release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 2020 Remi Collet <remi@remirepo.net> - 5.6-1
- WordPress 5.6 “Simone”

* Sat Oct 31 2020 Remi Collet <remi@remirepo.net> - 5.5.3-1
- WordPress 5.5.3 Maintenance Release

* Fri Oct 30 2020 Remi Collet <remi@remirepo.net> - 5.5.2-1
- WordPress 5.5.2 Security and Maintenance Release

* Tue Oct 20 2020 Remi Collet <remi@remirepo.net> - 5.5.1-2
- Change FS_METHOD default to 'direct' to allow enabling FILE_MODS #1889644

* Wed Sep  2 2020 Remi Collet <remi@remirepo.net> - 5.5.1-1
- WordPress 5.5.1 Maintenance Release

* Wed Aug 12 2020 Remi Collet <remi@remirepo.net> - 5.5-1
- WordPress 5.5 “Eckstine”
- requires php-phpmailer6 instead of old php-PHPMailer

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Remi Collet <remi@remirepo.net> - 5.4.2-1
- WordPress 5.4.2 Security and Maintenance Release

* Thu Apr 30 2020 Remi Collet <remi@remirepo.net> - 5.4.1-1
- WordPress 5.4.1 Security and Maintenance Release

* Wed Apr  1 2020 Remi Collet <remi@remirepo.net> - 5.4-1
- WordPress 5.4 “Adderley”

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 5.4~rc5-1
- WordPress 5.4 RC 5

* Wed Mar 25 2020 Remi Collet <remi@remirepo.net> - 5.4~rc4-1
- WordPress 5.4 RC 4

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Remi Collet <remi@remirepo.net> - 5.3.2-1
- WordPress 5.3.2 Maintenance Release

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 5.3.1-1
- WordPress 5.3.1 Security and Maintenance Release

* Wed Nov 13 2019 Remi Collet <remi@remirepo.net> - 5.3-1
- WordPress 5.3 “Kirk”

* Tue Oct 15 2019 Remi Collet <remi@remirepo.net> - 5.2.4-1
- WordPress 5.2.4 Security Release

* Thu Sep  5 2019 Remi Collet <remi@remirepo.net> - 5.2.3-1
- WordPress 5.2.3 Security and Maintenance Release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Remi Collet <remi@remirepo.net> - 5.2.2-1
- WordPress 5.2.2 Maintenance Release

* Wed May 22 2019 Remi Collet <remi@remirepo.net> - 5.2.1-1
- WordPress 5.2.1 Maintenance Release

* Wed May  8 2019 Remi Collet <remi@remirepo.net> - 5.2.0-1
- WordPress 5.2 “Jaco”

* Fri Apr 26 2019 Remi Collet <remi@remirepo.net> - 5.2.0~rc1-1
- WordPress 5.2 RC 1

* Wed Apr 17 2019 Remi Collet <remi@remirepo.net> - 5.2.0~beta3-1
- WordPress 5.2 Beta 3

* Tue Apr  9 2019 Remi Collet <remi@remirepo.net> - 5.2.0~beta2-1
- WordPress 5.2 Beta 2

* Thu Mar 28 2019 Remi Collet <remi@remirepo.net> - 5.2.0~beta1-1
- WordPress 5.2 Beta 1
- raise dependency on PHP 7.2

* Fri Mar 22 2019 Remi Collet <remi@remirepo.net> - 5.1.1-4
- fix wp-tinymce.js is missing, wp-tinymce.js.gz is empty #1691524

* Wed Mar 13 2019 Remi Collet <remi@remirepo.net> - 5.1.1-1
- WordPress 5.1.1 Security and Maintenance Release

* Fri Feb 22 2019 Remi Collet <remi@remirepo.net> - 5.1-1
- WordPress 5.1 “Betty”

* Thu Feb 21 2019 Remi Collet <remi@remirepo.net> - 5.1~RC2-1
- WordPress 5.1-RC2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Remi Collet <remi@remirepo.net> - 5.0.3-1
- WordPress 5.0.3 Maintenance Release

* Thu Dec 20 2018 Remi Collet <remi@remirepo.net> - 5.0.2-1
- WordPress 5.0.2 Maintenance Release

* Thu Dec 13 2018 Remi Collet <remi@remirepo.net> - 5.0.1-1
- WordPress 5.0.1 Security Release

* Wed Dec 12 2018 Remi Collet <remi@remirepo.net> - 5.0-1
- WordPress 5.0 “Bebo”

* Fri Aug 03 2018 Kevin Fenzi <kevin@scrye.com> - 4.9.8-1
- Update to 4.9.8. Fixes bug #1611877

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Kevin Fenzi <kevin@scrye.com> - 4.9.7-1
- Update to 4.9.7 security update. Fixes bug #1598612
- Fixes CVE-2018-12895 bugs #1595584 and #1595585

* Fri May 18 2018 Kevin Fenzi <kevin@scrye.com> - 4.9.6-1
- Update to 4.9.6. Fixes bug #1579584

* Wed Apr  4 2018 Remi Collet <remi@remirepo.net> - 4.9.5-1
- WordPress 4.9.5 Security and Maintenance Release

* Wed Feb  7 2018 Remi Collet <remi@remirepo.net> - 4.9.4-1
- WordPress 4.9.4 Maintenance Release

* Wed Jan 17 2018 Remi Collet <remi@remirepo.net> - 4.9.2-1
- WordPress 4.9.2 Security and Maintenance Release
- drop non-free jshint.js file #1528765

* Thu Nov 30 2017 Remi Collet <remi@remirepo.net> - 4.9.1-1
- WordPress 4.9.1 Security and Maintenance Release

* Thu Nov 16 2017 Remi Collet <remi@remirepo.net> - 4.9-1
- WordPress 4.9 “Tipton”
- minify patched JS files

* Tue Oct 31 2017 Kevin Fenzi <kevin@scrye.com> - 4.8.3-1
- Update to 4.8.3. Security release. Fixes bug #1508255

* Wed Sep 20 2017 Remi Collet <remi@remirepo.net> - 4.8.2-1
- Update to 4.8.2 Security and Maintenance Release

* Thu Aug  3 2017 Remi Collet <remi@remirepo.net> - 4.8.1-1
- Update to 4.8.1 Maintenance Release.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun  9 2017 Remi Collet <remi@remirepo.net> - 4.8-1
- WordPress 4.8 “Evans”

* Wed May 17 2017 Remi Collet <remi@remirepo.net> - 4.7.5-1
- WordPress 4.7.5 Security and Maintenance Release

* Wed May 10 2017 Remi Collet <remi@remirepo.net> - 4.7.4-2
- protect .phar from being executed from uploads directory

* Sat Apr 22 2017 Kevin Fenzi <kevin@scrye.com> - 4.7.4-1
- Update to 4.7.4. Maintenance Release.

* Tue Mar  7 2017 Remi Collet <remi@fedoraproject.org> - 4.7.3-1
- WordPress 4.7.3 Security and Maintenance Release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Remi Collet <remi@fedoraproject.org> - 4.7.2-1
- WordPress 4.7.2 Security Release

* Thu Jan 12 2017 Remi Collet <remi@fedoraproject.org> - 4.7.1-1
- WordPress 4.7.1 Security and Maintenance Release

* Wed Dec  7 2016 Remi Collet <remi@fedoraproject.org> - 4.7.0-1
- WordPress 4.7 “Vaughan”

* Thu Sep  8 2016 Remi Collet <remi@fedoraproject.org> - 4.6.1-1
- WordPress 4.6.1 Security and Maintenance Release

* Sat Sep  3 2016 Remi Collet <remi@fedoraproject.org> - 4.6-2
- WordPress 4.6 “Pepper”
- fix directory permissions #1305687

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 4.5.3-2
- add patch to drop ereg dependency, see
  https://core.trac.wordpress.org/ticket/37194

* Wed Jun 22 2016 Remi Collet <remi@fedoraproject.org> - 4.5.3-1
- WordPress 4.5.3 Maintenance and Security Release

* Sat May 14 2016 Remi Collet <remi@fedoraproject.org> - 4.5.2-2
- never bundle ca-bundle.crt (EL-5)
- provide nginx configuration (fedora)
- drop mandatory dependency on httpd (suggested) #1336091
- protect php files in uploads directory

* Tue May 10 2016 Remi Collet <remi@fedoraproject.org> - 4.5.2-1
- WordPress 4.5.2 Security Release

* Wed Apr 27 2016 Remi Collet <remi@fedoraproject.org> - 4.5.1-1
- WordPress 4.5.1 Maintenance Release

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 4.5-1
- WordPress 4.5 “Coleman”

* Fri Mar 25 2016 Remi Collet <remi@fedoraproject.org> - 4.5-0.1.RC1
- WordPress 4.5 Release Candidate

* Wed Feb  3 2016 Remi Collet <remi@fedoraproject.org> - 4.4.2-1
- WordPress 4.4.2 Security and Maintenance Release

* Thu Jan  7 2016 Remi Collet <remi@fedoraproject.org> - 4.4.1-1
- WordPress 4.4.1 Security and Maintenance Release

* Wed Dec  9 2015 Remi Collet <remi@fedoraproject.org> - 4.4-1
- WordPress 4.4 “Clifford”

* Wed Sep 16 2015 Remi Collet <remi@fedoraproject.org> - 4.3.1-1
- WordPress 4.3.1 Security and Maintenance Release

* Wed Aug 26 2015 Remi Collet <remi@fedoraproject.org> - 4.3-1
- WordPress 4.3 “Billie”

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 4.2.4-1
- WordPress 4.2.4 Security and Maintenance Release

* Fri Jul 24 2015 Remi Collet <remi@fedoraproject.org> - 4.2.3-1
- WordPress 4.2.3 Security and Maintenance Release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May  7 2015 Remi Collet <remi@fedoraproject.org> - 4.2.2-1
- WordPress 4.2.2 Security and Maintenance Release

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 4.2.1-1
- WordPress 4.2.1 Security Release

* Fri Apr 24 2015 Remi Collet <remi@fedoraproject.org> - 4.2-1
- WordPress 4.2 “Powell”

* Thu Apr 23 2015 Remi Collet <remi@fedoraproject.org> - 4.1.2-1
- WordPress 4.1.2 Security Release

* Thu Feb 19 2015 Remi Collet <remi@fedoraproject.org> - 4.1.1-1
- WordPress 4.1.1 Maintenance Release

* Mon Dec 22 2014 Remi Collet <remi@fedoraproject.org> - 4.1-1
- WordPress 4.1 “Dinah”

* Fri Nov 21 2014 Remi Collet <remi@fedoraproject.org> - 4.0.1-1
- WordPress 4.0.1 Security Release

* Tue Sep 30 2014 Remi Collet <remi@fedoraproject.org> - 4.0-3
- use system php-getid3 when available #1145574

* Mon Sep  8 2014 Remi Collet <remi@fedoraproject.org> - 4.0-1
- WordPress 4.0 “Benny”

* Fri Aug  8 2014 Remi Collet <remi@fedoraproject.org> - 3.9.2-3
- config dir only readable by apache group, better fix for #1124582
- fix license handling

* Thu Aug  7 2014 Remi Collet <remi@fedoraproject.org> - 3.9.2-2
- update to 3.9.2 Security Release #1127547
- config file only readable by apache user (httpd or php-fpm) #1124582

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  9 2014 Remi Collet <remi@fedoraproject.org> - 3.9.1-1
- update to 3.9.1 Maintenance Release

* Wed May  7 2014 Remi Collet <remi@fedoraproject.org> - 3.9-1
- update to 3.9 “Smith”

* Tue Apr 15 2014 Remi Collet <remi@fedoraproject.org> - 3.8.3-1
- update to 3.8.3 Maintenance Release
  http://wordpress.org/news/2014/04/wordpress-3-8-3/

* Wed Apr  9 2014 Remi Collet <remi@fedoraproject.org> - 3.8.2-1
- update to 3.8.2 Security Release
- fix privilege escalation issue  CVE-2014-0165
- fix authentication bypass issue CVE-2014-0166

* Sat Jan 25 2014 Remi Collet <remi@fedoraproject.org> - 3.8.1-3
- ignore WP_AUTO_UPDATE_CORE (always false)

* Fri Jan 24 2014 Remi Collet <remi@fedoraproject.org> - 3.8.1-2
- comment provided configuration about auto-updater
- disable auto-updater on default configuration #1057521
- switch some sed to patch (more robust)

* Thu Jan 23 2014 Adam Williamson <awilliam@redhat.com> - 3.8.1-1
- new upstream release 3.8.1 (bugfixes)

* Mon Dec 16 2013 Remi Collet <rcollet@redhat.com> - 3.8-1
- update to 3.8 “Parker” #1043104
- link to README.fedora in package description
- add note about optional packages #1037516
- add php dependencies: ereg, ftp, gd, xml
- del php dependencies: pdo, reflection

* Wed Oct 30 2013 Remi Collet <rcollet@redhat.com> - 3.7.1-1
- update to 3.7.1 (bugfixes)

* Fri Oct 25 2013 Remi Collet <rcollet@redhat.com> - 3.7-1
- update to 3.7
- requires ca-certificates for ca-bundle.crt

* Thu Sep 12 2013 Paul Wouters <pwouters@redhat.com> - 3.6.1-1
- update to 3.6.1, various bugs and security fixes:
  CVE-2013-4338 CVE-2013-4339 CVE-2013-4340

* Thu Aug 22 2013 Adam Williamson <awilliam@redhat.com> - 3.6.0-1
- update to 3.6.0
- drop pre-compiled Flash and Silverlight binaries - #1000267

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Remi Collet <rcollet@redhat.com> - 3.5.2-1
- version 3.5.2, various bug and security fixes:
  CVE-2013-2173 CVE-2013-2199 CVE-2013-2200 CVE-2013-2201
  CVE-2013-2202 CVE-2013-2203 CVE-2013-2204

* Tue Feb 12 2013 Remi Collet <rcollet@redhat.com> - 3.5.1-2
- provides POP3 class #905867
  POP3 is not from PHPMailer, but from SquirrelMail

* Wed Jan 30 2013 Remi Collet <rcollet@redhat.com> - 3.5.1-1.1
- fix simplepie links (for all branches)

* Wed Jan 30 2013 Remi Collet <rcollet@redhat.com> - 3.5.1-1
- version 3.5.1, various bug and security fixes:
  CVE-2013-0235, CVE-2013-0236 and CVE-2013-0237
- drop -f option from rm to break build if
  upstream archive content change
- protect akismet content (from upstream .htaccess)

* Wed Jan  2 2013 Remi Collet <rcollet@redhat.com> - 3.5-3
- fix links to system PHPMailer library

* Sun Dec 16 2012 Remi Collet <rcollet@redhat.com> - 3.5-2
- fix use of system Simplepie
- give access from local (httpd 2.4)

* Wed Dec 12 2012 Matěj Cepl <mcepl@redhat.com> - 3.5-1
- New upstream release.

* Tue Dec 04 2012 Matěj Cepl <mcepl@redhat.com> - 3.5-0.5.RC3
- New upstream release candidate.

* Fri Nov 30 2012 Matěj Cepl <mcepl@redhat.com> - 3.5-0.5.RC2
- New upstream release candidate.

* Sat Nov 24 2012 Matěj Cepl <mcepl@redhat.com> - 3.5-0.5.RC1
- New upstream release candidate.

* Tue Nov 13 2012 Matěj Cepl <mcepl@redhat.com> - 3.5-0.4.beta3
- New upstream beta3 version

* Mon Oct 29 2012 Remi Collet <rcollet@redhat.com> - 3.5-0.3.beta2
- use system PHPMailer
- requires needed php extensions

* Sat Oct 13 2012 Matěj Cepl <mcepl@redhat.com> - 3.5-0.2.beta2
- New upstream beta2 version

* Thu Oct 04 2012 Matěj Cepl <mcepl@redhat.com> - 3.5-0.2.beta1
- New upstream beta1 version
- Don’t even bother with removing gettext.php ... it is not used anymore

* Thu Sep 06 2012 Matej Cepl <mcepl@redhat.com> - 3.4.2-2
- Upstream security update.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Matej Cepl <mcepl@redhat.com> - 3.4.1-1
- New upstream release. Just improvements and security issues.

* Wed Jun 13 2012 Matej Cepl <mcepl@redhat.com> - 3.4-1
- New upstream release. The main changes from the upstream
  release notes:
  * theme customizer
  * XML-RPC themes and API improvements

* Tue Jun 12 2012 Matej Cepl <mcepl@redhat.com> - 3.4-0.2.RC3
- They still haven’t released.

* Thu Jun 07 2012 Matej Cepl <mcepl@redhat.com> - 3.4-0.2.RC2
- And yet another release candidate.

* Wed May 30 2012 Matej Cepl <mcepl@redhat.com> - 3.4-0.2.RC1
- We have a release candidate now.

* Thu May 03 2012 'Matej Cepl <mcepl@redhat.com>' - 3.4-0.2.beta4
- New week, new upstream beta. Less drama than last time.

* Mon Apr 23 2012 'Matěj Cepl <mcepl@redhat.com>' - 3.4-0.2.beta3
- And yet another upstream beta (fixes CVE-2011-0700 and
  CVE-2011-0701)

* Mon Apr 16 2012 Matěj Cepl <mcepl@redhat.com> - 3.4-0.2.beta2
- And yet another upstream beta

* Thu Apr 05 2012 'Matej Cepl <mcepl@redhat.com>' - 3.4-0.1.beta1
- New upstream beta release (just for Rawhide, to be sure we build)

* Wed Jan 04 2012 'Matej Cepl <mcepl@redhat.com>' - 3.3.1-1
- Security (XSS) and maintenance upstream release.

* Tue Dec 13 2011 'Matěj Cepl <mcepl@redhat.com>' - 3.3-1
- New upstream release.

* Wed Dec 07 2011 'Matěj Cepl <mcepl@redhat.com>' - 3.3-0.5.RC2
- ... and one day after I upgraded to RC1, we have new RC2 ;)

* Tue Dec 06 2011 'Matěj Cepl <mcepl@redhat.com>' - 3.3-0.4.RC1
- Cool we are on RC1!

* Thu Nov 24 2011 'Matěj Cepl <mcepl@redhat.com>' - 3.3-0.3.beta4
- Another upstream beta release (now hopefully, really close to RC)

* Fri Nov 11 2011 'Matěj Cepl <mcepl@redhat.com>' - 3.3-0.3.beta3
- Fix version requirement for php (Closes #753192)

* Wed Nov 09 2011 'Matěj Cepl <mcepl@redhat.com>' - 3.3-0.2.beta3
- Another upstream beta release.

* Thu Oct 20 2011 'Matěj Cepl <mcepl@redhat.com>' - 3.3-0.1.beta2
- New upstream beta release (just for Rawhide, to be sure we build)

* Sat Jul 30 2011 Matěj Cepl <mcepl@redhat.com> - 3.2.1-2
- Rebuilt against new libraries.

* Wed Jul 13 2011 Matěj Cepl <mcepl@redhat.com> - 3.2.1-1
- New upstream release. Small fixes missed in 3.2.

* Tue Jul 05 2011 Matěj Cepl <mcepl@redhat.com> - 3.2-1
- New upstream release.

* Wed Jun 29 2011 Matěj Cepl <mcepl@redhat.com> - 3.2-0.1.RC3
- Updated prerelease version (security and minor fixes).

* Sun Jun 19 2011 Matěj Cepl <mcepl@redhat.com> - 3.2-0.1.RC1
- Prerelease version.

* Thu Jun 02 2011 Matěj Cepl <mcepl@redhat.com> - 3.1.3-3
- Actually, we just don't need gettext.php at all, it is provided by
  php itself. Just remove the file, don't make a symlink.
- revert back to wp-content in /usr/share/wordpress, I am not able to make it
  work. Not fixing BZ 522897.

* Wed Jun 01 2011 Matěj Cepl <mcepl@redhat.com> - 3.1.3-2
- Fix old FSF address and Summary to make rpmlint happy.
- Make wp-content directory owned by apache:apache
- Correctly Provides/Obsoletes (with versions)

* Wed May 25 2011 Matěj Cepl <mcepl@redhat.com> - 3.1.3-1
- Upgrade to the latest upstream version (security fixes and enhancements, BZ 707772)
- Move wp-content directory to /var/www/wordpress/ (BZ 522897)
- Simplify overly detailed %%files

* Sun May 01 2011 Matěj Cepl <mcepl@redhat.com> - 3.1.2-1
- New upstream release.

* Tue Apr 12 2011 Matěj Cepl <mcepl@redhat.com> - 3.1.1-1
- 3.1.1

* Wed Feb 23 2011 Jon Ciesla <limb@jcomserv.net> - 3.1-1
- 3.1.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Jon Ciesla <limb@jcomserv.net> - 3.0.4-2
- Obsoletes wordpress-mu, deprecated by upstream as of 3.0.x.

* Mon Jan 03 2011 Jon Ciesla <limb@jcomserv.net> - 3.0.4-1
- 3.0.4. Security fixes, BZ 666782.

* Thu Dec 23 2010 Jon Ciesla <limb@jcomserv.net> - 3.0.3-2
- Change Requires from httpd to webserver, BZ 523480.
- Patch for Hello Dolly lyrics, BZ 663966.

* Fri Dec 10 2010 Jon Ciesla <limb@jcomserv.net> - 3.0.3-1
- 3.0.3. Security fixes, BZ 659319.

* Fri Dec 10 2010 Jon Ciesla <limb@jcomserv.net> - 3.0.2-1
- 3.0.2. Security fixes, BZ 659319.

* Mon Aug 09 2010 Jon Ciesla <limb@jcomserv.net> - 3.0.1-1
- 3.0.1.

* Mon Jul 12 2010 Jon Ciesla <limb@jcomserv.net> - 2.8.6-3
- Remove bundled php-gettext and php-simplepie,
- require and link to system versions, BZ 544720.

* Mon Nov 16 2009 Adrian Reber <adrian@lisas.de> - 2.8.6-2
- updated to 2.8.6 (Security Release)

* Wed Oct 21 2009 Adrian Reber <adrian@lisas.de> - 2.8.5-1
- updated to 2.8.5 (Hardening Release)

* Sun Aug 30 2009 Adrian Reber <adrian@lisas.de> - 2.8.4-1
- updated to 2.8.4 (security fixes were already available with 2.8.3-2)

* Tue Aug 11 2009 Adrian Reber <adrian@lisas.de> - 2.8.3-2
- another security update to fix "Remote admin reset password":
  http://lists.grok.org.uk/pipermail/full-disclosure/2009-August/070137.html

* Mon Aug 03 2009 Adrian Reber <adrian@lisas.de> - 2.8.3-1
- updated to 2.8.3 for security fixes

* Tue Jul 28 2009 Adrian Reber <adrian@lisas.de> - 2.8.2-1
- updated to 2.8.2 for security fixes - BZ 512900
- fixed "wrong-script-end-of-line-encoding" of license.txt
- correctly disable auto update check
- fixed an error message from 'find' during the build

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Adrian Reber <adrian@lisas.de> - 2.8.1-1
- updated to 2.8.1 for security fixes - BZ 510745

* Mon Jun 22 2009 Adrian Reber <adrian@lisas.de> - 2.8-1
- updated to 2.8

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Adrian Reber <adrian@lisas.de> - 2.7.1-1
- updated to 2.7.1

* Wed Nov 26 2008 Adrian Reber <adrian@lisas.de> - 2.6.5-2
- updated to 2.6.5

* Fri Oct 24 2008 Adrian Reber <adrian@lisas.de> - 2.6.3-1
- updated to 2.6.3

* Tue Sep 09 2008 Adrian Reber <adrian@lisas.de> - 2.6.2-1
- updated to 2.6.2

* Sun Aug 24 2008 Adrian Reber <adrian@lisas.de> - 2.6.1-1
- updated to 2.6.1

* Mon Jul 21 2008 Adrian Reber <adrian@lisas.de> - 2.6-1
- updated to 2.6

* Sat Apr 26 2008 Adrian Reber <adrian@lisas.de> - 2.5.1-1
- updated to 2.5.1 for security fixes - BZ 444396

* Fri Feb  8 2008 John Berninger <john at ncphotography dot com> - 2.3.3-0
- update to 2.3.3 for security fixes - BZ 431547

* Sun Dec 30 2007 Adrian Reber <adrian@lisas.de> - 2.3.2-1
- updated to 2.3.2 (bz 426431, Draft Information Disclosure)

* Tue Oct 30 2007 Adrian Reber <adrian@lisas.de> - 2.3.1-1
- updated to 2.3.1 (bz 357731, wordpress XSS issue)

* Mon Oct 15 2007 Adrian Reber <adrian@lisas.de> - 2.3-1
- updated to 2.3
- disabled wordpress-core-update

* Tue Sep 11 2007 Adrian Reber <adrian@lisas.de> - 2.2.3-0
- updated to 2.2.3 (security release)

* Wed Aug 29 2007 John Berninger <john at ncphotography dot com> - 2.2.2-0
- update to upstream 2.2.2
- license tag update

* Mon Apr 16 2007 john Berninger <jwb at redhat dot com> - 2.1.3-1
- update to 2.1.3 final - bz235912

* Mon Mar 26 2007 John Berninger <jwb at redhat dot com> - 2.1.3-rc2
- update to 2.1.3rc2 for bz 233703

* Sat Mar  3 2007 John Berninger <jwb at redhat dot com> - 2.1.2-0
- update to 2.1.2 - backdoor exploit introduced upstream in 2.1.1 - bz 230825

* Tue Feb 27 2007 John Berninger <jwb at redhat dot com> - 2.1.1-0
- update to 2.1.1 to fix vuln in bz 229991

* Wed Jan 31 2007 John Berninger <jwb at redhat dot com> - 2.1-0
- update to v2.1 to fix multiple bz/vuln's

* Sun Dec  3 2006 John Berninger <jwb at redhat dot com> - 2.0.5-2
- Remove mysql-server dependency

* Sun Dec  3 2006 John Berninger <jwb at redhat dot com> - 2.0.5-1
- Update to upstream 2.0.5 to fix vuln in bz 213985

* Thu Oct 26 2006 John Berninger <jwb at redhat dot com> - 2.0.4-1
- Doc fix for BZ 207822

* Sat Aug 12 2006 John Berninger <jwb at redhat dot com> - 2.0.4-0
- Upstream security vulns - bz 201989

* Sun Jul 23 2006 John Berninger <jwb at redhat dot com> - 2.0.3-4
- Fix broken upgrade path from FE4

* Tue Jul  4 2006 John Berninger <jwb at redhat dot com> - 2.0.3-3
- Add a README.fedora file
- Add php-mysql requires

* Tue Jun 20 2006 John Berninger <jwb at redhat dot com> - 2.0.3-2
- Remove use of installprefix macro
- %%{_datadir}/wordpress/wp-config.php is not a config file
- Symlink is relative

* Mon Jun 19 2006 John Berninger <jwb at redhat dot com> - 2.0.3-1
- Changes from Jarod Wilson as below
- Update to 2.0.3
- Rearrange to use /usr/share/wordpress and /etc/wordpress
- Remove patch (included upstream)
- Remove empty files to make rpmlint happy

* Tue May 30 2006 John Berninger <jwb at redhat dot com> - 2.0.2-1
- Added patch for \n cache injection - upstream changeset #3797

* Sat May 27 2006 John Berninger <jwb at redhat dot com> - 2.0.2-0
- Initial build
