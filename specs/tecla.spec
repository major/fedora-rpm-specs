%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           tecla
Version:        50.0
Release:        %autorelease
Summary:        Keyboard layout viewer

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/tecla
Source:         https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  /usr/bin/desktop-file-validate

%description
Tecla is a keyboard layout viewer. It uses GTK/Libadwaita for UI, and
libxkbcommon to deal with keyboard maps.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains a pkg-config file for
developing applications that use %{name}.


%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang tecla


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Tecla.desktop
%meson_test


%files -f tecla.lang
%license LICENSE
%doc NEWS README.md
%{_bindir}/tecla
%{_datadir}/applications/org.gnome.Tecla.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Tecla.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Tecla-symbolic.svg


%files devel
%{_datadir}/pkgconfig/tecla.pc


%changelog
%autochangelog
