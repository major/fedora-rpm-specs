Name: subscription-manager-cockpit
Version: 7
Release: 2%{?dist}
Summary: Subscription Manager Cockpit UI
%if 0%{?suse_version}
Group: System Environment/Base
License: LGPLv2
%else
License: LGPL-2.1-or-later
%endif
URL: https://www.candlepinproject.org/

Source0: %{name}-%{version}.tar.xz
Source1: %{name}-node-%{version}.tar.xz
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
%if 0%{?fedora}
BuildRequires: nodejs-devel
%endif
BuildRequires: nodejs
BuildRequires: make
BuildRequires: libappstream-glib
BuildRequires: gettext
BuildRequires: desktop-file-utils
%if 0%{?rhel} && 0%{?rhel} <= 8
BuildRequires: libappstream-glib-devel
%endif

Requires: subscription-manager
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: rhsm-icons
%if %{defined rhel} && %{undefined centos}
Suggests: insights-client
%endif

%description
Subscription Manager Cockpit UI

%package -n rhsm-icons
Summary: Icons for Red Hat Subscription Management client tools

# As these two packages previously contained the icons now contained in
# rhsm-icons package, we need to specify the logical complement to a
# "Requires", which is "Conflicts". With any luck the underlying
# depsolver will cause the removal of this package if the request
# is to downgrade either of the following to a version below these
# requirements.
Conflicts: rhsm-gtk < 1.26.7
Conflicts: subscription-manager-cockpit < 1.26.7

%description -n rhsm-icons
This package contains the desktop icons for the graphical interfaces provided for management
of Red Hat subscriptions: subscription-manager-gui, subscription-manager-cockpit-plugin.

%prep
%autosetup -n %{name} -a 1
# ignore pre-built webpack in release tarball and rebuild it
rm -rf dist

%build
ESLINT=0 NODE_ENV=production make

%install
%make_install PREFIX=/usr

# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*
desktop-file-validate %{buildroot}/%{_datadir}/applications/*

# this can't be meaningfully tested during package build

%files
%license LICENSE
%dir %{_datadir}/cockpit/subscription-manager
%{_datadir}/applications/*
%{_datadir}/cockpit/subscription-manager/*
%{_datadir}/metainfo/*

%files -n rhsm-icons
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/symbolic/apps/*.svg

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Pino Toscano <ptoscano@redhat.com> 7-1
- Translated using Weblate (Italian) (info@salvatorecocuzza.it)
- Translated using Weblate (Finnish) (ricky.tigg@gmail.com)
- Translated using Weblate (Finnish) (noreply-mt-weblate-translation-
  memory@weblate.org)
- Translated using Weblate (Finnish) (jiri.gronroos@iki.fi)
- Translated using Weblate (French) (leane.grasser@proton.me)
- test: drop no more used machine_python() helper function
  (ptoscano@redhat.com)
- test: use a simpler way to append content to a file (ptoscano@redhat.com)
- test: use f-strings to replace other string formattings (ptoscano@redhat.com)
- test: use curl directly to wait for Candlepin (ptoscano@redhat.com)
- test: drop extra activation key code (ptoscano@redhat.com)
- test: upload product certificates to /etc/pki/product-default
  (ptoscano@redhat.com)
- test: use onlyImage() from cockpit test lib (ptoscano@redhat.com)
- Makefile: fix names of po extractor tools (ptoscano@redhat.com)
- fix: Drop deprecated cockpit.resolve() (martin@piware.de)
- Bump cockpit testlib to 327 (martin@piware.de)
- fix: adapt to the new state of insights-client.service on failure
  (ptoscano@redhat.com)
- Update cockpit test lib to 323 (ptoscano@redhat.com)
- test: switch one more org to SCA one (ptoscano@redhat.com)
- test: Use SCA to register (mhorky@redhat.com)
- fix: switch to the proper URL for Red Hat's Hybrid Cloud Console
  (ptoscano@redhat.com)
- test: setup the subscription repositories (ptoscano@redhat.com)
- test: mock-insights: switch away from ssl.wrap_socket() (ptoscano@redhat.com)
- test: switch to CERT auth for insights-client (ptoscano@redhat.com)
- chore: ignore node_modules for flake8 (ptoscano@redhat.com)
- test: mock-insights: implement upload and delete platform endpoints
  (ptoscano@redhat.com)
- test: mock-insights: fix/improve handling of IDs (ptoscano@redhat.com)
- test: mock-insights: refactor of two platform endpoints (ptoscano@redhat.com)
- feat: switch from .last-upload.results to .lastupload (ptoscano@redhat.com)
- fix: Remove Auto-attach button (jhnidek@redhat.com)
- chore: test: use the new syspurpose command (ptoscano@redhat.com)
- Translated using Weblate (Russian) (aleksejfedorov963@gmail.com)
- Translated using Weblate (Georgian) (temuri.doghonadze@gmail.com)
- Translated using Weblate (Korean) (simmon@nplob.com)
- Translated using Weblate (Italian) (toscano.pino@tiscali.it)
- chore: bump version of black to 24.3.0 (ptoscano@redhat.com)
- test: wait more when registering to Insights (ptoscano@redhat.com)
- test: break insights-client in a different way (ptoscano@redhat.com)
- test: mock-insights: return 404 for missing systems in /systems
  (ptoscano@redhat.com)
- test: wait longer in certain situations (ptoscano@redhat.com)
- Fix obsolete cockpit defer API (martin@piware.de)
- ci: bump actions/checkout from 3 to 4
  (49699333+dependabot[bot]@users.noreply.github.com)
- ci: add dependabot config for GitHub Actions (ptoscano@redhat.com)
- spec: convert License to SPDX (ptoscano@redhat.com)
- Update cockpit test lib and webpack build (martin@piware.de)
- Use proper imports (martin@piware.de)
- flake8: update/improve the config (ptoscano@redhat.com)
- test: split/wrap overly long strings (ptoscano@redhat.com)
- test: minor comment updates (ptoscano@redhat.com)
- test: format embedded Python snippets with black==23.3.0
  (ptoscano@redhat.com)
- test: assume /root/run-candlepin to start candlepin (ptoscano@redhat.com)
- test: drop bits for rhel-8-5 (ptoscano@redhat.com)
- Use 'type' instead of 'which' which is standard unix (kkoukiou@redhat.com)
- Format code with black==23.3.0 (ptoscano@redhat.com)
- Update black to version 23.3.0 (ptoscano@redhat.com)
- Fix usage of exception state (mmarusak@redhat.com)
- Drop usage of obsolete cockpit.defer() (martin@piware.de)
- Fix getSyspurposeStatus to not return an ever-pending promise
  (martin@piware.de)
- Makefile: Fix "make watch" to work from a clean tree (martin@piware.de)
- build: use `pip wheel` to get cockpit wheel (allison.karlitskaya@redhat.com)
- Set autocomplete to "current-password" for password inputs
  (jhnidek@redhat.com)
- Run `npm install` with `--ignore-scripts` (mpitt@redhat.com)
- README: document development dependencies for Fedora/Ubuntu
  (jvanderwaa@redhat.com)
- Install into /usr/local/ by default (martin@piware.de)
- Makefile: Some noise cleanup (martin@piware.de)
- build: use translation tools from pkg/lib (martin@piware.de)
- Makefile: Drop update-po rule (martin@piware.de)
- Start using cockpit-po-plugin instead of Po2Json (kkoukiou@redhat.com)
- Add support for dark theme (kkoukiou@redhat.com)
- Bump up pkg/lib reference tag (kkoukiou@redhat.com)
- Bump up patternfly (kkoukiou@redhat.com)
- Bump up react version and start using new client API (kkoukiou@redhat.com)
- node_modules: Update chrome-remote-interface to 0.32 (martin@piware.de)
- Makefile: Add support for /pybridge scenario (martin@piware.de)

* Mon Feb 20 2023 Pino Toscano <ptoscano@redhat.com> 6-1
- Translated using Weblate (Kannada) (jsefler@redhat.com)
- Translated using Weblate (Georgian) (temuri.doghonadze@gmail.com)
- 2169976: insights: fix spawn_error_to_string in more cases
  (ptoscano@redhat.com)

* Fri Jan 06 2023 Pino Toscano <ptoscano@redhat.com> 5-1
- Translated using Weblate (French) (vincent.lefebvre59@gmail.com)
- Translated using Weblate (Korean) (simmon@nplob.com)
- Translated using Weblate (Georgian) (temuri.doghonadze@gmail.com)
- 2077759: invoke cockpit.translate() after document loading
  (ptoscano@redhat.com)
- test: Drop outdated copy of packagelib.py (martin@piware.de)
- Added missing keys to react components (jhnidek@redhat.com)
- Fix the issue, when it is not possible to install insights-client
  (jhnidek@redhat.com)
- test: Sync packagelib.py with cockpit main (martin@piware.de)
- New target and added one project directory to .gitignore (jhnidek@redhat.com)

* Wed Jul 27 2022 Jiri Hnidek <jhnidek@redhat.com> 4-1

* Tue Jul 26 2022 Jiri Hnidek <jhnidek@redhat.com> 3-1
- Translated using Weblate (Korean) (simmon@nplob.com)
- test: drop unused reference-image file (ptoscano@redhat.com)
- Drop the static npm-shrinkwrap.json (ptoscano@redhat.com)
- Bump cockpit test API to 273 + run-tests scheduler fix (martin@piware.de)
- spec: suggest insights-client on RHEL (ptoscano@redhat.com)
- tito: remove autogenerated spec file before tagging (ptoscano@redhat.com)

* Fri Jun 24 2022 Jiri Hnidek <jhnidek@redhat.com> 2-1
- New package built with tito
- New pattern of versioning. Starting version is 2

