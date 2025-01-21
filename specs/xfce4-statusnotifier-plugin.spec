%global _icondir %{_datadir}/icons/hicolor
%global basever 0.2

Name:           xfce4-statusnotifier-plugin
Version:        0.2.2
Release:        14%{?dist}
Summary:        Panel area status notifier plugin for Xfce4
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{basever}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  xfce4-dev-tools
BuildRequires:  libtool
BuildRequires:  gtk3-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  xfce4-panel-devel
BuildRequires:  libdbusmenu-gtk3-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

%description
This plugin provides a panel area for status notifier items (application
indicators). Applications may use these items to display their status and
interact with user. This technology is a modern alternative to systray and
has the freedesktop.org specification.

%prep
%setup -q

%build
%configure 
%make_build

%install
%make_install
find %{buildroot} -name \*.la -exec rm {} \;
if [ ! -d %{buildroot}/%{_libdir} ]; then
mv %{buildroot}/usr/lib %{buildroot}/%{_libdir}
fi

%find_lang %{name}


%files -f %{name}.lang
%{_libdir}/xfce4/panel/plugins/libstatusnotifier.*
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/icons/hicolor/*/apps/xfce4-statusnotifier-plugin.png
%{_datadir}/icons/hicolor/*/apps/xfce4-statusnotifier-plugin.svg
%{_datadir}/xfce4/panel/plugins/statusnotifier.desktop

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 22 2024 Mukundan Ragavan <nonamedotc@gmail.com> - 0.2.2-13
- rebuild for xfce-4.20

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.2-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 09 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.1-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Fri Sep 08 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.0-2
- Fix build errors

* Fri Sep 08 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Tue Jul 25 2017 Zamir SUN <zsun@fedoraproject.org> - 0.1.0-1
- Initial xfce4-statusnotifier-plugin

