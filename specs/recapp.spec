%global appname RecApp
%global uuid    com.github.amikha1lov.%{appname}

Name:           recapp
Version:        1.1.1
Release:        11%{?dist}
Summary:        User friendly Open Source screencaster for Linux written in GTK
BuildArch:      noarch

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/amikha1lov/recapp
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)

Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-pulsectl
Requires:       python3-pydbus
Requires:       slop

# For future
#Recommends:     gstreamer1-plugins-ugly

%description
User friendly Open Source screencaster for Linux written in GTK. Using free
GStreamer modules and not depend on FFmpeg.


%prep
%autosetup -n %{appname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license COPYING
%doc README.md CREDITS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.appdata.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.1-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 16 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.1-1
- build(update): 1.1.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Thu May 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Fri May 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Wed May 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-2
- Update to 1.0.1

* Mon May 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Sat May 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200509gitcee6555
- Update to latest git snapshot

* Fri May 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200508gitd7429a7
- Update to latest git snapshot

* Wed May 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200506gitfba20ea
- Update to latest git snapshot

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200505git61c6ee7
- Update to latest git snapshot

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200504gitfa5858f
- Update to latest git snapshot

* Sat May 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200502git1aaec32
- Update to latest git snapshot

* Fri May 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200502git454cd87
- Update to latest git snapshot

* Thu Apr 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200501gitbbe43eb
- Update to latest git snapshot

* Fri Apr 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200424git7afef69
- Update to latest git snapshot
- Add missing dep

* Sun Feb 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200223gitf6d8678
- Update to latest git snapshot

* Wed Feb 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200219gitccd1e90
- Update to latest git snapshot

* Sat Feb 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200208git5b6cda4
- Update to latest git snapshot

* Sat Jan 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200125git2fddefb
- Update to latest git snapshot

* Sat Jan 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-7.20200125git78505f6
- Add symbolic icon

* Fri Jan 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-6.20200124git3655672
- Add new icon

* Thu Jan 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-5.20200123git37b0fe3
- Update to latest git snapshot

* Wed Jan 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-4.20200122git0ce555c
- Update to latest git snapshot

* Mon Jan 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-3.20200120git8121a4f
- Update to latest git snapshot

* Sat Jan 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-2.20200118git79dc497
- Update to latest git snapshot

* Sat Jan 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20200118git4cc704a
- Initial package
