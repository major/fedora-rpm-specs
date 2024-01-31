Name:          dfuzzer
Version:       2.3
Release:       %autorelease
Summary:       D-Bus fuzz testing tool

#global commit 15fcfa6b5f8109e07f06c7ada0b8690a36f91654
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

License:       GPLv3+
URL:           https://github.com/dbus-fuzzer/dfuzzer

%if %{defined commit}
Source0:       https://github.com/dbus-fuzzer/dfuzzer/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:       https://github.com/dbus-fuzzer/dfuzzer/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
BuildRequires: docbook-style-xsl
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: libxslt
BuildRequires: meson

%description
Tool for fuzz testing processes communicating through D-Bus. It can be
used to test processes connected to both, the session bus and the system
bus daemon. Dfuzzer works as a client, it first connects to the bus
daemon and then it traverses and fuzz tests all the methods provided
by a D-Bus service.

%prep
%autosetup -p1 -n %{name}-%{!?commit:%{version}}%{?commit:%{commit}}

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/dfuzzer.conf
%{_mandir}/man1/dfuzzer.1*
%doc README.md ChangeLog COPYING

%changelog
%autochangelog
