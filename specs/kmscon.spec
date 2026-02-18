Name:           kmscon
Version:        9.3.2
Release:        %autorelease
Summary:        Linux KMS/DRM based virtual Console Emulator
License:        MIT
URL:            https://github.com/kmscon/kmscon/
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  check-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  libtsm-devel >= 4.4.0
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  xsltproc
BuildRequires:  xz
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 172
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0

# Fix agetty launch option
Patch20: 0001-kmsconvt-fix-agetty-launch-option.patch

%description
Kmscon is a simple terminal emulator based on linux kernel mode setting (KMS).
It is an attempt to replace the in-kernel VT implementation with a userspace
console.

%package pango
Summary: This adds pango support to kmscon
Requires: %{name}%{?_isa} = %{version}-%{release}

%description pango
This package provide the pango plugin to kmscon
mod-pango.so

%package gl
Summary: This adds opengl support to kmscon
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gl
This package provides 2 plugins for kmscon:
mod-drm3d.so
mod-gltex.so

%prep
%autosetup -p1

%conf
%meson -Dmulti_seat=disabled -Dvideo_fbdev=disabled

%build
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_post kmscon.service
%systemd_post kmsconvt@.service

%preun
%systemd_preun kmscon.service
%systemd_preun kmsconvt@.service

%postun
%systemd_postun_with_reload kmscon.service
%systemd_postun_with_reload kmsconvt@.service

%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/kmscon-launch-gui
%{_libdir}/kmscon/mod-unifont.so
%dir %{_libexecdir}/kmscon
%{_libexecdir}/kmscon/kmscon
%{_mandir}/man1/kmscon.1*
%{_mandir}/man5/kmscon.conf.5*
%{_unitdir}/kmscon.service
%{_unitdir}/kmsconvt@.service
%config /etc/kmscon/kmscon.conf.example

%files pango
%{_libdir}/kmscon/mod-pango.so

%files gl
%{_libdir}/kmscon/mod-drm3d.so
%{_libdir}/kmscon/mod-gltex.so

%changelog
%autochangelog

