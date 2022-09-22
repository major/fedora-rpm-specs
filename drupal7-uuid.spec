%{?drupal7_find_provides_and_requires}

%global module uuid

Name:          drupal7-%{module}
Version:       1.3
Release:       9%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Adds support for universally unique identifiers

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# uuid.info
Requires:      drupal7(node)
Requires:      drupal7(user)
# phpcompatinfo (computed from version 1.3)
Requires:      php-pcre

%description
This module provides an API for adding universally unique identifiers (UUID) to
Drupal objects, most notably entities.

This package provides the following Drupal modules:
* %{module}
* %{module}_path
* %{module}_services
* %{module}_services_example


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3-1
- Update to 1.3 (RHBZ #1715182 / SA-CONTRIB-2019-052)
- https://www.drupal.org/sa-contrib-2019-052

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-1
- Update to 1.2 (RHBZ #1598258 / SA-CONTRIB-2018-045)
- https://www.drupal.org/sa-contrib-2018-045

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-1
- Update to 1.0 (RHBZ #1446183)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.2.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.1.beta2
- Initial package
