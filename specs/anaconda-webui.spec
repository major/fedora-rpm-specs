Name:           anaconda-webui
Version:        17
Release:        1%{?dist}
Summary:        Anaconda installer Web interface
License:        LGPL-2.1-or-later AND MIT
URL:            https://github.com/rhinstaller/%{name}

Source0:        https://github.com/rhinstaller/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  gettext
# Needed for the unitdir macro
BuildRequires: systemd-rpm-macros

%global anacondacorever 0

%if 0%{?fedora} > 41
%global anacondacorever 42.5
%endif

%global cockpitver 275
%global cockpitstorver 311

%define _unitdir /usr/lib/systemd/system

Requires: cockpit-storaged >= %{cockpitstorver}
Requires: cockpit-bridge >= %{cockpitver}
Requires: cockpit-ws >= %{cockpitver}
Requires: anaconda-core  >= %{anacondacorever}
# Firefox dependency needs to be specified there as cockpit web-view does not have a hard dependency on Firefox as
# it can often fall back to a diferent browser. This does not work in the limited installer
# environment, so we need to make sure Firefox is available. Exclude on RHEL, only Flatpak version will be there.
%if ! 0%{?rhel}
Requires: firefox
%endif
%if 0%{?fedora}
Requires: fedora-logos
%endif

Provides: bundled(npm(@patternfly/patternfly)) = 5.4.1
Provides: bundled(npm(@patternfly/react-core)) = 5.4.1
Provides: bundled(npm(@patternfly/react-icons)) = 5.4.2
Provides: bundled(npm(@patternfly/react-log-viewer)) = 5.3.0
Provides: bundled(npm(@patternfly/react-styles)) = 5.4.1
Provides: bundled(npm(@patternfly/react-table)) = 5.4.1
Provides: bundled(npm(@patternfly/react-tokens)) = 5.4.1
Provides: bundled(npm(attr-accept)) = 2.2.4
Provides: bundled(npm(dequal)) = 2.0.3
Provides: bundled(npm(file-selector)) = 0.6.0
Provides: bundled(npm(focus-trap)) = 7.5.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(memoize-one)) = 5.2.1
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-dom)) = 18.2.0
Provides: bundled(npm(react-dropzone)) = 14.2.10
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react)) = 18.2.0
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.2.0
Provides: bundled(npm(throttle-debounce)) = 5.0.2
Provides: bundled(npm(tslib)) = 2.8.0

%description
Anaconda installer Web interface

%prep
%setup -q -n %{name}

%build
# Nothing to build

%install
%make_install PREFIX=/usr
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%check
exit 0
# We have some integration tests, but those require running a VM, so that would
# be an overkill for RPM check script.

%files
%dir %{_datadir}/cockpit/anaconda-webui
%doc README.rst
%license LICENSE dist/index.js.LEGAL.txt
%{_datadir}/cockpit/anaconda-webui/logo.svg
%{_datadir}/cockpit/anaconda-webui/qr-code-feedback.svg
%{_datadir}/cockpit/anaconda-webui/index.js.LEGAL.txt
%{_datadir}/cockpit/anaconda-webui/index.html
%{_datadir}/cockpit/anaconda-webui/index.js.gz
%{_datadir}/cockpit/anaconda-webui/index.js.map
%{_datadir}/cockpit/anaconda-webui/index.css.gz
%{_datadir}/cockpit/anaconda-webui/index.css.map
%{_datadir}/cockpit/anaconda-webui/manifest.json
%{_datadir}/metainfo/org.cockpit-project.anaconda-webui.metainfo.xml
%{_datadir}/cockpit/anaconda-webui/po.*.js.gz
%dir %{_datadir}/anaconda/firefox-theme
%dir %{_datadir}/anaconda/firefox-theme/default
%dir %{_datadir}/anaconda/firefox-theme/default/chrome
%{_datadir}/anaconda/firefox-theme/default/user.js
%{_datadir}/anaconda/firefox-theme/default/chrome/userChrome.css
%dir %{_datadir}/anaconda/firefox-theme/live
%dir %{_datadir}/anaconda/firefox-theme/live/chrome
%{_datadir}/anaconda/firefox-theme/live/user.js
%{_datadir}/anaconda/firefox-theme/live/chrome/userChrome.css
%{_libexecdir}/anaconda/webui-desktop
%{_unitdir}/webui-cockpit-ws.service


# The changelog is automatically generated and merged
%changelog
* Fri Oct 25 2024 Packit <hello@packit.dev> - 17-1
- Run browser as liveuser instead of root
- Introduce new guided partitioning scenario 'Home reuse'
- Update strings based on latest mockups
- storage: mount-point-mapping page: group devices in selector by disk
- storage: disk selection: do not show sync-alt Icon when the spinner is on
- storage: emphasize the hint text in the reclaim modal
- review: storage section: show first column device and last column mount point
- Change the wording from 'Modify storage' to 'Launch storage editor'
- Move the cockpit-ws spawning to a service file
- Do not run firefox when remote installation is requested
- And few more enhancements with lower impact

* Mon Sep 23 2024 Packit <hello@packit.dev> - 16-1
- storage: mount point assignment: show partition labels in device selection
- components: common: remove AddressContext provider as it's not used
- Reimplement error handling using error boundaries (Resolves: rhbz#2308279)
- storage: re-design the disk selection component
- storage: move 'Modify storage' to the header kebab

* Wed Sep 11 2024 Packit <hello@packit.dev> - 15-1
- storage: use `console.warn` not `console.warning` to fix crash

* Mon Sep 09 2024 Adam Williamson <awilliam@redhat.com> - 14-3
- Backport #435 to really fix crash when device path doesn't exist

* Thu Sep 05 2024 Adam Williamson <awilliam@redhat.com> - 14-2
- Rebuild to get a combined update with anaconda

* Wed Sep 4 2024 Packit <hello@packit.dev> - 14-1
- Move webui-desktop in libexec to our subdirectory
- storage: fix crash when device path is not existing

* Mon Aug 19 2024 Packit <hello@packit.dev> - 13-1
- storage: Update text for cockpit storage confirmation modal
- storage: increase the radio button spacing in the scenario selection group
- storage: reclaim: don't schedule actions for partitions whose parents are removed
- review: switch from confirmation modal to checkbox
- storage: increase spacing between password fields
- users: fix spelling of 'privilege'
- storage: make reclaim dialog table compact
- storage: don't wrap disk name away from the icon
- storage: use name not device-id in the Name column in reclaim dialog
- Allow having duplicate device names
- storage: wait for iframe to load before adding event listeners
- storage: reclaim dialog: show format type not device type

* Tue Aug 6 2024 Packit <hello@packit.dev> - 12-1
- storage: display names not IDs in the storage screens

* Sat Aug 3 2024 Packit <hello@packit.dev> - 11-1
- Re-add alert confirmation before Cockpit Storage
- storage: implement shrink partition action in reclaim dialog
- review: show previous and new size of resized devices
- review: remove the seperate 'Disk encryption' section
- review: hide account section for Workstation media
- storage: give hint on how to resize bitlocker encrypted windows partitions
- review: show resized partitions that belong to an OS
- storage: show icon for encrypted LUKS devices in Reclaim dialog

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Packit <hello@packit.dev> - 10-1
- review: show hostname and configuration option in server variant
- Adopt modal based design for the cockpit-storage iframe
- apis: Read storage-scenario-id from sessionStorage where it's stored
- storage: helpers: fix the calculation of device children
- storage: cockpit-integration: do not overwrite request object structure - only extend it  (Resolves: rhbz#226441)
- review: organize groups and seperate with gutter
- storage: create MANUAL partitioning after unlocking the devices
- Show the storage layout in the review page for all scenarios
- Do not filter steps manually as the isHidden property is handled internally
- actions: use modern async / await when reading device data
- storage: set InitializationMode when creating the partitioning
- storage: disable form before applying the partitioning
- Disable also navigation items when the form is disabled
- Introduce some logic for knowing if devices are currently being fetched
- Disable 'Return to installation' in cockpit storage dialog when fetching device data
- storage: reset the partitioning only if there is one applied
- storage: reset partitioning before loading the scenario selection
- storage: use getNewPartitioning reusable method also for manual
- storage: do not update the scenario selection while cockpit storage mode is open
- Disable the form by default on page enter and let each page enable it after initialization
- storage: reset the partitioning before enabling the form in the disk encryption screen
- Explicitely disable all scenarios when there are not selected disks
- Remove unused isHidden property from FormHelperText
- storage: get the partitioning information only for the last created partitioning
- storage: Introduce 'Reclaim space' dialog
- review: show delete actions only for partitions
- review: get the information about deleted devices from the original device tree
- test: fix test case for installation against a disk with an existing Linux OS
- review: show existing systems affected by deleted partitions
- review: extend note about deleted systems to show affected systems
- review: use helper functions for parsing the device tree data
- storage: fix available space in reclaim dialog when parent device is deleted

* Thu Apr 4 2024 Packit <hello@packit.dev> - 9-1
- Translation updates
- A large series code cleanups

* Wed Feb 21 2024 Packit <hello@packit.dev> - 8-1
- Change hardcoded installation phases to new API
- Add bootloader partition early check based on mount point constraints

* Mon Feb 19 2024 Packit <hello@packit.dev> - 7-1
- storage: fix password visibility toggle when clicking on 'eye' button (#2250790)
- storage: enhance integration between Anaconda Web UI and Cockpit storage (#2263971)
- storage: inform user when oops happens in cockpit-storage (#2264041)
- storage: do not force reformatting /
- storage: add storage layout review text in the cockpit-storage exit dialog

* Fri Feb 16 2024 Packit <hello@packit.dev> - 6-1
- Tests stabilization

* Wed Feb 7 2024 Packit <hello@packit.dev> - 5.2-1
- Packaging fixes and introduced installability test upstream

* Tue Jan 30 2024 Packit <hello@packit.dev> - 4-1
- storage: add support for recommended mount points

* Tue Jan 23 2024 Packit <hello@packit.dev> - 3-1
- Accounts: allow to set root password
- Add feedback section in the installation screen

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 5 2023 Packit <hello@packit.dev> - 2-1
- Improved field validation and other improvements in the user creation step

* Wed Nov 24 2021 Katerina Koukiou <kkoukiou@redhat.com> - 1-1
- First public preview of Anaconda Web UI after repository move
