Name: htop
Version: 3.4.1
Release: %autorelease
Summary: Interactive process viewer
License: GPL-2.0-or-later
URL: https://htop.dev/
Source0: https://github.com/htop-dev/htop/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: ncurses-devel
%if 0%{?rhel} == 8
BuildRequires: platform-python
BuildRequires: /usr/bin/pathfix.py
%else
BuildRequires: python
%endif
BuildRequires: libtool
BuildRequires: make
BuildRequires: lm_sensors-devel
BuildRequires: hwloc-devel
BuildRequires: libcap-devel
BuildRequires: libnl3-devel

%description
htop is an interactive text-mode process viewer for Linux, similar to
top(1).

%prep
%autosetup -p1

%if 0%{?rhel} == 8
pathfix.py -pni "/usr/libexec/platform-python" scripts/
%endif

%build
autoreconf -vfi

%configure \
	--enable-openvz \
	--enable-vserver \
	--enable-hwloc \
	--enable-unicode \
	--enable-sensors \
	--enable-delayacct \
	--enable-capabilities

%make_build

%install
%make_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/htop
%{_datadir}/pixmaps/htop.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/htop.1*

%changelog
%autochangelog
