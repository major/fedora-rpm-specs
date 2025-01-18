%global short_version 1.4.0

%if 0%{?fedora} || 0%{?rhel} >= 8
%global with_python3_cups 1
%endif

Name: dymo-cups-drivers
Version: %{short_version}.5
Release: 22%{?dist}
Summary: DYMO LabelWriter Drivers for CUPS
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.dymo.com

Source0: http://download.dymo.com/dymo/Software/Download%20Drivers/Linux/Download/dymo-cups-drivers-%{short_version}.tar.gz#/%{name}-%{version}.tar.gz

# https://github.com/matthiasbock/dymo-cups-drivers/pull/6
Patch0: dymo-cups-drivers-fix-fsf-address.patch
# https://github.com/matthiasbock/dymo-cups-drivers/commit/2433fa303dd9925f8b36b18406863c56766c651b
Patch1: dymo-cups-drivers-replace-boolean-or-with-bitwise.patch
# https://github.com/matthiasbock/dymo-cups-drivers/commit/d7ef90a48c61c898a3d69f353673d81d7540c892
Patch2: dymo-cups-drivers-unused-var-statusok.patch
# https://github.com/matthiasbock/dymo-cups-drivers/commit/697cfb8115054fb95b9e91d54d68f47ee3805060
Patch3: dymo-cups-drivers-replace-deprecated-type.patch
# https://github.com/matthiasbock/dymo-cups-drivers/pull/7
Patch4: dymo-cups-drivers-autotools-deprecations.patch

# Patch files obtained from printer-driver-dymo Debian source package
Patch5: 0001-Inheritate-CXXFLAGS-from-the-environment-to-use-dpkg.patch
Patch6: 0002-Port-to-newer-cups-headers-ppd_file_t-is-only-define.patch
Patch7: 0005-Include-cups-sidechannel.h-for-cupsBackChannelRead-s.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cups-devel
BuildRequires: glibc-headers
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: sed
BuildRequires: make
%{?with_python3_cups:BuildRequires: python3-cups}
%{!?with_python3_cups:BuildRequires: python-cups}

Requires: cups

%description
DYMO LabelWriter and DYMO LabelMANAGER series drivers for CUPS

%prep
%autosetup -p 1

%build
autoreconf --force --install
# Must enable c++11 for el7
%{configure} CXXFLAGS="${CXXFLAGS} -std=c++11"
%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS ChangeLog README docs/ samples/
%{_cups_serverbin}/filter/*
%{_datadir}/cups/model/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.0.5-21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-10
- Fix FTBS cupsBackChannelRead was not declared in this scope

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-8
- Buildrequire python3-cups for rhel >= 8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-6
- BZ1669976: update License tag, buildrequires python3-cups

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-4
- don't own cups folders
- COPYING not needed, since content is the same as LICENSE
- fix autotools deprecration warnings

* Mon Jan 07 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-3
- fix typo calling configure macro
- add license and doc files
- use _cups_serverbin macro
- use autoreconf

* Mon Nov 26 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-2
- Add gcc buildrequires for f29

* Sat Sep 1 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-1
- Initial specfile
