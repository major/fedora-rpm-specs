# Fedora spec file for php-pear-DB
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name DB

# run rpmbuild --with sqlite if sqlite extension available
%global with_sqlite 0%{?_with_sqlite:1}

Name:           php-pear-DB
Version:        1.11.0
Release:        4%{?dist}
Summary:        PEAR: Database Abstraction Layer

License:        PHP
URL:            http://pear.php.net/package/DB
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

Patch0:         %{pear_name}-php8.patch

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.10.0
%if %{with_sqlite}
BuildRequires:  php-sqlite
%endif
BuildRequires:  php-mysqli

Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}
Requires:       php-pear(PEAR) >= 1.10.0


%description
DB is a database abstraction layer providing:
* an OO-style query API
* portability features that make programs written for one DBMS work with
  other DBMS's
* a DSN (data source name) format for specifying database servers
* prepare/execute (bind) emulation for databases that don't support it natively
* a result object for each query response
* portable error codes
* sequence emulation
* sequential and non-sequential row fetching as well as bulk fetching
* formats fetched rows as associative arrays, ordered arrays or objects
* row limit support
* transactions support
* table information interface
* DocBook and phpDocumentor API documentation

DB layers itself on top of PHP's existing database extensions.


%prep
%setup -q -c

cd %{pear_name}-%{version}
%patch0 -p1

# Package is V2
sed -e 's/md5sum="[^"]*"//' ../package.xml >%{name}.xml

# update run test suite
sed -e 's@^ *DB_TEST_RUN_TESTS=.*$@[ -d /usr/lib64 ] \&\& DB_TEST_RUN_TESTS=/usr/lib64/php/build/run-tests.php || DB_TEST_RUN_TESTS=/usr/lib/php/build/run-tests.php@' \
    -e 's@^ *DB_TEST_DIR=.*$@DB_TEST_DIR=%{pear_testdir}/DB/tests@' \
    -e 's@^ *TEST_PHP_EXECUTABLE=.*$@TEST_PHP_EXECUTABLE=%{_bindir}/php@' \
    tests/run.cvs >tests/run

sed -e 's@^ *DB_TEST_RUN_TESTS=.*$@[ -d /usr/lib64 ] \&\& DB_TEST_RUN_TESTS=/usr/lib64/php/build/run-tests.php || DB_TEST_RUN_TESTS=/usr/lib/php/build/run-tests.php@' \
    -e 's@^ *DB_TEST_DIR=.*$@DB_TEST_DIR=%{pear_testdir}/DB/tests/driver@' \
    -e 's@^ *TEST_PHP_EXECUTABLE=.*$@TEST_PHP_EXECUTABLE=%{_bindir}/php@' \
    tests/driver/run.cvs >tests/driver/run


%build
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}

# Install new test suite
install -pm 755 tests/run $RPM_BUILD_ROOT%{pear_testdir}/DB/tests/
install -pm 755 tests/driver/run $RPM_BUILD_ROOT%{pear_testdir}/DB/tests/driver/

mv $RPM_BUILD_ROOT%{pear_docdir}/%{pear_name}/doc/TESTERS .
iconv -f ISO-8859-1 -t UTF-8  TESTERS \
   -o $RPM_BUILD_ROOT%{pear_docdir}/%{pear_name}/doc/TESTERS
touch -r TESTERS $RPM_BUILD_ROOT%{pear_docdir}/%{pear_name}/doc/TESTERS


%check
top=$PWD

cd %{pear_name}-%{version}/tests
pear \
   run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   . | tee $top/tests.log

cd driver
%if %{with_sqlite}
sed -e "s://'sqlite':'sqlite':" -i setup.inc
%{__pear} \
   run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   . | tee -a $top/tests.log
%else
echo "Driver test skipped (need sqlite extension)"
%endif

grep "FAILED TESTS" $top/tests.log && exit 1 || exit 0


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
%{pear_phpdir}/DB*
%{pear_testdir}/DB


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0
- open https://github.com/pear/DB/pull/12 fix for PHP 8

* Fri Jul 30 2021 Remi Collet <remi@remirepo.net> - 1.10.0-5
- fix DB-dbase::query prototype, fix FTBFS #1987844

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 1.9.3-1
- update to 1.9.3
- drop patch merged upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Remi Collet <remi@fedoraproject.org> - 1.9.2-6
- fix condition in test suite, FTBFS #1556118
- fix count usage for PHP 7.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Remi Collet <remi@fedoraproject.org> - 1.9.2-1
- update to 1.9.2
- raise dependency on PEAR 1.10.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 28 2014 Remi Collet <remi@fedoraproject.org> - 1.8.2-1
- update to 1.8.2

* Fri Nov 21 2014 Remi Collet <remi@fedoraproject.org> - 1.8.1-1
- update to 1.8.1
- drop generated changelog

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug  5 2013 Remi Collet <remi@fedoraproject.org> - 1.7.14-8
- xml2changelog need simplexml

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Remi Collet <remi@fedoraproject.org> - 1.7.14-6
- fix metadata location, FTBFS #914358

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.7.14-4
- rebuilt for new pear_testdir

* Sat Aug 04 2012 Remi Collet <remi@fedoraproject.org> 1.7.14-3
- disable E_STRICT in tests, fix FTBFS

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 27 2011 Remi Collet <remi@fedoraproject.org> 1.7.14-1
- update to 1.7.14

* Wed Apr 13 2011 Remi Collet <Fedora@FamilleCollet.com> 1.7.13-5
- doc in /usr/share/doc/pear
- define timezone during build
- rename DB.xml to php-pear-DB.xml
- fix libdir in provided tests (%%{_libdir} have no value for noarch package)
- run tests in %%check (no driver as no sqlite extension)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 21 2007 Remi Collet <Fedora@FamilleCollet.com> 1.7.13-1
- update to 1.7.13
- fix TEXTERS encoding

* Thu Aug 23 2007 Remi Collet <Fedora@FamilleCollet.com> 1.7.12-2
- Fix License

* Mon Jul 23 2007 Remi Collet <Fedora@FamilleCollet.com> 1.7.12-1
- update to 1.7.12
- change requires from php to php-common
- update test suite to run (but only after install)
- add %%check, only for documentation purpose

* Mon Apr 30 2007 Remi Collet <Fedora@FamilleCollet.com> 1.7.11-1
- update to 1.7.11
- add generated CHANGELOG

* Sun Sep 10 2006 Tim Jackson <rpm@timj.co.uk> 1.7.6-7
- Update spec to new conventions (#198706)

* Wed Jun 28 2006 Tim Jackson <rpm@timj.co.uk> 1.7.6-6
- Move tests to peardir/test instead of peardir/tests (bug #196764)

* Wed May 17 2006 Tim Jackson <rpm@timj.co.uk> 1.7.6-5
- Moved package XML file to %%{peardir}/.pkgxml (see bug #190252)
- Abstracted package XML directory
- Removed some "-f"s on rm's to avoid masking possible errors

* Tue Jan 24 2006 Tim Jackson <rpm@timj.co.uk> 1.7.6-4
- Move package XML file to _libdir/php/pear rather than _var/lib/pear

* Tue Jan 24 2006 Tim Jackson <rpm@timj.co.uk> 1.7.6-3
- Requires(post,postun) php-pear

* Sat Dec 31 2005 Tim Jackson <rpm@timj.co.uk> 1.7.6-2
- Rearranged so it makes more sense
- Remove external license file
- peardir definition now comes from "pear config-get"
- BR php-pear
- shorten description
- be explicit about the files in the package
- use macro for /var
- remove versioning from pear(PEAR) dep; 1.0b1 is very old

* Sat Dec 31 2005 Tim Jackson <rpm@timj.co.uk> 1.7.6-1
- First RPM build
