Name:           wlopm
Version:        0.1.0
Release:        %autorelease
Summary:        wlr-output-power-management-v1 client

License:        GPLv3
URL:            https://sr.ht/~leon_plickat/wlopm/
Source0:        https://git.sr.ht/~leon_plickat/wlopm/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
# Fix exec bit on the man file
# https://lists.sr.ht/~leon_plickat/public-inbox/patches/34406
Patch:          wlopm-0.1.0-Install-man-file-with-correct-permissions.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(wayland-client) >= 1.20.0
BuildRequires:  pkgconfig(wayland-scanner)

%description
Wayland output power management.
Simple client implementing zwlr-output-power-management-v1.

%prep
%autosetup -p1 -n %{name}-v%{version}


%build
%set_build_flags
%make_build


%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
