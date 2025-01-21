Name:           stk
Version:        4.6.1
Release:        10%{?dist}
Summary:        Synthesis ToolKit in C++
License:        MIT
URL:            https://ccrma.stanford.edu/software/stk/
Source0:        %{name}-%{version}.stripped.tar.gz
# Original tarfile can be found at %%{url}/release/%%{name}-%%{version}.tar.gz
# We remove legeally questionable files as well as accidentally packed
# object files.
Source1:        README.fedora
Patch0:         stk-4.6.1-header.patch
Patch1:         stk-4.6.1-cflags-lib.patch
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  symlinks
BuildRequires:  autoconf


%description
The Synthesis ToolKit in C++ (STK) is a set of open source audio
signal processing and algorithmic synthesis classes written in the C++
programming language. STK was designed to facilitate rapid development
of music synthesis and audio processing software, with an emphasis on
cross-platform functionality, realtime control, ease of use, and
educational example code. The Synthesis ToolKit is extremely portable
(it's mostly platform-independent C and C++ code), and it's completely
user-extensible (all source included, no unusual libraries, and no
hidden drivers). We like to think that this increases the chances that
our programs will still work in another 5-10 years. In fact, the
ToolKit has been working continuously for about 10 years now. STK
currently runs with realtime support (audio and MIDI) on Linux,
Macintosh OS X, and Windows computer platforms. Generic, non-realtime
support has been tested under NeXTStep, Sun, and other platforms and
should work with any standard C++ compiler.


%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package demo
Summary:        Demo applications for %{name}
Requires:       tk
Requires:       %{name} = %{version}-%{release}

%description demo
The %{name}-demo package contains the demo applications for the
C++ Sound Synthesis ToolKit.


%prep
%autosetup -p1

# we patched configure.ac
autoconf

cp -a %{SOURCE1} README.fedora

# remove backup and other extra files
find . -name '*~' -exec rm {} \;
find . -name '._*' -exec rm {} \;


%build
%configure --with-jack --with-alsa \
  --disable-static --enable-shared \
  RAWWAVE_PATH=%{_datadir}/stk/rawwaves/
%make_build
%make_build -C projects/demo libMd2Skini


%install
mkdir -p \
  %{buildroot}%{_includedir}/stk \
  %{buildroot}%{_libdir} \
  %{buildroot}%{_bindir} \
  %{buildroot}%{_datadir}/stk/rawwaves \
  %{buildroot}%{_datadir}/stk/demo \
  %{buildroot}%{_datadir}/stk/examples \
  %{buildroot}%{_datadir}/stk/effects \
  %{buildroot}%{_datadir}/stk/ragamatic \
  %{buildroot}%{_datadir}/stk/eguitar

cp -p include/* %{buildroot}%{_includedir}/stk
cp -pd src/libstk*.so %{buildroot}%{_libdir}
cp -p rawwaves/*.raw %{buildroot}%{_datadir}/stk/rawwaves

cp -pr projects/demo/tcl %{buildroot}%{_datadir}/stk/demo
cp -pr projects/demo/scores %{buildroot}%{_datadir}/stk/demo
cp -p projects/demo/stk-demo %{buildroot}%{_bindir}/stk-demo
cp -p projects/demo/Md2Skini %{buildroot}%{_bindir}/Md2Skini
for f in Banded Drums Modal Physical Shakers StkDemo Voice ; do
  chmod +x projects/demo/$f
  sed -e '1i#! /bin/sh' -i projects/demo/$f
  cp -p projects/demo/$f %{buildroot}%{_datadir}/stk/demo
done

cp -pr projects/examples/midifiles %{buildroot}%{_datadir}/stk/examples
cp -pr projects/examples/rawwaves %{buildroot}%{_datadir}/stk/examples
cp -pr projects/examples/scores %{buildroot}%{_datadir}/stk/examples
for f in sine sineosc foursine audioprobe midiprobe duplex play \
    record inetIn inetOut rtsine crtsine bethree controlbee \
    threebees playsmf grains ; do
  cp -p projects/examples/$f %{buildroot}%{_bindir}/stk-$f
  # absolute links, will be shortened later
  ln -s %{buildroot}%{_bindir}/stk-$f %{buildroot}%{_datadir}/stk/examples/$f
done

cp -pr projects/effects/tcl %{buildroot}%{_datadir}/stk/effects
cp -p projects/effects/effects %{buildroot}%{_bindir}/stk-effects
sed -e 's,\./effects,%{_bindir}/stk-effects,' -e '1i#! /bin/sh' \
  -i projects/effects/StkEffects
cp -p projects/effects/StkEffects %{buildroot}%{_datadir}/stk/effects

cp -pr projects/ragamatic/tcl %{buildroot}%{_datadir}/stk/ragamatic
cp -pr projects/ragamatic/rawwaves %{buildroot}%{_datadir}/stk/ragamatic
cp -p projects/ragamatic/ragamat %{buildroot}%{_bindir}/stk-ragamat
sed -e 's,\./ragamat,%{_bindir}/stk-ragamat,' -e '1i#! /bin/sh' \
  -i projects/ragamatic/Raga
cp -p projects/ragamatic/Raga %{buildroot}%{_datadir}/stk/ragamatic

cp -pr projects/eguitar/tcl %{buildroot}%{_datadir}/stk/eguitar
cp -pr projects/eguitar/scores %{buildroot}%{_datadir}/stk/eguitar
cp -p projects/eguitar/eguitar %{buildroot}%{_bindir}/stk-eguitar
sed -e 's,\./eguitar,%{_bindir}/stk-eguitar,' -e '1i#! /bin/sh' \
  -i projects/eguitar/ElectricGuitar
cp -p projects/eguitar/ElectricGuitar %{buildroot}%{_datadir}/stk/eguitar

# fix encoding
iconv -f iso-8859-1 -t utf-8 doc/doxygen/index.txt \
  -o doc/doxygen/index.txt.tmp
mv doc/doxygen/index.txt.tmp doc/doxygen/index.txt

# fix symlinks
symlinks -crv %{buildroot}

# fix permissions
find %{buildroot} \( -name '*.h' -o -name '*.raw' -o -name '*.tcl' \
     -o -name '*.xbm' -o -name '*.bmp' -o -name 'README' \) -a -exec chmod -x {} \;
find doc README.md README.fedora -type f -exec chmod -x {} \;
chmod -R u=rwX,go=rX %{buildroot}


%ldconfig_scriptlets


%files
%doc README.md
%{_libdir}/libstk-*.so
%dir %{_datadir}/stk
%{_datadir}/stk/rawwaves


%files devel
%doc README.md doc/* README.fedora
%{_libdir}/libstk.so
%{_includedir}/*


%files demo
%doc README.md README.fedora
%{_bindir}/stk-*
%{_bindir}/Md2Skini
%{_datadir}/stk/demo
%{_datadir}/stk/examples
%{_datadir}/stk/effects
%{_datadir}/stk/ragamatic
%{_datadir}/stk/eguitar


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.6.1-1
- Update to 4.6.1.

* Sat Sep 12 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.6.0-1
- Update to 4.6.0.

* Sat Sep 12 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.5.1-1
- Update to 4.5.1.
- Rebase patches.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.5.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Thomas Moschny <thomas.moschny@gmx.de> - 4.5.0-1
- Update to 4.5.0.
- Rebase patches.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 16 2012 Thomas Moschny <thomas.moschny@gmx.de> - 4.4.4-1
- Update to 4.4.4.
- Rebase patches.
- Follow upstream and use version 4 for the soname.
- Modernize spec file.
- Pack new demo project 'eguitar'.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 13 2010 Thomas Moschny <thomas.moschny@gmx.de> - 4.4.2-1
- Update to 4.4.2.
- Rebase patches. Ensure CXXFLAGS are in effect.
- Follow Debian and use version 0 for the soname.
- Specfile cleanups.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb  3 2009 Thomas Moschny <thomas.moschny@gmx.de> - 4.3.1-8
- Update header patch: Add more missing includes. Should fix
  compilation with gcc 4.4.0.

* Mon Dec  1 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 4.3.1-7
- Include /usr/share/stk directory in main package.

* Mon Sep 15 2008 Thomas Moschny <thomas.moschny@gmx.de> - 4.3.1-6
- Include updated config.guess and config.sub scripts.

* Tue Sep  9 2008 Thomas Moschny <thomas.moschny@gmx.de> - 4.3.1-5
- Don't ship the static library.

* Sun Sep  7 2008 Thomas Moschny <thomas.moschny@gmx.de> - 4.3.1-4
- Remove all .mid and .ski files from the tarball.
- Add README.fedora.

* Thu Jul 31 2008 Thomas Moschny <thomas.moschny@gmx.de> - 4.3.1-3
- Remove src/include/dsound.h, and src/include/*asio* files from the
  tarball, for legal reasons. Only used on windows anyway.
- Remove src/include/soundcard.h (explicitly forbids modification) and
  disable OSS support.
- Build and pack Md2Skini.
- Build and pack the examples.

* Tue Jul 15 2008 Thomas Moschny <thomas.moschny@gmx.de> - 4.3.1-2
- Update sharedlib patch, fixes alsa problem.
- Fix path for include files in -devel.
- Change path for docs in -devel.

* Sun Jul  6 2008 Thomas Moschny <thomas.moschny@gmx.de> - 4.3.1-1
- New package.
