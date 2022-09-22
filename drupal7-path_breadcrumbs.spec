%{?drupal7_find_provides_and_requires}

%global module path_breadcrumbs

Name:          drupal7-%{module}
Version:       3.4
Release:       9%{?dist}
Summary:       Allows creation of custom breadcrumbs for any page using contexts

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# path_breadcrumbs
Requires:      drupal7(ctools)
Requires:      drupal7(entity)
Requires:      drupal7(entity_token)
# phpcompatinfo (computed from version 3.4)
Requires:      php-pcre

%description
Path breadcrumbs module helps you to create breadcrumbs for any page with any
selection rules and load any entity from the URL.

Features
* Breadcrumbs navigation may be added to any kind of page: static
  (example: node/1) or dynamic (example: node/NID).
* You can load contexts from URL and use it like tokens for breadcrumb path or
  title.
* You can use selection rules for every breadcrumbs navigation.
* Supports ALL tokens from Entity tokens module (part of Entity module).
* You can import/export breadcrumbs (supports single operations, Features and
  Ctools bulk export).
* Breadcrumbs can be cloned to save you time while building navigation.
* Module provides rich snippets support for breadcrumbs (RDFa and Microdata).
* Module provides first/last/odd/even classes to every breadcrumb link.
* You can change breadcrumbs delimiter.
* Breadcrumbs could be hidden if they contain only one element.
* You can disable breadcrumbs and enable them later.
* All breadcrumb titles are translatable.
* Usable interface.

This package provides the following Drupal modules:
* %{module}
* %{module}_i18n (requires drupal7-i18n)
* %{module}_ui


%prep
%setup -qn %{module}


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{?_licensedir:%license LICENSE.txt}
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.4-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.4-1
- Updated to 3.4 (RHBZ #1683781 / SA-CONTRIB-2019-027)
- https://www.drupal.org/sa-contrib-2019-027

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.3-1
- Updated to 3.3 (RHBZ #1243614; SA-CONTRIB-2015-133)
- Removed RPM README b/c it only explained common Drupal workflow
- Keep documentation where end-users expect it

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 07 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2-1
- Updated to 3.2 (BZ #1190389; SA-CONTRIB-2015-037)

* Sun Jan 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.1-1
- Updated to 3.1 (BZ #1178332)
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.9.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-0.8.rc2
- Updated to 3.0-rc2 (BZ #1066282; release notes https://drupal.org/node/2197523)

* Sun Jan 26 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-0.7-rc1
- Updated to 3.0-rc1 (BZ #1050855; release notes https://drupal.org/node/2181867)

* Thu Nov 07 2013 Peter Borsa <peter.borsa@gmail.com> - 3.0-0.6.beta6
- Update to upstream 3.0-beta6 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2119965

* Sat Aug 10 2013 Peter Borsa <peter.borsa@gmail.com> - 3.0-0.5.beta4
- Update to upstream 3.0-beta4 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2058787

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.4.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-0.3.beta3
- Updated to 3.0-beta3 (BZ #981354)

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-0.2.beta2
- Updated to 3.0-beta2
- Updated for drupal7-rpmbuild 7.22-5

* Tue Mar 26 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-0.1.beta1
- Initial package
