%global commit 41bbf185db8af3bd3443207510677ca87b2177de
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251228

Name:           gnome-shell-extension-pipewire-settings
Version:        9~git%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        Minimal PipeWire configuration menu for GNOME Shell

License:        GPL-3.0-or-later
URL:            https://github.com/gaheldev/pipewire-settings
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  gnome-shell-rpm-generators

Requires: gnome-shell(api) = 49

%description
A drop-down menu for GNOME Shell for configuring the PipeWire quantum and
sample rate values.

Setting a sample rate or buffer size will incite PipeWire to run with that
fixed value. Toggling Force Settings will force the graph to run at the
specified sample rate and buffer size unless set to dynamic. Toggling
Persist on restart will load the current configuration on restart,
however, settings can't be forced automatically on restart.

%prep
%autosetup -C

%build
# No build steps required

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/
cp -a pipewire-settings@gaheldev.github.com %{buildroot}%{_datadir}/gnome-shell/extensions/

%files
%license LICENSE.md
%doc README.md
%{_datadir}/gnome-shell/extensions/pipewire-settings@gaheldev.github.com/

%changelog
* Fri Jan 16 2026 Erich Eickmeyer <erich@ericheickmeyer.com> - 9~git20251228.41bbf18-1
- Initial release.
