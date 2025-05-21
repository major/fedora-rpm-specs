%bcond check 1

Name:           xwayland-satellite
Version:        0.5.1
Release:        %autorelease
Summary:        Rootless Xwayland integration for Wayland compositors

SourceLicense:  MPL-2.0
# (MIT OR Apache-2.0) AND Unicode-3.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# Unlicense OR MIT
# Zlib
License:        %{shrink:
    MPL-2.0 AND
    MIT AND
    Unicode-3.0 AND
    Zlib AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
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

ExcludeArch:    %{ix86}

BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcb-cursor)

Requires:       xorg-x11-server-Xwayland

%description
xwayland-satellite grants rootless Xwayland integration to any Wayland
compositor implementing xdg_wm_base and viewporter. This is particularly
useful for compositors that (understandably) do not want to go through
implementing support for rootless Xwayland themselves.

%prep
%autosetup -n xwayland-satellite-%{version} -a1 -p1
%cargo_prep -v vendor

%build
%cargo_build -f systemd

%{cargo_license_summary -f systemd}
%{cargo_license -f systemd} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -Dpm0755 target/rpm/xwayland-satellite -t %{buildroot}%{_bindir}
install -Dpm0644 resources/xwayland-satellite.service -t %{buildroot}%{_userunitdir}

%if %{with check}
%check
# * integration tests require an active wayland session
%cargo_test -f systemd -- --lib
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
