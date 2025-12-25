%bcond check 1

Name:           xwayland-satellite
Version:        0.8
Release:        %autorelease
Summary:        Rootless Xwayland integration for Wayland compositors

SourceLicense:  MPL-2.0
# (MIT OR Apache-2.0) AND Unicode-3.0
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# BSD-3-Clause OR MIT OR Apache-2.0
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    MPL-2.0 AND
    Apache-2.0 AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (BSD-3-Clause OR MIT OR Apache-2.0) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/Supreeeme/xwayland-satellite
Source0:        %{url}/archive/v%{version}/xwayland-satellite-%{version}.tar.gz
Source1:        xwayland-satellite-%{version}-vendor.tar.xz

# * fix executable path in systemd unit:
#   the executable gets installed to /usr/bin, not /usr/local/bin
Patch:          0001-fix-executable-path-in-systemd-unit.patch
# * allow loading window decoration font at runtime instead of embedding it:
#   https://github.com/Supreeeme/xwayland-satellite/pull/327
Patch:          0001-optionally-load-decoration-font-at-runtime-instead-o.patch

ExcludeArch:    %{ix86}

BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcb-cursor)

Requires:       xorg-x11-server-Xwayland
Requires:       font(opensans)

%description
xwayland-satellite grants rootless Xwayland integration to any Wayland
compositor implementing xdg_wm_base and viewporter. This is particularly
useful for compositors that (understandably) do not want to go through
implementing support for rootless Xwayland themselves.

%prep
%autosetup -n xwayland-satellite-%{version} -a1 -p1
%cargo_prep -v vendor
# remove vendored decoration font
rm OpenSans-Regular.ttf

%build
%cargo_build -f systemd,fontconfig

%{cargo_license_summary -f systemd,fontconfig}
%{cargo_license -f systemd,fontconfig} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -Dpm0755 target/rpm/xwayland-satellite -t %{buildroot}%{_bindir}
install -Dpm0644 resources/xwayland-satellite.service -t %{buildroot}%{_userunitdir}

%if %{with check}
%check
# * integration tests require an active wayland session
%cargo_test -f systemd,fontconfig -- --lib
%endif

%post
%systemd_user_post xwayland-satellite.service

%preun
%systemd_user_preun xwayland-satellite.service

%postun
%systemd_user_postun_with_reload xwayland-satellite.service

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/xwayland-satellite
%{_userunitdir}/xwayland-satellite.service

%changelog
%autochangelog
