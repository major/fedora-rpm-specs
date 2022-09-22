%{?drupal7_find_provides_and_requires}

%global module domain

Name:          drupal7-%{module}
Version:       3.17
Release:       7%{?dist}
Summary:       A domain-based access control system

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 3.17)
Requires:      php-hash
Requires:      php-pcre
Requires:      php-session

%description
The Domain Access project is a suite of modules that provide tools for running
a group of affiliated sites from one Drupal installation and a single shared
database. The module allows you to share users, content, and configurations
across a group of sites such as:
* example.com
* one.example.com
* two.example.com
* my.example.com
* thisexample.com <-- can use any domain string
* example.com:3000 <-- treats non-standard ports as unique

By default, these sites share all tables in your Drupal installation. The
Domain Prefix module (for Drupal 6) allows for selective, dynamic table
prefixing for advanced users.

This package provides the following Drupal modules:
* %{module}
* %{module}_alias
* %{module}_conf
* %{module}_content
* %{module}_nav
* %{module}_settings
* %{module}_source
* %{module}_strict
* %{module}_theme


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/
for DOC in $(find . -type f -name 'README.txt')
do
    DIR=$(dirname "$DOC")
    mkdir -p .rpm/docs/${DIR}
    mv $DOC .rpm/docs/${DIR}/
done


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.17-2
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Sun Apr 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.17-1
- Updated to 3.17 (RHBZ #1784584)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.16-1
- Updated to 3.16 (RHBZ #1626732)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.13-1
- Updated to 3.13 (RHBZ #1415427)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.12-1
- Updated to 3.12 (RHBZ #1249432)
- %%license usage
- Keep documentation where end-users expect it
- Removed RPM README b/c it only explained common Drupal workflow

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.11-1
- Updated to 3.11 (BZ #1071895; release notes https://drupal.org/node/2208987)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 29 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.10-2
- Removed empty, unused, and unreferenced file "domain.overlay.js"

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.10-1
- Updated to 3.10
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.9-1
- Initial package
