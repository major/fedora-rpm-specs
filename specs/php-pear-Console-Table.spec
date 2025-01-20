# remirepo/fedora spec file for php-pear-Console-Table
#
# Copyright (c) 2006-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Console_Table

Name:           php-pear-Console-Table
Version:        1.3.1
Release:        19%{?dist}
Summary:        Class that makes it easy to build console style tables

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/Console_Table
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

Patch0:         %{pear_name}-php8.patch

BuildArch:      noarch
BuildRequires:  php-pear
# For tests
BuildRequires:  php-mbstring

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pcre
Requires:       php-pear(PEAR)
%if 0%{?fedora} > 21
Recommends:     php-mbstring
%else
Requires:       php-mbstring
%endif

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/console_table) = %{version}


%description
Provides methods such as addRow(), insertRow(), addCol() etc. to build
console tables with or without headers and with user defined table rules
and padding.
 

%prep
%setup -q -c

cd %{pear_name}-%{version}
%patch -P0 -p1 -b .php8
sed -e '/Table.php/s/md5sum=.*name/name/' ../package.xml >%{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%check
cd %{pear_name}-%{version}
%{__pear} \
   run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests | tee ../tests.log
# pear doesn't set return code
if grep -q "FAILED TESTS" ../tests.log; then
  for fic in tests/*.diff; do
    cat $fic; echo -e "\n"
  done
  exit 1
fi


%files
%{pear_phpdir}/Console/Table.php
%{pear_testdir}/Console_Table
%{pear_xmldir}/%{name}.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.1-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr  1 2021 Remi Collet <remi@fedoraproject.org> - 1.3.1-9
- add patch for PHP 8 from
  https://github.com/pear/Console_Table/pull/15

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to 1.3.1

* Mon Oct  9 2017 Remi Collet <remi@fedoraproject.org> - 1.3.0-5
- add patch for PHP 7.2 from
  https://github.com/pear/Console_Table/pull/14

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Remi Collet <remi@fedoraproject.org> - 1.3.0-2
- drop dependency on Console_Color2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0
- provide php-composer(pear/console_table)
- soft dependencies on mbstring and Console_Color2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 31 2014 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- Version 1.2.1 (stable) - API 1.2.0 (stable)
- require Console_Color2 instead of Console_Color
- drop generated changelog

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 12 2013 Remi Collet <remi@fedoraproject.org> - 1.1.6-1
- Version 1.1.6 (stable) - API 1.1.1 (stable)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec  8 2012 Remi Collet <remi@fedoraproject.org> - 1.1.5-1
- Version 1.1.4 (stable) - API 1.1.1 (stable)

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.1.4-5
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 27 2010 Remi Collet <Fedora@FamilleCollet.com> 1.1.4-1
- Version 1.1.4 (stable) - API 1.1.1 (stable) - QA release
- set timezone during build
- run tests in %%check

* Fri May 21 2010 Remi Collet <Fedora@FamilleCollet.com> 1.1.3-4
- spec cleanup
- rename Console_Table.xml to php-pear-Console-Table.xml

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 21 2008 Remi Collet <Fedora@FamilleCollet.com> 1.1.3-1
- update to 1.1.3
- Requires php-pear-Console-Color
- cleanup old fixe.

* Sun Jul 27 2008 Remi Collet <Fedora@FamilleCollet.com> 1.1.2-1
- update to 1.1.2

* Thu Apr 10 2008 Remi Collet <Fedora@FamilleCollet.com> 1.1.1-1
- update to 1.1.1

* Sun Mar 30 2008 Remi Collet <Fedora@FamilleCollet.com> 1.1.0-1
- update to 1.1.0

* Wed Jan 09 2008 Remi Collet <Fedora@FamilleCollet.com> 1.0.8-1
- update to 1.0.8
- fix tests, http://pear.php.net/bugs/bug.php?id=12863
- add %%check
- fixed xml2changelog

* Wed May 02 2007 Remi Collet <Fedora@FamilleCollet.com> 1.0.7-1
- update to 1.0.7

* Sat Jan 20 2007 Remi Collet <Fedora@FamilleCollet.com> 1.0.6-1
- update to 1.0.6
- add CHANGELOG (generated)

* Wed Sep 13 2006 Remi Collet <Fedora@FamilleCollet.com> 1.0.5-2.fc5.1
- FC5 rebuild

* Mon Sep 11 2006 Remi Collet <Fedora@FamilleCollet.com> 1.0.5-2
- don't own %%{pear_phpdir}/Console

* Sat Sep 09 2006 Remi Collet <Fedora@FamilleCollet.com> 1.0.5-1
- generated specfile (pear make-rpm-spec) + cleaning
- add french summary and description
