%if 0%{?rhel}
%global bundled_rust_deps 1
%else
%global bundled_rust_deps 0
%endif

%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           gnome-tour
Version:        50.0
Release:        %autorelease
Summary:        GNOME Tour and Greeter

# * gnome-tour source code is GPL-3.0-or-later
# * welcome-fedora.svg is CC-BY-SA-3.0
# * rust crate dependencies are:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        (Apache-2.0 OR MIT) AND CC-BY-SA-3.0 AND GPL-3.0-or-later AND MIT AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Unlicense OR MIT)
URL:            https://gitlab.gnome.org/GNOME/gnome-tour
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz
# https://pagure.io/fedora-workstation/issue/175
Source1:        welcome-fedora.svg

BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
%endif

%description
A guided tour and greeter for GNOME.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%if 0%{?fedora}
# Install Fedora branding
install -p %{SOURCE1} data/resources/assets/welcome.svg
%endif

%if 0%{?bundled_rust_deps}
%cargo_prep -v vendor
%else
%cargo_prep
rm -rf vendor/
%endif


%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires
%endif


%build
%meson
%meson_build

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif


%install
%meson_install

%find_lang gnome-tour


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Tour.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Tour.desktop


%files -f gnome-tour.lang
%license LICENSE.md
%license LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%license cargo-vendor.txt
%endif
%doc NEWS README.md
%{_bindir}/gnome-tour
%{_datadir}/gnome-tour/
%{_datadir}/applications/org.gnome.Tour.desktop
%{_datadir}/dbus-1/services/org.gnome.Tour.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Tour.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Tour-symbolic.svg
%{_metainfodir}/org.gnome.Tour.metainfo.xml


%changelog
%autochangelog
