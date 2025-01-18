Name:             gawk-redis
Summary:          Redis client library for gawk
Version:          1.7.8
Release:          17%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
# Note: rpmbuild should find the hiredis library dependency automatically
BuildRequires:    gawk-devel
BuildRequires:    gcc
BuildRequires:    hiredis-devel

# Make sure the API version is compatible with our source code:
BuildRequires:    gawk(abi) >= 1.1
BuildRequires:    gawk(abi) < 5.0
BuildRequires: make

# At runtime, the ABI must be compatible with the compile-time version
%global gawk_api_version %(gawk 'BEGINFILE {if (ERRNO) nextfile} match($0, /#define gawk_api_(major|minor)_version[[:space:]]+([[:digit:]]+)/, f) {v[f[1]] = f[2]} END {print (v["major"] "." v["minor"])}' /usr/include/gawkapi.h)
Requires:         gawk(abi) >= %{gawk_api_version}
Requires:         gawk(abi) < %(echo %{gawk_api_version} | gawk -F. '{printf "%d.0\n", $1+1}')

# This is the default as of Fedora 23:
%global _hardened_build 1

%description
The %{name} module provides a gawk extension library for accessing Redis
database servers using the hiredis C library API.

# =============================================================================

%prep
%autosetup

%build
%configure
%make_build

%check
make check

%install
%make_install

# The */dir file is not necessary for info pages to work correctly...
rm -f %{buildroot}%{_infodir}/dir

# Install NLS language files, if translations are present:
#%find_lang %{name}

# if translations are present: %files -f %{name}.lang
%files
%license COPYING
%doc NEWS
%doc doc/README.md
%{_libdir}/gawk/redis.so

# =============================================================================

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.8-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 11 2024 Kevin Fenzi <kevin@scrye.com> - 1.7.8-14
- rebuild for hiredis soname bump

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 14 2024 Andrew Schorr <ajschorr@fedoraproject.org> - 1.7.8-11
- Update BuildRequires gawk(abi) to indicate compatibility with gawk 5.3 major
  api version 4

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Kevin Fenzi <kevin@scrye.com> - 1.7.8-6
- Rebuild for hiredis 1.0.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Andrew Schorr <ajschorr@fedoraproject.org> - 1.7.8-1
- Update to new upstream release

* Tue Jul 23 2019 Andrew Schorr <ajschorr@fedoraproject.org> - 1.7.4-5
- Update BuildRequires gawk(abi) to indicate compatibility with gawk 5 major
  api version 3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Andrew J. Schorr <ajschorr@fedoraproject.org> - 1.7.4-2
- Add BuildRequires: gcc

* Tue Feb 13 2018 Andrew Schorr <ajschorr@fedoraproject.org> - 1.7.4-1
- Packaged for Fedora
