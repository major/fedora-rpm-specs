Name: htop
Version: 3.2.1
Release: %autorelease
Summary: Interactive process viewer
License: GPLv2+
URL: http://hisham.hm/htop/
Source0: https://github.com/htop-dev/htop/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: ncurses-devel
%if 0%{?rhel} >= 8
BuildRequires: platform-python
BuildRequires: /usr/bin/pathfix.py
%else
BuildRequires: python
%endif
BuildRequires: libtool
BuildRequires: make
BuildRequires: lm_sensors-devel

%description
htop is an interactive text-mode process viewer for Linux, similar to
top(1).

%prep
%autosetup -p1

%if 0%{?rhel} >= 8
pathfix.py -pni "/usr/libexec/platform-python" scripts/
%endif

%build
autoreconf -vfi

%configure \
	--enable-openvz \
	--enable-vserver \
	--enable-taskstats \
	--enable-unicode \
	--with-sensors \
	--enable-cgroup

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
