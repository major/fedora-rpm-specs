# remirepo/fedora spec file for php-pear-phing
#
# Copyright (c) 2013-2022 Remi Collet
# Copyright (c) 2010-2013 Christof Damian
# Copyright (c) 2007-2010 Alexander Kahl
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    phing
%global pear_channel pear.phing.info

Summary:       A project build system based on Apache Ant
Name:          php-pear-phing
Version:       2.17.4
Release:       2%{?dist}

License:       LGPLv2
URL:           http://phing.info/trac/

# remove non-free stuff
# pear download phing/phing
# ./strip.sh %%{version}
Source0:       %{pear_name}-%{version}-strip.tgz
Source1:       strip.sh

BuildArch:	noarch
BuildRequires: php(language) >= 5.2.0
BuildRequires: php-pear(PEAR) >= 1.8.0
BuildRequires: php-channel(%{pear_channel})
BuildRequires: dos2unix

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:      php-cli
# From package.xml, Required
Requires:      php(language) >= 5.2.0
Requires:      php-pear(PEAR) >= 1.8.0
Requires:      php-channel(%{pear_channel})
# From package.xml, Optional
Requires:      php-pear(Archive_Tar) >= 1.3.8
Requires:      php-pear(HTTP_Request2) >= 2.1.1
Requires:      php-pear(PHP_CodeSniffer) >= 1.5.0
Requires:      php-pear(pear.pdepend.org/PHP_Depend) >= 0.10.0
Requires:      php-pear(pear.phpmd.org/PHP_PMD) >= 1.1.0
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
# Removed from package.xml as no more available in pear
Recommends:    phpunit
Recommends:    phploc
Recommends:    phpcpd
Recommends:    phpcov
%endif

# TODO
# pear.phing.info/phingdocs >= 2.9.0
# VersionControl_SVN >= 0.4.0
# VersionControl_Git >= 0.4.3
# PEAR_PackageFileManager >= 1.5.2
# Services_Amazon_S3 >= 0.3.1
# pear.phpdoc.org/phpDocumentor >= 2.0.0a10

Provides:      php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:      php-composer(phing/phing) = %{version}
# The project/command
Provides:      phing = %{version}


%description
PHing Is Not GNU make; it's a project build system based on Apache Ant.

You can do anything with it that you could do with a traditional build
system like GNU make, and its use of simple XML build files and extensible
PHP "task" classes make it an easy-to-use and highly flexible build
framework. Features include file transformations (e.g. token replacement,
XSLT transformation, Smarty template transformations), file system operations,
interactive build support, SQL execution, CVS operations, tools for creating
PEAR packages, and much more.


%prep
%setup -qc
cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

rm -rf %{buildroot}%{pear_metadir}/.??*

mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{_bindir}/phing
%doc %{pear_docdir}/%{pear_name}
%{pear_datadir}/%{pear_name}
%{pear_phpdir}/%{pear_name}
%{pear_phpdir}/%{pear_name}.php
%{pear_xmldir}/%{name}.xml


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Remi Collet <remi@remirepo.net> - 2.17.4-1
- update to 2.17.4

* Thu May  5 2022 Remi Collet <remi@remirepo.net> - 2.17.3-1
- update to 2.17.3

* Wed Feb  9 2022 Remi Collet <remi@remirepo.net> - 2.17.2-1
- update to 2.17.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Remi Collet <remi@remirepo.net> - 2.17.1-1
- update to 2.17.1

* Thu Sep  2 2021 Remi Collet <remi@remirepo.net> - 2.17.0-1
- update to 2.17.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb  4 2021 Remi Collet <remi@remirepo.net> - 2.16.4-1
- update to 2.16.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Remi Collet <remi@remirepo.net> - 2.16.1-7
- use weak dependencies for phpunit, phploc, phpcpd and phpcov

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Remi Collet <remi@remirepo.net> - 2.16.1-1
- Update to 2.16.1 (no change)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Remi Collet <remi@fedoraproject.org> - 2.16.0-1
- Update to 2.16.0

* Thu Oct 13 2016 Remi Collet <remi@fedoraproject.org> - 2.15.2-1
- Update to 2.15.2

* Wed Oct 12 2016 Remi Collet <remi@fedoraproject.org> - 2.15.1-1
- Update to 2.15.1

* Thu Sep 15 2016 Remi Collet <remi@fedoraproject.org> - 2.15.0-1
- Update to 2.15.0

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 2.14.0-1
- Update to 2.14.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Remi Collet <remi@fedoraproject.org> - 2.13.0-1
- Update to 2.13.0
- provide phing

* Tue Aug 25 2015 Remi Collet <remi@fedoraproject.org> - 2.12.0-1
- Update to 2.12.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Remi Collet <remi@fedoraproject.org> - 2.11.0-1
- Update to 2.11.0

* Fri Feb 20 2015 Remi Collet <remi@fedoraproject.org> - 2.10.1-1
- Update to 2.10.1 (stable)

* Fri Feb 13 2015 Remi Collet <remi@fedoraproject.org> - 2.10.0-1
- Update to 2.10.0 (stable)

* Wed Dec 03 2014 Remi Collet <remi@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1 (stable)

* Wed Nov 26 2014 Remi Collet <remi@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0 (stable)

* Fri Oct 10 2014 Remi Collet <remi@fedoraproject.org> - 2.8.2-1
- Update to 2.8.2
- cleanup and changes from remi repo
- add dependencies on the available optional tools
- doc in pear_docdir
- provide php-composer(phing/phing)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov  2 2013 Christof Damian <christof@damian.net> - 2.6.1-1
- upstream 2.6.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 20 2013 Christof Damian <christof@damian.net> - 2.5.0-2
- remove more mentions of non-free stuff

* Sat Apr 20 2013 Christof Damian <christof@damian.net> - 2.5.0-1
- upstream 2.5.0
- remove non-free stuff from defaults.properties (Remi Collet <fedora@famillecollet.com>)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Christof Damian <christof@damian.net> - 2.4.14-1
- upstream 2.4.14
- remove non-free stuff
- remove optional xdebug requirement
- use pear_metadir

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 2.4.12-3
- rebuilt for new pear_datadir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 11 2012 Christof Damian <christof@damian.net> - 2.4.12-1
- upstream 2.4.12

* Fri Mar  2 2012 Christof Damian <christof@damian.net> - 2.4.9-1
- upstream 2.4.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov  4 2011 Christof Damian <christof@damian.net> - 2.4.8-2
- remove (optional) phpunit requirement

* Thu Nov  3 2011 Christof Damian <christof@damian.net> - 2.4.8-1
- upstream 2.4.8

* Fri Jul 15 2011 Christof Damian <christof@damian.net> - 2.4.6-1
- upstream 2.4.6

* Sat Mar  5 2011 Christof Damian <christof@damian.net> - 2.4.5-1
- remove requires hint

* Fri Mar  4 2011 Christof Damian <christof@damian.net> - 2.4.5-1
- upstream 2.4.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  8 2010 Christof Damian <christof@damian.net> - 2.4.4-1
- upstream 2.4.4

* Tue Nov 23 2010 Christof Damian <christof@damian.net> - 2.4.3-1
- upstream 2.4.3

* Sat Jul 31 2010 Christof Damian <christof@damian.net> - 2.4.2-1
- upstream 2.4.2

* Thu May 27 2010 Christof Damian <christof@damian.net> - 2.4.1-1
- upstream 2.4.1
- taking over package

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  6 2007 Alexander Kahl <akahl@iconmobile.com> - 2.3.0-1
- stable version

* Tue Oct 30 2007 Alexander Kahl <akahl@iconmobile.com> - 2.3.0-0.1.RC2
- new release candidate version

* Tue Oct 16 2007 Alexander Kahl <akahl@iconmobile.com> - 2.3.0-0.1.RC1
- new release candidate version
- consequently adapted macros for all shell operations
- sanitized requires
- switched build root macro style
- additional s/\r\n/\n/g fixes

* Mon Sep  3 2007 Alexander Kahl <akahl@iconmobile.com> - 2.3.0-0.6.beta1
- name change (lowercase)
- changed pear datadir macro

* Fri Aug 24 2007 Alexander Kahl <akahl@iconmobile.com> - 2.3.0-0.5.beta1
- Fixed dos line terminators.

* Wed Aug 22 2007 Alexander Kahl <akahl@iconmobile.com> - 2.3.0-0.4.beta1
- New beta version.

* Tue Aug 21 2007 Alexander Kahl <akahl@iconmobile.com> - 2.2.0-3
- Adapted new Fedora layout.

* Tue Aug 21 2007 Alexander Kahl <akahl@iconmobile.com> - 2.2.0-2
- Updated PHPUnit dependency.

* Fri May 25 2007 Alexander Kahl <akahl@iconmobile.com> - 2.2.0-1
- Removed ant dependency.
- Added channel dependency.

* Wed May 23 2007 Alexander Kahl <akahl@iconmobile.com> 2.2.0-0
- Initial RPM release.
