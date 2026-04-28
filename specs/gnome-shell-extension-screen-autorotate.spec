# This GNOME Shell extension automatically rotates the screen on laptops/tablets
# using the accelerometer (iio-sensor-proxy). It works on both X11 and Wayland.
# The extension includes a GSettings schema that must be compiled during build.

%global         extension  screen-rotate
%global         srcname    screen-autorotate
%global         uuid       %{extension}@shyzus.github.io

Name:           gnome-shell-extension-%{srcname}
Version:        29
Release:        %autorelease
Summary:        Dynamic Screen rotation for GNOME Shell

License:        GPL-3.0-only
URL:            https://github.com/shyzus/gnome-shell-extension-%{srcname}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  glib2-devel
Requires:       iio-sensor-proxy
Recommends:     gnome-shell

%description
A GNOME extension to enable screen rotation regardless of touch mode.
This extension uses Mutter's D-Bus API, so it works on both X11 and Wayland.

%prep
%autosetup -n %{name}-%{version}

%build
# Compile the GSettings schema. This creates gschemas.compiled.
if [ -d schemas ]; then
    glib-compile-schemas --strict schemas
fi

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
cp -r %{uuid} %{buildroot}%{_datadir}/gnome-shell/extensions

%check
# Ensure the extension directory exists (sanity)
test -d %{uuid}

%files
%license LICENSE.md
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
%autochangelog
