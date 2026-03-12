Name:           mactelnet
Version:        0.6.3
Release:        %autorelease
Summary:        MikroTik MAC-Telnet protocol tools

License:        GPL-2.0-or-later
URL:            https://github.com/haakonnessjoen/MAC-Telnet
Source0:        https://github.com/haakonnessjoen/MAC-Telnet/archive/refs/tags/v%{version}/MAC-Telnet-%{version}.tar.gz

BuildRequires:  automake autoconf make
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  openssl-devel
# "optional but preffered" as per upstream
BuildRequires:  libbsd-devel

%description
Console tools for connecting to, and serving, devices 
using MikroTik RouterOS MAC-Telnet protocol.
(Avoiding packaging mactelnetd for now)


%prep
%autosetup -n MAC-Telnet-%{version}


%build
autoreconf -i
# Do not package mactelenetd for now. Needs proper security considerations.
%configure --without-mactelnetd --without-config
%make_build


%install
%make_install


%find_lang %{name}

%files -f %{name}.lang
%doc README.markdown
%license LICENSE
%{_bindir}/{mac*,mndp}
%{_mandir}/man1/{mac*,mndp}.1*


%changelog
%autochangelog
