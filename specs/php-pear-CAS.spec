# remirepo/fedora spec file for php-pear-CAS
#
# Copyright (c) 2010-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    c129708154852656aabb13d8606cd5b12dbbabac
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     apereo
%global gh_project   phpCAS


Name:           php-pear-CAS
Version:        1.6.1
Release:        7%{?dist}
Summary:        Central Authentication Service client library in php

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://wiki.jasig.org/display/CASC/phpCAS

Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-fedora-autoloader-devel
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/log) >= 1.0.0 with php-composer(psr/log) < 4)
%else
BuildRequires:  php-PsrLog
%endif
# only for pear macros
BuildRequires:  php-pear
# for %%check
BuildRequires:  php-cli

Requires:       php(language) >= 7.1
Requires:       php-curl
Requires:       php-dom
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(psr/log) >= 1.0.0 with php-composer(psr/log) < 4)
%else
Requires:       php-PsrLog
%endif
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-session
Requires:       php-spl
# Optional: php-imap (when use Proxied Imap)
Requires:       php-composer(fedora/autoloader)

Provides:       php-pear(__uri/CAS) = %{version}
Provides:       php-composer(jasig/phpcas) = %{version}
Provides:       php-composer(apereo/phpcas) = %{version}
# this library is mostly known as phpCAS
Provides:       phpCAS = %{version}-%{release}


%description
This package is a PEAR library for using a Central Authentication Service.

Autoloader: %{pear_phpdir}/CAS/Autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}



%build
# Rewrite a classmap autoloader (upstream is broken)
%{_bindir}/phpab \
    --template fedora \
    --output source/CAS/Autoload.php  \
             source

cat << 'EOF' | tee -a source/CAS/Autoload.php
\Fedora\Autoloader\Dependencies::required([
    dirname(__DIR__) . '/CAS.php',
    [
        '%{_datadir}/php/Psr/Log3/autoload.php',
        '%{_datadir}/php/Psr/Log2/autoload.php',
        '%{_datadir}/php/Psr/Log/autoload.php',
    ],
]);
EOF


%install
mkdir -p %{buildroot}%{pear_phpdir}
cp -pr source/* %{buildroot}%{pear_phpdir}/


%check
: Ensure our autoloader works
php -r '
require "%{buildroot}%{pear_phpdir}/CAS/Autoload.php";
if (!class_exists("phpCAS")) {
  echo "Class not found\n";
  exit(1);
}
if (phpCAS::getVersion() != "%{version}") {
  echo "Bad version (found=" . phpCAS::getVersion()  . ", expected=%{version})\n";
  exit(1);
}
echo "Ok\n";
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc NOTICE *.md
%{pear_phpdir}/CAS
%{pear_phpdir}/CAS.php


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul  24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.1-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov  3 2022 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May  4 2022 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 7.1
- allow psr/log version 2 and 3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on PHP 7.0

* Thu Feb  4 2021 Remi Collet <remi@remirepo.net> - 1.3.9-1
- update to 1.3.9
- add dependency on psr/log

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Remi Collet <remi@remirepo.net> - 1.3.8-1
- update to 1.3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Remi Collet <remi@remirepo.net> - 1.3.7-1
- update to 1.3.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Remi Collet <remi@remirepo.net> - 1.3.6-1
- update to 1.3.6
- new github and packagist owner

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Remi Collet <remi@remirepo.net> - 1.3.5-1
- update to 1.3.5
- sources from github
- add minimal check for our autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 19 2016 Remi Collet <remi@fedoraproject.org> - 1.3.4-3
- fix broken autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Remi Collet <remi@fedoraproject.org> - 1.3.4-1
- update to Version 1.3.4
- add provides php-composer(jasig/phpcas)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 28 2014 Remi Collet <remi@fedoraproject.org> - 1.3.4-1
- update to Version 1.3.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 29 2012 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to Version 1.3.2, security fix for
  CVE-2012-5583 Missing CN validation of CAS server certificate
- add requires for all needed php extensions

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to Version 1.3.1

* Wed Mar 14 2012 Remi Collet <remi@fedoraproject.org> - 1.3.0-2
- License is ASL 2.0, https://github.com/Jasig/phpCAS/issues/32
- New sources,        https://github.com/Jasig/phpCAS/issues/31

* Tue Mar 13 2012 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to Version 1.3.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 11 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.2.2-1
- update to Version 1.2.2 (stable) - API 1.2.2 (stable)

* Wed Mar 30 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.2.1-1
- update to Version 1.2.1 (stable) - API 1.2.1 (stable)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.2.0-1
- update to Version 1.2.0 (stable) - API 1.2.0 (stable)
- dont requires domxml-php4-to-php5 anymore
- fix URL
- link %%doc to pear_docdir

* Mon Oct 04 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.3-1
- update to 1.1.3
- fix CVE-2010-3690, CVE-2010-3691, CVE-2010-3692
- set timezone during build

* Tue Aug 03 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.2-1
- update to 1.1.2
- fix  CVE-2010-2795, CVE-2010-2796, #620753

* Thu May 20 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.1-1
- update to 1.1.1

* Thu May 20 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.0-1
- update to 1.1.0 finale

* Sun Mar 14 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.0-0.1.RC7
- initial packaging (using pear make-rpm-spec CAS-1.1.0RC7.tgz)

