Name:           bustle
Version:        0.13.0
Release:        %autorelease
Summary:        Visualize D-Bus activity

# bustle itself is LGPL-2.1-or-later
SourceLicense:  LGPL-2.1-or-later
# statically linked Rust dependencies are:
# - (MIT OR Apache-2.0) AND Unicode-3.0
# - (MIT OR Apache-2.0) AND Unicode-DFS-2016
# - Apache-2.0 OR MIT
# - MIT
# - MIT OR Apache-2.0
# - Unlicense OR MIT
# LICENSE.dependencies contains a full license breakdown
License:        %{shrink:
    LGPL-2.1-or-later AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}

URL:            https://gitlab.gnome.org/World/bustle
Source:         %{url}/-/archive/%{version}/bustle-%{version}.tar.gz
Patch:          0001-adapt-meson-wrapper-code-for-cargo-for-compatibility.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson

Requires:       hicolor-icon-theme

%description
Bustle draws sequence diagrams of D-Bus activity, showing signal
emissions, method calls and their corresponding returns, with timestamps
for each individual event and the duration of each method call. This can
help you check for unwanted D-Bus traffic, and pinpoint why your
D-Bus-based application isn't performing as well as you like. It also
provides statistics like signal frequencies and average method call
times.

%prep
%autosetup -n bustle-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%meson
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%meson_install
%find_lang bustle

%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/org.freedesktop.Bustle.desktop

appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/org.freedesktop.Bustle.metainfo.xml

%files -f bustle.lang
%license COPYING
%license LICENSE.dependencies
%doc README.md
%doc CONTRIBUTING.md

%{_bindir}/bustle
%dir %{_datadir}/bustle
%{_datadir}/bustle/resources.gresource

%{_datadir}/applications/org.freedesktop.Bustle.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Bustle.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Bustle.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.freedesktop.Bustle{,-symbolic}.svg
%{_datadir}/metainfo/org.freedesktop.Bustle.metainfo.xml

%changelog
%autochangelog
