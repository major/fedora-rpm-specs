%global pecl_name  imagick
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Summary:        Provides a wrapper to the ImageMagick library
Name:           php-pecl-%pecl_name
Version:        3.7.0
Release:        16%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%pecl_name

Source0:        https://pecl.php.net/get/%{sources}.tgz

Patch0:        %{pecl_name}-tests.patch
Patch1:        %{pecl_name}-pr690.patch

ExcludeArch:    %{ix86}

BuildRequires:  php-pear
BuildRequires:  php-devel
BuildRequires:  pkgconfig(ImageMagick)

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%pecl_name               = %{version}
Provides:       php-%pecl_name%{?_isa}       = %{version}
Provides:       php-pecl(%pecl_name)         = %{version}
Provides:       php-pecl(%pecl_name)%{?_isa} = %{version}

Conflicts:      php-pecl-gmagick


%description
Imagick is a native php extension to create and modify images using the
ImageMagick API.


%package devel
Summary:       %{pecl_name} extension developer files (header)
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}

%description devel
These are the files needed to compile programs using %{pecl_name} extension.


%prep
%setup -qc

# don't install any font (and test using it)
# don't install empty file (d41d8cd98f00b204e9800998ecf8427e)
sed -e '/anonymous_pro_minus.ttf/d' \
    -e '/015-imagickdrawsetresolution.phpt/d' \
    -e '/OFL.txt/d' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

if grep '\.ttf' package.xml
then : "Font files detected!"
     exit 1
fi

cd %{sources}
%patch -P0 -p1
%patch -P1 -p1

: Avoid arginfo to be regenerated
rm *.stub.php

extver=$(sed -n '/#define PHP_IMAGICK_VERSION/{s/.* "//;s/".*$//;p}' php_imagick.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension = %{pecl_name}.so

; Documentation: http://php.net/imagick

; Don't check builtime and runtime versions of ImageMagick
imagick.skip_version_check=1

; Fixes a drawing bug with locales that use ',' as float separators.
;imagick.locale_fix=0

; Used to enable the image progress monitor.
;imagick.progress_monitor=0

; multi-thread management
;imagick.set_single_thread => 1 => 1
;imagick.shutdown_sleep_count => 10 => 10

; to allow null images
;imagick.allow_zero_dimension_images => 0 => 0
EOF


%build
cd %{sources}

: Standard build
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --with-imagick=%{prefix} --with-php-config=%{__phpconfig}

%make_build


%install
cd %{sources}
: Install the extension
%make_install

: Drop in the bit of configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -p -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install Test and Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do [ -f $i ] && install -Dpm 644 $i %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do [ -f $i ] && install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}

: simple module load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

# Ignore know failed test on some ach (s390x, armv7hl, aarch64) with timeout
rm tests/229_Tutorial_fxAnalyzeImage_case1.phpt
rm tests/244_Tutorial_psychedelicFontGif_basic.phpt
# very long, and erratic results
rm tests/073_Imagick_forwardFourierTransformImage_basic.phpt
rm tests/086_Imagick_forwardFourierTransformImage_basic.phpt
# https://github.com/Imagick/imagick/issues/645
rm tests/316_Imagick_getImageKurtosis.phpt

: upstream test suite for the extension
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%files devel
%doc %{pecl_testdir}/%{pecl_name}
%{php_incldir}/ext/%{pecl_name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Remi Collet <remi@fedoraproject.org> - 3.7.0-15
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 3.7.0-14
- rebuild for https://fedoraproject.org/wiki/Changes/php84
- add patch for PHP 8.4 from
  https://github.com/Imagick/imagick/pull/690

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Remi Collet <remi@remirepo.net> - 3.7.0-12
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Mon Jan 29 2024 Remi Collet <remi@remirepo.net> - 3.7.0-11
- ignore 1 test failing with recent ImageMagick version

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 3.7.0-9
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Remi Collet <remi@remirepo.net> - 3.7.0-7
- use SPDX license ID

* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 3.7.0-6
- Rebuild for ImageMagick 7

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 3.7.0-5
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 22 2022 Remi Collet <remi@remirepo.net> - 3.7.0-3
- hack to avoid arginfo to be regenerated

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Remi Collet <remi@remirepo.net> - 3.7.0-1
- update to 3.7.0

* Thu Nov 18 2021 Remi Collet <remi@remirepo.net> - 3.6.0-1
- update to 3.6.0
- drop patch merged upstream

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 3.5.1-3
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Oct 15 2021 Remi Collet <remi@remirepo.net> - 3.5.1-2
- fix #457 failed test with ImageMagick 6.9.12-23
  using patch from https://github.com/Imagick/imagick/pull/458

* Fri Jul 23 2021 Remi Collet <remi@remirepo.net> - 3.5.1-1
- update to 3.5.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0
- drop all patches merged upstream
- run test suite in parallel
- add new options in configuration file

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 3.4.4-7
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 3.4.4-3
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May  7 2019 Remi Collet <remi@remirepo.net> - 3.4.4-1
- update to 3.4.4
- drop patch merged upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 3.4.3-10
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 3.4.3-9
- Rebuild for ImageMagick 6.9.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4.3-7
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 3.4.3-5
- undefine _strict_symbol_defs_build
- use patch from https://github.com/mkoppanen/imagick/pull/221

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 3.4.3-4
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Tue Sep 05 2017 Adam Williamson <awilliam@redhat.com> - 3.4.3-3
- Rebuild for ImageMagick 6 reversion

* Thu Aug 24 2017 Remi Collet <remi@remirepo.net> - 3.4.3-2
- rebuild for new ImageMagick

* Mon Aug 14 2017 Remi Collet <remi@remirepo.net> - 3.4.3-1
- update to 3.4.3
- add devel subpackage
- add ZTS extension
- big spec file cleanup and fix FTBFS from Koschei

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-0.4.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-0.3.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 3.4.3-0.2.RC1
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 3.4.3-0.1.RC1
- update to 3.4.3RC1
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Thu Feb 25 2016 Remi Collet <remi@fedoraproject.org> - 3.1.2-5
- drop scriptlets (replaced by file triggers in php-pear) #1310546

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 3.1.2-1
- update to 1.1.7RC2
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-0.9.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 13 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 3.1.0-0.8.RC2
- ImageMagick 6.8.8.10-3 rebuild.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-0.7.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 3.1.0-0.6.RC2
- update to 3.1.0RC2
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Sat Mar 16 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 3.1.0-0.5.RC1
- Rebuild to ImageMagick soname change (ml: http://www.mail-archive.com/devel@lists.fedoraproject.org/msg57163.html).
	Thanks to Remi Collet for the patch: http://svn.php.net/viewvc?view=revision&revision=329769

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-0.4.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-0.3.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 4 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 3.1.0-0.2.RC1
- Rebuild to ImageMagick soname change.

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 3.1.0-0.1.RC1
- update to 3.1.0RC1 for php 5.4
- add filter to avoid private-shared-object-provides
- add minimal %%check

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.0-10
- Fix FBFS f16-17. Bz#716201

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 3.0.0-8
- Rebuilt for gcc bug 634757

* Thu Sep 16 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.0-7
- Rebuild against new ImageMagick

* Fri Jul 23 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.0-6
- Update to 3.0.0
- Add Conflicts: php-pecl-gmagick - BZ#559675
- Delete new and unneeded files "rm -rf %%{buildroot}/%%{_includedir}/php/ext/%%peclName/"

* Sat May 15 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 2.3.0-5
- New version 2.3.0

* Wed Mar 24 2010 Mike McGrath <mmcgrath@redhat.com> - 2.2.2-4.1
- Rebuilt for broken dep fix

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Remi Collet <Fedora@FamilleCollet.com> - 2.2.2-3
- rebuild for new PHP 5.3.0 ABI (20090626)

* Tue Mar 10 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 2.2.2-2
- Rebuild due ImageMagick update

* Sat Feb 28 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 2.2.2-1
- Step to version 2.2.2

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 11 2009 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] spb [ dOt.] su> - 2.2.1-3
- All modifications in this release inspired by Fedora review by Remi Collet.
- Add versions to BR for php-devel and ImageMagick-devel
- Remove -n option from %%setup which was excessive with -c
- Module install/uninstall actions surround with %%if 0%%{?pecl_(un)?install:1} ... %%endif
- Add Provides: php-pecl(%%peclName) = %%{version}

* Sat Jan 3 2009 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] spb [ dOt.] su> - 2.2.1-2
- License changed to PHP (thanks to Remi Collet)
- Add -c flag to %%setup (Remi Collet)
	And accordingly it "cd %%peclName-%%{version}" in %%build and %%install steps.
- Add (from php-pear template)
	Requires(post):	%%{__pecl}
	Requires(postun):	%%{__pecl}
- Borrow from Remi Collet php-api/abi requirements.
- Use macroses: (Remi Collet)
	%%pecl_install instead of direct "pear install --soft --nobuild --register-only"
	%%pecl_uninstall instead of pear "uninstall --nodeps --ignore-errors --register-only"
- %%doc examples/{polygon.php,captcha.php,thumbnail.php,watermark.php} replaced by %%doc examples (Remi Collet)
- Change few patchs to macroses: (Remi Collet)
	%%{_libdir}/php/modules - replaced by %%{php_extdir}
	%%{xmldir} - by %%{pecl_xmldir}
- Remove defines of xmldir, peardir.
- Add 3 recommended macroses from doc http://fedoraproject.org/wiki/Packaging/PHP : php_apiver, __pecl, php_extdir

* Sat Dec 20 2008 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] spb [ dOt.] su> - 2.2.1-1
- Step to version 2.2.1
- As prepare to push it into Fedora:
	- Change release to 1%%{?dist}
	- Set setup quiet
	- Escape all %% in changelog section
	- Delete dot from summary
	- License change from real "PHP License" to BSD (by example with php-peck-phar and php-pecl-xdebug)
- %%defattr(-,root,root,-) changed to %%defattr(-,root,root,-)

* Mon May 12 2008 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] spb [ dOt.] su> - 2.2.0b2-0.Hu.0
- Step to version 2.2.0b2
- %%define	peclName	imagick and replece to it all direct appearances.

* Thu Mar 6 2008 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] info> - 2.1.1RC1-0.Hu.0
- Steep to version 2.1.1RC1 -0.Hu.0
- Add Hu-part and %%{?dist} into Release
- Add BuildRequires: ImageMagick-devel

* Fri Oct 12 2007 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] info> - 2.0.0RC1
- Global rename from php-pear-imagick to php-pecl-imagick. This is more correct.

* Wed Aug 22 2007 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] info> - 2.0.0RC1
- Initial release. (Re)Written from generated (pecl make-rpm-spec)
