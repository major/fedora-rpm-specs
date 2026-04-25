%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           gnome-2048
Version:        50.2
Release:        %autorelease
Summary:        A 2048 clone for GNOME

# gnome-2048: GPL-3.0-or-later
# Rust dependencies:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
    GPL-3.0-or-later AND
    ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND
    (Apache-2.0 OR MIT) AND
    (MIT) AND (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown
URL:            https://wiki.gnome.org/Apps/2048
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

Patch:          0001-fix-build-options-for-rpm.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
%endif

BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Provides:       bundled(libgnome-games-support)

%description
A GNOME clone of the popular game 2048
http://en.wikipedia.org/wiki/2048_(video_game)


%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

rm -rf vendor
%cargo_prep
%generate_buildrequires
%cargo_generate_buildrequires -t -a


%build
%meson -Dprofile=rpm
%meson_build

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
%meson_install
%find_lang %{name} --with-gnome
%find_lang gnome-2048_libgnome-games-support --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop


%files -f %{name}.lang -f gnome-2048_libgnome-games-support.lang
%doc README.md code-of-conduct.md
%license COPYING
%license LICENSE.dependencies
%{_bindir}/gnome-2048
%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop
%{_datadir}/dbus-1/services/org.gnome.TwentyFortyEight.service
%{_datadir}/glib-2.0/schemas/org.gnome.TwentyFortyEight.gschema.xml
%{_datadir}/metainfo/org.gnome.TwentyFortyEight.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.TwentyFortyEight*
%{_mandir}/man6/gnome-2048*


%changelog
%autochangelog
