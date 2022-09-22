%global theme zen

Name:          drupal7-theme-%{theme}
Version:       6.4
Release:       14%{?dist}
Summary:       Zen is a powerful, yet simple, HTML5 starting theme

# Licenses:
# - GPLv2+
#     - Drupal zen theme itself
# - MIT or GPLv2
#     - js/html5shiv.min.js (bundled)
License:       GPLv2+ and (MIT or GPLv2)
URL:           http://drupal.org/project/%{theme}
Source0:       http://ftp.drupal.org/files/projects/%{theme}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 6.4)
Requires:      php-pcre

# drupal7-{PROJECT}
Provides:      drupal7-%{theme} = %{version}

# Bundled
## js/html5.js
###     License: MIT or GPLv2
###     Upstream: https://github.com/aFarkas/html5shiv
Provides:      bundled(js-html5shiv) = 3.7.2


%description
Zen is a powerful, yet simple, HTML5 starting theme with a responsive,
mobile-first grid design. If you are building your own standards-compliant
theme, you will find it much easier to start with Zen than to start with
Garland or Stark. This theme has fantastic online documentation
(http://drupal.org/node/193318) and tons of helpful code comments
in its' PHP, HTML, CSS and Sass.


%prep
%setup -q -n %{theme}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/
for README in $(find . -type f -name 'README.txt')
do
    README_DIRNAME=$(dirname $README)
    mkdir -p .rpm/docs/${README_DIRNAME}
    mv $README .rpm/docs/${README_DIRNAME}/
done


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}%{drupal7_themes}/%{theme}
cp -pr * %{buildroot}%{drupal7_themes}/%{theme}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_themes}/%{theme}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 6.4-9
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 6.4-1
- Updated to 6.4 (RHBZ #1287340)

* Sun Aug 07 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.6-1
- Updated to 5.6
- Changed license from "GPLv2 and MIT" to "GPLv2+ and (MIT or GPLv2) and (MIT or BSD)"
  per bundled libs
- Added "bundled(*)" virtual provides
- Minor spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Peter Borsa <peter.borsa@gmail.com> - 5.4-1
- Update to upstream 5.4 release for security and bug fixes
- SA-CONTRIB-2013-070 https://drupal.org/node/2071157
- Upstream changelog for this release is available at https://drupal.org/node/2071055

* Thu Aug 08 2013 Peter Borsa <peter.borsa@gmail.com> - 5.3-1
- Update to upstream 5.3 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2054707

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 08 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.1-3
- Added drupal7-%%{theme} virtual provide

* Thu May 02 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.1-2
- Fixed license

* Thu Mar 28 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.1-1
- Initial package
