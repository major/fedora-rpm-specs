Name:           miriway
Version:        24.11
Release:        2%{?dist}
Summary:        Simple Wayland compositor built on Mir

License:        GPL-3.0-only
URL:            https://miriway.github.io/
Source0:        https://github.com/Miriway/Miriway/archive/v%{version}/Miriway-%{version}.tar.gz
Source1:        anaconda-initial-setup-run-gui-backend

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(miral) >= 5.1
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  systemd-rpm-macros
Requires:       inotify-tools
Requires:       swaybg
Requires:       xkeyboard-config
Requires:       xorg-x11-server-Xwayland

%description
Miriway is a starting point for creating a Wayland based
desktop environment using Mir.


%package        session
Summary:        Miriway desktop session
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    session
This package contains configuration and dependencies for
the basic Miriway session.


%package -n sddm-wayland-%{name}
Summary:        Miriway SDDM greeter configuration
Provides:       sddm-greeter-displayserver
Conflicts:      sddm-greeter-displayserver
Requires:       %{name} = %{version}-%{release}
Requires:       layer-shell-qt
Supplements:    (sddm and %{name})
BuildArch:      noarch

%description -n sddm-wayland-%{name}
This package contains configuration and dependencies for SDDM
to use Miriway for the Wayland compositor for the greeter.


%package -n initial-setup-gui-wayland-%{name}
Summary:        Run initial-setup GUI on Miriway
Provides:       firstboot(gui-backend)
Conflicts:      firstboot(gui-backend)
Requires:       %{name} = %{version}-%{release}
Requires:       initial-setup-gui >= 0.3.99
Supplements:    ((initial-setup or initial-setup-gui) and %{name})
Enhances:       (initial-setup-gui and %{name})
BuildArch:      noarch

%description -n initial-setup-gui-wayland-%{name}
This package contains configuration and dependencies for
the initial-setup GUI to use Miriway for the Wayland
compositor.


%prep
%autosetup -n Miriway-%{version} -S git_am

# Drop -Werror
sed -e "s/-Werror//g" -i CMakeLists.txt


%build
# Deal with some goofiness around sysconfdir
%cmake -GNinja -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} -DSDDM=ON
%cmake_build


%install
%cmake_install

# Remove miriway-unsnap as it's kind of pointless
rm -f %{buildroot}%{_bindir}/%{name}-{unconfine,unsnap}

# move sddm configuration snippet to the right place
mkdir -p %{buildroot}%{_prefix}/lib/sddm
mv %{buildroot}%{_sysconfdir}/sddm.conf.d %{buildroot}%{_prefix}/lib/sddm

# install initial-setup-gui backend script
mkdir -p %{buildroot}%{_libexecdir}/initial-setup
install -pm 0755 %{S:1} %{buildroot}%{_libexecdir}/initial-setup/run-gui-backend


%files
%doc README.md CONFIGURING_MIRIWAY.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-background
%{_bindir}/%{name}-run
%{_bindir}/%{name}-run-shell
%{_bindir}/%{name}-shell
%{_bindir}/%{name}-terminal
%dir %{_sysconfdir}/xdg/xdg-%{name}
%config(noreplace) %{_sysconfdir}/xdg/xdg-%{name}/%{name}-shell.config

%files session
%doc example-configs
%{_bindir}/%{name}-session
%{_libexecdir}/%{name}-session*
%{_datadir}/wayland-sessions/%{name}.desktop
%{_userunitdir}/%{name}-session.target

%files -n sddm-wayland-%{name}
%{_prefix}/lib/sddm/sddm.conf.d/%{name}.conf

%files -n initial-setup-gui-wayland-%{name}
%{_libexecdir}/initial-setup/run-gui-backend


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 01 2024 Neal Gompa <ngompa@fedoraproject.org> - 24.11-1
- Update to 24.11

* Thu Oct 31 2024 Neal Gompa <ngompa@fedoraproject.org> - 24.10-1
- Update to 24.10

* Wed Oct 23 2024 Neal Gompa <ngompa@fedoraproject.org> - 24.09-3
- Add SDDM and initial-setup-gui configuration packages
- Split desktop session file into its own subpackage

* Tue Oct 08 2024 Neal Gompa <ngompa@fedoraproject.org> - 24.09-2
- Add patches for miriway-run

* Tue Oct 01 2024 Neal Gompa <ngompa@fedoraproject.org> - 24.09-1
- Update to 24.09

* Sat Jun 15 2024 Neal Gompa <ngompa@fedoraproject.org> - 0^git20240613.2e88df7-1
- Bump to new git snapshot

* Mon Mar 11 2024 Neal Gompa <ngompa@fedoraproject.org> - 0^git20240306.d58ec46-1
- Intial package
