Name:           persepolis
Version:        4.1.0
Release:        5%{?dist}
Summary:        A powerful download manager powered by aria2

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://persepolisdm.github.io/
Source0:        https://github.com/persepolisdm/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  meson ninja-build
BuildRequires:  libappstream-glib
# libnotify is required for notify-send
Requires:       aria2 libnotify python3-requests pulseaudio-utils
Requires:       python3-setproctitle sound-theme-freedesktop python3-psutil
%if 0%{?fedora} >= 41
Requires:       python3-pyside6 qt6-qtsvg
%else
Requires:       python3-qt5 qt5-qtsvg
%endif
Recommends:     yt-dlp ffmpeg-free

%description
Persepolis is a download manager and a GUI for aria2 powered by Python.
 - Graphical UI front end for aria2
 - Multi-segment downloading
 - Scheduling downloads
 - Download queue


%prep
%autosetup -p1
rm 'persepolis/Persepolis Download Manager.py'
find -type f -exec \
   sed -i '1s=^#!/usr/bin/\(python\|env python.*\)$=#!%{__python3}=' {} \;


%build
%meson
%meson_build


%install
%meson_install
chmod a+x %{buildroot}/%{python3_sitelib}/persepolis/__main__.py

%check
# No valid tests available
#%{__python3} setup.py test
desktop-file-validate %{buildroot}/%{_datadir}/applications/*persepolis.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/*
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{name}
%{_datadir}/metainfo/com.github.persepolisdm.persepolis.appdata.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.0-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.13

* Fri Apr 19 2024 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 4.1.0-1
- New upstream release: 4.1.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.2.0-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 25 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.2.0-10
- Replace youtube-dl dependency with yt-dlp, fixes fedora#2100540

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2.0-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.2.0-1
- Update to 3.2.0, with some bug fixes and new features

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.7

* Mon Apr 02 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.0-2
- Add youtube-dl dependency

* Sat Mar 31 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.1-3
- Fix a bug in registering for startup, fixes #1535604

* Mon Jan 01 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.1-2
- Add a comment about the patch
- more specific %files section

* Sat Dec 30 2017 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.1-1
- Initial version
