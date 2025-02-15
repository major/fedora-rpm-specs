#
# Copyright (C) 2017-2020 Red Hat, Inc.
#
# Cockpit is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or
# (at your option) any later version.
#
# Cockpit is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Cockpit; If not, see <http://www.gnu.org/licenses/>.
#

Name:           cockpit-podman
Version:        101
Release:        1%{?dist}
Summary:        Cockpit component for Podman containers
License:        LGPL-2.1-or-later
URL:            https://github.com/cockpit-project/cockpit-podman

Source0:        https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
%if 0%{?suse_version}
# Suse's package has a different name
BuildRequires:  appstream-glib
%else
BuildRequires:  libappstream-glib
%endif
BuildRequires:  make
BuildRequires: gettext
%if 0%{?rhel} && 0%{?rhel} <= 8
BuildRequires: libappstream-glib-devel
%endif

Requires:       cockpit-bridge
Requires:       podman >= 2.0.4
# HACK https://github.com/containers/crun/issues/1091
%if 0%{?centos} == 9
Requires:       criu-libs
%elif 0%{?suse_version}
Requires:       libcriu2
%endif

Provides: bundled(npm(@patternfly/patternfly)) = 5.4.2
Provides: bundled(npm(@patternfly/react-core)) = 5.4.12
Provides: bundled(npm(@patternfly/react-icons)) = 5.4.2
Provides: bundled(npm(@patternfly/react-styles)) = 5.4.1
Provides: bundled(npm(@patternfly/react-table)) = 5.4.14
Provides: bundled(npm(@patternfly/react-tokens)) = 5.4.1
Provides: bundled(npm(@xterm/addon-canvas)) = 0.7.0
Provides: bundled(npm(@xterm/xterm)) = 5.5.0
Provides: bundled(npm(attr-accept)) = 2.2.5
Provides: bundled(npm(docker-names)) = 1.2.1
Provides: bundled(npm(file-selector)) = 2.1.2
Provides: bundled(npm(focus-trap)) = 7.6.2
Provides: bundled(npm(ipaddr.js)) = 2.2.0
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(react-dropzone)) = 14.3.5
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.2.0
Provides: bundled(npm(throttle-debounce)) = 5.0.2
Provides: bundled(npm(tslib)) = 2.8.1

%description
The Cockpit user interface for Podman containers.

%prep
%setup -q -n %{name}

%build
# Nothing to build

%install
%make_install PREFIX=/usr
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc README.md
%license LICENSE dist/index.js.LEGAL.txt dist/index.css.LEGAL.txt
%{_datadir}/cockpit/*
%{_datadir}/metainfo/*

%changelog
* Thu Feb 13 2025 Packit <hello@packit.dev> - 101-1
- automatically start podman.socket

* Wed Jan 29 2025 Packit <hello@packit.dev> - 100-1
- Automatically start podman.socket
- Identify quadlets by a 'service' label

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 20 2024 Packit <hello@packit.dev> - 99-1
- Update to translations

* Wed Nov 06 2024 Packit <hello@packit.dev> - 98-1
- Bug fixes and translation updates

* Wed Oct 23 2024 Packit <hello@packit.dev> - 97-1
- Bug fixes and translation updates

* Wed Oct 09 2024 Packit <hello@packit.dev> - 96-1
- pull images from registries without search API

* Wed Sep 25 2024 Packit <hello@packit.dev> - 95-1
- Bug fixes and translation updates

* Wed Sep 04 2024 Packit <hello@packit.dev> - 94-1
- Render ports are ranges in container integration tab

* Thu Aug 22 2024 Packit <hello@packit.dev> - 93-1
- Bug fixes and translation updates

* Thu Aug 08 2024 Packit <hello@packit.dev> - 92-1
- Bug fixes

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Packit <hello@packit.dev> - 91-1
- Bug fixes and performance improvements

* Wed Jun 26 2024 Packit <hello@packit.dev> - 90-1
- Implement pull option for existing images

* Wed Jun 05 2024 Packit <hello@packit.dev> - 89-1
- Use binary http channel for podman socket for non-UTF-8 robustness
- Stop using obsolete cockpit.utf8_{de,en}coder() API
- Fix tests for CentOS/RHEL 10

* Wed May 29 2024 Packit <hello@packit.dev> - 88-1
- Translation updates

* Thu Apr 25 2024 Packit <hello@packit.dev> - 87-1
- Bug fixes and performance improvements

* Wed Mar 27 2024 Packit <hello@packit.dev> - 86-1
- Bug fixes and performance improvements

* Wed Mar 13 2024 Packit <hello@packit.dev> - 85-1
- "bug fixes & performance improvements"

* Tue Feb 20 2024 Packit <hello@packit.dev> - 84.1-1
- Translation updates (RHEL-25556/RHEL-25557)

* Wed Feb 14 2024 Packit <hello@packit.dev> - 84-1
- Bug fixes and stability improvements

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Packit <hello@packit.dev> - 83-1
- bug fixes and library updates

* Wed Nov 29 2023 Packit <hello@packit.dev> - 82-1
- Delete intermediate images

* Wed Nov 15 2023 Packit <hello@packit.dev> - 81-1
- Performance and stability improvements

* Wed Nov 01 2023 Packit <hello@packit.dev> - 80-1
- Performance and stability improvements

* Wed Oct 18 2023 Packit <hello@packit.dev> - 79-1
- Validate fields in "Create container" dialog

* Thu Oct 05 2023 Packit <hello@packit.dev> - 78-1
- Label Toolbox and Distrobox containers

* Wed Sep 20 2023 Packit <hello@packit.dev> - 77-1
- Performance and stability improvements

* Wed Sep 06 2023 Packit <hello@packit.dev> - 76-1
- Performance and stability improvements

* Wed Aug 23 2023 Packit <hello@packit.dev> - 75-1
- Performance and stability improvements

* Wed Aug 09 2023 Packit <hello@packit.dev> - 74-1
- PatternFly 5
- Bug fixes and translation updates

* Wed Jul 26 2023 Packit <hello@packit.dev> - 73-1
- show time of container's latest checkpoint

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Packit <hello@packit.dev> - 72-1
- Bug fixes and translation updates

* Sat Jun 17 2023 Packit <hello@packit.dev> - 71-1
- Add manifest condition for the Python bridge

* Thu Jun 01 2023 Packit <hello@packit.dev> - 70-1
- Add ability to prune unused containers

* Tue May 16 2023 Packit <hello@packit.dev> - 69-1
- PatternFly 5 fixes
- Translation updates

* Wed May 03 2023 Packit <hello@packit.dev> - 68-1
- Update to PatternFly 5 Alpha

* Wed Apr 19 2023 Packit <hello@packit.dev> - 67-1
- Fix building on non-x86_64 machines with esbuild-wasm
- Translation updates

* Tue Apr 11 2023 Packit <hello@packit.dev> - 66-1
 - Container list can be sorted
 - Custom healthcheck actions

* Wed Mar 22 2023 Packit <hello@packit.dev> - 65-1
- Show dialog errors at the top of the dialogs
- Build system and documentation improvements

* Wed Mar 08 2023 Packit <hello@packit.dev> - 64-1
- Supports the esbuild bundler
- Stability and performance improvements

* Wed Feb 22 2023 Packit <hello@packit.dev> - 63-1
- Stability and performance improvements

* Wed Feb 08 2023 Packit <hello@packit.dev> - 62-1
- Stability and performance improvements

* Wed Jan 25 2023 Packit <hello@packit.dev> - 61-1
- Use container image's default command
- Fix tabular numbers font

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Packit <hello@packit.dev> - 60-1
- Patternfly update and other maintenance

* Thu Dec 22 2022 Packit <hello@packit.dev> - 59-1
- Start using tabular fonts
- Other UI fixes and improvements


* Thu Dec 01 2022 Packit <hello@packit.dev> - 58-1
- Performance and stability improvements


* Wed Nov 16 2022 Packit <hello@packit.dev> - 57-1
- Performance and stability improvements


* Mon Nov 07 2022 Packit <hello@packit.dev> - 56-1
- Dark theme support


* Wed Oct 19 2022 Packit <hello@packit.dev> - 55-1
- Pod CPU, memory, port and volume details
- Create new pod group functionality


* Wed Sep 21 2022 Packit <hello@packit.dev> - 54-1
- Show all containers by default


* Wed Sep 07 2022 Packit <hello@packit.dev> - 53-1
 - Stability and performance improvements


* Wed Aug 24 2022 Packit <hello@packit.dev> - 52-1
- Add Volumes and Env Variables to container details
- Show volume permission in container integration tab
- Allow no system users to set restart policy
- Show image history


* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 51.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Packit <hello@packit.dev> - 51.1-1
- Fix FMF tests running on release tarball


* Thu Jun 23 2022 Packit <hello@packit.dev> - 50-1
- Use NumberInput for Image Run Dialog


* Thu Jun 09 2022 Packit <hello@packit.dev> - 49.1-1
- Fix release tarball


* Wed Jun 08 2022 Packit <hello@packit.dev> - 49-1
- Show container names in CPU usage overview


* Tue May 24 2022 Marius Vollmer <mvollmer@redhat.com> - 48-1
- Podman: Container renaming
- Podman: Health check support

* Thu Apr 28 2022 Jelle van der Waa <jvanderwaa@redhat.com> - 47-1
- Translation updates

* Wed Apr 13 2022 Martin Pitt <martin@piware.de> - 46-1
- Translation updates
- Test fixes

* Wed Mar 30 2022 Matej Marusak <mmarusak@redhat.com> - 45-1
- Translation updates

* Wed Mar 16 2022 Simon Kobyda <skobyda@redhat.com> - 44-1
- Always use base 10 size units
- Move owner option to details tab

* Wed Mar 02 2022 Martin Pitt <martin@piware.de> - 43-1
- Translation updates (rhbz#2017345, #2017266)

* Wed Feb 16 2022 Jelle van der Waa <jvanderwaa@redhat.com> - 42-1
- Tests improvements and stabilization

* Wed Feb 02 2022 Martin Pitt <martin@piware.de> - 41-1
- Adjust for podman 4.0 API break
- Improve page layout on mobile devices

* Mon Jan 24 2022 Matej Marusak <mmarusak@redhat.com> - 40-1
- Add pause/resume to containers
- Always pull the latest image when creating a new container

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Simon Kobyda <skobyda@redhat.com> - 39-1
- Create container in pod
- Podman restart policy
- Allow inserting multiple environment variables

* Thu Dec 09 2021 Marius Vollmer <mvollmer@redhat.com> - 38-1
- Updated translations
- Consistent colors for pod and container running status

* Wed Nov 24 2021 Allison Karlitskaya <allison.karlitskaya@redhat.com> - 37-1
- Improved image commit UI
- PatternFly updates and fixes

* Wed Nov 10 2021 Katerina Koukiou <kkoukiou@redhat.com> - 36-1
- Prune unused images
- New “Create container” workflow

* Wed Sep 15 2021 Katerina Koukiou <kkoukiou@redhat.com> - 35-1
- Some nice UI improvements

* Wed Sep 01 2021 Simon Kobyda <skobyda@redhat.com> - 34-1
- First iteration of page redesign

* Wed Aug 04 2021 Martin Pitt <martin@piware.de> - 33-1
- Add Japanese translations (rhbz#1980212)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 02 2021 Martin Pitt <martin@piware.de> - 32-1
- PatternFly and other npm module updates


* Wed May 26 2021 Matej Marusak <mmarusak@redhat.com> - 31-1
- Added Korean translation


* Wed Apr 14 2021 Matej Marusak <mmarusak@redhat.com> - 30-1
- Translation updates
- PatternFly 4 updates
- Fix crash with "Used Images" links


* Fri Feb 19 2021 Martin Pitt <martin@piware.de> - 29-1
- PatternFly 4 updates for a more consistent UI
- Accessibility fixes
- Add FMF tests for sharing tests with up- and downstream


* Thu Feb 11 2021 Matej Marusak <mmarusak@redhat.com> - 28.1-1
- Improve tests to be more robust against unstable Podman API


* Thu Feb 04 2021 Matej Marusak <mmarusak@redhat.com> - 28-1
- Drop cockpit-system dependency
- Correctly show selected option for SELinux labels


* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Matej Marusak <mmarusak@redhat.com> - 27.1-1
- test: Drop forgotten sit() to make tests work in gating


* Thu Jan 07 2021 Matej Marusak <mmarusak@redhat.com> - 27-1
- images: Indicate that force deletion is in progress
- images: Fix handling of errors on pull
- Use packaged sassc instead of node-sass
- tests: Adjust to new Podman versions and robustify them


* Wed Dec 09 2020 Marius Vollmer <mvollmer@redhat.com> - 26-1
- run: Make hostPort optional
- run: Enable setting up IP address for exposed ports

* Wed Oct 14 2020 Sanne Raymaekers <sanne.raymaekers@gmail.com> - 25-1
- Listen for image build event


* Wed Sep 30 2020 Marius Vollmer <mvollmer@redhat.com> - 24-1
- Use sentence case in the UI


* Wed Sep 02 2020 Martin Pitt <martin@piware.de> - 23-1
- Translation updates


* Wed Aug 19 2020 Marius Vollmer <mvollmer@redhat.com> - 22-1
- Support for pod group deletion


* Wed Aug 05 2020 Matej Marusak <mmarusak@redhat.com> - 21-1
- Support for pod groups
- Support checkpoint and restore
- Registry selection in "download image" dialog
- Selected tag removal during deletion


* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Katerina Koukiou <kkoukiou@redhat.com> - 20-1
- Show networking information for containers
- Enable filtering images and containers by owner
- Optionally show intermediate images
- Enable setting up SELinux label when mounting volumes


* Wed Jul 15 2020 Matej Marusak <mmarusak@redhat.com> - 19-1
- Switch to the new Podman REST API
- Improve displaying on small screens


* Mon Jun 15 2020 Matej Marusak <mmarusak@redhat.com> - 18-1
- Bump NPM dependencies to their latest versions
- Stop importing cockpit's deprecated base1/patternfly.css
- Synchronize style with the newest Cockpit


* Thu May 14 2020 Matej Marusak <mmarusak@redhat.com> - 17-1
- Translation updates
- Adjust tests to changed Services page in Cockpit 218


* Wed Apr 29 2020 Martin Pitt <martin@piware.de> - 16-1
- Restyle buttons and dropdowns to be consistent with Cockpit
- Disable button and show a spinner while delete operation is in progress
- Translation updates


* Thu Apr 16 2020 Martin Pitt <martin@piware.de> - 15-3
- Drop obsolete functionality for Fedora Atomic
- Localize dates and times
- Make tests non-destructive, to support Fedora gating


* Wed Mar 04 2020 Martin Pitt <martin@piware.de> - 14-1
- Fix crash on filtering anonymous images
- Translation updates


* Wed Feb 05 2020 sanne raymaekers <sanne.raymaekers@gmail.com> - 13-1
- Show historical logs


* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Katerina Koukiou <kkoukiou@redhat.com> - 12-1
- Configure CPU share for system containers


* Wed Nov 27 2019 Martin Pitt <martin@piware.de> - 11-1
- Fix Alert notification in Image Search Modal
- Allow more than a single Error Notification for Container action errors
- Various Alert cleanups
- Translation updates


* Wed Oct 30 2019 Sanne Raymaekers <sanne.raymaekers@gmail.com> - 10-1
- Support for user containers


* Wed Oct 02 2019 Martin Pitt <martin@piware.de> - 9-1
- Minimize CSS in production builds
- Bump NPM dependencies to latest versions


* Wed Sep 04 2019 Martin Pitt <martin@piware.de> - 8-1
- Show list of containers that use given image
- Show placeholder while loading containers and images
- Fix setting memory limit


* Wed Jul 31 2019 Martin Pitt <martin@piware.de> - 7-1
- Fix AppStream ID
- Adjust tests to changed Cockpit Services page


* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Martin Pitt <martin@piware.de> - 6-1
- Fix various UI regressions from Cockpit's PatternFly 4 switch
- Add packit configuration (https://packit.dev/)


* Wed Jul 10 2019 Martin Pitt <martin@piware.de> - 5-1
- Add container Terminal


* Wed Jun 26 2019 Katerina Koukiou <kkoukiou@redhat.com> - 4-1
- Fix regression in container commit


* Mon Jun 17 2019 Martin Pitt <martin@piware.de> - 3-1
- Enable Commit button for running containers
- Fix race condition with container deletion
- Stop fetching all containers/images for each container/image event


* Fri May 24 2019 Cockpit Project <cockpituous@gmail.com> - 2-1
- Update to upstream 2 release

* Wed Apr 17 2019 Cockpit Project <cockpituous@gmail.com> - 1-2
- Update to upstream 1 release

