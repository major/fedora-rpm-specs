Name:           pavucontrol
Version:        6.2
Release:        %autorelease
Summary:        Volume control for PulseAudio

License:        GPL-2.0-or-later
URL:            https://www.freedesktop.org/software/pulseaudio/%{name}
Source0:        https://www.freedesktop.org/software/pulseaudio/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  meson >= 0.59.0
BuildRequires:  lynx
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(sigc++-3.0)

Requires:       hicolor-icon-theme

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK based volume control
tool ("mixer") for the PulseAudio sound server. In contrast to classic mixer
tools this one allows you to control both the volume of hardware devices and
of each playback stream separately.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

rm -f $RPM_BUILD_ROOT%{_docdir}/pavucontrol/README.html
rm -f $RPM_BUILD_ROOT%{_docdir}/pavucontrol/style.css

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.pulseaudio.pavucontrol.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.pulseaudio.pavucontrol.metainfo.xml

%files -f %{name}.lang
%license LICENSE
%doc doc/README
%{_bindir}/pavucontrol
%{_datadir}/applications/org.pulseaudio.pavucontrol.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.pulseaudio.pavucontrol.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.pulseaudio.pavucontrol-symbolic.svg
%{_metainfodir}/org.pulseaudio.pavucontrol.metainfo.xml

%changelog
%autochangelog
