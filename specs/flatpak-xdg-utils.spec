Name:     flatpak-xdg-utils
Summary:  Command-line tools for use inside Flatpak sandboxes
Version:  1.0.6
Release:  2%{?dist}
License:  LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:      https://github.com/flatpak/flatpak-xdg-utils
Source:   https://github.com/flatpak/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)

Requires: flatpak-spawn%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
This package contains a number of command-line utilities for use inside
Flatpak sandboxes. They work by talking to portals.

%package -n     flatpak-spawn
Summary:        Command-line frontend for the org.freedesktop.Flatpak service
License:        LGPL-2.1-or-later

%description -n flatpak-spawn
This package contains the flatpak-spawn command-line utility. It can be
used to talk to the org.freedesktop.Flatpak service to spawn new sandboxes,
run commands on the host, or use one of the session or system helpers.

%package tests
Summary:   Tests for %{name}
License:   LGPL-2.1-or-later AND MIT
Requires:  %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:  flatpak-spawn%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description tests
This package contains installed tests for %{name}.

%prep
%autosetup

%build
%meson -Dinstalled_tests=true
%meson_build

%install
%meson_install

mv $RPM_BUILD_ROOT%{_bindir}/xdg-email $RPM_BUILD_ROOT%{_bindir}/flatpak-xdg-email
mv $RPM_BUILD_ROOT%{_bindir}/xdg-open $RPM_BUILD_ROOT%{_bindir}/flatpak-xdg-open

%files
%doc README.md
%license COPYING
%{_bindir}/flatpak-xdg-email
%{_bindir}/flatpak-xdg-open

%files -n flatpak-spawn
%license COPYING
%{_bindir}/flatpak-spawn

%files tests
%{_datadir}/installed-tests
%{_libexecdir}/installed-tests

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 09 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.6-1
- Update to 1.0.6

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 02 2022 Debarshi Ray <rishi@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5
- Enable installed tests

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 05 2021 Kalev Lember <klember@redhat.com> - 1.0.4-3
- Add flatpak- prefix to executables to avoid conflicting with xdg-utils

* Fri Feb 05 2021 Kalev Lember <klember@redhat.com> - 1.0.4-2
- Add explicit conflicts with xdg-utils

* Tue Feb 02 2021 Kalev Lember <klember@redhat.com> - 1.0.4-1
- Update to 1.0.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Kalev Lember <klember@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 15 2019 Kalev Lember <klember@redhat.com> - 1.0.0-5
- Fix the name of the new subpackage to actually be flatpak-spawn

* Fri Sep 13 2019 Debarshi Ray <rishi@fedoraproject.org> - 1.0.0-4
- Split flatpak-spawn into a separate sub-package

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Owen Taylor <otaylor@redhat.com> - 1.0.0-1
- Initial version
