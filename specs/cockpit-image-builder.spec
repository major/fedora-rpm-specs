Name:           cockpit-image-builder
Version:        94
Release:        1%{?dist}
Summary:        Image builder plugin for Cockpit

License:        Apache-2.0
URL:            http://osbuild.org/
Source0:        https://github.com/osbuild/image-builder-frontend/releases/download/v%{version}/%{name}-%{version}.tar.gz

Obsoletes:      cockpit-composer < 54
Provides:       cockpit-composer = %{version}-%{release}

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  /usr/bin/node

Requires:       cockpit
Requires:       cockpit-files
Requires:       osbuild-composer >= 131

Recommends:     cockpit-machines

%description
The image-builder-frontend generates custom images suitable for
deploying systems or uploading to the cloud. It integrates into Cockpit
as a frontend for osbuild.

%prep
%setup -q -n %{name}

%build
# Nothing to build

%install
%make_install PREFIX=/usr
# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc cockpit/README.md
%license LICENSE
%{_datadir}/cockpit/cockpit-image-builder
%{_datadir}/metainfo/*

%changelog
* Wed Feb 18 2026 Packit <hello@packit.dev> - 94-1
Changes with 94
----------------
  - Wizard/Review: fix section visibility for net-installer type (HMS-9568) (#4123)
    - Author: Michal Gold, Reviewers: Klara Simickova
  - cockpit: Re-organize Security step (HMS-10217) (#4125)
    - Author: Klara Simickova, Reviewers: Lucas Garfield

— Somewhere on the Internet, 2026-02-18


* Tue Feb 17 2026 Packit <hello@packit.dev> - 93-1
Changes with 93
----------------
  - Add customization support labels to wizard steps (HMS-10201) (#4112)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  - Fix undefined distro handling for image-mode in requestMapper (HMS-10207) (#4118)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  - ImagesTable: change permission of artifact dir on launch (#4122)
    - Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli, Klara Simickova
  - Wizard: Hide "Other" label when it's the only category (HMS-10198) (#4111)
    - Author: Klara Simickova, Reviewers: Achilleas Koutsou
  - Wizard: clean up AWS registration from SPUR notes (HMS-10107) (#4036)
    - Author: Katarína Sieklová, Reviewers: Nobody
  - build(deps): bump the minor-and-patch group with 16 updates (#4119)
    - Author: {}, Reviewers: Klara Simickova
  - build(deps-dev): bump qs from 6.14.1 to 6.14.2 (#4115)
    - Author: {}, Reviewers: Michal Gold

— Somewhere on the Internet, 2026-02-17


* Fri Feb 13 2026 Packit <hello@packit.dev> - 92-1
Changes with 92
----------------
  - ImageOutput: switch to dynamic bootc image selection (HMS-10191) (#4107)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  - src/constants: add support for fedora 45 (#4109)
    - Author: Sanne Raymaekers, Reviewers: Klara Simickova

— Somewhere on the Internet, 2026-02-13


* Wed Feb 4 2026 Packit <hello@packit.dev> - 90-1
Changes with 90
----------------
  - Image mode compose request (HMS-10010) (#4009)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  - ImagesTable/Status: fix on-prem error messages (HMS-10099) (#4030)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova, Simon Steinbeiß
  - Move image-mode image type filtering to cockpitApi (HMS-10098) (#4028)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  - Wizard: Add password validation to inline alert in Users step (HMS-10078) (#4007)
    - Author: Michal Gold, Reviewers: Klara Simickova
  - Wizard: Combine alert and empty state in Additional Packages step (HMS-10126) (#4052)
    - Author: Michal Gold, Reviewers: Gianluca Zuccarelli
  - Wizard: Fix aria issues (HMS-10108) (#4039)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - Wizard: Fix crash when searching for group with repeatable build (HMS-10111) (#4042)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - Wizard: Fix padding of popover button for package groups (HMS-10112) (#4043)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - Wizard: Remove validation for non-required empty input (HMS-10081) (#4011)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - Wizard: Update hostname step description (HMS-10138) (#4062)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - build(deps): bump lodash from 4.17.21 to 4.17.23 (#4016)
    - Author: {}, Reviewers: Klara Simickova
  - build(deps): bump the minor-and-patch group with 16 updates (#4040)
    - Author: {}, Reviewers: Klara Simickova
  - build(deps): bump the minor-and-patch group with 7 updates (#4063)
    - Author: {}, Reviewers: Michal Gold
  - build(deps-dev): bump @types/node from 24.10.2 to 25.0.10 (#4041)
    - Author: {}, Reviewers: Klara Simickova
  - chore(deps): update build-tools digest to 7e1d036 (#4058)
    - Author: {}, Reviewers: Michal Gold
  - chore(deps): update konflux references (#4031)
    - Author: {}, Reviewers: Klara Simickova
  - cockpit: Add mountpoint policies for the image mode (HMS-10101) (#4037)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - cockpit: Filter image mode targets and customizations (HMS-10021) (#4008)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - cockpit: Fix crash in edit mode (HMS-10092) (#4023)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - cockpit: Fix useFlag import (HMS-10091) (#4022)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - cockpit: Gate blueprint mode label for on-prem only (HMS-10125) (#4051)
    - Author: Klara Simickova, Reviewers: Michal Gold
  - cockpit: Update validation for required Users step (HMS-9996) (#4034)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - playwright: Remove redundant next in target select (#4026)
    - Author: Tomáš Koscielniak, Reviewers: Klara Simickova
  - src: Rename "suffix" to "subpath" (HMS-10109) (#4038)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - vitest.config: remove sourcemap errors (HMS-10120) (#4048)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova

— Somewhere on the Internet, 2026-02-04


* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Dec 10 2025 Packit <hello@packit.dev> - 86-1
Changes with 86
----------------
  - ActivationKeysList: add a proxy on stage (#3907)
    - Author: Ondřej Budai, Reviewers: Michal Gold, Sanne Raymaekers
  - Update API (HMS-9824) (#3881)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - Update build-tools digest to ded5385 (#3894)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - Update dependency @types/react to v18.3.27 (#3897)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - Wizard/GCP: Accept domains as well as email addresses (HMS-4988) (#3868)
    - Author: Simon Steinbeiß, Reviewers: Klara Simickova
  - Wizard: Add safeguards to disk customization and fix min_size (HMS-9664) (#3835)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - Wizard: Update date format in default blueprint name (HMS-9854) (#3888)
    - Author: Klara Simickova, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli
  - Wizard: add information about firstboot and registration ordering (HMS-8555) (#3906)
    - Author: Katarína Sieklová, Reviewers: Klara Simickova
  - build(deps-dev): bump express from 4.21.2 to 4.22.1 (#3879)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump vitest-canvas-mock from 0.3.3 to 1.1.3 (#3901)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - docstrings: Drop references to RPM-DNF (#3873)
    - Author: Simon Steinbeiß, Reviewers: Klara Simickova
  - playwright: Fix tests after OpenSCAP configs regeneration (HMS-9862) (#3899)
    - Author: Klara Simickova, Reviewers: Michal Gold
  - playwright: re-enable the compliance test (#3905)
    - Author: Ondřej Budai, Reviewers: Gianluca Zuccarelli, Klara Simickova

— Somewhere on the Internet, 2025-12-10


* Fri Nov 28 2025 Packit <hello@packit.dev> - 85-1
Changes with 85
----------------
  - Remove build_deploy.sh script (HMS-9806) (#3860)
    - Author: Klara Simickova, Reviewers: Anna Vítová
  - Wizard: add AAP documentation (HMS-9757) (#3848)
    - Author: Katarína Sieklová, Reviewers: Klara Simickova
  - Wizard: edit Security review step according to mocks (HMS-9597) (#3850)
    - Author: Katarína Sieklová, Reviewers: Klara Simickova
  - Wizard: refactor ManageButton since it became widely used (#3859)
    - Author: Katarína Sieklová, Reviewers: Klara Simickova
  - actions/BootTests: Add a second Slack notification to frontend (#3867)
    - Author: Tomáš Koscielniak, Reviewers: Klara Simickova, Simon Steinbeiß
  - blueprints: default to host distro when importing in cockpit (RHEL-123840) (#3831)
    - Author: Sanne Raymaekers, Reviewers: Klara Simickova
  - build(deps): bump the minor-and-patch group across 1 directory with 17 updates (#3869)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - src: Bump smol-toml to 1.5.2 and update export mocks (HMS-9807) (#3865)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - src: Fix rendering validation for `ValidatedInput` (HMS-9797) (#3855)
    - Author: Klara Simickova, Reviewers: Katarína Sieklová

— Somewhere on the Internet, 2025-11-28


* Fri Nov 21 2025 Packit <hello@packit.dev> - 83-1
Changes with 83
----------------
  - Wizard: Disk customization (HMS-8945) (#3692)
    - Author: Klara Simickova, Reviewers: Nobody
  - Wizard: fix repeatable build behavior in pkg and repo steps (#3731)
    - Author: Dominik Vágner, Reviewers: Klara Simickova
  - Wizard: remove add and clear buttons from the LabelInput (HMS-9576) (#3818)
    - Author: Katarína Sieklová, Reviewers: Gianluca Zuccarelli, Klara Simickova
  - api: stop updating provisioning (HMS-5862) (#3829)
    - Author: Sanne Raymaekers, Reviewers: Klara Simickova
  - onPrem: Hide blueprint version warning (HMS-9782) (#3842)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - playwright: Add "node" to tsconfig types (HMS-9772) (#3834)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - playwright: Add Satellite boot tests (HMS-6024) (#3810)
    - Author: Klara Simickova, Reviewers: Nobody
  - store/cockpit: correct users customization (#3847)
    - Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  - store/cockpit: simplify customization conversion (HMS-9786) (#3846)
    - Author: Gianluca Zuccarelli, Reviewers: Sanne Raymaekers

— Somewhere on the Internet, 2025-11-21


* Wed Nov 12 2025 Packit <hello@packit.dev> - 82-1
Changes with 82
----------------
  - Playwright: Add non-repeatable build integration test (HMS-9497) (#3724)
    - Author: Tomáš Koscielniak, Reviewers: Klara Simickova, Michal Gold
  - Update latest API (HMS-9637) (#3784)
    - Author: Michal Gold, Reviewers: Klara Simickova
  - Update latest API (HMS-9685) (#3808)
    - Author: Michal Gold, Reviewers: Gianluca Zuccarelli, Klara Simickova
  - Wizard: Compliance revamp (HMS-9396) (#3732)
    - Author: Katarína Sieklová, Reviewers: Klara Simickova
  - build(deps-dev): bump @vitejs/plugin-react from 5.0.3 to 5.1.0 (#3782)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - chore(deps): lock file maintenance (#3728)
    - Author: red-hat-konflux[bot], Reviewers: Gianluca Zuccarelli, Klara Simickova
  - chore(deps): lock file maintenance (#3812)
    - Author: red-hat-konflux[bot], Reviewers: Michal Gold
  - chore(deps): update build-tools digest to 098cc75 (#3793)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - chore(deps): update build-tools digest to f15b565 (#3814)
    - Author: red-hat-konflux[bot], Reviewers: Michal Gold
  - chore(deps): update konflux references (#3789)
    - Author: red-hat-konflux[bot], Reviewers: Michal Gold
  - chore(deps): update react monorepo (#3797)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - chore(deps): update typescript-eslint monorepo to v8.46.3 (#3815)
    - Author: red-hat-konflux[bot], Reviewers: Tomáš Koscielniak
  - cockpit-image-builder: export blueprints (RHEL-123840) (#3779)
    - Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  - dependabot: Switch from daily to weekly updates (HMS-9650) (#3787)
    - Author: Klara Simickova, Reviewers: Michal Gold
  - devDeps: Bump eslint-plugin-playwright from 2.2.2 to 2.3.0 (HMS-9654) (#3795)
    - Author: Klara Simickova, Reviewers: Tomáš Koscielniak
  - fix(deps): update dependency @redhat-cloud-services/frontend-components to v7.0.13 (#3816)
    - Author: red-hat-konflux[bot], Reviewers: Tomáš Koscielniak
  - packit.yaml: Release into fedora-all (HMS-9619) (#3778)
    - Author: Klara Simickova, Reviewers: Sanne Raymaekers

— Somewhere on the Internet, 2025-11-12


* Wed Oct 29 2025 Packit <hello@packit.dev> - 81-1
Changes with 81
----------------
  - Wizard: add custom EPEL repo warning (#3757)
    - Author: Bryttanie, Reviewers: Klara Simickova
  - build(deps): bump @patternfly/react-table from 6.3.1 to 6.4.0 (#3759)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps): bump @redhat-cloud-services/frontend-components from 7.0.6 to 7.0.12 (#3774)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps): bump @scalprum/react-core from 0.10.0 to 0.11.0 (#3772)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @eslint/js from 9.36.0 to 9.38.0 (#3760)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - chore(deps): update babel monorepo to v7.28.5 (#3762)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - chore(deps): update dependency chart.js to v4.5.1 (#3764)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - chore(deps): update dependency sass-loader to v16.0.6 (#3765)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - package.json: replace @ltd/j-toml with smol-toml (RHEL-123840) (#3770)
    - Author: Sanne Raymaekers, Reviewers: Klara Simickova
  - schutzbot/terraform: bump terraform sha (#3769)
    - Author: Sanne Raymaekers, Reviewers: Klara Simickova

— Somewhere on the Internet, 2025-10-29


* Fri Oct 24 2025 Packit <hello@packit.dev> - 80-1
Changes with 80
----------------
  - CI/Playwright: Run boot tests on PR when changed and increase global timeout (HMS-9465) (#3718)
    - Author: Tomáš Koscielniak, Reviewers: Gianluca Zuccarelli, Sanne Raymaekers
  - LandingPage: Add "service unavailable" alert (HMS-9582) (#3739)
    - Author: Klara Simickova, Reviewers: Sanne Raymaekers
  - Playwright: Change AAP tests file extension, remove redundant timeout (#3725)
    - Author: Tomáš Koscielniak, Reviewers: Anna Vítová
  - Wizard: Add status polling for pending repositories (HMS-9591) (#3749)
    - Author: Tomáš Koscielniak, Reviewers: Gianluca Zuccarelli
  - Wizard: Firewall revamp (HMS-9399) (#3675)
    - Author: Katarína Sieklová, Reviewers: Gianluca Zuccarelli
  - Wizard: address Google Cloud Platform renaming (HMS-9577) (#3727)
    - Author: Anna Vítová, Reviewers: Tomáš Koscielniak
  - build(deps): bump @patternfly/react-code-editor from 6.3.1 to 6.4.0 (#3746)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @redhat-cloud-services/tsc-transform-imports from 1.0.25 to 1.0.26 (#3726)
    - Author: dependabot[bot], Reviewers: Anna Vítová
  - build(deps-dev): bump msw from 2.11.3 to 2.11.6 (#3745)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - chore(deps): replace dependency npm-run-all with npm-run-all2 5.0.0 (#3736)
    - Author: red-hat-konflux[bot], Reviewers: Michal Gold
  - chore(deps): update build-tools digest to 4eea3e7 (#3737)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - ci: update typescript-eslint packages to 8.46.1 (HMS-9579) (#3733)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  - devDeps: Bump playwright and @playwright/test (HMS-9583) (#3743)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - devDeps: Bump typescript deps (HMS-9581) (#3742)
    - Author: Klara Simickova, Reviewers: Tomáš Koscielniak
  - playwright: Registration step tests (#3721)
    - Author: Anna Vítová, Reviewers: Gianluca Zuccarelli
  - src/constants: add support for fedora 43 and 44 (#3754)
    - Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli, Klara Simickova

— Somewhere on the Internet, 2025-10-24


* Wed Oct 1 2025 Packit <hello@packit.dev> - 78-1
Changes with 78
----------------
  - Notifications: fix mutations with notifications hook (HMS-9449) (#3683)
    - Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli, Klara Simickova, Tomáš Koscielniak
  - Remove frontend components dependencies of Launch (#3657)
    - Author: Anna Vítová, Reviewers: Gianluca Zuccarelli
  - Update Konflux references (#3660)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - Update the list of known vulnerable packages (#3653)
    - Author: Florian Schüller, Reviewers: Gianluca Zuccarelli, Lukáš Zapletal
  - Wizard: Increase limit for Compliance policies in selector to 50 (#3679)
    - Author: Tomáš Koscielniak, Reviewers: Klara Simickova
  - Wizard: Update Satellite registration based on mocks (HMS-9414) (#3423)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli, Katarína Sieklová
  - Wizard: don't clear first boot systemd service (HMS-9306) (#3690)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  - Wizard: fix root not removable when duplicate (#3614)
    - Author: Anna Vítová, Reviewers: Michal Gold, Tomáš Koscielniak
  - Wizard: remove deprecated satellite flag (#3664)
    - Author: Anna Vítová, Reviewers: Gianluca Zuccarelli, Klara Simickova
  - build(deps): bump @redhat-cloud-services/frontend-components-notifications from 6.1.8 to 6.1.11 (#3686)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps): bump @redhat-cloud-services/frontend-components-utilities from 7.0.6 to 7.0.8 (#3685)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @types/node from 24.5.0 to 24.5.2 (#3678)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @types/uuid from 10.0.0 to 11.0.0 (#3671)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @vitejs/plugin-react from 5.0.2 to 5.0.3 (#3667)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump eslint from 9.34.0 to 9.36.0 (#3661)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump stylelint-config-recommended-scss from 16.0.0 to 16.0.1 (#3681)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - check-vulnerable-packages: show packages we have installed (#3654)
    - Author: Florian Schüller, Reviewers: Gianluca Zuccarelli
  - devDeps: Remove unused @types/uuid dependency (HMS-9431) (#3674)
    - Author: Klara Simickova, Reviewers: Anna Vítová
  - npm/deps-dev: Add fec dev-proxy to npm run start:stage (#3689)
    - Author: Tomáš Koscielniak, Reviewers: Gianluca Zuccarelli, Klara Simickova
  - src: Update API and remove Azure source ID from imagesTable (HMS-9424) (#3669)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  - test: Clean up mocked flags (#3663)
    - Author: Klara Simickova, Reviewers: Anna Vítová, Gianluca Zuccarelli
  - tests: Add integration test for Compliance - CIS policy (HMS-5964) (#3676)
    - Author: Tomáš Koscielniak, Reviewers: Gianluca Zuccarelli

— Somewhere on the Internet, 2025-10-01


* Wed Sep 17 2025 Packit <hello@packit.dev> - 77-1
Changes with 77
----------------
  - Fix filesystem and languages errors not renderring properly (#3623)
    - Author: Anna Vítová, Reviewers: Michal Gold
  - Wizard: clean up analytics to track image creation failure or success (HMS-9219) (#3604)
    - Author: Katarína Sieklová, Reviewers: Gianluca Zuccarelli, Sanne Raymaekers
  - build(deps): bump @redhat-cloud-services/frontend-components-utilities from 7.0.4 to 7.0.6 (#3645)
    - Author: dependabot[bot], Reviewers: Klara Simickova, Michal Gold
  - build(deps): bump @sentry/webpack-plugin from 4.2.0 to 4.3.0 (#3625)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @eslint/js from 9.32.0 to 9.35.0 (#3644)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @types/node from 24.3.0 to 24.5.0 (#3648)
    - Author: dependabot[bot], Reviewers: Gianluca Zuccarelli
  - build(deps-dev): bump globals from 16.3.0 to 16.4.0 (#3643)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - chore(deps): update konflux references (#3642)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - npm: check for vulnerable packages on each PR (#3639)
    - Author: Florian Schüller, Reviewers: Klara Simickova
  - src: Advanced partitioning scaffolding, import, edit (HMS-8963) (#3580)
    - Author: Klara Simickova, Reviewers: Katarína Sieklová

— Somewhere on the Internet, 2025-09-17


* Wed Sep 3 2025 Packit <hello@packit.dev> - 76-1
Changes with 76
----------------
  - Hooks: extract auth.getUser to its own hook (HMS-9085) (#3557)
    - Author: Gianluca Zuccarelli, Reviewers: Michal Gold, Sanne Raymaekers
  - Remove MSW browser (HMS-9225) (#3590)
    - Author: Klara Simickova, Reviewers: Katarína Sieklová
  - Wizard: Fix tenant/subscription ID population after source clear (HMS-9167) (#3570)
    - Author: Michal Gold, Reviewers: Klara Simickova
  - Wizard: Show package recommendations for RHEL 10 (#3566)
    - Author: Klara Simickova, Reviewers: Lukáš Zapletal
  - Wizard: add support for shared EPEL repos (HMS-5986) (#3548)
    - Author: Bryttanie, Reviewers: Klara Simickova
  - Wizard: give language and timezone default values (HMS-9182) (#3571)
    - Author: Katarína Sieklová, Reviewers: Klara Simickova, Michal Gold
  - Wizard: hide azure sources integration (HMS-9092) (#3579)
    - Author: Anna Vítová, Reviewers: Klara Simickova
  - build(deps): bump @redhat-cloud-services/frontend-components-utilities from 7.0.3 to 7.0.4 (#3586)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps): bump @redhat-cloud-services/types from 3.0.1 to 3.1.0 (#3600)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps): bump @sentry/webpack-plugin from 4.1.1 to 4.2.0 (#3597)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @babel/core from 7.28.0 to 7.28.3 (#3583)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @babel/preset-env from 7.28.0 to 7.28.3 (#3581)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @currents/playwright from 1.15.3 to 1.16.0 (#3561)
    - Author: dependabot[bot], Reviewers: Gianluca Zuccarelli
  - build(deps-dev): bump @testing-library/jest-dom from 6.6.4 to 6.8.0 (#3588)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @vitejs/plugin-react from 4.7.0 to 5.0.1 (#3560)
    - Author: dependabot[bot], Reviewers: Gianluca Zuccarelli
  - build(deps-dev): bump copy-webpack-plugin from 13.0.0 to 13.0.1 (#3601)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump mini-css-extract-plugin from 2.9.2 to 2.9.4 (#3576)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump msw from 2.10.5 to 2.11.1 (#3606)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump sass from 1.90.0 to 1.91.0 (#3585)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - chore(deps): update build-tools digest to 967d954 (#3603)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - chore(deps): update konflux references (#3594)
    - Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  - schutzbot/playwright_tests: halve workers on schutzbot (#3569)
    - Author: Sanne Raymaekers, Reviewers: Klara Simickova
  - tests/playwright: Add nightly action for Boot tests with Slack notification (#3582)
    - Author: Tomáš Koscielniak, Reviewers: Katarína Sieklová, Klara Simickova
  - tests/playwright: qcow2 boot test (HMS-8985) (#3525)
    - Author: Tomáš Koscielniak, Reviewers: Gianluca Zuccarelli, Sanne Raymaekers
  - tsconfig: Enable strict mode (HMS-9075) (#3546)
    - Author: Klara Simickova, Reviewers: Katarína Sieklová

— Somewhere on the Internet, 2025-09-03


* Thu Aug 21 2025 Packit <hello@packit.dev> - 75-1
Changes with 75
----------------
  - BlueprintCard: fix name truncation (HMS-9079) (#3556)
    - Author: Gianluca Zuccarelli, Reviewers: Sanne Raymaekers
  - Launch: implement guidance for Azure (HMS-9003) (#3549)
    - Author: Anna Vítová, Reviewers: Gianluca Zuccarelli
  - Wizard: on-prem aws region in edit (HMS-9096) (#3564)
    - Author: Gianluca Zuccarelli, Reviewers: Sanne Raymaekers
  - build(deps-dev): bump @types/node from 24.1.0 to 24.3.0 (#3553)
    - Author: dependabot[bot], Reviewers: Gianluca Zuccarelli
  - devDeps: Bump msw from 2.10.4 to 2.10.5 (HMS-9088) (#3559)
    - Author: Gianluca Zuccarelli, Reviewers: Michal Gold
  - plans: add gating tests (#3531)
    - Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli

— Somewhere on the Internet, 2025-08-21


* Wed Aug 20 2025 Packit <hello@packit.dev> - 74-1
Changes with 74
----------------
  - Launch: implement guidance for GCP (HMS-9004) (#3537)
    - Author: Anna Vítová, Reviewers: Klara Simickova
  - Wizard: Enable fips for OpenSCAP profile and compliance policy (HMS-8919) (#3501)
    - Author: Michal Gold, Reviewers: Gianluca Zuccarelli
  - Wizard: Fix lint warnings and snapshot button behaviour (HMS-9013) (#3511)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli, Michal Gold
  - Wizard: Update public cloud logo links (HMS-9009) (#3505)
    - Author: Klara Simickova, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli
  - build(deps): bump @redhat-cloud-services/frontend-components from 6.1.1 to 7.0.3 (#3514)
    - Author: dependabot[bot], Reviewers: Michal Gold
  - build(deps): bump @sentry/webpack-plugin from 4.1.0 to 4.1.1 (#3544)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump @patternfly/react-icons from 6.3.0 to 6.3.1 (#3512)
    - Author: dependabot[bot], Reviewers: Michal Gold
  - build(deps-dev): bump eslint from 9.32.0 to 9.33.0 (#3542)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump eslint-plugin-prettier from 5.5.3 to 5.5.4 (#3543)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump sass from 1.89.2 to 1.90.0 (#3508)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - build(deps-dev): bump typescript-eslint from 8.38.0 to 8.40.0 (#3551)
    - Author: dependabot[bot], Reviewers: Klara Simickova
  - chore(deps): update konflux references (#3538)
    - Author: red-hat-konflux[bot], Reviewers: Michal Gold
  - devDeps: Bump stylelint deps (HMS-9069) (#3535)
    - Author: Klara Simickova, Reviewers: Michal Gold
  - devDeps: Bump typescript deps (HMS-9068) (#3534)
    - Author: Klara Simickova, Reviewers: Michal Gold
  - devDeps: fix npm vulnerabilities (HMS-9010) (#3504)
    - Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  - src: Fix more lint warnings (HMS-9007) (#3503)
    - Author: Klara Simickova, Reviewers: Gianluca Zuccarelli

— Somewhere on the Internet, 2025-08-20


* Wed Aug 6 2025 Packit <hello@packit.dev> - 73-1
Changes with 73
----------------
  * ESLint: Set `no-unused-vars` rule to error (HMS-8923) (#3463)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli, Michal Gold
  * Move prettier config to ESLint config (HMS-8997) (#3495)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Refactor oscap (#3299)
    * Author: Anna Vítová, Reviewers: Gianluca Zuccarelli
  * Revert "playwright: Add duration to test account creation request (HMS-8958)" (#3489)
    * Author: Klara Simickova, Reviewers: Michal Gold
  * Update API (HMS-8938) (#3472)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli, Michal Gold
  * Wizard: Add FIPS state management infrastructure (HMS-8992) (#3490)
    * Author: Michal Gold, Reviewers: Klara Simickova
  * Wizard: Add fetch and error state for target environments (HMS-8941) (#3474)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Fix registration validation for Satellite on edit (HMS-8998) (#3498)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli, Michal Gold
  * Wizard: disable adding empty user tabs (HMS-8652) (#3300)
    * Author: Katarína Sieklová, Reviewers: Klara Simickova
  * api: remove pull command (#3454)
    * Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  * build(deps): bump @patternfly/react-code-editor from 6.1.0 to 6.3.0 (#3458)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @patternfly/react-core from 6.1.0 to 6.3.0 (#3473)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @patternfly/react-table from 6.3.0 to 6.3.1 (#3500)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @redhat-cloud-services/frontend-components from 6.1.0 to 6.1.1 (#3464)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @redhat-cloud-services/frontend-components-notifications from 6.1.0 to 6.1.1 (#3470)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @redhat-cloud-services/frontend-components-notifications from 6.1.1 to 6.1.3 (#3497)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @redhat-cloud-services/frontend-components-utilities from 6.1.0 to 6.1.1 (#3478)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @sentry/webpack-plugin from 3.6.1 to 4.0.0 (#3453)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @sentry/webpack-plugin from 4.0.0 to 4.0.1 (#3465)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @sentry/webpack-plugin from 4.0.1 to 4.0.2 (#3482)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @unleash/proxy-client-react from 5.0.0 to 5.0.1 (#3471)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump axios from 1.10.0 to 1.11.0 (#3457)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @currents/playwright from 1.15.2 to 1.15.3 (#3492)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @eslint/js from 9.31.0 to 9.32.0 (#3496)
    * Author: dependabot[bot], Reviewers: Gianluca Zuccarelli
  * build(deps-dev): bump @patternfly/react-icons from 6.1.0 to 6.3.0 (#3461)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @testing-library/dom from 10.4.0 to 10.4.1 (#3476)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @types/node from 24.0.13 to 24.1.0 (#3460)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump eslint from 9.30.1 to 9.32.0 (#3484)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump eslint-plugin-playwright from 2.2.0 to 2.2.1 (#3466)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump eslint-plugin-playwright from 2.2.1 to 2.2.2 (#3491)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump eslint-plugin-testing-library from 7.6.0 to 7.6.3 (#3483)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump stylelint from 16.22.0 to 16.23.0 (#3493)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * on-prem: enable building & uploading AWS images (HMS-5823) (#3055)
    * Author: Gianluca Zuccarelli, Reviewers: Sanne Raymaekers
  * playwright: Add duration to test account creation request (HMS-8958) (#3485)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * playwright: Update required Oscap packages (#3488)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli

— Somewhere on the Internet, 2025-08-06


* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

# the changelog is distribution-specific, therefore there's just one entry
# to make rpmlint happy.

* Wed Jul 23 2025 Packit <hello@packit.dev> - 72-1
Changes with 72
----------------
  * CreateImageWizard: Implement user-friendly error messages (HMS-8704) (#3219)
    * Author: Florian Schüller, Reviewers: Klara Simickova
  * ESLint: Deduplicate imports and sort within import groups (HMS-8809) (#3407)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Migrate ESLint to v 9.x (HMS-6277) (#3405)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Fix stuck page for package search (HMS-8863) (#3439)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Make the blueprint name unclickable after filtering (#3438)
    * Author: Katarína Sieklová, Reviewers: Klara Simickova
  * Wizard: Move org ID into a copy-able field (HMS-8821) (#3421)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Update activation keys dropdown (HMS-8825) (#3427)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * build(deps): bump @patternfly/patternfly from 6.1.0 to 6.3.0 (#3451)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @patternfly/react-table from 6.1.0 to 6.3.0 (#3452)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @sentry/webpack-plugin from 3.5.0 to 3.6.1 (#3444)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump form-data from 4.0.1 to 4.0.4 (#3450)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump on-headers and compression (#3440)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @currents/playwright from 1.14.1 to 1.15.1 (#3415)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @redhat-cloud-services/tsc-transform-imports from 1.0.24 to 1.0.25 (#3414)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/parser from 8.36.0 to 8.37.0 (#3441)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @vitejs/plugin-react from 4.6.0 to 4.7.0 (#3445)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump eslint-plugin-import from 2.31.0 to 2.32.0 (#3410)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump eslint-plugin-testing-library from 7.5.3 to 7.5.4 (#3413)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump eslint-plugin-testing-library from 7.5.4 to 7.6.0 (#3432)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump stylelint from 16.21.1 to 16.22.0 (#3446)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * chore(deps): update konflux references (#3416)
    * Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  * chore(deps): update konflux references (#3443)
    * Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  * devDeps: Bump msw from 2.10.2 to 2.10.3 (#3411)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * devDeps: Bump msw from 2.10.3 to 2.10.4 (HMS-8864) (#3435)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * devDeps: Bump typecript deps (HMS-8881) (#3449)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * on-prem: cloud provider config modal (COMPOSER-2488) (#3103)
    * Author: Gianluca Zuccarelli, Reviewers: Nobody
  * src: Fix status text color (HMS-8865) (#3442)
    * Author: Klara Simickova, Reviewers: Simon Steinbeiß
  * src: Remove more `data-testid`s (HMS-6151) (#3204)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli

— Somewhere on the Internet, 2025-07-23


* Wed Jul 9 2025 Packit <hello@packit.dev> - 71-1
Changes with 71
----------------
  * Remove IQE scripts and configs (HMS-8779) (#3395)
    * Author: Klara Simickova, Reviewers: Tomáš Koscielniak
  * Remove devel dockerfile and update README (HMS-8780) (#3396)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Remove the Edge Management federated module (HMS-8637) (#3296)
    * Author: Simon Steinbeiß, Reviewers: Klara Simickova
  * Update Konflux references (#3374)
    * Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  * Wizard: Fix package search bug with RH repos in template (#3321)
    * Author: Dominik Vágner, Reviewers: Klara Simickova
  * Wizard: Hide FSC step for WSL targets (HMS-8758) (#3380)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Hide Kernel step for WSL (HMS-8759) (#3389)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Parse locale codes to readable options (HMS-8577) (#3259)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Remove repository column from packages table (HMS-8701) (#3339)
    * Author: Klara Simickova, Reviewers: Anna Vítová
  * Wizard: Render labels for all FSC table columns (#3379)
    * Author: Klara Simickova, Reviewers: Simon Steinbeiß
  * Wizard: Replace VMware radios with checkboxes (HMS-8778) (#3393)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Replace deprecated Modals with non-deprecated ones (HMS-8691) (#3325)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Show error with duplicated values (HMS-6306) (#3368)
    * Author: Klara Simickova, Reviewers: Katarína Sieklová
  * api: Update pull.sh, regenerate schemas and fix errors (HMS-8720) (#3331)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * build(deps): bump @redhat-cloud-services/frontend-components-notifications from 5.0.4 to 6.1.0 (#3382)
    * Author: dependabot[bot], Reviewers: Gianluca Zuccarelli
  * build(deps-dev): bump @babel/core from 7.27.4 to 7.27.7 (#3384)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @babel/core from 7.27.7 to 7.28.0 (#3401)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @babel/preset-env from 7.27.2 to 7.28.0 (#3400)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/eslint-plugin from 8.35.1 to 8.36.0 (#3404)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/parser from 8.35.1 to 8.36.0 (#3403)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @vitejs/plugin-react from 4.4.1 to 4.6.0 (#3361)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump stylelint from 16.18.0 to 16.21.0 (#3376)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump stylelint from 16.21.0 to 16.21.1 (#3402)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * chore(deps): update konflux references (#3399)
    * Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  * cockpit/README.md: initial version (#3367)
    * Author: Florian Schüller, Reviewers: Gianluca Zuccarelli
  * split out dev checks (HMS-8754) (#3372)
    * Author: Gianluca Zuccarelli, Reviewers: Klara Simickova
  * test: Add mock handler for `repository_parameters` (HMS-8721) (#3349)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli

— Somewhere on the Internet, 2025-07-09


* Wed Jun 11 2025 Packit <hello@packit.dev> - 69-1
Changes with 69
----------------
  * Fix makefile (#3289)
    * Author: Anna Vítová, Reviewers: Gianluca Zuccarelli
  * Remove elses after return (#3295)
    * Author: Anna Vítová, Reviewers: Katarína Sieklová
  * Wizard: fix filtering of Timezone (HMS-8631) (#3282)
    * Author: Katarína Sieklová, Reviewers: Anna Vítová
  * Wizard: switch tiles to cards (HMS-8623) (#3281)
    * Author: Gianluca Zuccarelli, Reviewers: Anna Vítová
  * build(deps): bump @sentry/webpack-plugin from 3.4.0 to 3.5.0 (#3278)
    * Author: dependabot[bot], Reviewers: Anna Vítová
  * src: PF6 migration (HMS-8570) (#3078)
    * Author: Klara Simickova, Reviewers: Katarína Sieklová, Lucas Garfield

— Somewhere on the Internet, 2025-06-11


* Wed May 28 2025 Packit <hello@packit.dev> - 68-1
Changes with 68
----------------
  * API: update api (#3245)
    * Author: Lucas Garfield, Reviewers: Nobody
  * Add el10 releases (#3238)
    * Author: Sanne Raymaekers, Reviewers: Lucas Garfield
  * LandingPage: Add Users to `NewAlert` (#3237)
    * Author: Klara Simickova, Reviewers: Simon Steinbeiß
  * Satellite: Add instructions for obtaining certificate + token expiration info (#3224)
    * Author: Anna Vítová, Reviewers: Klara Simickova
  * Update Konflux references (#3250)
    * Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  * Wizard: Fix vertical height bug (#3234)
    * Author: Lucas Garfield, Reviewers: Klara Simickova, Simon Steinbeiß
  * Wizard: encode satellite cmd properly (#3221)
    * Author: Lukáš Zapletal, Reviewers: Anna Vítová
  * Wizard: fix blueprints showing incorrect template versions (#3271)
    * Author: Bryttanie, Reviewers: Klara Simickova
  * Wizard: fix token not having expiration fails (#3244)
    * Author: Anna Vítová, Reviewers: Klara Simickova
  * build(deps-dev): bump @babel/preset-env from 7.27.1 to 7.27.2 (#3241)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build: add testing proxy to playwright CI (#3257)
    * Author: Dominik Vágner, Reviewers: Klara Simickova
  * devDeps: Manually bump @currents/playwright to 1.13.2 (HMS-8600) (#3260)
    * Author: Klara Simickova, Reviewers: Tomáš Koscielniak
  * src: Fix user groups validation on import (HMS-6279) (#3215)
    * Author: Klara Simickova, Reviewers: Anna Vítová
  * support fedora 42 (HMS-6153) (#3205)
    * Author: Sanne Raymaekers, Reviewers: Klara Simickova
  * tsconfig: Specify `include` (HMS-8601) (#3209)
    * Author: Klara Simickova, Reviewers: Anna Vítová

— Somewhere on the Internet, 2025-05-28


* Wed Apr 16 2025 Packit <hello@packit.dev> - 65-1
Changes with 65
----------------
  * .github: new stage user on each playwright run (HMS-5956) (#3098)
    * Author: Sanne Raymaekers, Reviewers: Tomáš Koscielniak
  * Fedora-services: add support for fedora env (#2984)
    * Author: Amir Fefer, Reviewers: Klara Simickova
  * ImagesTable: Fix AWS regions indicator (off by one) (#3094)
    * Author: Simon Steinbeiß, Reviewers: Klara Simickova
  * Playwright: Add customizations test template and refactor (HMS-5942) (#3050)
    * Author: Tomáš Koscielniak, Reviewers: Nobody
  * Promote WSL to production stable (HMS-5950) (#3092)
    * Author: Simon Steinbeiß, Reviewers: Klara Simickova
  * Satellite registration followup (#3072)
    * Author: Anna Vítová, Reviewers: Klara Simickova
  * Update Konflux references (#3100)
    * Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  * Wizard: Replace deprecated select in OpenSCAP step (HMS-5671) (#3059)
    * Author: Klara Simickova, Reviewers: Katarína Sieklová
  * Wizard: Switch from deprecated select in `ActivationKeys` (HMS-5620) (#2970)
    * Author: Klara Simickova, Reviewers: Katarína Sieklová
  * Wizard: Update microcopy on Locale step (HMS-5656) (#3064)
    * Author: Klara Simickova, Reviewers: Katarína Sieklová
  * Wizard: add segment tracking to buttons in wizard footer (HMS-5977) (#3104)
    * Author: Katarína Sieklová, Reviewers: Klara Simickova
  * Wizard: make optional steps clickable on prem (HMS-5852) (#3066)
    * Author: Katarína Sieklová, Reviewers: Klara Simickova, Tomáš Koscielniak
  * build(deps): bump @babel/runtime from 7.26.0 to 7.27.0 (#3102)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @sentry/webpack-plugin from 3.2.2 to 3.3.1 (#3113)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @unleash/proxy-client-react from 4.5.2 to 5.0.0 (#3070)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @currents/playwright from 1.11.4 to 1.12.0 (#3077)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/eslint-plugin from 8.29.0 to 8.29.1 (#3091)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/eslint-plugin from 8.29.1 to 8.30.1 (#3105)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump jsdom from 26.0.0 to 26.1.0 (#3101)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump typescript from 5.8.2 to 5.8.3 (#3085)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * devDeps: Bump vitest deps (HMS-5928) (#3074)
    * Author: Klara Simickova, Reviewers: Lucas Garfield

— Somewhere on the Internet, 2025-04-16


* Wed Mar 5 2025 Packit <hello@packit.dev> - 62-1
Changes with 62
----------------
  * Blueprints: Import Blueprint modal error rendering (HMS-5528) (#2918)
    * Author: Katarína Sieklová, Reviewers: Klara Simickova
  * Blueprints: invalid message variant on upload (HMS-5555) (#2931)
    * Author: Katarína Sieklová, Reviewers: Klara Simickova
  * Fix trigger-gitlab workflow (#2930)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * Update Konflux references (#2951)
    * Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  * Wizard: Remove first boot script from services when no script (HMS-5481) (#2871)
    * Author: Klara Simickova, Reviewers: Lucas Garfield
  * Wizard: fix indentation of manual file system config (HMS-5564) (#2943)
    * Author: Katarína Sieklová, Reviewers: Klara Simickova
  * build(deps): bump @sentry/webpack-plugin from 3.1.2 to 3.2.0 (HMS-5543) (#2920)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump @unleash/proxy-client-react from 4.5.1 to 4.5.2 (#2933)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/eslint-plugin from 8.24.0 to 8.24.1 (HMS-5546) (#2926)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/eslint-plugin from 8.24.1 to 8.26.0 (#2962)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/parser from 8.24.0 to 8.24.1 (HMS-5544) (#2921)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/parser from 8.24.1 to 8.25.0 (#2945)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump uuid from 11.0.5 to 11.1.0 (#2939)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * deps: Bump @redhat-cloud-services/frontend-components from 4.2.22 to 5.2.6 (HMS-5495) (#2890)
    * Author: Klara Simickova, Reviewers: Florian Schüller

— Somewhere on the Internet, 2025-03-05


* Tue Feb 11 2025 Packit <hello@packit.dev> - 60-1
Changes with 60
----------------
  * CreateImageWizard: default to major releases on prem (#2879)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * Update Konflux references (#2866)
    * Author: red-hat-konflux[bot], Reviewers: Klara Simickova
  * Wizard: Gate services on OpenSCAP step behind flag (HMS-5406) (#2808)
    * Author: Klara Simickova, Reviewers: Michal Gold
  * build(deps): bump @redhat-cloud-services/frontend-components-notifications from 4.1.1 to 4.1.16 (HMS-5482) (#2876)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @babel/core from 7.26.0 to 7.26.8 (HMS-5483) (#2875)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @babel/preset-env from 7.26.0 to 7.26.8 (HMS-5485) (#2869)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/eslint-plugin from 8.21.0 to 8.24.0 (HMS-5484) (#2874)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * dependabot: Increase limit of opened pull requests (HMS-5486) (#2867)
    * Author: Klara Simickova, Reviewers: Michal Gold

— Somewhere on the Internet, 2025-02-11


* Fri Feb 7 2025 Packit <hello@packit.dev> - 59-1
Changes with 59
----------------
  * cockpit/spec: add obsoletes & fix release workflow (#2863)
    * Author: Sanne Raymaekers, Reviewers: Nobody

— Somewhere on the Internet, 2025-02-07


* Fri Feb 7 2025 Packit <hello@packit.dev> - 58-1
Changes with 58
----------------
  * api: add composer's cloudapi (HMS-5465) (#2855)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * cockpit plugin: enable all customizations and implement updating blueprints (HMS-5459) (#2848)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli, Klara Simickova
  * cockpit: add basic test for the images table (#2814)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli, Klara Simickova
  * devDeps: Manually bump vitest (HMS-5373) (#2784)
    * Author: Klara Simickova, Reviewers: Sanne Raymaekers
  * test: test hostname step on cockpit (#2861)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli

— Somewhere on the Internet, 2025-02-07


* Fri Jan 31 2025 Packit <hello@packit.dev> - v55-1
Changes with 55
----------------
  * .github/workflows/release: fix make dist step (#2771)
    * Author: Sanne Raymaekers, Reviewers: Klara Simickova
  * .github/workflows/release: fix release workflow 2      (#2822)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * .github/workflows/release: make sure GH_TOKEN is set for upload (#2824)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * .github/workflows/release: work around git clean (#2823)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * Build images with cockpit (HMS-5417) (#2787)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * Cockpit release improvements (#2768)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * ESLint: Disable autofix for "no-unnecessary-condition" (HMS-5374) (#2772)
    * Author: Klara Simickova, Reviewers: Sanne Raymaekers
  * ESLint: Set "no-unnecessary-condition" rule to error (#2755)
    * Author: Klara Simickova, Reviewers: Lucas Garfield
  * Fix release workflow (#2821)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * LandingPage: Hide NewAlert (HMS-5295) (#2731)
    * Author: Klara Simickova, Reviewers: Sanne Raymaekers
  * Use cockpit-files for local targets (HMS-5422) (#2820)
    * Author: Sanne Raymaekers, Reviewers: Gianluca Zuccarelli
  * Wizard: Add Kernel name input (HMS-5204) (#2690)
    * Author: Klara Simickova, Reviewers: Sanne Raymaekers
  * Wizard: Add kernel append input (HMS-5299) (#2734)
    * Author: Klara Simickova, Reviewers: Gianluca Zuccarelli
  * Wizard: Firewall ports input (HMS-5332) (#2750)
    * Author: Klara Simickova, Reviewers: Lucas Garfield
  * Wizard: Fix repo status formatting (HMS-5346) (#2761)
    * Author: Klara Simickova, Reviewers: Lucas Garfield
  * Wizard: Reset error text and validate on plus button (HMS-5329) (#2747)
    * Author: Klara Simickova, Reviewers: Michal Gold, Sanne Raymaekers
  * build(deps): bump @sentry/webpack-plugin from 2.22.7 to 3.0.0 (HMS-5344) (#2753)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps): bump vite from 5.4.11 to 5.4.14 (HMS-5367) (#2781)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/eslint-plugin from 8.18.1 to 8.20.0 (HMS-5351) (#2765)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * build(deps-dev): bump @typescript-eslint/eslint-plugin from 8.20.0 to 8.21.0 (#2790)
    * Author: dependabot[bot], Reviewers: Klara Simickova
  * cockpit/spec: post-release version bump (#2757)
    * Author: Sanne Raymaekers, Reviewers: Achilleas Koutsou
  * cockpit: make `CreateImageWizard` functional (HMS-5408) (#2780)
    * Author: Gianluca Zuccarelli, Reviewers: Sanne Raymaekers
  * on-prem add blueprint pagination and fix filtering (HMS-5306) (#2739)
    * Author: Gianluca Zuccarelli, Reviewers: Lucas Garfield
  * on-prem: add ability to delete blueprints (HMS-5224) (#2704)
    * Author: Gianluca Zuccarelli, Reviewers: Lucas Garfield
  * on-prem: cockpit create image wizard (HMS-5301) (#2735)
    * Author: Gianluca Zuccarelli, Reviewers: Sanne Raymaekers
  * src: Fix "no-unnecessary-condition" issues (HMS-5355) (#2760)
    * Author: Klara Simickova, Reviewers: Lucas Garfield
  * validators: Remove undefined where only string value expected (HMS-5354) (#2754)
    * Author: Klara Simickova, Reviewers: Michal Gold
  * wizard: add Administrator checkbox to users step (HMS-4903) (#2717)
    * Author: Michal Gold, Reviewers: Klara Simickova
  * wizard: add support of TextArea for ssh_key field (HMS-5304) (#2737)
    * Author: Michal Gold, Reviewers: Lucas Garfield
  * wizard: add user name validation (HMS-5285) (#2716)
    * Author: Michal Gold, Reviewers: Klara Simickova, Sanne Raymaekers

— Somewhere on the Internet, 2025-01-31


* Thu Jan 16 2025 Packit <hello@packit.dev> - v54-1
Initial release of cockpit-image-builder, bringing image-builder-frontend to cockpit! 

* Mon Jan 13 2025 Image Builder team <osbuilders@redhat.com> - 0-1
- The changelog was added to the rpm spec file.
