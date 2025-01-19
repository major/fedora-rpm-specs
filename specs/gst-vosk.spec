Name:  gst-vosk
Version:  0.3.1
Release:  2%{?dist}
Summary:  GStreamer plugin for VOSK voice recognition engine
# gst-vosk has build dependency on vosk-api-devel which depends on 64-bit systems
ExclusiveArch:  x86_64 aarch64 ppc64le
License:  LGPL-2.1-only
URL:      https://github.com/PhilippeRo/gst-vosk
Source0:  https://github.com/PhilippeRo/gst-vosk/archive/refs/tags/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gstreamer1-devel
BuildRequires:  glib2-devel
BuildRequires:  gettext
BuildRequires:  vosk-api-devel

Requires:  vosk-api-devel

%description
GStreamer plugin for VOSK voice recognition engine

%prep
%autosetup
# remove prebuilt libvosk
rm -f vosk/libvosk.so 
sed -i "/install_data('libvosk.so', install_dir : get_option('libdir'))/d" vosk/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%{_libdir}/gstreamer-1.0/libgstvosk.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 20 2024 Manish Tiwari <matiwari@redhat.com> 0.3.1-1
- Initial release of the package
