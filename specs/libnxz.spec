# Keep the *.la file around
# See https://fedoraproject.org/wiki/Changes/RemoveLaFiles
%global __brp_remove_la_files %nil

Name:		libnxz
Version:	0.64
Release:	7%{?dist}
Summary:	Zlib implementation for POWER processors
License:    Apache-2.0 OR GPL-2.0-or-later
Url:		https://github.com/libnxz/power-gzip
BuildRequires:	zlib-devel
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fixes for GCC 14 and zlib-ng compat usage
Patch0:         %{url}/pull/209.patch

# Be explicit about the soname in order to avoid unintentional changes.
%global soname libnxz.so.0

ExclusiveArch:	ppc64le
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	systemd-rpm-macros

# udev rules for nx-gzip dev
Requires: powerpc-utils-core > 1.3.10-2

%description
libnxz is a zlib-compatible library that uses the NX GZIP Engine available on
POWER9 or newer processors in order to provide a faster zlib/gzip compression
without using the general-purpose cores.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains header files for developing application that
use %{name}.

%package	static
Summary:	Static library for %{name} development
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description	static
The %{name}-static package contains static libraries for developing
application that use %{name}.

%prep
%autosetup -p1 -n power-gzip-%{version}

%build
%configure --enable-zlib-api
%make_build

%check
# libnxz tests only work on P9 servers or newer, with Linux >= 5.8.
# This combination is not guaranteed to have at build time.  Check if
# NX GZIP engine device is available before deciding to run the tests.
if [[ -w "/dev/crypto/nx-gzip" ]]; then
	make check
fi

%install
%make_install

%pre
%{_sbindir}/groupadd -r -f nx-gzip

%files
%{_libdir}/%{soname}
%{_libdir}/libnxz.so.0.%{version}
%license %{_docdir}/%{name}/APACHE-2.0.txt
%license %{_docdir}/%{name}/gpl-2.0.txt
%doc README.md

%files devel
%{_includedir}/libnxz.h
%{_libdir}/libnxz.so

%files static
%{_libdir}/libnxz.a
%{_libdir}/libnxz.la

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 26 2022 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 0.64-1
- Update to libnxz 0.64.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 0.63-4
- Fix an issue that caused premature fallback to software.

* Tue Jun 14 2022 Jakub Čajka <jcajka@redhat.com> - 0.63-3
- Move udev rule to the powerpc-utils-core

* Thu Apr 14 2022 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 0.63-2
- Backport fixes from upstream.
- Create the nx-gzip group and add udev rules.

* Fri Mar 04 2022 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 0.63-1
- Update to libnxz 0.63.
- Fix the soname to the right string.
- Properly list the dual-licensing scenario of the project.

* Wed Jan 26 2022 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 0.62-4
- Fix issue with GCC 12.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 03 2021 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 0.62-2
- Enable tests if the NX GZIP engine is available.

* Mon Aug 16 2021 Raphael Moreira Zinsly <rzinsly@linux.ibm.com> - 0.62-1
- Update version.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 0.61-2
- Fix release version and match with changelog.

* Tue Oct 27 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 0.61-0
- Initial packaging
