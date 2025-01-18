Name:           glyph-keeper
Version:        0.32
Release:        40%{?dist}
Summary:        Library for text rendering
License:        zlib
URL:            http://www.allegro.cc/resource/Libraries/Text/GlyphKeeper
# Upstream is MIA
Source0:        %{name}-%{version}.zip
Patch0:         glyph-keeper-0.29.1-fixes.patch
Patch1:         glyph-keeper-0.32-so-compat.patch
BuildRequires:  gcc
BuildRequires:  freetype-devel >= 2.1.10
BuildRequires:  SDL_gfx-devel allegro-devel
BuildRequires: make

%description
Glyph Keeper is a library for text rendering. It is written in C and can be
used by C or C++ code. Glyph Keeper helps your program to load a font, render
character glyphs and write them to the target surface. Right now only Allegro
and SDL targets are supported, but there will be more in future. Glyph Keeper
uses FreeType as a font engine.


%package        allegro
Summary:        Library for text rendering with Allegro
# Only the allegro package is currently actually used in Fedora, so make this
# one obsolete the old glyph-keeper package which had both allegro and SDL
# variants in one package
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < 0.32-9

%description    allegro
Glyph Keeper is a library for text rendering. It is written in C and can be
used by C or C++ code. Glyph Keeper helps your program to load a font, render
character glyphs and write them to the target surface. Glyph Keeper uses
FreeType as a font engine. This package contains glyph-keeper build for use
with Allegro apps.

%package        allegro-devel
Summary:        Development files for glyph-keeper-allegro
Requires:       allegro-devel
Requires:       glyph-keeper-allegro = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{name}-devel < 0.32-9

%description    allegro-devel
The glyph-keeper-allegro-devel package contains libraries and header files for
developing applications that use glyph-keeper-allegro.


%package        SDL
Summary:        Library for text rendering with SDL

%description    SDL
Glyph Keeper is a library for text rendering. It is written in C and can be
used by C or C++ code. Glyph Keeper helps your program to load a font, render
character glyphs and write them to the target surface. Glyph Keeper uses
FreeType as a font engine. This package contains glyph-keeper build for use
with SDL apps.

%package        SDL-devel
Summary:        Development files for glyph-keeper-SDL
Requires:       SDL-devel
Requires:       glyph-keeper-SDL = %{version}-%{release}

%description    SDL-devel
The glyph-keeper-SDL-devel package contains libraries and header files for
developing applications that use glyph-keeper-SDL.


%prep
%setup -q
%patch -P0 -p1 -z .fix
%patch -P1 -p1 -z .compat
sed -i 's/\r//' docs/*.html *.txt


%build
make %{?_smp_mflags} -f Makefile.GNU.all TARGET=ALLEGRO FT_LIB=-lfreetype \
  OFLAGS="$RPM_OPT_FLAGS -fpic -I/usr/include/freetype2" lib
gcc -shared -o libglyph-alleg.so.0 -Wl,-soname,libglyph-alleg.so.0 \
  obj/glyph-alleg.o -lfreetype $(allegro-config --libs)

make %{?_smp_mflags} -f Makefile.GNU.all TARGET=SDL FT_LIB=-lfreetype \
  OFLAGS="$RPM_OPT_FLAGS -fpic $(sdl-config --cflags) -I/usr/include/freetype2" lib
gcc -shared -o libglyph-sdl.so.0 -Wl,-soname,libglyph-sdl.so.0 \
  obj/glyph-sdl.o -lfreetype -lSDL -lSDL_gfx


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 libglyph-*.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libglyph-alleg.so.0 $RPM_BUILD_ROOT%{_libdir}/libglyph-alleg.so
ln -s libglyph-sdl.so.0 $RPM_BUILD_ROOT%{_libdir}/libglyph-sdl.so
install -m 644 include/glyph.h $RPM_BUILD_ROOT%{_includedir}


%ldconfig_scriptlets allegro

%ldconfig_scriptlets SDL


%files allegro
%doc license.txt changes.txt authors.txt docs/*
%{_libdir}/libglyph-alleg.so.0

%files allegro-devel
%{_includedir}/glyph.h
%{_libdir}/libglyph-alleg.so

%files SDL
%doc license.txt changes.txt authors.txt docs/*
%{_libdir}/libglyph-sdl.so.0

%files SDL-devel
%{_includedir}/glyph.h
%{_libdir}/libglyph-sdl.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Hans de Goede <hdegoede@redhat.com> - 0.32-30
- Fix FTBFS (rhbz#1863639)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-29
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 0.32-16
- Rebuild for new SDL_gfx

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.32-14
- Rebuild for new SDL_gfx

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Hans de Goede <hdegoede@redhat.com> - 0.32-9
- Rebuilt for new SDL_gfx
- Split into glyph-keeper-allegro[-devel] and glyph-keeper-SDL[-devel]

* Wed Jul 13 2011 Hans de Goede <hdegoede@redhat.com> - 0.32-8
- Rebuilt for new allegro-4.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.32-4
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.32-3
- Rebuild for buildId
- Update license tag for new license tag guidelines

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 0.32-2
- Rebuild against SDL_gfx 2.0.16.

* Fri Feb 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.32-1
- New upstream release 0.32

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.29.1-4
- Fix building with newer freetype
- Build .so files instead of a static lib

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.29.1-3
- FE6 Rebuild

* Mon Mar 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.29.1-2
-change license to "zlib License"
-add authors.txt and docs/* to %%doc

* Sat Mar 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.29.1-1
- Initial Fedora Extras package
