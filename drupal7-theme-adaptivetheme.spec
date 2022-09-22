%global theme adaptivetheme

Name:          drupal7-theme-%{theme}
Version:       3.4
Release:       14%{?dist}
Summary:       Adaptivetheme is a powerful theme framework

# Licenses:
# - GPLv2+
#     - Drupal adaptivetheme theme itself
# - MIT
#     - at_core/scripts/onmediaquery.js (bundled)
# - MIT or BSD
#     - at_core/scripts/matchMedia.js (bundled)
#     - at_core/scripts/matchMedia.addListener.js (bundled)
# - MIT or GPL+
#     - at_core/scripts/outside-events.js (bundled)
# - MIT or GPLv2
#     - at_core/scripts/html5.js (bundled)
#     - at_core/scripts/scalefix.js
# - (MIT or GPLv2) and (MIT or BSD)
#     - at_core/scripts/respond.js (bundled)
License:       GPLv2+ and MIT and (MIT or BSD) and (MIT or GPL+) and (MIT or GPLv2)
URL:           http://drupal.org/project/%{theme}
Source0:       http://ftp.drupal.org/files/projects/%{theme}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 3.4)
Requires:      php-date
Requires:      php-filter
Requires:      php-pcre

# drupal7-{PROJECT}
Provides:      drupal7-%{theme} = %{version}-%{release}

# Bundled
## at_core/scripts/html5.js
###     License: MIT or GPLv2
###     Upstream: https://github.com/aFarkas/html5shiv
Provides:      bundled(js-html5shiv) = 3.7.2
## at_core/scripts/matchMedia.js
## at_core/scripts/matchMedia.addListener.js
###     License: MIT or BSD
###     Upstream: https://github.com/paulirish/matchMedia.js/
Provides:      bundled(js-matchMedia)
## at_core/scripts/onmediaquery.js
###     License: MIT
###     Upstream: https://github.com/JoshBarr/js-media-queries
Provides:      bundled(js-onMediaQuery)
## at_core/scripts/outside-events.js
###     License: MIT or GPL
###     Upstream: http://benalman.com/projects/jquery-outside-events-plugin/
Provides:      bundled(js-jquery-outside-events) = 1.1
## at_core/scripts/respond.js
###     License: (MIT or GPLv2) and (MIT or BSD)
###     Upstream: https://github.com/scottjehl/Respond
Provides:      bundled(js-respond) = 1.1.0
## at_core/scripts/scalefix.js
###     License: MIT or GPLv2
###     Upstream: https://github.com/scottjehl/iOS-Orientationchange-Fix
Provides:      bundled(js-iOS-Orientationchange-Fix)


%description
Adaptivetheme is a powerful theme framework with smoking hot support
for mobile and tablet devices using responsive design techniques.


%prep
%setup -q -n %{theme}

: Remove git files
find . -type f -name '.git*' | xargs rm -f

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/
for README in $(find . -type f -name '_README.txt')
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.4-9
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.4-1
- Updated to 3.4 (RHBZ #1354480)
- Changed license from "GPLv2+" to "GPLv2+ and MIT and (MIT or BSD) and (MIT or GPL+) and (MIT or GPLv2)"
  per bundled libs
- Spec cleanup
- Added drupal7-{PROJECT} virtual provide
- Added bundled virtual provides

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Peter Borsa <peter.borsa@gmail.com> - 3.1-1
- Updated to 3.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 10 2012 Peter Borsa <peter.borsa@gmail.com> - 3.0-1
- Updated to 3.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 Peter Borsa <peter.borsa@gmail.com> - 2.2-1
- Updated to 2.2.

* Sun Feb  5 2012 Peter Borsa <peter.borsa@gmail.com> - 2.1-1
- Initial packaging.
