Name:           langpacks-install
Version:        1.0.0
Release:        12%{?dist}
Summary:        Tool to get auto installed langpacks on GNOME session startup

License:        GPL-3.0-or-later
URL:            https://pagure.io/%{name}
Source0:        http://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gettext-devel
BuildRequires:  desktop-file-utils
BuildRequires: make
# we need gnome-software for actual package installation
Requires:       gnome-software
# we need PackageKit to make sure dbus call will be successful
Requires:       PackageKit

%description
This tool will help to automatically install the langpacks on your system.
It automatically runs at the start of GNOME desktop environment. It will
first check if langpacks package for your language is already installed
or not. If not then ask the PackageKit to install that package. Its then
upto end user to check the PackageKit notification and install the package.

%prep
%autosetup


%build
%configure
%make_build


%install
%make_install

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%license LICENSE
%doc README NEWS AUTHORS
%{_bindir}/langpacks-install
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop

%changelog
* Thu Dec 01 2022 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-12
- Update license tag to SPDX format

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-2
- Added Requires: PackageKit
- Added Requires: gnome-software

* Wed Feb  7 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial release
- 
