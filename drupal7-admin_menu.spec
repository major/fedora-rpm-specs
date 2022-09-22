%{?drupal7_find_provides_and_requires}

%global module admin_menu
%global pre_release rc6

Name:          drupal7-%{module}
Version:       3.0
Release:       0.21%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Provides a drop-down menu to most administrative tasks

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# admin_menu.info
Requires:      drupal7(core) > 7.10
# phpcompatinfo (computed from version 3.0-rc6)
Requires:      php-pcre


%description
The module provides a theme-independent administration interface (aka.
navigation, back-end). It's a helper for novice users coming from other CMS,
a time-saver for site administrators, and useful for developers and site
builders.

Administrative links are displayed in a CSS/JS-based menu at the top on all
pages of your site. It not only contains regular menu items - tasks and actions
are also included, enabling fast access to any administrative resource your
Drupal site provides.

This package provides the following Drupal 7 module:
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.21.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.20.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.19.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.18.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.17.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-0.16.rc6
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.15.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.14.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Shawn Iwinski <shawn@iwin.ski> - 3.0-0.13.rc6
- Update to 3.0-rc6
- Modernize spec

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.12.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.11.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.10.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.9.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.8.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.7.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.6.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 27 2014 Peter Borsa <peter.borsa@gmail.com> - 3.0-0.5.rc5
- Update to rc5 (BZ #1176868; release notes https://www.drupal.org/node/2396363)

* Fri Jun 27 2014 Sam Wilson <sam.wilson@nextdc.com> - 3.0-0.4.rc4
- Removed incorrect requires for PHP lang. Its added by drupal7-rpmbuild

* Thu May 08 2014 Sam Wilson <sam.wilson@nextdc.com> - 3.0-0.3.rc4
- Updated to include PHP deps

* Wed May 07 2014 Sam Wilson <sam.wilson@nextdc.com> - 3.0-0.2.rc4
- Updated to meet drupal7 guidelines https://fedoraproject.org/wiki/Packaging:Drupal7

* Mon Apr 28 2014 Sam Wilson <sam.wilson@nextdc.com> - 3.0-0.1.rc4
- Initial Package
