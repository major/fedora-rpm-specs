Name:           pavucontrol
Version:        5.0
Release:        %autorelease
Summary:        Volume control for PulseAudio

License:        GPLv2+
URL:            http://freedesktop.org/software/pulseaudio/%{name}
Source0:        http://freedesktop.org/software/pulseaudio/%{name}/%{name}-%{version}.tar.xz
Source1:        org.pulseaudio.pavucontrol.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  lynx
BuildRequires:  make
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(sigc++-2.0)

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK based volume control
tool ("mixer") for the PulseAudio sound server. In contrast to classic mixer
tools this one allows you to control both the volume of hardware devices and
of each playback stream separately.

%prep
%autosetup -p1

%build
%configure \
  --disable-silent-rules

%make_build V=1

%install
%make_install V=1

rm -f $RPM_BUILD_ROOT%{_docdir}/pavucontrol/README
rm -f $RPM_BUILD_ROOT%{_docdir}/pavucontrol/README.html
rm -f $RPM_BUILD_ROOT%{_docdir}/pavucontrol/style.css

%find_lang %{name}

mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/pavucontrol.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.pulseaudio.pavucontrol.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc doc/README
%{_bindir}/pavucontrol
%{_datadir}/pavucontrol
%{_datadir}/applications/pavucontrol.desktop
%{_metainfodir}/org.pulseaudio.pavucontrol.appdata.xml

%changelog
%autochangelog
