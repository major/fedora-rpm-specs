Name:      plasma-welcome-fedora
Version:   6.1.2
Release:   2%{?dist}
Summary:   Fedora-related customizations for Plasma-welcome
# License is specified in 01-EnableExtraRepos.qml
License:   (GPL-2.0-only OR GPL-3.0-only) AND CC-BY-SA-4.0
URL:       https://pagure.io/fedora-kde/plasma-welcome-fedora
Source0:   https://pagure.io/fedora-kde/plasma-welcome-fedora/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch: noarch

BuildRequires: kf6-rpm-macros

Requires:  plasma-welcome
Requires:  fedora-third-party
Requires:  fedora-workstation-repositories
Requires:  fedora-flathub-remote

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-v%{version}

%install
install -D -m 0644 -p \
    ./%{_kf6_datadir}/plasma/plasma-welcome/intro-customization.desktop \
    %{buildroot}%{_kf6_datadir}/plasma/plasma-welcome/intro-customization.desktop
install -D -m 0644 -p \
    ./%{_kf6_datadir}/plasma/plasma-welcome/extra-pages/01-EnableExtraRepos.qml \
    %{buildroot}%{_kf6_datadir}/plasma/plasma-welcome/extra-pages/01-EnableExtraRepos.qml
install -D -m 0644 -p \
    ./%{_datadir}/icons/hicolor/scalable/apps/fedora-loves-kde.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/fedora-loves-kde.svg
install -D -m 0644 -p \
    ./%{_datadir}/icons/hicolor/scalable/apps/mascot_konqi_3rdparty.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mascot_konqi_3rdparty.svg

%files
%license LICENSES/* COPYING
%{_kf6_datadir}/plasma/plasma-welcome/intro-customization.desktop
%{_kf6_datadir}/plasma/plasma-welcome/extra-pages
%{_datadir}/icons/hicolor/scalable/apps/fedora-loves-kde.svg
%{_datadir}/icons/hicolor/scalable/apps/mascot_konqi_3rdparty.svg

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Timothée Ravier <tim@siosm.fr> - 6.1.2-1
- Update mascot image and text for third part page
- Remove documentation
- Make sure we own the directories we install
- Update license to include the one used for the new mascot

* Mon Aug 19 2024 Steve Cossette <farchord@gmail.com> - 6.1.1-1
- 6.1.1

* Tue Jul 02 2024 Steve Cossette <farchord@gmail.com> - 6.1.0-1
- Bringing versioning in line with KDE versions

* Tue Jul 02 2024 Steve Cossette <farchord@gmail.com> - 1.1-1
- Updated customization, added images

* Fri Feb 16 2024 Steve Cossette <farchord@gmail.com> - 1.0-1
- Initial release of the customization scripts for plasma-welcome
