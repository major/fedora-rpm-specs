%{?drupal7_find_provides_and_requires}

%global module panels

Name:          drupal7-%{module}
Version:       3.9
Release:       13%{?dist}
Summary:       Allows a site administrator to create customized layouts

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# panels.info
#
# From 3.8 release notes (https://www.drupal.org/project/panels/releases/7.x-3.8):
#     Note: This release requires ctools 7.x-1.11. Make sure you update both!
Requires:      drupal7(ctools) >= 1.11
# phpcompatinfo (computed from version 3.9)
Requires:      php-date
Requires:      php-pcre
Requires:      php-spl

%description
The Panels module allows a site administrator to create customized layouts for
multiple uses. At its core it is a drag and drop content manager that lets you
visually design a layout and place content within that layout. Integration with
other systems allows you to create nodes that use this, landing pages that use
this, and even override system pages such as taxonomy and the node page so that
you can customize the layout of your site with very fine grained permissions.

This package provides the following Drupal modules:
* %{module}
* %{module}_ipe
* %{module}_mini
* %{module}_node
* i18n_%{module}


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.9-8
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 26 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.9-1
- Updated to 3.9 (RHBZ #1419759)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.8-2
- Require ctools >= 1.11

* Thu Nov 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.8-1
- Updated to 3.8 (RHBZ #1385610)

* Sun Sep 11 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.7-1
- Updated to 3.7 (RHBZ #1370663 / SA-CONTRIB-2016-047)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 07 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.5-2
- Added drupal7(ctools) requirement

* Tue Feb 03 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.5-1
- Updated to 3.5 (BZ #1187881)
- Spec cleanup

* Mon May 26 2014 Peter Borsa <peter.borsa@gmail.com> - 3.4-1
- Initial package
