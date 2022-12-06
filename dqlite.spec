Name:           dqlite
Version:        1.12.0
Release:        1%{?dist}
Summary:        Embeddable, replicated and fault tolerant SQL engine

License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://github.com/canonical/dqlite
Source0:        %{URL}/archive/v%{version}.tar.gz

BuildRequires:  autoconf libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(raft) >= 0.16.0
BuildRequires:  pkgconfig(sqlite3)

%description
dqlite is a C library that implements an embeddable and replicated SQL database
engine with high-availability and automatic failover.

%package devel
Summary:        Development libraries for dqlite
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and library for dqlite.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -i
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libdqlite.la

%check
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/libdqlite.so.*

%files devel
%{_libdir}/libdqlite.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h

%changelog
* Sun Dec 04 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.12.0-1
- Update to 1.12.0

* Sun Oct 02 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.11.1-1
- Update to 1.11.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 27 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.9.1-1
- Update to 1.9.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.9.0-1
- Initial import (#2017476).
