%{?drupal7_find_provides_and_requires}

%global module taxonomy_access_fix

Name:          drupal7-%{module}
Version:       2.4
Release:       11%{?dist}
Summary:       Fixes the crooked access checks for Taxonomy pages

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

Requires:      drupal7(taxonomy)
# phpcompatinfo (computed from version 2.4)
# <none>

%description
This module:
* adds 1 permission per vocabulary: "add terms in X"
* changes the way vocabulary specific permissions are handled
* changes the Taxonomy admin pages' access checks
* alters the vocabularies overview table to show only what you have access to
  edit or delete

The module does what native Taxonomy lacks: more specific Taxonomy permissions
(and checking them correctly).

Note: In order to access the admin/structure/taxonomy page, you must first set
permissions for the desired vocabularies.

Note: A module can't add permissions to another module, so the extra "add terms
in X" permissions are located under "Taxonomy access fix" and not under
"Taxonomy".

This package provides the following Drupal module:
* %{module}


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4-6
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4-1
- Updated to 2.4 (RHBZ #1544047)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 12 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3-1
- Updated to 2.3 (RHBZ #1280514)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2-1
- Updated to 2.2 (RHBZ #1223140)
- Removed RPM README b/c it only explained common Drupal workflow
- Keep documentation where end-users expect it
- %%license usage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 26 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1-1
- Updated to 2.1 (BZ #1101179; release notes https://www.drupal.org/node/2274235)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-1
- Updated to 2.0 (BZ #1060000; release notes https://drupal.org/node/2152445)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-2
- Updated for drupal7-rpmbuild 7.22-5

* Tue Mar 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-1
- Initial package
