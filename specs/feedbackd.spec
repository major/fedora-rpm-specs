Name:           feedbackd
Version:        0.6.0
Release:        %autorelease
Summary:        Feedback library for GNOME

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://source.puri.sm/Librem5/feedbackd
Source0:        https://source.puri.sm/Librem5/feedbackd/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gmobile) >= 0.1.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(umockdev-1.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  systemd-devel
BuildRequires:  vala
BuildRequires:  dbus-daemon
BuildRequires:  systemd-rpm-macros
Requires: lib%{name}%{?_isa} = %{version}-%{release}

ExcludeArch:    i686

%description
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. It offers a library (libfeedback) and
GObject introspection bindings to ease using it from applications.

%package -n libfeedbackd
Summary: Library for %{name}

%description -n libfeedbackd
The lib%{name} package contains libraries for %{name}

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_user_post fbd-alert-slider.service

%preun
%systemd_user_preun fbd-alert-slider.service

%postun
%systemd_user_postun_with_reload fbd-alert-slider.service

%files
%{_bindir}/fbcli
%{_bindir}/fbd-theme-validate
%{_libexecdir}/feedbackd
%{_libexecdir}/fbd-ledctrl
%{_libexecdir}/fbd-alert-slider
%{_udevrulesdir}/90-feedbackd.rules
%{_datadir}/dbus-1/interfaces/org.sigxcpu.Feedback.xml
%{_datadir}/dbus-1/interfaces/org.sigxcpu.Feedback.Haptic.xml
%{_datadir}/dbus-1/services/org.sigxcpu.Feedback.service
%{_datadir}/feedbackd
%{_datadir}/glib-2.0/schemas/org.sigxcpu.feedbackd.gschema.xml
%{_userunitdir}/fbd-alert-slider.service

%files -n libfeedbackd
%{_libdir}/libfeedback-0.0.so.0
%{_libdir}/girepository-1.0/Lfb-0.0.typelib

%files devel
%{_libdir}/libfeedback-0.0.so
%{_includedir}/libfeedback-0.0/
%{_datadir}/vala/vapi/libfeedback-0.0.*
%{_datadir}/gir-1.0/Lfb-0.0.gir
%{_libdir}/pkgconfig/libfeedback-0.0.pc

%changelog
%autochangelog
