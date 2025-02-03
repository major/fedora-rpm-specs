%bcond check 1
%global debug_package %{nil}

# https://github.com/linuxdeepin/dde-daemon
%global goipath         github.com/linuxdeepin/dde-daemon
Version:                6.0.43
%global tag             %{version}

%gometa -L

Name:           deepin-daemon
Release:        %autorelease
Summary:        Daemon handling the DDE session settings
License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        %{gosource}

# upstream default mono font set to 'Noto Mono', which is not yet available in
# Fedora. We change to 'Noto Sans Mono'
Source1:        fontconfig.json
Source2:        deepin-daemon.sysusers

Patch0:         https://gitlab.archlinux.org/archlinux/packaging/packages/deepin-daemon/-/raw/main/deepin-daemon-fix-vanilla-libinput.patch

# accord with ddcutil
ExcludeArch:    s390x

BuildRequires:  python3
BuildRequires:  deepin-gettext-tools
BuildRequires:  fontpackages-devel
BuildRequires:  librsvg2-tools
BuildRequires:  pam-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  libnl3-devel
BuildRequires:  libgudev-devel
BuildRequires:  libinput-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libXcursor-devel
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3-gobject
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  pkgconfig(ddcutil)
# for test
BuildRequires:  deepin-desktop-base
BuildRequires:  deepin-desktop-schemas
BuildRequires:  gcc-c++

Requires:       bamf-daemon
Requires:       bluez-obexd
Requires:       gnome-keyring
Requires:       deepin-desktop-base
Requires:       deepin-desktop-schemas
Requires:       deepin-session-ui
Requires:       deepin-polkit-agent
Requires:       rfkill
Requires:       gvfs
Requires:       iw
Requires:       lightdm
Requires:       xsettingsd

Recommends:     lshw
Recommends:     iso-codes
Recommends:     imwheel
Recommends:     %{_bindir}/xmodmap
Recommends:     mobile-broadband-provider-info
Recommends:     google-noto-mono-fonts
Recommends:     google-noto-sans-fonts
Recommends:     google-noto-sans-mono-fonts

%description
Daemon handling the DDE session settings

%gopkg

%prep
%goprep -A
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

sed -i 's|${DESTDIR}/lib/udev|${DESTDIR}$(PREFIX)/lib/udev|' Makefile
sed -i 's|${DESTDIR}/lib/systemd|${DESTDIR}$(PREFIX)/lib/systemd|' Makefile
sed -i 's|/etc/modules-load.d|/usr/lib/modules-load.d|g' Makefile

sed -i 's|lib/NetworkManager|libexec|' network/utils_test.go

sed -i 's|/etc/os-version|/etc/uos-version|' keybinding/shortcuts/shortcut_manager.go

sed -i "s|/usr/share/dde/zoneinfo/zone1970.tab|$(pwd)/misc/zoneinfo/zone1970.tab|" \
    timedate1/zoneinfo/zone.go

# Fix grub.cfg path
sed -i 's|boot/grub|boot/grub2|' grub2/{grub2,grub_params}.go

# Replace reference of google-chrome to chromium-browser
sed -i 's/google-chrome/chromium-browser/g' misc/dde-daemon/mime/data.json

%build
export GOPATH="$(pwd)/gopath:%{gopath}"
export %{gomodulesmode}
%make_build -C network/nm_generator gen-nm-code

# build different golang binaries with different build-id
make prepare

for cmd in bin/* ; do
  if ! [ -f $cmd/main.c ]; then
    %gobuild -o out/bin/$(basename $cmd) github.com/linuxdeepin/dde-daemon/$cmd
  fi
done

BUILDID="0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"
%make_build GO_BUILD_FLAGS=-trimpath GOBUILD="go build -compiler gc -ldflags \"-B $BUILDID\""

%install
BUILDID="0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"
export GOPATH="$(pwd)/build:%{gopath}"
export %{gomodulesmode}
%make_install GOBUILD="go build -compiler gc -ldflags \"-B $BUILDID\""

# Install sysusers.d configuration
install -Dm644 %{SOURCE2} %{buildroot}%{_sysusersdir}/deepin-daemon.conf

# fix systemd/logind config
install -d %{buildroot}%{_prefix}/lib/systemd/logind.conf.d/
cat > %{buildroot}%{_prefix}/lib/systemd/logind.conf.d/10-deepin-daemon.conf <<EOF
[Login]
HandlePowerKey=ignore
HandleSuspendKey=ignore
EOF

# install default settings
install -Dm644 %{SOURCE1} \
    %{buildroot}%{_datadir}/deepin-default-settings/fontconfig.json

# install systemd service file
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/deepin-accounts1-daemon.service

%find_lang dde-daemon


%if %{with check}
%check
%gocheck -d session/eventlog -d accounts1 -d accounts1/users
%endif

%post
%systemd_post deepin-accounts1-daemon.service
if [ $1 -ge 1 ]; then
  systemd-sysusers deepin-daemon.conf
  %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
    x-terminal-emulator %{_prefix}/lib/deepin-daemon/default-terminal 30
fi

%preun
%systemd_preun deepin-accounts1-daemon.service
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove x-terminal-emulator \
    %{_prefix}/lib/deepin-daemon/default-terminal
fi

%postun
%systemd_postun_with_restart deepin-accounts1-daemon.service
if [ $1 -eq 0 ]; then
  rm -f /var/cache/deepin/mark-setup-network-services
  rm -f /var/log/deepin.log
fi

%files -f dde-daemon.lang
%doc README.md
%license LICENSE
%dir %{_libexecdir}/dde-daemon/
%dir %{_libexecdir}/dde-daemon/keybinding
%{_libexecdir}/dde-daemon/keybinding/shortcut-dde-grand-search.sh
%{_prefix}/lib/deepin-daemon/
%{_prefix}/lib/systemd/logind.conf.d/10-deepin-daemon.conf
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/deepin/scheduler/config.json
%{_datadir}/dde-daemon/
%{_datadir}/dde/data/
%{_datadir}/dde/zoneinfo/zone1970.tab
%{_datadir}/deepin-default-settings/fontconfig.json
%dir %{_datadir}/dsg/configs/org.deepin.dde.daemon
%{_datadir}/dsg/configs/org.deepin.dde.daemon/org.deepin.dde.daemon.*.json
%{_datadir}/icons/hicolor/*/status/dialog-window-scale.png
%{_datadir}/icons/hicolor/scalable/status/dialog-window-scale.svg
%{_unitdir}/deepin-accounts1-daemon.service
%{_userunitdir}/*.service
%{_userunitdir}/dde-session-initialized.target.wants/org.dde.session.Daemon1.service
%{_var}/lib/polkit-1/localauthority/10-vendor.d/*.pkla
%{_udevrulesdir}/80-deepin-fprintd.rules
%{_sysusersdir}/deepin-daemon.conf
%{_sysconfdir}/acpi/actions/deepin_lid.sh
%{_sysconfdir}/acpi/events/deepin_lid
%{_sysconfdir}/pam.d/deepin-auth-keyboard
%{_sysconfdir}/NetworkManager/conf.d/deepin.dde.daemon.conf
%{_sysconfdir}/pulse/daemon.conf.d/10-deepin.conf
%exclude %{_sysconfdir}/deepin/grub2_edit_auth.conf
%exclude %{_sysconfdir}/default/grub.d/10_deepin.cfg

%changelog
%autochangelog
