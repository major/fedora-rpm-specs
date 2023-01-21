Name:       libguess
Version:    1.2
Release:    18%{?dist}
Summary:    High-speed character set detection library
License:    BSD
URL:        https://github.com/kaniini/libguess

# Upstream website no longer existing, git repository has no tags.
# Relese 1.2 matches with commit 86db073fafa2686de30d3d3e081e39e854e774a3.
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  make

%description
libguess employs discrete-finite automata to deduce the character set of the
input buffer. The advantage of this is that all character sets can be checked in
parallel, and quickly. Right now, libguess passes a byte to each DFA on the same
pass, meaning that the winning character set can be deduced as efficiently as
possible.

libguess is fully reentrant, using only local stack memory for DFA operations.

%package devel
Summary:    Files needed for developing with %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the files that are needed when building software that uses
%{name}.

%prep
%autosetup

sed -i '\,^.SILENT:,d' buildsys.mk.in

%build
%configure
%make_build

%install
%make_install

%check
cd src/tests/testbench
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make

%{?ldconfig_scriptlets}

%files
%license COPYING
%doc README
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.*

%files devel
%{_libdir}/%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Simone Caronni <negativo17@gmail.com> - 1.2-16
- Clean up SPEC file.
- Trim changelog.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
