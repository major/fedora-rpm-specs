%define moodlewebdir %{_var}/www/moodle/web
%define moodledatadir %{_var}/www/moodle/data

# Suppress finding Perl libraries supplied by filter/algebra/*.p?
%define __perl_requires %{nil}
%define __perl_provides %{nil}

Name:           moodle
Version:        4.5.1
Release:       	2%{?dist}
Summary:        A Course Management System

License:        GPL-2.0-or-later
URL:            https://moodle.org/
Source0:        https://download.moodle.org/download.php/direct/stable405/%{name}-%{version}.tgz
Source1:        moodle.conf
Source2:        moodle-config.php
Source3:        moodle.cron
Source4:        moodle-cron
Source5:        moodle.service
Source6:        moodle-README-rpm
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  unzip
Requires:       php-gd dailyjobs mimetex perl(lib) php-mysqlnd
Requires:       perl(Encode) hunspell perl(HTML::Parser) php
Requires:       perl(HTML::Entities) perl(CGI)
Requires:	php-adodb
Requires:	gnu-free-sans-fonts
Requires:	php-markdown
Requires:       php-simplepie
Requires:       php-soap
Requires:	php-pear-OLE
Requires:       php-pecl-xmlrpc
Requires:	crontabs

BuildRequires:  systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Provides: bundled(php-tcpdf)
Provides: bundled(php-google-apiclient1)

Provides: php-google-apiclient1 = 1.1.7-14
Obsoletes: php-google-apiclient1 < 1.1.7-14

%description
Moodle is a course management system (CMS) - a free, Open Source software
package designed using sound pedagogical principles, to help educators create
effective online learning communities.

%prep
%setup -q -n %{name}
cp %{SOURCE6} README-rpm

find . -type f \! -name \*.pl -exec chmod a-x {} \;
find . -name \*.cgi -exec chmod a+x {} \;
chmod a+x admin/process_email.php
chmod a+x mod/chat/chatd.php

%build
rm config-dist.php install.php filter/tex/mimetex.* filter/tex/README.mimetex

# Get rid of language files in subordinate packages for languages not supported
# by moodle itself.
rm lib/phpmailer/language/phpmailer.lang-fo.php

#Drop precompiled flash
find . -type f -name '*.swf' | xargs rm -f

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{moodlewebdir}
mkdir -p %{buildroot}%{moodledatadir}
cp -a * %{buildroot}%{moodlewebdir}
rm %{buildroot}%{moodlewebdir}/README*
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/moodle.conf
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{moodlewebdir}/config.php
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/cron.d/moodle
install -p -D -m 0755 %{SOURCE4} %{buildroot}%{_sbindir}/moodle-cron
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/moodle.service
find %{buildroot} -name \*.mimetex-\* -exec rm {} \;
rm -f %{buildroot}${moodlewebdir}/pix/.cvsignore

#use system adodb
rm -rf %{buildroot}/var/www/moodle/web/lib/adodb
ln -s /usr/share/php/adodb/ %{buildroot}%{moodlewebdir}/lib/adodb

#Symlink to FreeSans, to save space.
rm -f %{buildroot}%{moodlewebdir}/lib/default.ttf
ln -s /usr/share/fonts/gnu-free/FreeSans.ttf %{buildroot}%{moodlewebdir}/lib/default.ttf

#use system markdown
rm -rf %{buildroot}%{moodlewebdir}/lib/markdown.php
ln -s /usr/share/php/markdown.php %{buildroot}%{moodlewebdir}/lib/markdown.php

#use system php-pear-OLE
rm -rf %{buildroot}/var/www/moodle/web/lib/pear/OLE
ln -s /usr/share/pear/OLE %{buildroot}/var/www/moodle/web/lib/pear/OLE

#use system php-simplepie
cp -p %{buildroot}%{moodlewebdir}/lib/simplepie/moodle_simplepie.php .
rm -rf %{buildroot}%{moodlewebdir}/lib/simplepie
mkdir -p %{buildroot}%{_datadir}/php/php-simplepie
ln -s /usr/share/php/php-simplepie/ %{buildroot}%{moodlewebdir}/simplepie
cp -p moodle_simplepie.php %{buildroot}%{_datadir}/php/php-simplepie

%post
%systemd_post moodle.service

if [ -d /var/www/moodle/web/lib/adodb -a ! -L /var/www/moodle/web/lib/adodb ]; then
  mv /var/www/moodle/web/lib/adodb /var/www/moodle/web/lib/adodb.rpmbak && \
  ln -s /usr/share/php/adodb/ /var/www/moodle/web/lib/adodb
  rm -rf /var/www/moodle/web/lib/adodb.rpmbak
fi

if [ ! -L /var/www/moodle/web/lib/adodb ]; then
  ln -s /usr/share/php/adodb/ /var/www/moodle/web/lib/adodb
fi

if [ ! -L /var/www/moodle/web/lib/pear/OLE ]; then
  ln -s /usr/share/pear/OLE /var/www/moodle/web/lib/pear/OLE
fi

%preun
%systemd_preun moodle.service

%postun
%systemd_postun_with_restart moodle.service

%pretrans -p <lua>
-- Remove symlinks that will become directories
dirs = {"/var/www/moodle/web/lib/magpie", "/var/www/moodle/web/lib/google", "/var/www/moodle/web/auth/cas", "/var/www/moodle/web/auth/cas/CAS"}
for i, path in ipairs(dirs) do
  st = posix.stat(path)
  if st and st.type == "link" then
    os.remove(path)
  end
end

-- Remove directories that will become symlinks
dirs = {"/var/www/moodle/web/auth/cas/CAS"}
for i, path in ipairs(dirs) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end

%files
%license COPYING.txt
%doc README* TRADEMARK.txt local/readme.txt
%dir %{_var}/www/moodle
%config(noreplace) %{moodlewebdir}/config.php
%{moodlewebdir}
%attr(-,apache,apache) %{moodledatadir}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/moodle.conf
%{_unitdir}/%{name}.service
%{_sbindir}/%{name}-cron
%ghost /var/www/moodle/web/lib/adodb
%ghost /var/www/moodle/auth/cas/CAS.rpmmoved
%exclude %{moodlewebdir}/COPYING.txt
%{_datadir}/php/php-simplepie/moodle_simplepie.php

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 06 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.5.1-1
- 4.5.1

* Mon Oct 07 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.5-1
- 4.5

* Tue Sep 03 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.4.3-1
- 4.4.3

* Mon Aug 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.4.2-1
- 4.4.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.4.1-1
- 4.4.1

* Mon Apr 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.4-1
- 4.4

* Fri Feb 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.3.3-1
- 4.3.3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.3.2-1
- 4.3.2

* Fri Dec 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.3.1-1
- 4.3.1

* Tue Oct 10 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.3-1
- 4.3

* Fri Aug 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.2.2-1
- 4.2.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.2.1-2
- aspell->hunspell.

* Sat Jun 10 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.2.1-1
- 4.2.1

* Mon Apr 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.2-1
- 4.2

* Sat Mar 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.1.2-1
- 4.1.2

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.1.1-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.1.1-1
- 4.1.1

* Mon Nov 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.1.0-1
- 4.1.0

* Wed Nov 16 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.0.5-2
- Fix php-google-apiclient1 requirements.

* Mon Nov 14 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.0.5-1
- 4.0.5

* Wed Oct 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.0.4-2
- Rebundle google-apiclient

* Mon Sep 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.0.4-1
- 4.0.4

* Fri Aug 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.0.3-1
- 4.0.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.0.2-1
- 4.0.2

* Mon May 09 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.0.1-1
- 4.0.1

* Tue Apr 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.0-1
- 4.0

* Mon Mar 14 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.11.6-1
- 3.11.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.11.5-1
- 3.11.5

* Mon Nov 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.11.4-1
- 3.11.4

* Mon Sep 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.11.3-1
- 3.11.3

* Thu Jul 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.11.2-1
- 3.11.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.11.1-1
- 3.11.1

* Mon May 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.11-1
- 3.11

* Mon May 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.4-2
- Fix cron job

* Mon May 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.4-1
- 3.10.4

* Sun Apr 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.3-3
- Rebundle php-tcpdf

* Mon Mar 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.3-2
- Conditionalize xmlrpc.

* Thu Mar 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.3-1
- 3.10.3

* Mon Mar 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.2-1
- 3.10.2, switch to php-pecl-xmlrpc.

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.10.1-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.1-1
- 3.10.1

* Mon Nov 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10-1
- 3.10

* Mon Sep 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.9.2-1
- 3.9.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.9.1-1
- 3.9.1

* Fri Jun 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.9-1
- 3.9

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.8.3-1
- 3.8.3

* Mon Mar 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.8.2-1
- 3.8.2

* Sat Feb 22 2020 Shawn Iwinski <shawn@iwin.ski> - 3.8.1-3
- Remove php-lessphp dependency as it is no longer used

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.8.1-1
- 3.8.1

* Mon Nov 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.8-1
- 3.8

* Mon Nov 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.7.3-1
- 3.7.3

* Mon Sep 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.7.2-1
- 3.7.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.7.1-1
- 3.7.1

* Tue Jun 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.7-2
- Update php-google-apiclient requires per BZ 1721307.

* Mon May 20 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.7-1
- 3.7

* Mon May 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.6.4-1
- 3.6.4

* Mon Mar 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.6.3-1
- 3.6.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Gwyn Ciesla <limburgher@gmail.com> - 3.6.2-1
- 3.6.2

* Wed Nov 21 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.5.3-1
- 3.5.3

* Tue Oct 30 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.5.2-2
- Fix URL, drop php-Smarty.

* Mon Sep 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.5.2-1
- 3.5.2

* Fri Aug 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.5.1-2
- Drop Quickform patch.

* Mon Jul 30 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.5.1-1
- 3.5.1, drop php-password-compat.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.5-1
- 3.5.

* Sun Mar 18 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.4.2-1
- 3.4.2.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.4.1-1
- 3.4.1.

* Mon Nov 13 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.4-1
- 3.4.

* Mon Sep 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.3.2-1
- 3.3.2.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.3.1-1
- 3.3.1.

* Mon May 15 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.3-1
- 3.3.

* Mon May 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.2.3-1
- 3.2.3

* Mon Mar 13 2017 Jon Ciesla <limburgher@gmail.com> - 3.2.2-1
- 3.2.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Jon Ciesla <limburgher@gmail.com> - 3.2.1-1
- 3.2.1

* Thu Dec 08 2016 Jon Ciesla <limburgher@gmail.com> - 3.2-2
- Use bundleed php-pear-HTML* per remi.

* Mon Dec 05 2016 Jon Ciesla <limburgher@gmail.com> - 3.2-1
- 3.2

* Mon Nov 14 2016 Jon Ciesla <limburgher@gmail.com> - 3.1.3-1
- 3.1.3

* Thu Sep 15 2016 Jon Ciesla <limburgher@gmail.com> - 3.1.2-1
- 3.1.2

* Thu Aug 11 2016 Jonathan Dieter <jdieter@lesbg.com> - 3.1-1-2
- Unbundle CAS again
- Fix simplepie paths
- Fix Google API paths
- Fix CAS paths
- Follow guidelines re: switching from symlink to directory and vice versa

* Wed Jul 13 2016 Jon Ciesla <limburgher@gmail.com> - 3.1.1-1
- 3.1.1

* Tue Jun 28 2016 Jon Ciesla <limburgher@gmail.com> - 3.1-3
- php7 Requires fix.

* Fri Jun 24 2016 Jon Ciesla <limburgher@gmail.com> - 3.1-2
- Revert to bundled CAS.

* Mon May 23 2016 Jon Ciesla <limburgher@gmail.com> - 3.1-1
- 3.1

* Mon May 09 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.4-1
- 3.0.4

* Mon Mar 14 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.3-1
- 3.0.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.2-1
- 3.0.2

* Mon Dec 21 2015 Jon Ciesla <limburgher@gmail.com> - 3.0.1-1
- 3.0.1

* Tue Nov 17 2015 Jon Ciesla <limburgher@gmail.com> - 3.0-1
- 3.0

* Tue Nov 10 2015 Jon Ciesla <limburgher@gmail.com> - 2.9.3-1
- 2.9.3

* Thu Oct 01 2015 Jon Ciesla <limburgher@gmail.com> - 2.9.2-1
- 2.9.2

* Thu Sep 03 2015 Jon Ciesla <limburgher@gmail.com> - 2.9.1-1
- 2.9.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.9-1
- 2.9
- update RPM macroses
- provide systemd service instead of init

* Tue Mar 24 2015 Jon Ciesla <limburgher@gmail.com> - 2.8.5-1
- Latest upstream release.

* Thu Feb 05 2015 Jon Ciesla <limburgher@gmail.com> - 2.8.3-1
- Latest upstream release.

* Fri Nov 14 2014 Jon Ciesla <limburgher@gmail.com> - 2.8.1-1
- Latest upstream release.

* Fri Sep 12 2014 Jon Ciesla <limburgher@gmail.com> - 2.7.2-1
- 2.7.2, fix for security influences.

* Mon Jul 21 2014 Jon Ciesla <limburgher@gmail.com> - 2.7.1-1
- 2.7.1, Fix for CVE-2014-3541, CVE-2014-3542, CVE-2014-3543,
- CVE-2014-3544, CVE-2014-3545, CVE-2014-3546, CVE-2014-3547,
- CVE-2014-3548, CVE-2014-3549, CVE-2014-3550, CVE-2014-3551,
- CVE-2014-3552, CVE-2014-3553

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jon Ciesla <limburgher@gmail.com> - 2.7-1
- 2.7, Fix forCVE-2014-0213, CVE-2014-0214, CVE-2014-0215,
- CVE-2014-0216, CVE-2014-0217, CVE-2014-0218
- Dropped upstreamed tinymce patch.

* Wed Mar 19 2014 Jon Ciesla <limburgher@gmail.com> - 2.6.2-1
- Fix for CVE-2014-0122, CVE-2014-0123, CVE-2014-0124,
- CVE-2014-0125, CVE-2014-0126, CVE-2014-0127, CVE-2014-0129

* Wed Jan 22 2014 Jon Ciesla <limburgher@gmail.com> - 2.6.1-1
- Fix for CVE-2014-0008,9,10.

* Thu Dec 12 2013 Jon Ciesla <limburgher@gmail.com> - 2.6-1
- Latest upstream.

* Thu Nov 14 2013 Jon Ciesla <limburgher@gmail.com> - 2.5.3-1
- 2.5.3, BZ 1025655,6, 1030084,5.

* Wed Sep 11 2013 Jon Ciesla <limburgher@gmail.com> - 2.5.2-1
- 2.5.2, multiple securty fixes, BZ 1006678.
- CVE-2012-6087 patch upstreamed.

* Fri Aug 23 2013 Adam Williamson <awilliam@redhat.com> - 2.5.1-7
- patch tinymce to cope elegantly with Flash binary being removed

* Fri Aug 16 2013 Jon Ciesla <limburgher@gmail.com> - 2.5.1-6
- Drop precompiled flash.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Jon Ciesla <limburgher@gmail.com> - 2.5.1-4
- Add crontabs Requires, BZ 989079.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.5.1-3
- Perl 5.18 rebuild

* Fri Jul 12 2013 Jon Ciesla <limburgher@gmail.com> - 2.5.1-2
- Include two non-upstream additions to HTML-Quickform.

* Fri Jul 12 2013 Jon Ciesla <limburgher@gmail.com> - 2.5.1-1
- 2.5.1

* Mon May 20 2013 Jon Ciesla <limburgher@gmail.com> - 2.5-3
- Correct require_once path for tcpdf.

* Mon May 20 2013 Jon Ciesla <limburgher@gmail.com> - 2.5-2
- Use system tcpdf, BZ 965160.

* Mon May 20 2013 Jon Ciesla <limburgher@gmail.com> - 2.5-1
- Latest upstream.

* Mon May 20 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.4-1
- Latest upstream.

* Mon Mar 25 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.3-1
- Latest upstream.
- Fixes for multiple CVEs.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.1-1
- Patch for CVE-2012-6087.

* Tue Jan 15 2013 Jon Ciesla <limburgher@gmail.com> - 2.4.1-1
- Latest upstream.

* Fri Nov 23 2012 Marcela Mašláňová <mmaslano@redhat.com> - 2.3.3-2
- The requirement on vixie-cron is not correct anymore. The dailyjobs will be
  used as virtual requirement since now. #879550

* Mon Nov 19 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.3-1
- Latest upstream, BZ 878132.

* Wed Oct 31 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.2-3
- Fix conf.

* Tue Oct 30 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.2-2
- Fix for httpd 2.4, BZ 871431.

* Mon Sep 17 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.2-1
- Latest upstream.

* Mon Jul 23 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.1-1
- Latest upstream, BZ 841954.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.3-1
- Security update, BZ 824481.

* Wed May 09 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.2-3
- Unbundled php-markdown.
- Unbundled php-pear-Auth-RADIUS.
- Unbundled php-pear-Crypt-CHAP.
- Unbundled php-pear-HTML-Common.
- Unbundled php-pear-HTML-QuickForm.
- Unbundled php-pear-OLE.

* Wed May 09 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.2-2
- Dropped bundled language packs, BZ 748958.

* Tue Mar 13 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.2-1
- Latest upstream.

* Tue Mar 13 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.1-2
- Fixed CAS unbundling per rcollet.

* Tue Jan 24 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.1-1
- New upstream, BZ 783534.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Jon Ciesla <limburgher@gmail.com> - 2.2-1
- New upstream.

* Thu Dec 08 2011 Jon Ciesla <limburgher@gmail.com> - 2.1.3-1
- New upstream, BZ 761249.

* Fri Oct 21 2011 Jon Ciesla <limb@jcomserv.net> - 2.1.2-1
- New upstream, BZ 747445.

* Tue Sep 27 2011 Jon Ciesla <limb@jcomserv.net> - 2.1.1-2
- Switched to cli cron script, BZ 733957.

* Tue Aug 16 2011 Jon Ciesla <limb@jcomserv.net> - 2.1.1-1
- New upstream.

* Mon May 09 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.3-1
- New upstream.

* Wed Apr 27 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.2-2
- Moving from Perl-Text-Aspell to aspell.

* Fri Apr 22 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.2-1
- New upstream.
- Merged in, updated the language packs.
- Massive spec cleanup.

* Tue Feb 22 2011 Jon Ciesla <limb@jcomserv.net> - 1.9.11-1
- New upstream, security fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Jon Ciesla <limb@jcomserv.net> - 1.9.10-1
- New upstream, MSA-10-0017.
- htmlpurifier patch upstreamed.

* Mon Oct 04 2010 Jon Ciesla <limb@jcomserv.net> - 1.9.9-3
- Correction of CAS symlink typo.

* Thu Aug 19 2010 Jon Ciesla <limb@jcomserv.net> - 1.9.9-2
- Switch to system php-pear-CAS, BZ 577467, 620772.
- Patching htmlpurifier, BZ 624754.

* Tue Jun 22 2010 Jon Ciesla <limb@jcomserv.net> - 1.9.9-1
- Update to 1.9.9, BZ 605810.

* Thu Mar 25 2010 Jon Ciesla <limb@jcomserv.net> - 1.9.8-1
- Update to 1.9.8, BZ 575905.

* Tue Dec 08 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.7-1
- Update to 1.9.7, BZ 544766.

* Thu Nov 05 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.6-2
- Reverted erroneous cron fix.

* Thu Nov 05 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.6-1
- Update to 1.9.6.
- Make moodle-cron honor lock, BZ 533171.

* Wed Sep 23 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.5-3
- Using weekly snapshot downloaded 09/23/2009 for new PHP, BZ 525120
- Added Urdu installer.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.5-1
- Move symlink scripts from pretrans to post, pre.
- 1.9.5.

* Fri Apr 03 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.4-7
- Move symlink scripts from pre to pretrans.
- Corrented moodle-cron BZ 494090.

* Wed Apr 01 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.4-6
- Patch for CVE-2009-1171, BZ 493109.

* Tue Mar 24 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.4-5
- Update for freefont->gnu-free-fonts change.

* Thu Feb 26 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.4-4
- Fix for symlink dir replacement.

* Mon Feb 23 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.4-2
- Putting back bundled MagpieRSS due to incompatibility, BZ 486777.
- Corrected moodle-cron.

* Tue Feb 10 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.4-1
- Update to 1.9.4 to fix CVE-2009-0499,0500,0501,0502.

* Tue Jan 27 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.3-6
- Dropped and symlinked to khmeros-base-fonts.

* Tue Jan 20 2009 Jon Ciesla <limb@jcomserv.net> - 1.9.3-5
- Dropped and symlinked illegal sm and to fonts.
- Symlinking to FreeSans.
- Drop spell-check-logic.cgi, CVE-2008-5153, per upstream, BZ 472117, 472119, 472120.

* Wed Dec 17 2008 Jon Ciesla <limb@jcomserv.net> - 1.9.3-4
- Texed fix, BZ 476709.

* Fri Nov 07 2008 Jon Ciesla <limb@jcomserv.net> - 1.9.3-3
- Moved to weekly downloaded 11/7/08 to fix Snoopy CVE-2008-4796.

* Fri Oct 31 2008 Jon Ciesla <limb@jcomserv.net> - 1.9.3-2
- Fix for BZ 468929, overactive cron job.

* Wed Oct 22 2008 Jon Ciesla <limb@jcomserv.net> - 1.9.3-1
- Updated to 1.9.3.
- Updated language packs to 22 Oct 2008 versions.

* Wed Aug 06 2008 Jon Ciesla <limb@jcomserv.net> - 1.9.2-2
- Remove bundled adodb, use system php-adodb. BZ 457886.
- Remove bundled magpie, use system php-magpierss. BZ 457886.

* Wed Aug 06 2008 Jon Ciesla <limb@jcomserv.net> - 1.9.2-1
- Updated to 1.9.2.
- Remove bundled Smarty, use system php-Smarty. BZ 457886.
- Updated language packs to 06 Aug 2008 versions.

* Mon Jun 23 2008 Jon Ciesla <limb@jcomserv.net> - 1.9.1-2
- Add php Requires, BZ 452341.

* Thu May 22 2008 Jon Ciesla <limb@jcomserv.net> - 1.9.1-1
- Update to 1.9.1.
- Updated language packs to 22 May 2008 versions.
- Added Welsh, Uzbek support.
- Added php-xmlrpc Requires.

* Sat Mar 29 2008 Jon Ciesla <limb@jcomserv.net> - 1.9-1
- Update to 1.9.
- Updated language packs to 01 April 2008 versions.

* Sat Jan 12 2008 Jon Ciesla <limb@jcomserv.net> - 1.8.4-1
- Upgrade to 1.8.4, fix CVE-2008-0123.
- Added Tamil (Sri Lanka) support.

* Mon Nov 12 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.3-2
- Corrected init script to prevent starting by default.

* Thu Oct 25 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.3-1
- Update to 1.8.3.
- Fix init script for LSB BZ 246986.
- Updated language packs to 25 October 2007 versions.
- Added Armenian, Macedonian.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.2-2
- License tag correction.

* Wed Jul 25 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.2-1
- Update to 1.8.2.
- Updated language packs to the 25 July 2007 versions.
- Added Mongolian, Gujerati, Lao, Tongan, Maori (Waikato Uni), Samoan, Tamil.

* Tue May 15 2007 Jerry James <Jerry.James@usu.edu> - 1.8-5
- Fix language packs to not obsolete themselves.
- Update language packs to the 15 May 2007 versions.

* Mon May  7 2007 Jerry James <Jerry.James@usu.edu> - 1.8-4
- Mark a bunch of config.php files as configuration files.
- Update language packs to the 07 May 2007 versions.

* Fri Apr 20 2007 Jerry James <Jerry.James@usu.edu> - 1.8-3
- perl-Text-Aspell is now available, so use it.  Don't make the spellchecker
  a separate package, however, since it is an htmlarea plugin, not a moodle
  plugin.  Somebody we will provide htmlarea as a separate package.
- Fix version numbers on obsoletes.
- Update language packs to the 20 Apr 2007 versions.

* Tue Apr 17 2007 Jerry James <Jerry.James@usu.edu> - 1.8-2
- Fix a CVS gaffe.
- Obsolete language packs with old names.
- Update language packs to the 17 Apr 2007 versions.

* Fri Apr 13 2007 Jerry James <Jerry.James@usu.edu> - 1.8-1
- Update to 1.8 (fixes BZ 232103)
- Own /var/www/moodle/web (BZ 233882)
- Drop unused mimetex patches
- Add executable bits to 3 scripts that should have them
- Remove the installation language files from the main package (twice)
- Package the moodle language files, not just the installation files
- Rename/add several language files to match the upstream list
- Minor typo fixes in the scripts

* Sun Jan 07 2007 Mike McGrath <imlinux@gmail.com> - 1.7-1
- Security fix for BZ# 220041

* Sat Oct 28 2006 Mike McGrath <imlinux@gmail.com> - 1.6.3-3
- Release bump

* Sun Oct 22 2006 Mike McGrath <imlinux@gmail.com> - 1.6.3-2
- Added requires php-mysql

* Fri Oct 13 2006 Mike McGrath <imlinux@gmail.com> - 1.6.3-1
- Major changes, update to 1.6.3
- SpellChecker moved
- Language install method has been changed (added a cp)

* Thu Sep 07 2006 Mike McGrath <imlinux@gmail.com> - 1.5.4-2
- Release bump

* Thu Aug 24 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.5.4-1
- Update to 1.5.4.
- Remove SA18267.patch; not needed in 1.5.4.
- Add -nn subpackage for new Norwegian Nynorsk language.
- Change description for -no subpackage to indicate Bokmal explicitly.
  Note that I have purposefully misspelled "Bokmal" in order to avoid
  introducing a non-ASCII character.

* Mon Jan  9 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.5.3-2
- Add security patch for adodb (SA18267)

* Sat Dec 10 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.5.3-1
- Update to 1.5.3
- Split off spell check package due to lack of Text::Aspell

* Wed Oct 12 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.5.2-1
- Initial RPM release
