%{?drupal7_find_provides_and_requires}

%global module rules

Name:          drupal7-%{module}
Version:       2.12
Release:       9%{?dist}
Summary:       React on events and conditionally evaluate actions

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# rules.info
Requires:      drupal7(entity)
Requires:      drupal7(entity_token)
# phpcompatinfo (computed from version 2.12)
Requires:      php-date
Requires:      php-filter
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

%description
The Rules module allows site administrators to define conditionally executed
actions based on occurring events (known as reactive or ECA rules). It's a
replacement with more features for the trigger module in core and the successor
of the Drupal 5 workflow-ng module.

This package provides the following Drupal modules:
* %{module}
* %{module}_admin
* %{module}_i18n
* %{module}_scheduler


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/

# E: script-without-shebang /usr/share/drupal7/modules/rules/includes/rules.event.inc
chmod a-x includes/rules.event.inc



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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.12-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.12-1
- Updated to 2.12 (RHBZ #1579996)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.10-1
- Updated to 2.10 (RHBZ #1444241)
- Removed unneeded %%defattr

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Peter Borsa <peter.borsa@gmail.com> - 2.9-1
- Updated to 2.9 (BZ #1202771)

* Tue Jan 13 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8-1
- Updated to 2.8 (BZ #1180431)
- Spec cleanup
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Peter Borsa <peter.borsa@gmail.com> - 2.7-1
- Update to upstream 2.7 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2257127

* Wed Nov 06 2013 Peter Borsa <peter.borsa@gmail.com> - 2.6-1
- Update to upstream 2.6 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2123171

* Thu Sep 26 2013 Peter Borsa <peter.borsa@gmail.com> - 2.5-1
- Update to upstream 2.5 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2092781

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Peter Borsa <peter.borsa@gmail.com> - 2.3-1
- New upstream version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 4 2012 Peter Borsa <peter.borsa@gmail.com> - 2.2-1
- New upstream version.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 20 2012 Peter Borsa <peter.borsa@gmail.com> - 2.1-2
- New upstream version.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Peter Borsa <peter.borsa@gmail.com> - 2.0-1
- Initial packaging.
