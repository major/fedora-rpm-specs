%global sconsopts VERSION=%{version} PREFIX=%{_prefix} PREFIX_CONF=%{_sysconfdir} ZLIB_W32=%{mingw32_prefix} SKIPUTILS=NSISMenu STRIP_CP=false NSIS_MAX_STRLEN=8192 NSIS_CONFIG_LOG=yes
%global sconsopts64 %{sconsopts} TARGET_ARCH=amd64

Name:           mingw-nsis
Version:        3.10
Release:        3%{?dist}
Summary:        Nullsoft Scriptable Install System

License:        Zlib AND CPL-1.0
URL:            http://nsis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/nsis/nsis-%{version}-src.tar.bz2

# Workaround recent scons not handling the space in 'NSIS Menu' correctly, see also %%prep
# scons: *** Invalid value(s) for variable 'SKIPUTILS': 'NSIS,Menu'
Patch0:         nsis-nsismenu.patch
# Use RPM_OPT_FLAGS for the natively-built parts
Patch1:         0001-Use-RPM_OPT_FLAGS-for-the-natively-built-parts.patch

BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-scons
BuildRequires:  zlib-devel

BuildRequires:  mingw32-filesystem >= 40
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 40
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-zlib

# Don't build NSIS Menu as it doesn't actually work on POSIX systems: 1. it
# doesn't find its index.html file without patching, 2. it has various links to
# .exe files such as the makensisw.exe W32 GUI which are not available in the
# POSIX version at all and 3. the documentation links have backslashes in the
# URLs and the relative paths are wrong. Almost none of the links worked when I
# tested it (after patching problem 1.).
# Also removes unnecessary wxGTK dependency for this otherwise GUI-less package.
# (Does it really make sense to drag in wxGTK just to display a HTML file?)
# If you really want to reenable this, it needs a lot of fixing. Oh, and it'd
# need a .desktop file too.
# -- Kevin Kofler
# BuildRequires:  wxGTK-devel


%description
NSIS, the Nullsoft Scriptable Install System, is a script-driven
Windows installation system.

This package includes native Fedora binaries of makensis (etc.) and
all plugins.


%package -n mingw-nsis-base
Summary:        Nullsoft Scriptable Install System - base files

%description -n mingw-nsis-base
NSIS, the Nullsoft Scriptable Install System, is a script-driven
Windows installation system.

This package includes the natife Fedora binaries and the common
files for both mingw32-nsis and mingw64-nsis.


%package -n mingw32-nsis
Summary:        Nullsoft Scriptable Install System - win32
BuildArch:      noarch
Requires:       mingw-nsis-base = %{version}-%{release}

%description -n mingw32-nsis
NSIS, the Nullsoft Scriptable Install System, is a script-driven
Windows installation system.

This package includes the binaries compiled for win32.


%package -n mingw64-nsis
Summary:        Nullsoft Scriptable Install System - win64
BuildArch:      noarch
Requires:       mingw-nsis-base = %{version}-%{release}

%description -n mingw64-nsis
NSIS, the Nullsoft Scriptable Install System, is a script-driven
Windows installation system.

This package includes the binaries compiled for win64.


%prep
%autosetup -p1 -n nsis-%{version}-src

# Remove executable bits
find -type f -exec chmod -x {} \;

# See Patch0
mv 'Contrib/NSIS Menu' 'Contrib/NSISMenu'


%build
scons %{sconsopts}
scons %{sconsopts64}

%install
scons %{sconsopts} PREFIX_DEST=%{buildroot} install
scons %{sconsopts64} PREFIX_DEST=%{buildroot} install
mv %{buildroot}%{_docdir}/nsis %{buildroot}%{_docdir}/%{name}


%files -n mingw-nsis-base
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/GenPat
%{_bindir}/makensis
%{_sysconfdir}/nsisconf.nsh
%dir %{_datadir}/nsis
%dir %{_datadir}/nsis/Bin
%{_datadir}/nsis/Bin/MakeLangId.exe
%{_datadir}/nsis/Bin/makensisw.exe
%{_datadir}/nsis/Bin/zip2exe.exe
%{_datadir}/nsis/Contrib/
%{_datadir}/nsis/Include/
%dir %{_datadir}/nsis/Plugins
%dir %{_datadir}/nsis/Stubs
%{_datadir}/nsis/Stubs/uninst

%files -n mingw32-nsis
%{_datadir}/nsis/Bin/RegTool-x86.bin
%{_datadir}/nsis/Plugins/x86-ansi/
%{_datadir}/nsis/Plugins/x86-unicode/
%{_datadir}/nsis/Stubs/bzip2_solid-x86-ansi
%{_datadir}/nsis/Stubs/bzip2_solid-x86-unicode
%{_datadir}/nsis/Stubs/bzip2-x86-ansi
%{_datadir}/nsis/Stubs/bzip2-x86-unicode
%{_datadir}/nsis/Stubs/lzma_solid-x86-ansi
%{_datadir}/nsis/Stubs/lzma_solid-x86-unicode
%{_datadir}/nsis/Stubs/lzma-x86-ansi
%{_datadir}/nsis/Stubs/lzma-x86-unicode
%{_datadir}/nsis/Stubs/zlib_solid-x86-ansi
%{_datadir}/nsis/Stubs/zlib_solid-x86-unicode
%{_datadir}/nsis/Stubs/zlib-x86-ansi
%{_datadir}/nsis/Stubs/zlib-x86-unicode

%files -n mingw64-nsis
%{_datadir}/nsis/Bin/RegTool-amd64.bin
%{_datadir}/nsis/Plugins/amd64-unicode/
%{_datadir}/nsis/Stubs/bzip2-amd64-unicode
%{_datadir}/nsis/Stubs/bzip2_solid-amd64-unicode
%{_datadir}/nsis/Stubs/lzma-amd64-unicode
%{_datadir}/nsis/Stubs/lzma_solid-amd64-unicode
%{_datadir}/nsis/Stubs/zlib-amd64-unicode
%{_datadir}/nsis/Stubs/zlib_solid-amd64-unicode


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 02 2024 Sandro Mani <manisandro@gmail.com> - 3.10-1
- Update to 3.10

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Sandro Mani <manisandro@gmail.com> - 3.09-1
- Update to 3.09

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

<<<<<<< Updated upstream
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild
=======
* Fri May 06 2022 Sandro Mani <manisandro@gmail.com> - 3.08-3
- Add win64 build
>>>>>>> Stashed changes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Sandro Mani <manisandro@gmail.com> - 3.08-1
- Update to 3.08

* Sun Jul 25 2021 Sandro Mani <manisandro@gmail.com> - 3.07-1
- Update to 3.07

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.06.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.06.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Sandro Mani <manisandro@gmail.com> - 3.06-1
- Update to 3.06

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 09 2020 Sandro Mani <manisandro@gmail.com> - 3.05-2
- Add ability to log installs

* Sat Mar 07 2020 Richard W.M. Jones <rjones@redhat.com> - 3.05-1
- New upstream version 3.05.
- Remove scons/Python 3 patch which is upstream.
- Add patch to fix GCC 10 -fno-common bug.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Sandro Mani <manisandro@gmail.com> - 3.04-1
- Update to 3.04

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Sandro Mani <manisandro@gmail.com> - 3.03-1
- Update to 3.03

* Sat Oct 28 2017 Sandro Mani <manisandro@gmail.com> - 3.02.1-1
- Update to 3.02.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Christophe Fergeau <cfergeau@redhat.com> 3.01-1
- New upstream version 3.01.

* Thu Feb 18 2016 Richard W.M. Jones <rjones@redhat.com> - 2.50-1
- New upstream version 2.50.
- Fixes serious DLL hijacking attack:
  https://sourceforge.net/p/nsis/bugs/1125/

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Richard W.M. Jones <rjones@redhat.com> - 2.46-15
- Add NSIS_MAX_STRLEN=8192 to sconsopts (RHBZ#1090075).

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.46-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug  6 2013 Richard W.M. Jones <rjones@redhat.com> - 2.46-11
- Unversioned docdir on Fedora 20 (RHBZ#993867).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 2.46-7
- Renamed the source package to mingw-nsis (#800987)

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.46-6
- Rebuild against the mingw-w64 toolchain
- Added a patch to fix compatibility with mingw-w64

* Mon Jan 16 2012 Richard W.M. Jones <rjones@redhat.com> - 2.46-5
- Missing #include <unistd.h> to get close(2) function.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 08 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.46-3
- Make plugins not depend on libstdc++-6.dll (#734905)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.46-1
- Update to 2.46 (#544675)

* Mon Jan 11 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.45-3
- Make plugins not depend on libgcc_s_sjlj-1.dll (#553971)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.45-1
- Update to 2.45 (#512429)

* Tue Jun 30 2009 Stu Tomlinson <stu@nosnilmot.com> - 2.44-2
- Re-enable System.dll plugin, inline Microsoft assembler code was
  replaced in 2.42 (#509234)

* Sat Mar 14 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.44-1
- Update to 2.44 (#488522)

* Tue Mar  3 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.43-6
- Don't build the MinGW parts with debugging information, NSIS corrupts the
  debugging information in the stubs when building installers from them
- Drop debian-debug-opt patch, all its changes are either taken care of by our
  rpm-opt patch, unwanted (see above) or unneeded

* Wed Feb 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.43-5
- Use RPM_OPT_FLAGS for the natively-built parts

* Wed Feb 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.43-4
- Updated 64bit-fixes patch (remove some more -m32 use)
- Drop ExclusiveArch, not needed with the above
- Obsoletes/Provides nsis and nsis-data for migration path from CalcForge
- Disable NSIS Menu (does not work on *nix, see specfile comment for details)
- Drop BR wxGTK-devel

* Sat Feb 21 2009 Richard W.M. Jones <rjones@redhat.com> - 2.43-3
- Restore ExclusiveArch line (Levente Farkas).

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.43-2
- Rebuild for mingw32-gcc 4.4

* Fri Feb 13 2009 Levente Farkas <lfarkas@lfarkas.org> - 2.43-1
- update to the latest upstream

* Wed Jan 14 2009 Levente Farkas <lfarkas@lfarkas.org> - 2.42-1
- update to the latest upstream
- a few small changes

* Fri Oct 17 2008 Richard W.M. Jones <rjones@redhat.com> - 2.39-5
- Fix the Summary line.

* Wed Oct  8 2008 Richard W.M. Jones <rjones@redhat.com> - 2.39-4
- Initial RPM release.
