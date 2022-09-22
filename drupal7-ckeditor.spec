%{?drupal7_find_provides_and_requires}

%global module ckeditor

Name:          drupal7-%{module}
Version:       1.19
Release:       7%{?dist}
Summary:       Enables the usage of CKEditor (WYSIWYG) instead of plain text fields

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

Requires:      ckeditor
# phpcompatinfo (computed from version 1.19)
Requires:      php-date
Requires:      php-hash
Requires:      php-json
Requires:      php-pcre


%description
This module will allow Drupal to replace textarea fields with the CKEditor - a
visual HTML editor [1], usually called a WYSIWYG editor. This HTML text editor
brings many of the powerful WYSIWYG editing functions of known desktop editors
like Word to the web. It's very fast and doesn't require any kind of
installation on the client computer.

This package provides the following Drupal module:
* %{module}

[1] http://ckeditor.com/


%prep
%setup -qn %{module}
rm -rf ckeditor

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/

# Soft link to system CKEditor library
ln -s %{_datadir}/ckeditor %{buildroot}%{drupal7_modules}/%{module}/


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.19-2
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Sun Apr 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.19-1
- Updated to 1.19 (RHBZ #1814868, SA-CONTRIB-2020-007)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.18-1
- Updated to 1.18 (RHBZ #1465189)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 12 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.17-1
- Updated to 1.17 (RHBZ #1294109)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16-2
- Removed EPEL 5 bits

* Sun Nov 09 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16-1
- Updated to 1.16 (BZ #1153938)
- Removed RPM README b/c it only explained common Drupal workflow
- Spec cleanup

* Thu Aug 07 2014 Peter Borsa <peter.borsa@gmail.com> - 1.15-1
- Update to upstream 1.15 release for bug fixes
- Upstream changelog for this release is available at https://www.drupal.org/node/2303581

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Peter Borsa <peter.borsa@gmail.com> - 1.14-1
- Update to upstream 1.14 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2261789

* Thu Sep 26 2013 Peter Borsa <peter.borsa@gmail.com> - 1.13-1
- Update to upstream 1.13 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/1968526

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 6 2013 Orion Poplawski <orion@cora.nwra.com> - 1.12-1
- Update to 7.x-1.12

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9-1
- Update to 7.x-1.9
- Fix line endings in CHANGELOG.txt

* Wed Mar 14 2012 Orion Poplawski <orion@cora.nwra.com> - 1.7-1
- Update to 7.x-1.7

* Thu Jan 26 2012 Orion Poplawski <orion@cora.nwra.com> - 1.6-1
- Initial drupal 7 package
