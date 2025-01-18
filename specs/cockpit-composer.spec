Name:           cockpit-composer
Version:        53
Release:        2%{?dist}
Summary:        Composer GUI for use with Cockpit

License:        MIT
URL:            http://weldr.io/
Source0:        https://github.com/osbuild/cockpit-composer/releases/download/%{version}/cockpit-composer-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  libappstream-glib

Requires:       cockpit
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 8
Requires: osbuild-composer >= 28
%else
Requires: weldr
Suggests: osbuild-composer >= 28
%endif

%description
Composer generates custom images suitable for deploying systems or uploading to
the cloud. It integrates into Cockpit as a frontend for osbuild.

%prep
%setup -q -n cockpit-composer

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/cockpit/composer
cp -a public/* %{buildroot}/%{_datadir}/cockpit/composer
mkdir -p %{buildroot}/%{_datadir}/metainfo/
appstream-util validate-relax --nonet public/org.image-builder.cockpit-composer.metainfo.xml
cp -a public/org.image-builder.cockpit-composer.metainfo.xml %{buildroot}/%{_datadir}/metainfo/ 

%files
%doc README.md
%license LICENSE.txt
%{_datadir}/cockpit/composer
%{_datadir}/metainfo/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Packit <hello@packit.dev> - 53-1
- bump testlib
- translations update

* Thu Aug 22 2024 Packit <hello@packit.dev> - 52-1
Incorrect RHEL 10 repository overrides broke downstream tests.

* Thu Aug 22 2024 Packit <hello@packit.dev> - 51.1-1
Integrates with packit, tmt, and testing farm.

* Tue Aug 20 2024 Packit <hello@packit.dev> - 51-1
- remove empty customizations from blueprint when creating one

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Packit <hello@packit.dev> - 50-1
- Update metainfo.xml
- Fix issue with some customizations not displaying
- Set default language from cockpit's settings

* Mon Feb 26 2024 Packit <hello@packit.dev> - 49-1
- Update testing environment
- Update translations

* Wed Feb 14 2024 Packit <hello@packit.dev> - 48-1
- Fix rhsm bug
- Update translations and minor dependencies

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 28 2023 Packit <hello@packit.dev> - 47-1
- Fix OCI sizing bug

* Fri Aug 25 2023 Packit <hello@packit.dev> - 46-1
- Fix blueprint config bugs
- Update translations
- Update NPM dependencies

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Packit <hello@packit.dev> - 45-1
- Update translsations

* Thu Feb 23 2023 Packit <hello@packit.dev> - 44-1
- Minor bug fixes
- Update translations

* Wed Feb 15 2023 Packit <hello@packit.dev> - 43-1
- Add customizations
- Fix bugs

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Packit <hello@packit.dev> - 42-1
- Update most components to use React 17 and PF4
- Update store to user redux-toolkit
- Update all style, build, and translations config
- Update all NPM dependencies
- Readd edge-simplified-installer image type


* Mon Sep 05 2022 Packit <hello@packit.dev> - 41-1
- Update translations


* Tue Aug 23 2022 Packit <hello@packit.dev> - 40-1
- Improve blueprint loading
- Fix error state
- Improve OSTree customizations


* Fri Aug 19 2022 Packit <hello@packit.dev> - 39-1
- Improve save blueprint workflow
- Add all customizations to Wizard
- Fix sorting
- Improve tests
- Update translations
- Improve review step in Wizard


* Mon Aug 15 2022 Packit <hello@packit.dev> - 38-1
- Update major and minor NPM dependencies including React, Webpack, and
  Patternfly
- Migrate Wizard to use Data Driven Forms and improve validation
- Remove Edit Blueprint page and add package selection to Wizard
- Simplify tests and add tests for the new Wizard
- Remove Blueprint Undo/Redo features


* Mon Jul 25 2022 Packit <hello@packit.dev> - 37-1
- Improve test reliability
- Update translations


* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Jacob Kozol <jacobdkozol@gmail.com> - 35-1
- Update translations from Fedora Weblate (#1403)

* Thu Feb 17 2022 Jacob Kozol <jacobdkozol@gmail.com> - v34-1
- workflows: release tags now start with a v (#1401)
- Wizard: add oci section to review step (#1398)
- Makefile: bump cockpit to newest release (#1399)
- [no-test] Update translations from Fedora Weblate (#1397)

* Fri Feb 04 2022 Jacob Kozol <jacobdkozol@gmail.com> - 33-1
- Add support for OCI upload target
- Update translations
- Update dependencies

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Jacob Kozol <jacobdkozol@gmail.com> - 32-1
- Add Edge Raw, RHEL Installer, Edge Simplified Installer image types
- Improve user account modal responsiveness
- Update tests
- Update minor NPM dependencies
- Update translation files

* Thu Aug 26 2021 Jacob Kozol <jacobdkozol@gmail.com> - 31-1
- Add new ostree image types
- Improve loading state when waiting for api responses
- Improve notification system
- Improve test stability
- Update NPM dependencies
- Update translations

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 11 2021 Jacob Kozol <jacobdkozol@gmail.com> - 30-1
- Add and update translations
- Update NPM dependencies
- Improve test reliability


* Mon Feb 22 2021 Jacob Kozol <jacobdkozol@gmail.com> - 29-1
- Add ability to upload to VMWare
- Add support for additional ostree parameters
- Update NPM dependencies
- Add and update translations
- Minor test fixes


* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Jacob Kozol <jacobdkozol@gmail.com> - 28-1
- Use sentence case rather than title case
- Add and update tests
- Update translations from weblate
- Update minor NPM dependencies


* Wed Dec 09 2020 Jacob Kozol <jacobdkozol@gmail.com> - 27-1
- Improve test reliability
- Update translations from weblate
- Update minor NPM dependencies


* Thu Nov 19 2020 Jacob Kozol <jacobdkozol@gmail.com> - 26-1
- Add additional form validation for the Create Image Wizard
- Improve page size dropdown styling
- Update minor NPM dependencies
- Improve code styling
- Improve test reliability


* Tue Oct 06 2020 Jacob Kozol <jacobdkozol@gmail.com> - 25-1
- Improve error state messages
- Add additional console error logging
- Update CDP testing library
- Update translations from weblate
- Update minor NPM dependencies


* Fri Sep 11 2020 Jacob Kozol <jacobdkozol@gmail.com> - 24-1
- Improve text strings for image and upload types
- Standardize font families with those used by patternfly
- Add string translations
- Update minor NPM dependencies


* Thu Jul 30 2020 Jacob Kozol <jacobdkozol@gmail.com> - 23-1
- Update pagination component for pf4
- Add wildcards and support for multiple values to input filter
- Upgrade patternfly 4 package
- Add and improve tests
- Update minor NPM dependencies
- Update translations from weblate


* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Jacob Kozol <jacobdkozol@gmail.com> - 22-1
- Patternfly imports are standardized to be consistent with cockpit
- Cancel image build button bug fixed
- Empty components state provides a help message
- Wizard component has bug fixes and is refactored for future scalability
- Test updates
- ESLint upgraded to version 7 and the code style is improved across the
  project
- Translation files are updated from fedora weblate
- Cockpit-composer's dependency on osbuild-composer and the weldr group
  is more specific for fedora rawhide and rhel 8
- Coverity scan is now supported to help improve code quality


* Sun Jun 14 2020 Lars Karlitski <lars@karlitski.net> - 21-1
- Support setting parameters (ref and parent) for ostree images
- Loosen restrictions on password strength
- Various UI refinements


* Mon Jun 08 2020 Lars Karlitski <lars@karlitski.net> - 20-1
- Fix various missing translations
- Improve message when a blueprint is empty
- Hide logs button until logs are available
- Update test framework to be closer to that of other cockpit projects


* Wed Jun 03 2020 Jacob Kozol <jacobdkozol@gmail.com> - 19-1
- Minor UI improvements for the images list view and the images dropdown
- Fixes to the password tests
- Prepartion for future osbuild support
- Minor NPM updates for react
- Minor translation updates






* Wed May 20 2020 Jacob Kozol <jacobdkozol@gmail.com> - 18-1
- Fix flake8 E302 error in tests
- Minor NPM updates for patternfly and jquery
- Translations updates




* Wed May 06 2020 Jacob Kozol <jacobdkozol@gmail.com> - 17-1
- The support for uploading VHD images to Azure is now available.
- Help text is now provided for all AWS fields. This texts explains what
  each field represents and where to find their values in the AWS
  web console.
- The image size can now be specified when creating an image.
- Tests are refactored to run on Cockpit's testing framework. All tests
  have been moved away from selenium.
- Minor NPM updates






* Wed Apr 15 2020 Jacob Kozol <jacobdkozol@gmail.com> - 16-1
- The ability to upload to AWS has been added. The create image modal is
  replaced with a wizard enabling additional customizations and
  functionality. If the user creates an AMI the user can also enter the
  credentials and parameters needed to upload this image to EC2 in AWS.
- Cockpit-composer has migrated from Weldr to the OSBuild github
  organization. It can now be found at osbuild/cockpit-composer instead
  of weldr/cockpit-composer.
- Minor NPM updates have been made for React and Patternfly




* Wed Apr 01 2020 Jacob Kozol <jacobdkozol@gmail.com> - 15-1
- Migrate from lorax-composer to osbuild-composer backend
- Update tests for new backend
- Improve stability of tests
- Remove Zanata from Travis configuration
- Update NPM dependencies


* Wed Mar 18 2020 Jacob Kozol <jacobdkozol@gmail.com> - 14-1
- Test against lorax-composer explicitly
- Update NPM dependencies


* Wed Mar 04 2020 Jacob Kozol <jacobdkozol@gmail.com> - 13-1
- Update translations
- Update NPM dependencies


* Wed Feb 19 2020 Martin Pitt <martin@piware.de> - 12.1-1
- Fix integration tests, external test repository URL ceased to exist


* Wed Feb 19 2020 Martin Pitt <martin@piware.de> - 12-1
- Translation updates
- Add documentation URL page help menu


* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Martin Pitt <martin@piware.de> - 11-1
- Update translations
- Fix tests to work against current Cockpit as non-root


* Tue Dec 17 2019 Lars Karlitski <lars@karlitski.net> - 10-1
- Show depsolve errors on the blueprints page
- Add labels for additional output types
- Convert more components to PF4


* Fri Oct 25 2019 Martin Pitt <martin@piware.de> - 9-1
- Translation updates
- Expose Image Builder on /composer, not /welder
- NPM dependency updates


* Wed Oct 02 2019 Martin Pitt <martin@piware.de> - 8-1
- NPM dependency updates


* Fri Sep 06 2019 Jacob Kozol <jacobdkozol@gmail.com> - 7-1
- Define a URL for each tab on a blueprint page
- Provide a link in the image creation notification to the Images tab on the blueprint page

* Wed Aug 21 2019 Jacob Kozol <jacobdkozol@gmail.com> - 6-1
- Text string updates

* Wed Aug 07 2019 Jacob Kozol <jacobdkozol@gmail.com> - 5-1
- Fix PropTypes for the homepage
- Code clean up for the list of components


* Wed Jul 31 2019 Martin Pitt <martin@piware.de> - 4-1
- Fix AppStream ID
- Translation updates


* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Martin Pitt <martin@piware.de> - 3-1
- Use cockpit's PatternFly CSS, to pick up the new PatternFly 4 styling
- Add additional blueprint name validation
- Fix images not loading on refresh
- Add notification for source repo deletion


* Wed Jun 26 2019 Martin Pitt <martin@piware.de> - 2-1
- Strip newlines from SSH keys before saving
- Translation updates


* Wed Jun 05 2019 Cockpit Project <cockpituous@gmail.com> - 1-1
- Update to upstream 1 release

* Fri May 24 2019 Cockpit Project <cockpituous@gmail.com> - 0.4-1
- Update to upstream 0.4 release

* Mon May 06 2019 Cockpit Project <cockpituous@gmail.com> - 0.3-1
- Update to upstream 0.3 release

* Mon Apr 15 2019 Cockpit Project <cockpituous@gmail.com> - 0.2.1-1
- Update to upstream 0.2.1 release

* Mon Mar 25 2019 Cockpit Project <cockpituous@gmail.com> - 0.2.0-1
- Update to upstream 0.2.0 release

* Thu Mar 07 2019 Cockpit Project <cockpituous@gmail.com> - 0.1.9-2
- Update to upstream 0.1.9 release

