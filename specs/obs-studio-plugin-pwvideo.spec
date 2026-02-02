Name:           obs-studio-plugin-pwvideo
Version:        0.1.0
Release:        %autorelease
Summary:        Generic PipeWire video source for OBS Studio

License:        GPL-2.0-or-later
URL:            https://github.com/hoshinolina/obs-pwvideo
Source0:        %{url}/archive/%{version_no_tilde}/obs-pwvideo-%{version_no_tilde}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.22
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gl)

Requires:       obs-studio%{?_isa}
Supplements:    obs-studio%{?_isa}


%description
Generic PipeWire video source for OBS.
Useful for routing arbitrary video streams into
your scenes.

%prep
%autosetup -C

%conf
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -GNinja

%build
%cmake_build

%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/obs-plugins/obs-pwvideo.so
%{_datadir}/obs/obs-plugins/obs-pwvideo/


%changelog
%autochangelog
