Name:           cockpit-image-builder
Version:        68
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
BuildRequires:  nodejs

Requires:       cockpit
Requires:       cockpit-files
Requires:       osbuild-composer >= 131

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
# the changelog is distribution-specific, therefore there's just one entry
# to make rpmlint happy.

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
