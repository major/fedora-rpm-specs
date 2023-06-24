Name:           kfc
Version:        0.1.4
Release:        %autorelease
Summary:        Terminal-emulator color palette setter written in POSIX C99

License:        MIT
URL:            https://github.com/mcpcpc/kfc
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Remove unneeded -lX11 from Makefile
Patch:          %{url}/commit/5c8017255c976ca47bd027dda76df3e07010f667.patch

BuildRequires:  gcc
BuildRequires:  make

%description
kfc ("KISS for colors") is a terminal-emulator color palette setter written in
POSIX C99. This allows one to achieve consistent colors across all terminal
utilities and applications.

%prep
%autosetup

%build
%make_build \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{build_ldflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README docs
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
%autochangelog
