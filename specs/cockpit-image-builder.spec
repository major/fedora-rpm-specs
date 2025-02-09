Name:           cockpit-image-builder
Version:        59
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
