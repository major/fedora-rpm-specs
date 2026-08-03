Name:          android-tools
Version:       37.0.0
Release:       %autorelease
Epoch:         1
Summary:       Android platform tools(adb, fastboot)

License:       Apache-2.0 AND BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND LicenseRef-Fedora-Public-Domain
URL:           http://developer.android.com/guide/developing/tools/

#  Sources with all needed patches and cmakelists live there now: 
Source0:       https://github.com/nmeum/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# https://github.com/nmeum/android-tools/pull/208
Patch:         https://github.com/nmeum/android-tools/pull/208.patch

BuildRequires: brotli-devel
BuildRequires: cmake
BuildRequires: fmt-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: libusbx-devel
BuildRequires: libzstd-devel
BuildRequires: lz4-devel
BuildRequires: pcre2-devel
BuildRequires: protobuf-devel

Provides:      adb = %{epoch}:%{version}-%{release}
Provides:      fastboot = %{epoch}:%{version}-%{release}
Provides:      mke2fs.android = %{epoch}:%{version}-%{release}

# Bundled bits
Provides: bundled(boringssl)

# Bundled boringssl doesn't support the big endian architectures rhbz 1431379
ExcludeArch: ppc ppc64 s390x

%description

The Android Debug Bridge (ADB) is used to:

- keep track of all Android devices and emulators instances
  connected to or running on a given host developer machine

- implement various control commands (e.g. "adb shell", "adb pull", etc.)
  for the benefit of clients (command-line users, or helper programs like
  DDMS). These commands are what is called a 'service' in ADB.

Fastboot is used to manipulate the flash partitions of the Android phone. 
It can also boot the phone using a kernel image or root filesystem image 
which reside on the host machine rather than in the phone flash. 
In order to use it, it is important to understand the flash partition 
layout for the phone.
The fastboot program works in conjunction with firmware on the phone 
to read and write the flash partitions. It needs the same USB device 
setup between the host and the target phone as adb.

%prep
%autosetup -p1

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%{_bindir}/adb
%{_bindir}/avbtool
%{_bindir}/mke2fs.android
%{_bindir}/simg2img
%{_bindir}/img2simg
%{_bindir}/fastboot
%{_bindir}/append2simg
%{_bindir}/e2fsdroid
%{_bindir}/ext2simg
%{_bindir}/lpadd
%{_bindir}/lpdump
%{_bindir}/lpflash
%{_bindir}/lpmake
%{_bindir}/lpunpack
%{_bindir}/make_f2fs
%{_bindir}/mkbootimg
%{_bindir}/mkdtboimg
%{_bindir}/repack_bootimg
%{_bindir}/sload_f2fs
%{_bindir}/unpack_bootimg
%{_datadir}/android-tools/completions/adb
%{_datadir}/android-tools/completions/fastboot
%{_datadir}/android-tools/mkbootimg/gki/generate_gki_certificate.py
%{_datadir}/android-tools/mkbootimg/mkbootimg.py
%{_datadir}/bash-completion/completions/adb
%{_datadir}/bash-completion/completions/fastboot
%{_datadir}/zsh/site-functions/_adb
%{_datadir}/zsh/site-functions/_fastboot
%{_mandir}/man1/adb.1.*

%changelog
%autochangelog
