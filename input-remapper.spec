Name:           input-remapper
Version:        2.0.0
Release:        %autorelease
Summary:        An easy to use tool to change the behaviour of your input devices

License:        GPL-3.0-or-later
URL:            https://github.com/sezanzeb/%{name}
Source0:        %{url}/archive/master/%{name}-%{version}.tar.gz
Source1:        README.Fedora
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pyproject-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  gettext
Requires:       gtksourceview4

%generate_buildrequires
%pyproject_buildrequires -r


%description
An easy to use tool to change the mapping of your input device buttons. 
Supports mice, keyboards, gamepads, X11, Wayland, combined buttons and 
programmable macros. Allows mapping non-keyboard events (click, joystick, 
wheel) to keys of keyboard devices.
The program works at the evdev interface level, by filtering and redirecting 
the output of physical devices to that of virtual ones.


%prep
%autosetup -p1 -n %{name}-%{version}
cp %{SOURCE1} ./
#Fix rpmlint errors
#find inputremapper/ -iname "*.py" -type f -print0 | xargs -0 sed -i -e 's+\s*#\s*!/usr/bin/python3++'


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files inputremapper
mv %{buildroot}%{python3_sitelib}/etc %{buildroot}/etc
mv %{buildroot}%{python3_sitelib}/usr/bin %{buildroot}/usr/bin
mv %{buildroot}%{python3_sitelib}/usr/lib/systemd %{buildroot}/usr/lib/systemd
mv %{buildroot}%{python3_sitelib}/usr/lib/udev %{buildroot}/usr/lib/udev
mv %{buildroot}%{python3_sitelib}/usr/share %{buildroot}/usr/share
mkdir -p %{buildroot}/usr/share/dbus-1/system.d/
mv %{buildroot}/etc/dbus-1/system.d/inputremapper.Control.conf %{buildroot}/usr/share/dbus-1/system.d/

# clean up duplicate files
rm %{buildroot}%{_datadir}/%{name}/inputremapper.Control.conf
rm %{buildroot}%{_datadir}/%{name}/io.github.sezanzeb.input_remapper.metainfo.xml
rm %{buildroot}%{_datadir}/%{name}/%{name}-gtk.desktop
rm %{buildroot}%{_datadir}/%{name}/%{name}.policy


%post -n %{name}
%systemd_post %{name}.service


%preun -n %{name}
%systemd_preun %{name}.service


%postun -n %{name}
%systemd_postun_with_restart %{name}.service


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-gtk.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files -f %{pyproject_files}
%doc README.md README.Fedora
%license LICENSE
%{_datadir}/dbus-1/system.d/inputremapper.Control.conf
%{_sysconfdir}/xdg/autostart/%{name}-autoload.desktop
%{_bindir}/%{name}*
%{_unitdir}/%{name}.service
%{_udevrulesdir}/99-%{name}.rules
%{_datadir}/%{name}
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/polkit-1/actions/%{name}.policy
%{_metainfodir}/*.metainfo.xml


%changelog
%autochangelog
