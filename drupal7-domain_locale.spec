%{?drupal7_find_provides_and_requires}

%global module_name domain_locale
%global pre_release beta6

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.22.%{pre_release}%{?dist}
Summary:       Adds language handling functionality per domain basis

License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

Requires:      drupal7(domain)
Requires:      drupal7(domain_conf)
Requires:      drupal7(locale)
# phpcompatinfo (computed from version 1.0-beta6)
# <none>

%description
Domain Locale allows to customize language sets per domain for Drupal installs
using Domain Access and core Locale module. This module also offers drush
integration.

You need this module if:
* you want a different default language on different domains
* you want a different language set for each different domain

This package provides the following Drupal module:
* %{module_name}


%prep
%setup -qn %{module_name}


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal7_modules}/%{module_name}/



%files
%{?_licensedir:%license LICENSE.txt}
%{drupal7_modules}/%{module_name}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.21.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.20.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.19.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.17.beta6
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.11.beta6
- Updated to 1.0-beta6 (RHBZ #1469507)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.10.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.9.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.8.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.7.beta5
- Updated to 1.0-beta5 (RHBZ #1220585)
- Removed RPM README b/c it only explained common Drupal workflow
- Keep documentation where end-users expect it
- %%license usage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.4.beta4
- Update to upstream 1.0-beta4 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2219857

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.2.beta3
- Updated to 1.0-beta3
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta1
- Initial package
