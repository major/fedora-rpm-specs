# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global peclName  xmldiff

%{!?__pecl:     %{expand: %%global __pecl     %{_bindir}/pecl}}

%if "%{php_version}" < "5.6"
# After dom
%global ini_name %peclName.ini
%else
# After 20-dom
%global ini_name 40-%peclName.ini
%endif

Name:             php-pecl-%peclName
Version:          1.1.3
Release:          6%{?dist}
Summary:          Pecl package for XML diff and merge

License:          BSD
URL:              http://pecl.php.net/package/%peclName
Source0:          http://pecl.php.net/get/%peclName-%{version}.tgz

BuildRequires:    make
BuildRequires:    gcc
BuildRequires:    php-pear
BuildRequires:    php-devel
BuildRequires:    libxml2-devel, diffmark-devel, dos2unix
# dom.so needed by %%check
BuildRequires:    php-dom, php-libxml
Requires:         php-dom%{_isa}, php-libxml%{?_isa}
%if 0%{?fedora} < 24
Requires(post):   %{__pecl}
Requires(postun): %{__pecl}
%endif
Requires:         php(zend-abi) = %{php_zend_api}
Requires:         php(api) = %{php_core_api}
Requires:         php-xml

Provides:         php-%peclName = %{version}
Provides:         php-%peclName%{?_isa} = %{version}

# Filter private shared (RPM 4.9) (f20+ (and rhel7) does not require that)
%if 0%{?fedora} < 20 && 0%{?rhel} < 7
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}%{php_extdir}/.*\\.so$
%endif

%description
The extension is able to produce diffs of two XML documents and then
to apply the difference to the source document. The diff
is a XML document containing copy/insert/delete instruction nodes in
human readable format. DOMDocument objects, local files and strings in
memory can be processed.


%prep
%setup -qc

#rm bundled diffmark
rm -rf %peclName-%{version}/diffmark

# to make rpmlint happy
dos2unix --keepdate %peclName-%{version}/LICENSE

%build
cd %peclName-%{version}
phpize
%{configure} --with-%peclName --with-libdiffmark=%{_libdir}
make %{?_smp_mflags}


%install
cd %peclName-%{version}

make %{?_smp_mflags} install INSTALL_ROOT=%{buildroot}

# Install XML package description
install -m 0755 -d %{buildroot}%{pecl_xmldir}
install -m 0664 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
install -d %{buildroot}%{php_inidir}
# install config file
install -d %{buildroot}%{php_inidir}
cat << 'EOF' | tee %{buildroot}%{php_inidir}/%{ini_name}
extension=%{php_extdir}/%peclName.so
EOF

mkdir -p %{buildroot}/%{pecl_docdir}/%peclName/
mv {CREDITS,LICENSE} %{buildroot}/%{pecl_docdir}/%peclName/

rm -rf %{buildroot}/%{_includedir}/php/ext/%peclName/

%check
# only check if build extension can be loaded
php \
    --no-php-ini \
    --define extension=dom.so \
    --define extension=%{buildroot}%{php_extdir}/%peclName.so \
    --modules | grep %peclName

cd %peclName-%{version}

# Can't do just 'make %{?_smp_mflags} test' because path and option hardcoded. Makefile patching needed or run tests manually
TEST_PHP_EXECUTABLE=%{__php} \
  NO_INTERACTION=1 \
    TEST_PHP_ARGS="-n -d extension=dom.so -d extension=%{buildroot}%{php_extdir}/%peclName.so" \
      php -n run-tests.php

%if 0%{?fedora} < 24
%post
%{pecl_install} %{pecl_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ "$1" -eq "0" ]; then
  %{pecl_uninstall} %peclName >/dev/null || :
fi
%endif

%files
%doc %{pecl_docdir}/%peclName
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%peclName.so
%{pecl_xmldir}/%{name}.xml

%changelog
* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.1.3-6
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 1.1.3-3
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar  5 2021 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- update to 1.1.3
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.1.2-13
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.1.2-10
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 1.1.2-7
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.1.2-6
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-2
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-2
- update to 1.1.2
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Thu Feb 25 2016 Remi Collet <remi@fedoraproject.org> - 0.9.2-13
- drop scriptlets (replaced by file triggers in php-pear) #1310546

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.2-10
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 16 2015 Remi Collet <remi@fedoraproject.org> - 0.9.2-9
- rebuild with gcc 5 and diffmark (thanks Koschei)

* Mon Sep 15 2014 Remi Collet <rcollet@redhat.com> - 0.9.2-8
- make BuildRequires arch independent

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 0.9.2-6
- rebuild for https://fedoraproject.org/wiki/Changes/Php56

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.2-4
- Own %%{pecl_docdir}/%%peclName dir.

* Tue May 13 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.2-3
- Surround filter provides by condition %%if 0%%{?fedora} < 20 && 0%%{?rhel} < 7
- Fix %%doc installation issue.

* Mon May 12 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.2-2
- Changes by Fedora review bz#1094864 from Remi Collet comments.
- Remove define php_apiver, php_extdir.
- Tun upstream tests in %%check.
- Requires php-dom%%{_isa} and php-libxml%%{?_isa} instead of php-xml.
- Install docs into %%pecl_docdir.
- Prefix ini file with numeric value in rawhide.
- Drop protect %%{pecl_uninstall} present.

* Tue May 6 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.2-1
- Initial spec
