Name:           wmdocker
Version:        1.5
Release:        37%{?dist}
Summary:        KDE and GNOME2 system tray replacement docking application

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://icculus.org/openbox/2/docker/
Source0:        http://icculus.org/openbox/2/docker/docker-1.5.tar.gz

Patch0:         1.5-fix-parce_cmd_line.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libX11-devel

%description
Docker is a docking application (WindowMaker dock app) which acts as a system
tray for KDE and GNOME2. It can be used to replace the panel in either
environment, allowing you to have a system tray without running the KDE/GNOME
panel or environment.

%prep
%autosetup -n docker-%{version}


%build
%make_build CFLAGS="%{optflags}" XLIBPATH=%{_libdir}/X11


%install
%__mkdir_p %{buildroot}%{_bindir}
%make_install PREFIX=%{buildroot}/%{_prefix}
# due to package rename to prevent conflicts with docker
mv %{buildroot}/%{_bindir}/docker %{buildroot}/%{_bindir}/wmdocker


%files
%doc README
%license COPYING
%{_bindir}/wmdocker


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
