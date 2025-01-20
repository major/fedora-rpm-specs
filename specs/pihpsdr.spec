%global git_commit 7ad62180e8073f7c243195a0ff8632bdfbdf3742
%global git_date 20241105

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

# SERVER is not completed yet
# GPIO support temporally disabled due to:
# https://github.com/g0orx/pihpsdr/issues/195,
# reenable with (and uncomment the build require bellow):
# GPIO_INCLUDE=GPIO
%global features \\\
  GPIO_INCLUDE= \\\
  LOCALCW_INCLUDE=LOCALCW \\\
  SOAPYSDR_INCLUDE=SOAPYSDR \\\
  MIDI_INCLUDE=MIDI \\\
  PTT_INCLUDE=PTT \\\
  # SERVER_INCLUDE=SERVER

Name:		pihpsdr
Version:	2.0.8~rc1^%{git_suffix}
Release:	7%{?dist}
Summary:	Raspberry Pi standalone code for HPSDR
License:	GPL-2.0-or-later
URL:		https://github.com/g0orx/%{name}
#Source0:	%%{url}/archive/v%%{version_no_tilde}/%%{name}-%%{version_no_tilde}.tar.gz
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
# upstream desktop file needs a lot of patching, use own
Source1:	pihpsdr.desktop
Source2:	io.github.g0orx.pihpsdr.metainfo.xml
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gtk3-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	wdsp-devel
BuildRequires:	pulseaudio-libs-devel
#BuildRequires:	libgpiod-devel
%ifnarch s390x
BuildRequires:	libi2c-devel
%endif
BuildRequires:	desktop-file-utils
Requires:	hicolor-icon-theme
# https://github.com/g0orx/pihpsdr/pull/143
Patch0:		pihpsdr-2.0.8-distro-makefile.patch
# https://github.com/g0orx/pihpsdr/issues/154
Patch1:		pihpsdr-2.0.8-compile-fix.patch
# https://github.com/g0orx/pihpsdr/pull/197
Patch2:		pihpsdr-2.0.8-wdsp-in-home-dir.patch
# https://github.com/g0orx/pihpsdr/pull/198
Patch3:		pihpsdr-2.0.8-icon-system-path.patch

%description
The pihpsdr (Pi High Performance Software Defined Radio) is a port of PowerSDR
which works with the radios based on the OpenHPSDR project. These radios use
Ethernet to communicate with the software.

%package doc
Summary:	Documentation files for linhpsdr
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation files for linhpsdr.

%prep
%autosetup -n %{name}-%{git_commit} -T -b0 -p1

# drop binaries, save useful files
mv release/documentation .
pushd release/pihpsdr
mv -t ../.. hpsdr.png hpsdr_icon.png README.MIDI
popd
rm -rf release

%build
%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" %{features}

%install
%make_install BINDIR="%{buildroot}%{_bindir}" DATADIR="%{buildroot}%{_datadir}" %{features}

install -Dpm 0644 hpsdr.png %{buildroot}%{_datadir}/%{name}/hpsdr.png
install -Dpm 0644 hpsdr_icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/hpsdr_icon.png

# desktop file
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# AppStream metadata file
install -Dm 0644 %{SOURCE2} \
    %{buildroot}%{_metainfodir}/io.github.g0orx.pihpsdr.metainfo.xml

%files
%doc README.md README.MIDI
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/*

%files doc
%doc documentation/{MIDI-manual,piHPSDR-Controller-Users-Guide}.pdf

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8~rc1^20241105git7ad62180-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan  7 2025 Daniel Rusek <mail@asciiwolf.com> - 2.0.8~rc1^20241105git7ad62180-6
- Fixed desktop icon installation path

* Tue Jan  7 2025 Daniel Rusek <mail@asciiwolf.com> - 2.0.8~rc1^20241105git7ad62180-5
- Added AppStream metadata

* Fri Nov  8 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.8~rc1^20241105git7ad62180-4
- Updated wdsp-in-home-dir patch

* Wed Nov  6 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.8~rc1^20241105git7ad62180-3
- Updated according to the review

* Wed Nov  6 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.8~rc1^20241105git7ad62180-2
- Fixed icon
- Updated description

* Wed Nov  6 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.8~rc1^20241105git7ad62180-1
- New snapshot version
- Fixed compilation

* Tue Aug  2 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.8~rc1-1
- New version
- Updated according to the review
  Resolves: rhbz#1981103

* Sat Jul 10 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20210710git742658a9-1
- Initial release
