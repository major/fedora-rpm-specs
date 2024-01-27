%global file_name com.github.babluboy.nutty

Name:           nutty
Version:        1.1.1
Release:        15%{?dist}
Summary:        Simple utility for network information

# The entire source code is GPLv3+ except *speedtest-cli* which is ASL 2.0
License:        GPLv3+ and ASL 2.0
URL:            https://github.com/babluboy/nutty
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/babluboy/nutty/pull/51
Patch0:         %{name}-ambiguous-python-shebang.patch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9

Requires:       hicolor-icon-theme
Requires:       polkit

Recommends:     curl%{_isa}
Recommends:     iproute%{_isa}
Recommends:     net-tools%{_isa}
Recommends:     nethogs%{_isa}
Recommends:     nmap%{_isa}
Recommends:     pciutils%{_isa}
Recommends:     traceroute%{_isa}
Recommends:     vnstat%{_isa}
Recommends:     wireless-tools%{_isa}

%description
A simple application made for elementary OS to provide essential information on
network related aspects. The information presented in as the following tabs.

• My Info: Provides basic and detailed information for the device network card
• Usage: Provides network data usage in two views - historical usage and
  current usage
• Speed: Check Upload and Download speeds and get route times to a host
• Ports: Provides information on active ports and application using them on the
  local device
• Devices: Monitors, alerts and provides information on the other devices
  connected on the network

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
# "mo" does not a valid language code according to the Wikipedia list of
# ISO-639-1 codes
rm      %{buildroot}%{_datadir}/locale/mo/LC_MESSAGES/%{file_name}.mo
%find_lang %{file_name}
# Equal to regular and doesnt have HiDPI version for now
rm -r   %{buildroot}%{_datadir}/icons/hicolor/*@2

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{file_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{file_name}.desktop

%files -f %{file_name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{file_name}
%{_datadir}/%{file_name}
%{_datadir}/applications/%{file_name}.desktop
%{_datadir}/glib-2.0/schemas/%{file_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{file_name}.svg
%{_datadir}/polkit-1/actions/org.freedesktop.policykit.%{name}.policy
%{_metainfodir}/%{file_name}.appdata.xml

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-8
- Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.1-3
- Initial package
