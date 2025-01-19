%global commit cece62d8f565e57f74188227eddaaac212320acc
%global commitdate 20241021
%global shortcommit %{sub %{commit} 1 7}

Name:           miracle-wm-config
Version:        0~git.%{commitdate}.1.%{shortcommit}
Release:        2%{?dist}
Summary:        Miracle Window Manager system configuration

License:        GPL-3.0-or-later
URL:            https://pagure.io/fedora-miracle/miracle-wm-config
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

Requires:       desktop-backgrounds-compat
Requires:       miracle-wm >= 0.3.5
Requires:       swaybg
Requires:       swaylock
Requires:       swaync
Requires:       nwg-bar >= 0.1.6-3
Requires:       nwg-dock >= 0.4.1-3
Requires:       nwg-drawer >= 0.4.9-2
Requires:       nwg-panel >= 0.9.47

BuildArch:      noarch

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/miracle-wm
%{_datadir}/miracle-wm/default-config/

%dnl ----------------------------------------------------------------

%package -n     initial-setup-gui-wayland-miraclewm
Summary:        Miracle-WM Wayland Initial Setup GUI configuration
Provides:       firstboot(gui-backend)
Conflicts:      firstboot(gui-backend)

Requires:       xorg-x11-server-Xwayland
Requires:       initial-setup-gui >= 0.3.99
Requires:       miracle-wm >= 0.3.4
Supplements:    (initial-setup-gui and miracle-wm)

%description -n initial-setup-gui-wayland-miraclewm
This package contains configuration and dependencies for
Anaconda Initial Setup to use Miracle-WM for the display server.

%files -n initial-setup-gui-wayland-miraclewm
%license LICENSE
%{_libexecdir}/initial-setup/run-gui-backend

%dnl ----------------------------------------------------------------

%package -n     sddm-wayland-miraclewm
Summary:        Miracle-WM Wayland SDDM greeter configuration

Provides:       sddm-greeter-displayserver
Conflicts:      sddm-greeter-displayserver

Requires:       desktop-backgrounds-compat
Requires:       sddm >= 0.20.0
Requires:       layer-shell-qt
Requires:       miracle-wm >= 0.3.4

%description -n sddm-wayland-miraclewm
This package contains configuration and dependencies for SDDM
to use Miracle-WM for the greeter display server.

%files -n sddm-wayland-miraclewm
%license LICENSE
%{_prefix}/lib/sddm/sddm.conf.d/miracle-wm.conf


%dnl ----------------------------------------------------------------




%prep
%autosetup -n %{name}-%{commit}


%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/miracle-wm/
cp -av miraclewm-config %{buildroot}%{_datadir}/miracle-wm/default-config

mkdir -p %{buildroot}%{_libexecdir}/initial-setup
install -pm 0755 initial-setup/run-gui-backend %{buildroot}%{_libexecdir}/initial-setup/

mkdir -p %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d
install -pm 0644 sddm/miracle-wm.conf %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~git.20241021.1.cece62d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git.20241021.1.cece62d-1
- Bump to new git snapshot

* Mon Sep 09 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git.20240909.1.3721ee4-1
- Bump to new git snapshot

* Tue Sep 03 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git.20240903.1.7373fc2-1
- Bump to new git snapshot

* Wed Aug 28 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git.1.20240828.f8f59ac-2
- Upgrade nwg dependencies to Requires

* Wed Aug 28 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git.1.20240828.f8f59ac-1
- Bump to new git snapshot
  + miraclewm-config: Set better env vars to indicate XDG session data
- Install miraclewm-config as a full bundle of default configs

* Mon Aug 26 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git.1.20240825.13925df-1
- Bump to a new snapshot
  + sddm: Use Miracle in config-less mode
  + initial-setup: Use miracle-wm --exec

* Mon Aug 12 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git.2.20240812.f7b8c5b-1
- Bump to new snapshot

* Mon Aug 12 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git.1.20240812.486b4cb-1
- Add Anaconda Initial Setup and SDDM support

* Mon Aug 12 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git.0.20240812.16888af-1
- Initial package
