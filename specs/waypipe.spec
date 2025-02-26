Name:		waypipe
Version:	0.9.1
Release:	%autorelease
Summary:	Wayland forwarding proxy

License:	MIT
URL:		https://gitlab.freedesktop.org/mstoeckl/%{name}
Source0:	https://gitlab.freedesktop.org/mstoeckl/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:	waypipe.1

BuildRequires:	gcc
BuildRequires:	meson
%if !0%{?rhel}
BuildRequires:	scdoc
%endif
BuildRequires:	pkgconfig(gbm)
%if !0%{?rhel}
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libswscale)
%endif
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)

%description
Waypipe is a proxy for Wayland clients. It forwards Wayland messages and
serializes changes to shared memory buffers over a single socket. This makes
application forwarding similar to "ssh -X" feasible.


%prep
%autosetup -n %{name}-v%{version}


%build
%meson -Dwerror=false %{?rhel:-Dwith_video=disabled -Dman-pages=disabled}
%meson_build


%install
%meson_install
%if 0%{?rhel}
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
%endif


%check
%meson_test


%files
%{_bindir}/waypipe
%{_mandir}/man1/waypipe.1*
%doc CONTRIBUTING.md README.md
%license COPYING


%changelog
%autochangelog
