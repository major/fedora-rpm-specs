%{?drupal7_find_provides_and_requires}

%global module tmgmt
%global pre_release rc3

Name:          drupal7-%{module}
Version:       1.0
Release:       0.24%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Translation Management Tool

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2
BuildRequires: make

# tmgmt.info
Requires:      drupal7(entity)
Requires:      drupal7(locale)
Requires:      drupal7(views)
# phpcompatinfo (computed from version 1.0-rc3)
Requires:      php-date
Requires:      php-dom
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xmlreader
Requires:      php-xmlwriter

%description
The Translation Management Tool (TMGMT) module provides a tool set for
translating content from different sources. The translation can be done
by people or translation services of all kinds. It builds on and uses
existing language tools and data structures in Drupal and can be used
in automated workflow scenarios.

This module does not make i18n or any other language module for Drupal
obsolete. It does only facilitate the translation process.

The second alpha has been released, huge improvements have been made
(see the release notes for details) and there's even more work to do.
Please test the new version and report any bugs that you can find.

Important: The external translator plugins (Microsoft, MyGengo, Nativy,
Supertext) have been moved to separate projects. When any of these plugins,
make sure to download them as well and then run update.php when updating.

This package provides the following Drupal modules:
* %{module}
* %{module}_entity
* %{module}_entity_ui
* %{module}_field
* %{module}_file
* %{module}_i18n_string
* %{module}_language_combination
* %{module}_local
* %{module}_locale
* %{module}_node
* %{module}_node_ui
* %{module}_ui


%prep
%setup -qn %{module}

: Remove executable bits
find . -type f -perm /+x -print0 | xargs -0 chmod -x

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/
mkdir -p .rpm/docs/translators/tmgmt_local
mv translators/tmgmt_local/*.txt .rpm/docs/translators/tmgmt_local/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -pm 0755 %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.24.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.23.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.21.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.20.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.19.rc3
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.16.rc3
- Updated to 1.0-rc3 (RHBZ #1611856)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.10.rc2
- Updated to 1.0-rc2 (RHBZ #1352245)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.9.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.6.rc1
- Updated to 1.0-rc1 (BZ #1072782; release notes https://drupal.org/node/2210721)

* Fri Aug 16 2013 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.5.beta2
- Update to upstream 1.0-beta2 release for bug fixes
- Upstream changelog for this release is avalble at https://drupal.org/node/2066361

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.3.beta1
- Update to upstream 1.0-beta1 release for bug fixes
- Upstream changelog for this release is avalble at https://drupal.org/node/2045887

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.2.alpha3
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.1.alpha3
- Initial package
