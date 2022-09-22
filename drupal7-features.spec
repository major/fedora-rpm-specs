%{?drupal7_find_provides_and_requires}

%global module features

Name:          drupal7-%{module}
Version:       2.10
Release:       14%{?dist}
Summary:       Provides feature management for Drupal

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 2.10)
Requires:      php-ctype
Requires:      php-pcre

Obsoletes:     drupal7-features_plumber  < %{version}-%{release}
Provides:      drupal7-features_plumber  = %{version}-%{release}
Provides:      drupal7(features_plumber) = %{version}

%description
The features module enables the capture and management of features in Drupal.
A feature is a collection of Drupal entities which taken together satisfy a
certain use-case.

Features provides a UI and API for taking different site building components
from modules with exportables and bundling them together in a single feature
module. A feature module is like any other Drupal module except that it
declares its components (e.g. views, contexts, CCK fields, etc.) in its .info
file so that it can be checked, updated, or reverted programmatically.

This package provides the following Drupal module:
* %{module}


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
# Docs can be rendered at runtime by end-user
#cp *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
#%%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.10-9
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.10-1
- Updated to 2.10 (RHBZ #1320757 / SA-CONTRIB-2016-020)
- Removed %%defattr

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Paul W. Frields <stickster@gmail.com> - 2.7-1
- Update to 2.7
- Release notes found at https://www.drupal.org/node/2592441

* Wed Jul 01 2015 Peter Borsa <peter.borsa@gmail.com> - 2.6-1
- Update to 2.6
- Release notes can be found at https://www.drupal.org/node/2511520

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Jared Smith <jsmith@fedoraproject.org> - 2.5-1
- Update to upstream 2.5 release for bug fixes
- Upstream changelog for this release: https://www.drupal.org/node/2470129

* Thu Mar 05 2015 Jared Smith <jsmith@fedoraproject.org> - 2.4-1
- Update to upstream 2.4 release for bug fixes
- Upstream changelog for this release: https://www.drupal.org/node/2446159

* Tue Jan  6 2015 Paul W. Frields <stickster@gmail.com> - 2.3-1
- Update to upstream 2.3 release for bug fix

* Sat Oct 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2-2
- Spec cleanup

* Thu Aug 07 2014 Peter Borsa <peter.borsa@gmail.com> - 2.2-1
- Update to upstream 2.2 release for bug fixes

* Wed Jul 30 2014 Paul W. Frields <stickster@gmail.com> - 2.1-1
- Update to upstream 2.1 release for bug fixes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 06 2014 Peter Borsa <peter.borsa@gmail.com> - 2.0-6
- Increase obsolotes version number

* Wed Dec 18 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-5
- Fix Obsolotes line, remove zero

* Wed Dec 18 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-4
- Obsolete drupal7-features_plumber package

* Thu Nov 14 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-3
- Superfluous commit to make Bodhi happy

* Thu Nov 14 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-2
- Fixed non-versioned versus versioned doc dir issue

* Thu Nov 07 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-1
- Update to upstream 2.0 release for bug fixes
- Upstream changelog for this release: https://drupal.org/node/2106567

* Mon Oct  7 2013 Paul W. Frields <stickster@gmail.com> - 2.0-0.8.rc5
- Update to upstream 2.0-rc5 release for bug fixes
- Upstream changelog for this release: https://drupal.org/node/2106567

* Tue Aug 27 2013 Paul W. Frields <stickster@gmail.com> - 2.0-0.7.rc3
- Update to upstream 2.0-rc3 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2074581

* Thu Aug 08 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.6.rc2
- Update to upstream 2.0-rc2 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2056641

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.4.rc1
- Update to upstream 2.0-rc1 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/1999432

* Sat May 25 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.3.beta2
- README.txt in module directory for UI help (BZ 966932)

* Thu Apr 4 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.2.beta2
- New upstream version.

* Wed Mar 13 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.1.beta1
- New upstream version.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug  3 2012 Peter Borsa <peter.borsa@gmail.com> - 1.0-1
- New upstream version.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.6.rc3
- New upstream rc2 version

* Sat Apr 14 2012 Jared Smith <jsmith@fedoraproject.org> - 1.0-0.5.rc2
- New upstream rc2 version
- Leave the README.txt file in the module directory to avoid a Drupal warning

* Tue Mar 20 2012 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.5.rc1
- New upstream version.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan  7 2012 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.3.beta6
- New upstream version.

* Thu Dec 29 2011 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.2.beta5
- New upstream version.

* Fri Sep 23 2011 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.1.beta4
- Initial packaging
