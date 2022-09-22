%{?drupal7_find_provides_and_requires}

%global module file_entity

Name:          drupal7-%{module}
Version:       2.27
Release:       8%{?pre_release:.%{pre_release}}%{?dist}
Summary:       File entity (fieldable files)

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# file_entity.info
Requires:      drupal7(ctools)
Requires:      drupal7(field)
Requires:      drupal7(file)
Requires:      drupal7(system) >= 7.33
# phpcompatinfo (computed from version 2.27)
Requires:      php-date
Requires:      php-pcre

%description
File entity provides interfaces for managing files. It also extends the core
file entity, allowing files to be fieldable, grouped into types, viewed (using
display modes) and formatted using field formatters. File entity integrates
with a number of modules, exposing files to Views, Entity API, Token and more.

This package provides the following Drupal module:
* %{module}


%prep
%setup -q -n %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.27-3
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.27-1
- Update to 2.27
- Add .info file to repo

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.25-1
- Updated to 2.25 (RHBZ #1532086)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2-1
- Updated to 2.2 (RHBZ #1458526)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.8.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.7.beta3
- Updated to 2.0-beta3 (RHBZ #1327692)
- Minor spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.6.unstable7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.5.unstable7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.4.unstable7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.3.unstable7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.2.unstable7
- Updated for drupal7-rpmbuild 7.22-5

* Wed Apr 10 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.1.unstable7
- Initial package
