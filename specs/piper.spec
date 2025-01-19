Name: piper
Version: 0.8
Release: 9%{?dist}

License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://github.com/libratbag/%{name}
Summary: GTK application to configure gaming mice
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: python3-cairo
BuildRequires: python3-devel
BuildRequires: python3-evdev
BuildRequires: python3-flake8
BuildRequires: python3-gobject
BuildRequires: python3-lxml

BuildRequires: appstream
BuildRequires: desktop-file-utils
BuildRequires: gettext-devel
BuildRequires: git-core
BuildRequires: libappstream-glib
BuildRequires: libratbag-ratbagd
BuildRequires: meson
BuildRequires: gtk-update-icon-cache

Requires: gtk3
Requires: hicolor-icon-theme
Requires: libratbag-ratbagd >= 0.14
Requires: python3-cairo
Requires: python3-evdev
Requires: python3-gobject
Requires: python3-lxml

%{?python_provide:%python_provide python3-%{name}}

%description
Piper is a GTK+ application to configure gaming mice, using libratbag
via ratbagd.

%prep
%autosetup -S git
sed -e '/meson_install.sh/d' -i meson.build

# Workaround to https://bugzilla.redhat.com/show_bug.cgi?id=2100362
%if 0%{?fedora} && 0%{?fedora} >= 37
sed -e '/evdev/d' -i meson.build
%endif

%build
%meson
%meson_build

%check
%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python3_sitelib}/%{name}/
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*.1*

%changelog
* Fri Jan 17 2025 Vojtech Trefny <vtrefny@redhat.com> - 0.8-1
- piper 0.8

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 0.7-8
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 0.7-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild
