Name:           raft
Version:        0.22.1
Release:        3%{?dist}
Summary:        C implementation of the Raft consensus protocol

License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://raft.readthedocs.io/
Source0:        %{URL}/archive/v%{version}.tar.gz

BuildRequires:  autoconf libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libuv)
# Breaking header change
Conflicts:      dqlite < 1.16.0-2
Conflicts:      cowsql < 1.15.4

%description
Fully asynchronous C implementation of the Raft consensus protocol. It consists
of a core part that implements the core Raft algorithm logic and a pluggable
interface defining the I/O implementation for networking and disk persistence.

%package benchmark
Summary:        Benchmark operating system disk write performance
BuildRequires:  pkgconfig(liburing)

%description benchmark
Benchmark operating system disk write performance.

%package devel
Summary:        Development libraries for raft
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and library for raft.

%package doc
Summary:        C-Raft documentation
BuildArch:      noarch
BuildRequires:  python-sphinx

%description doc
This package contains the C-Raft documentation in HTML format.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -i
%configure --disable-static --enable-benchmark
%make_build
sphinx-build -b html -d docs/_build/doctrees docs docs/_build/html

%install
%make_install
rm -f %{buildroot}%{_libdir}/libraft.la

%check
# disable parallel build
%global _smp_mflags -j1
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/libraft.so.*

%files benchmark
%license LICENSE
%{_bindir}/raft-benchmark

%files devel
%{_libdir}/libraft.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/raft.h
%{_includedir}/raft/

%files doc
%license LICENSE
%doc docs/_build/html/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 13 2024 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.22.1-1
- Update to 0.22.1

* Fri Mar 08 2024 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.22.0-1
- Update to 0.22.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.18.3-1
- Switch upstream to https://github.com/cowsql/raft
- Update to 0.18.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 08 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.17.1-1
- Update to 0.17.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 04 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.16.0-1
- Update to 0.16.0

* Sat Oct 01 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.15.0-1
- Update to 0.15.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 12 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.3-3
- Fix tests on armv7hl architecture.

* Mon Jan 24 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.3-2
- Fix tests on i686 architecture.

* Sat Jan 22 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.3-1
- Update to 0.11.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.11.2-1
- Initial import (#2017459).
