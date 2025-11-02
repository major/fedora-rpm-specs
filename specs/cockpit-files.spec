Name: cockpit-files
Version: 31.1
Release: 1%{?dist}
Summary: A filesystem browser for Cockpit
License: LGPL-2.1-or-later

Source0: https://github.com/cockpit-project/cockpit-files/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch: noarch
BuildRequires: make
%if 0%{?suse_version}
# Suse's package has a different name
BuildRequires:  appstream-glib
%else
BuildRequires:  libappstream-glib
%endif
BuildRequires: gettext

Requires: cockpit-bridge >= 318

# Replace the older cockpit-navigator provided by 45Drives
Obsoletes: cockpit-navigator < 0.5.11

Provides: bundled(npm(@patternfly/patternfly)) = 6.4.0
Provides: bundled(npm(@patternfly/react-core)) = 6.4.0
Provides: bundled(npm(@patternfly/react-icons)) = 6.4.0
Provides: bundled(npm(@patternfly/react-styles)) = 6.4.0
Provides: bundled(npm(@patternfly/react-table)) = 6.4.0
Provides: bundled(npm(@patternfly/react-tokens)) = 6.4.0
Provides: bundled(npm(dequal)) = 2.0.3
Provides: bundled(npm(focus-trap)) = 7.6.4
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.2.0
Provides: bundled(npm(throttle-debounce)) = 5.0.2
Provides: bundled(npm(tslib)) = 2.8.1

%description
A filesystem browser for Cockpit

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

# this can't be meaningfully tested during package build; tests happen through
# FMF (see plans/all.fmf) during package gating

%files
%doc README.md
%license LICENSE dist/index.js.LEGAL.txt
%{_datadir}/cockpit/*
%{_datadir}/metainfo/*

%changelog
* Fri Oct 31 2025 Packit <hello@packit.dev> - 31.1-1
- don't initialise a git repo in gating tests (fixes fedora gating)


* Wed Oct 15 2025 Packit <hello@packit.dev> - 30-1
- Translations and dependency updates

* Thu Oct 2 2025 Packit <hello@packit.dev> - 29-1
- Bug fixes and translation updates

* Wed Sep 3 2025 Packit <hello@packit.dev> - 28-1
- Allow user to create empty files
- Bug fixes and translation updates

* Wed Aug 20 2025 Packit <hello@packit.dev> - 27-1
- Translation and dependency updates

* Wed Aug 6 2025 Packit <hello@packit.dev> - 26-1
Bug fixes and translation updates

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 23 2025 Packit <hello@packit.dev> - 25-1
- Bug fixes and translation updates

* Wed Jul 9 2025 Packit <hello@packit.dev> - 24-1
- Bug fixes and translation updates

* Wed Jun 25 2025 Packit <hello@packit.dev> - 23-1
- Bug fixes and translation updates

* Wed Jun 4 2025 Packit <hello@packit.dev> - 22-1
- Bug fixes and translation updates

* Wed May 21 2025 Packit <hello@packit.dev> - 21-1
- Bug fixes and translation updates

* Wed May 7 2025 Packit <hello@packit.dev> - 20-1
- Translation updates
- Bug fixes

* Wed Apr 23 2025 Packit <hello@packit.dev> - 19-1
- Upgraded to Patternfly 6
- Symbolic links

* Wed Mar 12 2025 Packit <hello@packit.dev> - 18-1
- Translation updates
- Bug fixes

* Thu Feb 27 2025 Packit <hello@packit.dev> - 17-1
- MacOS keyboard shortcuts

* Thu Feb 13 2025 Packit <hello@packit.dev> - 16-1
- support copy&pasting with administrator privileges

* Wed Jan 29 2025 Packit <hello@packit.dev> - 15-1
- Show user and group information in the footer

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Packit <hello@packit.dev> - 14-1
- Allow editing multiple file permissions
- Support uploading files with administrator privileges
- Add drag 'n drop support

* Wed Dec 4 2024 Packit <hello@packit.dev> - 13-1
- Translation updates

* Wed Nov 20 2024 Packit <hello@packit.dev> - 12-1
- File creation support

* Wed Nov 6 2024 Packit <hello@packit.dev> - 11-1
- Show SELinux security context in permissions dialog
- Support changing permissions of enclosed files

* Wed Oct 23 2024 Packit <hello@packit.dev> - 10-1
- Redesign the permissions dialog

* Wed Oct 9 2024 Packit <hello@packit.dev> - 9-1
-  basic keyboard shortcuts

* Wed Sep 25 2024 Packit <hello@packit.dev> - 8-1
- Move global menu to the toolbar

* Wed Sep 4 2024 Packit <hello@packit.dev> - 7-1
- Basic file editor and viewer

* Thu Aug 22 2024 Packit <hello@packit.dev> - 6-1
- Add owner column to details view
- Translation updates

* Thu Aug 8 2024 Packit <hello@packit.dev> - 5-1
- Display file permissions

* Thu Jul 18 2024 Packit <hello@packit.dev> - 4-1
- Bug fixes

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Packit <hello@packit.dev> - 3.1-1
- Allow breadcrumbs to wrap, fixes failing gating test

* Wed Jul 10 2024 Packit <hello@packit.dev> - 3-1
- Bug fixes and performance improvements

* Wed Jun 26 2024 Packit <hello@packit.dev> - 2-1
- Bookmark support

* Fri Jun 7 2024 Jelle van der Waa <jvanderwaa@redhat.com> - 1-1
- Update to upstream 1 release
