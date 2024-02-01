Name: ttf2pt1
Version: 3.4.4
Release: %autorelease
Summary: TrueType to Adobe Type 1 font converter
Summary(sv): Konverterare från TrueType till Adobe Type 1

License: GPLv2+ and BSD with advertising
URL: http://%name.sourceforge.net
Source: http://download.sourceforge.net/%name/%name-%version.tgz
Patch0: ttf2pt1-destdir.patch
Patch1: ttf2pt1-freetype.patch
Patch2: ttf2pt1-sed.patch
Patch3: ttf2pt1-doc.patch
Patch4: ttf2pt1-c99.patch
Patch5: ttf2pt1-gcc14.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: freetype-devel >= 2.0.3
BuildRequires: perl-generators
BuildRequires: perl-podlators
BuildRequires: fakeroot
BuildRequires: t1lib-devel

Requires: t1utils

%description
Ttf2pt1 is a font converter from the True Type format (and some other formats
supported by the FreeType library as well) to the Adobe Type1 format.

%description -l sv
Ttf2pt1 är en konverterare för typsnitt från formatet True Type (och
några andra format som stödjs av biblioteket FreeType) till formatet
Adobe Type 1.


%prep
%autosetup -p 0


%build
make CFLAGS_SYS='%optflags -D_GNU_SOURCE' CFLAGS_FT="-DUSE_FREETYPE `pkg-config --cflags freetype2`" LIBS_FT="`pkg-config --libs freetype2`" VERSION=%version all
rm -rf __dist_other
mkdir -p __dist_other/other
cp -p other/bz* other/Makefile other/README* __dist_other/other
make -C other cmpf dmpf

%install
# The installation does explicit chown to root and chgrp to bin.
# Use fakeroot to avoid getting errors in the build.  RPM will
# make sure the ownership is correct in the final package.
fakeroot make DESTDIR=%buildroot INSTDIR=%_prefix TXTFILES= MANDIR=%_mandir VERSION=%version install
# Use the system t1asm from t1utils instead of a local version.
rm -r %buildroot/%_libexecdir
# Remove scripts only used during build
rm %buildroot%_datadir/%name/scripts/{convert,convert.cfg.sample,frommap,html2man,inst_dir,inst_file,mkrel,unhtml}
# Put tools in the standard path
mv %buildroot/%_datadir/%name/other/cmpf %buildroot/%_bindir/%{name}_cmpf
mv %buildroot/%_datadir/%name/other/dmpf %buildroot/%_bindir/%{name}_dmpf
cp other/cntstems.pl %buildroot/%_bindir/%{name}_cntstems
cp other/lst.pl %buildroot/%_bindir/%{name}_lst
cp other/showdf %buildroot/%_bindir/%{name}_showdf
cp other/showg %buildroot/%_bindir/%{name}_showg


%files
%doc CHANGES* README* FONTS FONTS.html COPYRIGHT app/TeX __dist_other/other
%doc scripts/convert.cfg.sample
%_bindir/%{name}*
%_datadir/%name
%exclude %_datadir/%name/app
%exclude %_datadir/%name/other
%_mandir/man1/*


%changelog
%autochangelog
