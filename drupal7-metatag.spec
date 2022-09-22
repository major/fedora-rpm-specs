%{?drupal7_find_provides_and_requires}

%global module metatag

Name:          drupal7-%{module}
Version:       1.27
Release:       7%{?dist}
Summary:       Adds support and an API to implement meta tags

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# metatag.info
Requires:      drupal7(ctools)
Requires:      drupal7(system) >= 7.40
Requires:      drupal7(token)
# phpcompatinfo (computed from version 1.27)
Requires:      php-date
Requires:      php-pcre

%description
The Metatag module allows you to automatically provide structured metadata,
aka "meta tags", about your website. In the context of search engine
optimization, when people refer to meta tags they are usually referring to
the meta description tag and the meta keywords tag that may help improve
the rankings and display of your site in search engine results.

Meta tags have additional uses like the Open Graph Protocol used by Facebook,
specifying the canonical location of content across multiple URLs or domains.

This project is the designated Drupal 7 a from-the-ground-up rewrite and
successor of the Nodewords module.

This package provides the following Drupal modules:
* %{module}
* %{module}_app_links
* %{module}_context (requires drupal7-context)
* %{module}_dc
* %{module}_dc_advanced
* %{module}_devel
* %{module}_facebook
* %{module}_favicons
* %{module}_google_cse
* %{module}_google_plus
* %{module}_hreflang
* %{module}_importer
* %{module}_mobile
* %{module}_opengraph
* %{module}_opengraph_products
* %{module}_panels (requires drupal7-ctools and drupal7-token, as well as
      manual install of panels)
* %{module}_twitter_cards
* %{module}_verification
* %{module}_views (requires drupal7-views)


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
# Docs used at runtime
#mv *.txt .rpm/docs/

%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
# Docs used at runtime
#%%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.27-2
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Sun Apr 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.27-1
- Update to 1.27 (RHBZ #1785734)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.25-1
- Update to 1.25 (RHBZ #1563432)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.22-1
- Updated to 1.22 (RHBZ #1467454)

* Sun Feb 26 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.21-1
- Updated to 1.21 (RHBZ #1422700 / SA-CONTRIB-2017-019)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.20-1
- Updated to 1.20 (RHBZ #1409443)

* Thu Dec 15 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.18-1
- Updated to 1.18 (RHBZ #1400352)

* Thu Aug 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.17-1
- Updated to 1.17 (RHBZ #1298910)
- Minor spec cleanups

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7-1
- Updated to 1.7 (RHBZ #1246704)

* Mon Jul 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6-1
- Updated to 1.6 (RHBZ #1226487)
- Keep documentation where end-users expect it

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4-1
- Updated to 1.4 (BZ #1150459)
- Removed RPM README b/c it only explained common Drupal workflow

* Wed Sep 24 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-1
- Updated to 1.1 (BZ #1144307; release notes https://www.drupal.org/node/2341013)

* Thu Aug 07 2014 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.7.rc2
- Updated to 1.0-rc2 (BZ #1127134; release notes https://www.drupal.org/node/2315805)

* Sun Jul 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.6.rc1
- Updated to 1.0-rc1 (BZ #1119065; release notes https://www.drupal.org/node/2302051)
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.beta9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.4.beta9
- Updated to 1.0-beta9 (BZ #1059999; release notes https://drupal.org/node/2176579)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.2.beta7
- Updated for drupal7-rpmbuild 7.22-5

* Sun May 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.1.beta7
- Initial package
