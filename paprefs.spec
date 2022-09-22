Name:           paprefs
Version:        1.2
Release:        %autorelease
Summary:        Management tool for PulseAudio

License:        GPLv2+
URL:            http://freedesktop.org/software/pulseaudio/%{name}
Source0:        http://freedesktop.org/software/pulseaudio/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtkmm30-devel
BuildRequires:  lynx
BuildRequires:  meson
BuildRequires:  pulseaudio-libs-devel

Requires:       pulseaudio-module-gsettings
Suggests:       PackageKit-session-service
Suggests:       gnome-packagekit-common

%description
PulseAudio Preferences (paprefs) is a simple GTK based configuration dialog
for the PulseAudio sound server.

%prep
%autosetup -p1

%build
%meson -Dlynx=true
%meson_build

%install
%meson_install

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%license LICENSE
%doc %{_vpath_builddir}/doc/README
%{_bindir}/paprefs
%dir %{_datadir}/paprefs
%{_datadir}/paprefs/paprefs.glade
%{_datadir}/applications/paprefs.desktop


%changelog
%autochangelog
