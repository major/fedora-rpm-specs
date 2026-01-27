
%global debug_package %{nil}

Name:		mupen64plus
Version:	2.6.0
Release:	%autorelease

Summary:	Nintendo 64 Emulator
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:		http://www.mupen64plus.org/
Source:		https://github.com/mupen64plus/mupen64plus-core/releases/download/%{version}/mupen64plus-bundle-src-%{version}.tar.gz

# https://github.com/mupen64plus/mupen64plus-core/issues/1104 (merged, unreleased)
Patch1:		search-lib64.patch

# Fix missing includes bubbling up due gnu23 rules
# https://github.com/mupen64plus/mupen64plus-core/issues/1114 (merged, unreleased)
Patch2:		add-includes.patch

# Combined changes of four merged upstream PRs:
# https://github.com/mupen64plus/mupen64plus-core/pull/1122/commits
# https://github.com/mupen64plus/mupen64plus-core/pull/1123/commits
# https://github.com/mupen64plus/mupen64plus-core/pull/1080/commits
# https://github.com/mupen64plus/mupen64plus-core/pull/1119/commits
# 
# This should mitigate vulnerabilities:
# CVE-2025-29366
# CVE-2025-9688
# https://github.com/mupen64plus/mupen64plus-core/issues/1146
Patch3:		upstream-prs-1122-1123-1080-1119.patch

BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(lirc)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	gzip
BuildRequires:	pkgconfig(glew)
BuildRequires:	binutils
BuildRequires:	gcc-c++
BuildRequires:	nasm

Requires:	hicolor-icon-theme

Conflicts:	mupen64plus-qt
Conflicts:	mupen64plus-cli

ExcludeArch:	s390x
# i686 buils started failing in F44, disable it according to policy:
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Failure reported upstream:
# https://github.com/mupen64plus/mupen64plus-core/issues/1168
ExcludeArch:	%{ix86}

%description
Mupen64plus is a Nintendo 64 Emulator.
This package includes all the plug-ins.

%package devel
Summary:	Development files for mupen64plus
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mupen64plus

%prep
%autosetup -p1 -n %{name}-bundle-src-%{version}

# Need to avoid filename conflicts so they can be included in the package
cp -a source/mupen64plus-rsp-hle/LICENSES LICENSE-rsp-hle
cp -a source/mupen64plus-rom/mupen64plus/assets/LICENSES LICENSE-assets
cp -a source/mupen64plus-rom/LICENSES LICENSE-rom
cp -a source/mupen64plus-input-sdl/LICENSES LICENSE-input-sdl
cp -a source/mupen64plus-video-glide64mk2/LICENSES LICENSE-video-glide64mk2
cp -a source/mupen64plus-video-rice/LICENSES LICENSE-video-rice
cp -a source/mupen64plus-ui-console/LICENSES LICENSE-ui-console
cp -a source/mupen64plus-core/LICENSES LICENSE-core
cp -a source/mupen64plus-audio-sdl/LICENSES LICENSE-audio-sdl

%build

# Architecture build flags
ADDITIONAL_FLAGS=""
if [[ "$(uname -m)" = arm* ]] ; then
	ADDITIONAL_FLAGS="NEON=1 VFP_HARD=1 NO_SSE=1"
elif [[ "$(uname -m)" = aarch64 ]] ; then
	ADDITIONAL_FLAGS="NO_SSE=1"
elif [[ "$(uname -m)" = ppc* ]] ; then
	ADDITIONAL_FLAGS="NO_SSE=1"
fi

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
sh m64p_build.sh LIRC=1 $ADDITIONAL_FLAGS

%install

# NOTE: set LDCONFIG to true so it's not run during this script
./m64p_install.sh DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir} LIBDIR=%{_libdir} PIC=1 LDCONFIG='true'
find %{buildroot}%{_libdir} -type f -name "*.so*" -exec chmod 0755 "{}" \;

# NOTE: The build system should probably create this...
ln -sf libmupen64plus.so.2.0.0 %{buildroot}%{_libdir}/libmupen64plus.so

desktop-file-validate %{buildroot}/%{_datadir}/applications/mupen64plus.desktop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_libdir}/libmupen64plus.so.2
%{_libdir}/libmupen64plus.so.2.0.0
%{_datadir}/%{name}/
%{_datadir}/applications/mupen64plus.desktop
%{_datadir}/icons/hicolor/48x48/apps/mupen64plus.png
%{_datadir}/icons/hicolor/scalable/apps/mupen64plus.svg
%{_mandir}/man6/mupen64plus.6.gz
%license LICENSE-rsp-hle LICENSE-assets LICENSE-rom LICENSE-input-sdl LICENSE-video-glide64mk2 LICENSE-video-rice LICENSE-core LICENSE-audio-sdl


%files devel
%{_includedir}/mupen64plus/
%{_libdir}/libmupen64plus.so

%changelog
%autochangelog
