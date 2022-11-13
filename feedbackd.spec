Name:           feedbackd
Version:        0.0.1
Release:        1%{?dist}
Summary:        Feedback library for GNOME

License:        GPLv3+
URL:            https://source.puri.sm/Librem5/feedbackd
Source0:        https://source.puri.sm/Librem5/feedbackd/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  systemd-devel
BuildRequires:  vala
BuildRequires:  dbus-daemon
Requires: lib%{name}%{?_isa} = %{version}-%{release}

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
install -D -m 644 debian/feedbackd.udev %{buildroot}%{_udevrulesdir}/90-feedbackd.rules


%check
%meson_test


%files
%{_bindir}/fbcli
%{_libexecdir}/feedbackd
%{_libexecdir}/fbd-ledctrl
%{_udevrulesdir}/90-feedbackd.rules
%{_datadir}/dbus-1/interfaces/org.sigxcpu.Feedback.xml
%{_datadir}/dbus-1/services/org.sigxcpu.Feedback.service
%{_datadir}/feedbackd
%{_datadir}/glib-2.0/schemas/org.sigxcpu.feedbackd.gschema.xml

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
* Fri Nov 11 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.1-1
- Update to 0.0.1

* Thu Oct 20 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.0+git20220520-1
- Update to 0.0.0+git20220520

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0+git20220208-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.0+git20220208-1
- Update to 0.0.0+git20220208

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0+git20211018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.0+git20211018-1
- Update to 0.0.0git20211018

* Mon Aug 23 2021 Kalev Lember <klember@redhat.com> - 0.0.0+git20210426-3
- BR vala instead of vala-tools

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0+git20210426-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 27 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.0+git20210426-1
- Update to v0.0.0+git20210426

* Thu Jan 28 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.0+git20210125-1
- Update to v0.0.0+git20210125

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0+git20201114-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.0+git20201114-1
- Update to v0.0.0+git20201114

* Fri Aug 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.0+git20200726-1
- Update to v0.0.0+git20200726

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0+git20200714-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Peter Robinson <pbrobinson@fedoraproject.org>
- Update to v0.0.0+git20200714
- Split libs out to libfeedbackd
- Minor spec cleanups

* Tue Jul 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.0.0+git20200707-1
- Update to v0.0.0+git20200707

* Tue Jul 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.0.0+git20200527-2
- Install udev rules

* Fri Jun 12 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.0+git20200527-1
- Update to 0.0.0+git20200527

* Sat Feb 29 2020 Nikhil Jha <hi@nikhiljha.com> - 0.0.0+git20200305-1
- Initial packaging
