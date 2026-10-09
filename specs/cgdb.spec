Name:           cgdb
Version:        0.8.0
Release:        %autorelease
Summary:        CGDB is a curses-based interface to the GNU Debugger (GDB)

License:        GPL-2.0-only
URL:            https://cgdb.github.io/
Source0:        https://github.com/cgdb/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://cgdb.github.io/images/screenshot_debugging.png

Patch:          cgdb-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  texinfo
BuildRequires:  flex
BuildRequires:  make

Requires:       gdb


%description
CGDB is a curses-based interface to the GNU Debugger (GDB).
The goal of CGDB is to be lightweight and responsive; not encumbered with
unnecessary features.
The interface is designed to deliver the familiar GDB text interface,
with a split screen showing the source as it executes.
The UI is modeled on the classic Unix text editor, vi.
Those familiar with vi should feel right at home using CGDB.


%prep
%autosetup -p1
# Avoid re-running configure.
touch -r aclocal.m4 config/*.m4 configure

%build
autoconf
%configure
%make_build


%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir



%files
%doc AUTHORS NEWS ChangeLog
%license COPYING
%{_bindir}/cgdb
%{_datadir}/cgdb
%{_infodir}/cgdb.info.*

%changelog
%autochangelog
