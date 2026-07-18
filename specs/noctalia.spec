%define basever     5.0.0
%define prerel      beta
%define prerelnum   3
%define tag         v%{basever}-%{prerel}.%{prerelnum}

Name:           noctalia
Version:        %{basever}~%{prerel}.%{prerelnum}
Release:        %autorelease
ExcludeArch:    %{ix86}
Summary:        Sleek and minimal desktop shell thoughtfully crafted for Wayland

# The main source code is MIT.  Other licenses:
# Apache-2.0:
#   third_party/material_color_utilities
# BSD-3-Clause:
#   protocols/hyprland-focus-grab-v1.xml
#   protocols/hyprland-toplevel-mapping-v1.xml
# HPND-sell-variant:
#   protocols/text-input-unstable-v3.xml
#   protocols/wlr-data-control-unstable-v1.xml
#   protocols/wlr-foreign-toplevel-management-unstable-v1.xml
#   protocols/wlr-gamma-control-unstable-v1.xml
#   protocols/wlr-layer-shell-unstable-v1.xml
# LGPL-2.1-or-later:
#   protocols/org-kde-plasma-virtual-desktop.xml
# MIT:
#   assets/fonts/tabler.ttf
#   third_party/fzy
#   third_party/luau
# Apache-2.0 AND MIT:
#   third_party/wuffs
# MIT-0 OR Unlicense:
#   third_party/dr_wav
License:        Apache-2.0 AND MIT AND BSD-3-Clause AND HPND-sell-variant AND LGPL-2.1-or-later AND (MIT-0 OR Unlicense)
URL:            https://noctalia.dev
Source:         https://github.com/noctalia-dev/noctalia/archive/%{tag}/noctalia-%{tag}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(wireplumber-0.5)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pam-devel
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(md4c)
BuildRequires:  json-static
BuildRequires:  stb_image_resize2-static
BuildRequires:  stb_image_write-static

# Needed by plugin_git_export_test
BuildRequires:  git-core

# For desktop-file-validate command
BuildRequires:  desktop-file-utils

# For ownership of icon parent directories
Requires:       hicolor-icon-theme

# Noctalia will segfault at startup if it cannot connect to the pipewire daemon
Requires:       pipewire

# The plugin system uses git at runtime as well
Requires:       git-core

# Optional requirements for various functionality
Recommends:     upower
Recommends:     ddcutil
Recommends:     wtype

# Upstream doesn't currently offer a mechanism for building against system
# copies of these libraries.
Provides:       bundled(dr_wav)
Provides:       bundled(fzy)
Provides:       bundled(luau)
Provides:       bundled(material_color_utilities)
Provides:       bundled(wuffs)


%description
Noctalia is a native Wayland desktop shell for people who want a polished,
configurable Linux desktop without stitching together a separate bar, launcher,
notification daemon, lock screen, wallpaper tool, and settings UI.


%prep
%autosetup -p 1 -n noctalia-%{basever}-%{prerel}.%{prerelnum}

# Upstream uses a git describe command to determine part of the --version
# output.  Since we're not building from a git checkout, we can change the
# fallback value to set this instead.
sed -e '/fallback/ s/unknown/%{tag}/' -i meson.build

# Remove shebangs and execute permissions from template apply scripts to avoid
# rpmlint errors/warnings.
find assets/templates -type f -regextype egrep -regex '.*\.(sh|py)' \
    -exec sed -e '1 {/^#!/d}' -i '{}' + \
    -exec chmod -x '{}' +

# Move bundled licenses to the top level to make inclusion in %%files easier.
mv assets/fonts/tabler-icons-license.txt        LICENSE.tabler
mv third_party/dr_wav/LICENSE                   LICENSE.dr_wav
mv third_party/fzy/LICENSE                      LICENSE.fzy
mv third_party/luau/LICENSE.txt                 LICENSE.luau
mv third_party/luau/lua_LICENSE.txt             LICENSE.luau_lua
mv third_party/material_color_utilities/LICENSE LICENSE.material_color_utilities
mv third_party/wuffs/LICENSE-APACHE             LICENSE-Apache-2.0.wuffs
mv third_party/wuffs/LICENSE-MIT                LICENSE-MIT.wuffs


%conf
%meson -Dtests=enabled


%build
%meson_build


%install
%meson_install


%check
%meson_test

desktop-file-validate %{buildroot}%{_datadir}/applications/dev.noctalia.Noctalia.desktop


%files
%license LICENSE*
%{_bindir}/noctalia
%{_datadir}/applications/dev.noctalia.Noctalia.desktop
%{_datadir}/icons/hicolor/scalable/apps/noctalia.svg
%{_datadir}/noctalia


%changelog
%autochangelog
