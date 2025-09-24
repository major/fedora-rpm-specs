%global         extension  screen-rotate
%global         srcname    screen-autorotate
%global         uuid       %{extension}@shyzus.github.io

Name:           gnome-shell-extension-%{srcname}
Version:        26
Release:        %autorelease
Summary:        Dynamic Screen rotation for GNOME Shell

License:        GPL-3.0-only
URL:            https://github.com/shyzus/gnome-shell-extension-%{srcname}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gnome-shell-rpm-generators
Requires:       iio-sensor-proxy
Provides:       %{extension} = %{version}-%{release}

%description
A GNOME extension to enable screen rotation regardless of touch mode.
This extension uses Mutter's D-Bus API, so it works on both X11 and Wayland.

%prep
%autosetup -n %{name}-%{version}

%build
# nothing to build

%install
# install extension files
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
cp -r %{uuid} %{buildroot}%{_datadir}/gnome-shell/extensions

%files
%license LICENSE.md
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
%autochangelog
