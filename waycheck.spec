%global qt6_minver 6.5

Name:           waycheck
Version:        1.0.0
Release:        2%{?dist}
Summary:        Simple GUI that displays protocols implemented by a Wayland compositor

License:        Apache-2.0
URL:            https://gitlab.freedesktop.org/serebit/waycheck
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt6Core) >= %{qt6_minver}
BuildRequires:  pkgconfig(Qt6Gui) >= %{qt6_minver}
BuildRequires:  pkgconfig(Qt6WaylandClient) >= %{qt6_minver}
BuildRequires:  pkgconfig(Qt6Widgets) >= %{qt6_minver}
BuildRequires:  pkgconfig(wayland-client)

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -n %{name}-v%{version}

%if 0%{?rhel} && 0%{?rhel} < 10
# Drop unsupported attribute
sed -e '/<url type="vcs-browser">.*/d' -i resources/dev.serebit.Waycheck.metainfo.xml
%endif

%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/waycheck
%{_datadir}/applications/dev.serebit.Waycheck.desktop
%{_metainfodir}/dev.serebit.Waycheck.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/dev.serebit.Waycheck.svg

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Thu Sep 28 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.2.0-1
- Update to v0.2.0

* Mon Sep 25 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.1.3-1
- Update to v0.1.3

* Mon Sep 25 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.1-1
- Update to v0.1 final

* Sun Sep 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.1~202309242217.gitdb7f195-1
- New git snapshot

* Sun Sep 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.1~202309242146.git79cc28b-1
- New git snapshot

* Sun Sep 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.1~202309242112.gitc8cdc75-2
- Consistently use pkgconfig() deps

* Sun Sep 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.1~202309242112.gitc8cdc75-1
- Initial package
