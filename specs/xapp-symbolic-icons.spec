Name:           xapp-symbolic-icons
Version:        1.0.8
Release:        2%{?dist}
Summary:        A set of symbolic icons which replaces the GNOME-specific Adwaita set
License:        GPL-3.0-only AND LGPL-3.0-only
URL:            https://github.com/xapp-project/xapp-symbolic-icons
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson
Requires:       hicolor-icon-theme

%description
A set of symbolic icons which replaces the GNOME-specific Adwaita set.
All provided icons are prefixed with xsi-.
Icon names loosely follow the Adwaita names.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%transfiletriggerin -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license COPYING COPYING.LESSER
%doc AUTHORS README.md
%{_bindir}/xsi-replace-adwaita-symbolic
%{_datadir}/icons/hicolor/scalable/actions/xsi-*.svg
%{_datadir}/xapp/

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Jan 10 2026 Leigh Scott <leigh123linux@gmail.com> - 1.0.8-1
- Update to 1.0.8

* Fri Dec 12 2025 Leigh Scott <leigh123linux@gmail.com> - 1.0.6-1
- Update to 1.0.6

* Thu Nov 27 2025 Leigh Scott <leigh123linux@gmail.com> - 1.0.5-1
- Update to 1.0.5

