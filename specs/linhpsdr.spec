# git ls-remote git://github.com/g0orx/linhpsdr.git
%global git_commit 742658a9068392349ca1efc9d698dcaae541dda6
%global git_date 20210710

# git describe --abbrev=0 --tags
%global version_tag Beta
# git --no-pager show --date=short --format="%ai" --name-only | head -n 1 | cut -d' ' -f1
%global version_date 2021-02-25

%global features \\\
  SOAPYSDR_INCLUDE=SOAPYSDR

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		linhpsdr
Version:	0
Release:	0.14.%{git_suffix}%{?dist}
Summary:	An HPSDR application for Linux
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/g0orx/%{name}
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
Source1:	io.github.g0orx.LinHPSDR.metainfo.xml
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gtk3-devel
BuildRequires:	libsoundio-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	unixcw-devel
BuildRequires:	wdsp-devel
BuildRequires:	desktop-file-utils
Requires:	hicolor-icon-theme
# https://github.com/g0orx/linhpsdr/pull/107
Patch0:		linhpsdr-0-distro-makefile.patch
Patch1: linhpsdr-c99.patch

%description
An HPSDR (High Performance Software Defined Radio) application for controlling
HPSDR compatible radios, e.g. Orion, Angelia, Hermes, ...

%package doc
Summary:	Documentation files for linhpsdr
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation files for linhpsdr.

%prep
%autosetup -n %{name}-%{git_commit} -p1

%build
%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" \
  GIT_VERSION="%{version_tag}" GIT_DATE="%{version_date}" %{features}

%install
%make_install BINDIR="%{buildroot}%{_bindir}" DATADIR="%{buildroot}%{_datadir}" %{features}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/io.github.g0orx.LinHPSDR.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/io.github.g0orx.LinHPSDR.metainfo.xml

%files doc
%doc documentation/*.pdf

%changelog
* Tue Jan  7 2025 Daniel Rusek <mail@asciiwolf.com> - 0-0.14.20210710git742658a9
- Fixed desktop icon installation path

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.13.20210710git742658a9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Daniel Rusek <mail@asciiwolf.com> - 0-0.11.20210710git742658a9
- Added AppStream metadata

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 0-0.8.20210710git742658a9
- Fix C compatibility issue

* Mon Nov 20 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.7.20210710git742658a9
- Rebuilt for libcw

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.2.20210710git742658a9
- Updated description according to the review
  Related: rhbz#1981048

* Sat Jul 10 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20210710git742658a9
- Initial release
