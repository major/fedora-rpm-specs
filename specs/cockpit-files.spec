Name: cockpit-files
Version: 14
Release: 2%{?dist}
Summary: A filesystem browser for Cockpit
License: LGPL-2.1-or-later

Source0: https://github.com/cockpit-project/cockpit-files/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
BuildRequires: nodejs
BuildRequires: make
%if 0%{?suse_version}
# Suse's package has a different name
BuildRequires:  appstream-glib
%else
BuildRequires:  libappstream-glib
%endif
BuildRequires: gettext

Requires: cockpit-bridge >= 318

Provides: bundled(npm(@patternfly/patternfly)) = 5.4.2
Provides: bundled(npm(@patternfly/react-core)) = 5.4.11
Provides: bundled(npm(@patternfly/react-icons)) = 5.4.2
Provides: bundled(npm(@patternfly/react-styles)) = 5.4.1
Provides: bundled(npm(@patternfly/react-table)) = 5.4.12
Provides: bundled(npm(@patternfly/react-tokens)) = 5.4.1
Provides: bundled(npm(attr-accept)) = 2.2.5
Provides: bundled(npm(dequal)) = 2.0.3
Provides: bundled(npm(file-selector)) = 2.1.2
Provides: bundled(npm(focus-trap)) = 7.6.2
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
%license LICENSE dist/index.js.LEGAL.txt dist/index.css.LEGAL.txt
%{_datadir}/cockpit/*
%{_datadir}/metainfo/*

%changelog
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
