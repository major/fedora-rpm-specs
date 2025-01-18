Name:             gawk-xml
Summary:          XML support for gawk
Version:          1.1.2
Release:          1%{?dist}
# Automatically converted from old format: GPL+ and GPLv3+ - review is highly recommended.
License:          GPL-1.0-or-later AND GPL-3.0-or-later

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
# rpmbuild finds the expat dependency automatically
#Requires:        expat
BuildRequires:    gawk-devel
BuildRequires:    gcc
BuildRequires:    gawkextlib-devel
BuildRequires:    expat-devel

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
%{name} provides the gawk XML extension module, as well as the xmlgawk script
and some gawk include libraries for enhanced XML processing.

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

# Install NLS language files:
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS
%doc *.xml
%{_infodir}/*.info*
%{_libdir}/gawk/xml.so
%{_bindir}/xmlgawk
%{_datadir}/awk/*
%{_mandir}/man1/*
%{_mandir}/man3/*

# =============================================================================

%changelog
* Thu Jan 16 2025 Andrew Schorr <ajschorr@fedoraproject.org> - 1.1.2-1
- Upgrade to release 1.1.2 containing a minor packaging fix

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.1-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 14 2024 Andrew Schorr <ajschorr@fedoraproject.org> - 1.1.1-15
- Update BuildRequires gawk(abi) to indicate compatibility with gawk 5.3 major
  api version 4

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Andrew Schorr <ajschorr@fedoraproject.org> - 1.1.1-5
- Update BuildRequires gawk(abi) to indicate compatibility with gawk 5 major
  api version 3

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.1.1-4
- Remove obsolete requirements for %%post/%%preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Andrew J. Schorr <ajschorr@fedoraproject.org> - 1.1.1-1
- Upgrade to release 1.1.1 containing minor packaging fixes
- Remove Requires: expat, since rpmbuild finds this dependency automatically
- Add BuildRequires: gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 Andrew Schorr <ajschorr@fedoraproject.org> - 1.1.0-1
- Update to new upstream release with support for gawk API version 2

* Sat Jul 23 2016 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.7-1
- Rebuilt for new release

* Thu Oct 30 2014 Andrew Schorr <ajschorr@fedoraproject.org> - 1.0.0-1
- Now packaged as a separate rpm.

* Fri Aug 31 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.3.9-1
- Update a few obsolete references to xmlgawk to say gawkextlib.

* Sun Jul 22 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.3.0-1
- Rename from gawklib to gawkextlib.

* Sat Jul 21 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.2.0-1
- This version has been tested and should work.

* Thu Jul 19 2012 Andrew Schorr <ajschorr@fedoraproject.org> - 0.1.9-1
- Initial packaging.  This has not been tested and almost certainly contains
  errors.
