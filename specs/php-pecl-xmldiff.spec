%global pecl_name  xmldiff
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Name:             php-pecl-%{pecl_name}
Version:          1.1.4
Release:          2%{?dist}
Summary:          Pecl package for XML diff and merge

License:          BSD-2-Clause
URL:              http://pecl.php.net/package/%{pecl_name}
Source0:          http://pecl.php.net/get/%{sources}.tgz

ExcludeArch:      %{ix86}

BuildRequires:    make
BuildRequires:    gcc
BuildRequires:    php-pear
BuildRequires:    php-devel
BuildRequires:    libxml2-devel
BuildRequires:    diffmark-devel
BuildRequires:    dos2unix
# dom.so needed by %%check
BuildRequires:    php-dom
BuildRequires:    php-libxml

Requires:         php-dom%{?_isa}
Requires:         php-libxml%{?_isa}
Requires:         php(zend-abi) = %{php_zend_api}
Requires:         php(api) = %{php_core_api}

Provides:         php-%{pecl_name}               = %{version}
Provides:         php-%{pecl_name}%{?_isa}       = %{version}
Provides:         php-pecl(%{pecl_name})         = %{version}
Provides:         php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
The extension is able to produce diffs of two XML documents and then
to apply the difference to the source document. The diff
is a XML document containing copy/insert/delete instruction nodes in
human readable format. DOMDocument objects, local files and strings in
memory can be processed.


%prep
%setup -qc

sed -e '/name="diffmark/d' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}

# drop bundled library to ensure it is not used
rm -rf diffmark

# to make rpmlint happy
dos2unix --keepdate LICENSE

# Create configuration file
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-libdiffmark \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the documentation
install -D -m 644 CREDITS %{buildroot}/%{pecl_docdir}/%{pecl_name}/CREDITS

: Clean devel 
rm -rf %{buildroot}/%{_includedir}/php/ext/%{pecl_name}


%check
# only check if build extension can be loaded
php \
    --no-php-ini \
    --define extension=dom.so \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

cd %{sources}
TEST_PHP_ARGS="-n -d extension=dom.so -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
php -n run-tests.php -q --show-diff


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so
%{pecl_xmldir}/%{name}.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4
- drop patch merged upstream
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.1.3-14
- rebuild for https://fedoraproject.org/wiki/Changes/php84
- fix PHP 8.4 build using patch from
  https://github.com/php/pecl-xml-xmldiff/pull/2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 1.1.3-12
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.1.3-9
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 1.1.3-7
- use SPDX license ID

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
