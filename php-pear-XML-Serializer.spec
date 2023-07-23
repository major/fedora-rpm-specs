# spec file for php-pear-XML-Serializer
#
# Copyright (c) 2010-2016 Remi Collet
# Copyright (c) 2006-2009 Christopher Stone
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name XML_Serializer

Name:           php-pear-XML-Serializer
Version:        0.21.0
Release:        15%{?dist}
Summary:        Swiss-army knife for reading and writing XML files

License:        BSD
URL:            http://pear.php.net/package/XML_Serializer
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear
# for tests
BuildRequires:  php-phpunit-PHPUnit
BuildRequires:  php-pear(XML_Util) >= 1.1.1
BuildRequires:  php-pear(XML_Parser) >= 1.2.6

Requires:       php-pear(PEAR) 
Requires:       php-pear(XML_Util) >= 1.1.1
Requires:       php-pear(XML_Parser) >= 1.2.6
Requires:       php-xml
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/xml_serializer) = %{version}


%description
XML_Serializer serializes complex data structures like arrays or object as
XML documents. This class helps you generating any XML document you require
without the need for DOM.


%prep
%setup -q -c
cd %{pear_name}-%{version}
# package.xml is V2
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
rm -rf $RPM_BUILD_ROOT
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}



%check
# error_reporting = E_ALL & ~E_STRICT & ~E_DEPRECATED = 22527
cd %{pear_name}-%{version}/tests

## Don't execute outdated test (
rm *.phpt

phpunit \
   --include-path=$RPM_BUILD_ROOT%{pear_phpdir} \
   --verbose .


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/XML/*
%{pear_testdir}/%{pear_name}


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul  5 2016 Remi Collet <remi@fedoraproject.org> - 0.21.0-1
- update to 0.21.0
- provide php-composer(pear/xml_serializer)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 0.20.2-13
- fix FTBFS, skip outdated phpt tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Remi Collet <remi@fedoraproject.org> - 0.20.2-12
- set error_reporting during tests

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 0.20.2-10
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 0.20.2-8
- move todo.txt to doc

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 0.20.2-7
- rebuilt for new pear_testdir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Remi Collet <remi@fedoraproject.org> - 0.20.2-5
- fix from SVN for test suite

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul  6 2011 Remi Collet <Fedora@FamilleCollet.com> - 0.20.2-3
- fix include_path in test (FTBFS #716012)
- doc in /usr/share/doc/pear

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.20.2-1
- Version 0.20.2 (beta) - API 0.20.0 (beta) - QA release
- add generated Changelog
- run phpunit test suite in %%check

* Mon Aug 23 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.20.0-2
- clean define
- set date.timezone during build
- use version in "Requires".

* Sun Jan 24 2010 Remi Collet <Fedora@FamilleCollet.com> 0.20.0-1
- update to 0.20.0
- License is BSD (since 0.19.0)
- rename XML_Serializer.xml to php-pear-XML-Serializer.xml
- add tests
- add %%check (documentation only)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.18.0-4
- fix license tag

* Sun Jan 14 2007 Christopher Stone <chris.stone@gmail.com> 0.18.0-3
- Add license to %%files

* Mon Oct 16 2006 Christopher Stone <chris.stone@gmail.com> 0.18.0-2
- Move the todo file in %%{pear_datadir} into %%doc

* Sat Oct 14 2006 Christopher Stone <chris.stone@gmail.com> 0.18.0-1
- Initial release
