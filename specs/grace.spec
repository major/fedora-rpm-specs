%if 0%{?fedora}
%global editor  xterm -e sensible-editor
%global pkgs    sensible-utils xterm
%else
%global editor  emacs
%global pkgs    emacs
%endif

Name:           grace
Version:        5.1.25
Release:        42%{?dist}
Summary:        Numerical Data Processing and Visualization Tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
# cephes is LGPL, see also Source3 and Source4
URL:            http://plasma-gate.weizmann.ac.il/Grace/
Source0:        ftp://plasma-gate.weizmann.ac.il/pub/grace/src/grace5/grace-%{version}.tar.gz
Source1:        grace.desktop
Source3:        cephes-license.email
Source4:        LICENSE.cephes
Source5:        http://ftp.de.debian.org/debian/pool/main/g/grace/grace_5.1.25-6.debian.tar.xz
Source6:        FontDataBase
Patch0:         grace-detect-netcdf.diff
Patch1:         grace-configure-c99-1.patch
Patch2:         grace-configure-c99-2.patch
Patch3:         grace-c99.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fftw2-devel
BuildRequires:  gcc-gfortran
BuildRequires:  libXmu-devel
BuildRequires:  libXpm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  netcdf-devel
BuildRequires:  t1lib-devel
BuildRequires:  urw-base35-fonts-devel
BuildRequires:  xbae-devel
BuildRequires:  zlib-devel
Requires:       %{pkgs}
Requires:       urw-base35-fonts-common
Requires:       xdg-utils
%description
Grace is a Motif application for two-dimensional data
visualization. Grace can transform the data using free equations, FFT,
cross- and auto-correlation, differences, integrals, histograms, and
much more. The generated figures are of high quality.  Grace is a very
convenient tool for data inspection, data transformation, and for
making figures for publications.

%package        devel
Summary:        Files needed for grace development
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
Install these files if you need to compile software that requires grace.

%prep
%autosetup -p1 -D -a 5

# avoid duplicating debian patch
patch -p1 < debian/patches/binary_nostrip.diff
patch -p1 < debian/patches/gracerc.diff
patch -p1 < debian/patches/source-hardening.diff
patch -p1 < debian/patches/tmpnam_to_mkstemp.diff

# remove bundled libraries
rm -rf Xbae T1lib

%build
cp %{SOURCE3} %{SOURCE4} .
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export FFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure \
    --enable-editres \
    --with-editor="%{editor}" \
    --with-helpviewer="xdg-open %s" \
    --with-printcmd="lpr" \
    --enable-grace-home=%{_datadir}/%{name} \
    --disable-pdfdrv \
    --with-x \
    --with-f77=gfortran \
    --with-extra-incpath=%{_includedir}/netcdf \
    --with-bundled-xbae=no

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f doc/*.1
mkdir -pm 755                               \
    %{buildroot}%{_bindir}                  \
    %{buildroot}%{_includedir}              \
    %{buildroot}%{_libdir}                  \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps \
    %{buildroot}%{_datadir}/applications    \
    %{buildroot}%{_mandir}/man1             \
    %{buildroot}%{_sysconfdir}/%{name}

# Let's have some sanity
pushd %{buildroot}%{_datadir}/%{name}

install -pm 755 bin/* %{buildroot}%{_bindir}
rm %{buildroot}%{_bindir}/gracebat
ln -s xmgrace %{buildroot}%{_bindir}/gracebat
rm -rf bin
ln -s ../../bin bin

cp -p lib/* %{buildroot}%{_libdir}
rm -rf lib
ln -s ../../%_lib lib

install -pm 644 include/* %{buildroot}%{_includedir}
rm -rf include
ln -s ../../include include

# use fonts from urw-base53-legacy and install custom fontdb,
# see bz#1502175
rm -rf fonts/type1
ln -s %{urw_base35_fontpath} fonts/type1
rm fonts/FontDataBase
install -pm 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/%{name}/FontDataBase
ln -s ../../../..%{_sysconfdir}/%{name}/FontDataBase fonts/FontDataBase

# additional symlinks is also required
install -d -m0755 %{buildroot}/%{urw_base35_fontpath}
pushd %{buildroot}/%{urw_base35_fontpath}
for f in %{urw_base35_fontpath}/*.t1 ; do
    ln -s $(basename $f) $(basename $f .t1).pfb
done
popd

install -pm 644 doc/*.1 %{buildroot}%{_mandir}/man1/

# doc and example directories are removed from GRACE_HOME and put in %%doc
rm -rf doc examples
ln -s %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}/{doc,examples} .

# the convcal source file shouldn't be installed, it is removed here
rm -f auxiliary/convcal.c

# remove grconvert if built
rm -f %{buildroot}%{_bindir}/grconvert

# move config files to %%{_sysconfdir} and do symlinks
for conf in gracerc templates gracerc.user; do
    mv $conf %{buildroot}%{_sysconfdir}/%{name}
    ln -s ../../..%{_sysconfdir}/%{name}/$conf $conf
done
popd

# Desktop stuff
install -pm 644 debian/icons/grace.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
for sz in 16 22 24 32; do
    install -Dpm 644 debian/icons/grace${sz}.png %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/grace.png
done
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications          \
    %{SOURCE1}

# clean up docs
rm -rf __dist_doc
mkdir __dist_doc
cp -a doc __dist_doc
rm __dist_doc/doc/Makefile __dist_doc/doc/*.sgml

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc ChangeLog CHANGES COPYRIGHT DEVELOPERS README
%doc cephes-license.email LICENSE.cephes
%doc examples/ __dist_doc/doc/
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/convcal
%{_bindir}/fdf2fit
%{_bindir}/gracebat
%{_bindir}/xmgrace
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/include
%exclude %{_datadir}/%{name}/lib
%{_datadir}/applications/grace.desktop
%{_datadir}/icons/hicolor/*/apps/grace.png
%{_mandir}/man1/*.1*
%{urw_base35_fontpath}/*.pfb

%files devel
%license grace_np/LICENSE
%{_includedir}/grace_np.h
%{_datadir}/%{name}/include
%{_libdir}/libgrace_np.a
%{_datadir}/%{name}/lib

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 5.1.25-41
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-39
- Use autosetup macro

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-36
- Restore dep on fonts (rhbz#2244630).

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Florian Weimer <fweimer@redhat.com> - 5.1.25-33
- Port to C99 (#2155764)

* Fri Sep 02 2022 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-32
- No need for xterm on epel

* Sun Aug 28 2022 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-31
- Package name != binary name

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 31 2022 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-29
- Fix typo

* Fri Jan 28 2022 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-28
- Use emacs on EPEL

* Thu Jan 27 2022 Dave Love <loveshack@fedoraproject.org> - 5.1.25-27
- Don't require urw-base35-fonts-legacy (not in EL8, and appears unnecessary) (#2046509)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 5.1.25-25
- Rebuild for netcdf 4.8.0

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 5.1.25-24
- Rebuild for netcdf 4.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 24 2021 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-22
- Revert to xdg-open (rhbz#1951618)

* Wed Mar 24 2021 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-21
- Skip grconvert if built

* Sun Feb 07 2021 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-20
- use sensible-utils like debian
- gracebat and xmgrace is the same thing, use symlink

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 5.1.25-15
- Rebuild for netcdf 4.6.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Terje Rosten <terje.rosten@ntnu.no> - 5.1.25-12
- Fix font issue, thanks to Andrew Schultz, Michael Weinert, sammy,
  David Kaspar and others (rhbz#1502175)
- Remove icon cache update
- Some clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.25-5
- Rebuild for netcdf 4.4.0

* Sun Oct 18 2015 Dominik Mierzejewski <rpm@greysector.net> - 5.1.25-4
- don't unpack the main source twice
- clean up obsolete specfile parts
- clean up some rpmlint warnings
- tighten file list
- install icons from debian patch
- update icon cache scriptlets

* Fri Oct 16 2015 Kalev Lember <klember@redhat.com> - 5.1.25-3
- Rebuilt for libXm soname bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 José Matos <jamatos@fedoraproject.org> - 5.1.25-1
- update to 5.1.25

* Fri Nov 14 2014 José Matos <jamatos@fedoraproject.org> - 5.1.24-1
- update to 5.1.24

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 5.1.23-6
- Fix symlinks to doc and example dirs when doc dir is unversioned (#993800).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Jon Ciesla <limburgher@gmail.com> - 5.1.23-4
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 5.1.23-2
- rebuild due to "jpeg8-ABI" feature drop

* Mon Nov 26 2012 José Matos <jamatos@fedoraproject.org> - 5.1.23-1
- New upstream release (bugfixes)
- Drop libpng15 (fixed in this release)
- Use debian patches where it makes sense

* Wed Aug 01 2012 Jon Ciesla <limburgher@gmail.com> - 5.1.22-14
- Tom Lane's zlib, libpng15 fixes, BZ 843647.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 5.1.22-11
- Rebuild for new libpng

* Tue Nov  8 2011 José Matos <jamatos@fedoraproject.org> - 5.1.22-10
- Rebuild for new libpng

* Wed Apr 6 2011 Orion Poplawski <orion@cora.nwra.com> - 5.1.22-9
- Rebuild for netcdf 4.1.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr  8 2010 José Matos <jamatos@fc.up.pt> - 5.1.22-7
- Fix overzealous fix for bug 504413 (fixes bug 568559).

* Thu Nov 19 2009 José Matos <jamatos@fc.up.pt> - 5.1.22-6
- Add compile option -fPIC (#508888)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 José Matos <jamatos@fc.up.pt> - 5.1.22-4
- Fix #504413 (remove last newline in FontDataBase)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 16 2008 José Matos <jamatos[AT]fc.up.pt> - 5.1.22-2
- Compile with support for netcdf (# 465458).

* Mon Sep 29 2008 José Matos <jamatos[AT]fc.up.pt> - 5.1.22-1
- new upstream release (5.1.22)
- apply debian patches with -p1

* Thu Feb 14 2008 José Matos <jamatos[AT]fc.up.pt> - 5.1.21-9
- Rebuild for gcc 4.3

* Wed Jan 23 2008 Patrice Dumas <pertusus[AT]free.fr> - 5.1.21-8
- correct netcdf detection patch, thanks José.

* Wed Jan 23 2008 Patrice Dumas <pertusus[AT]free.fr> - 5.1.21-7
- add support for previous netcdf version (in epel).
- drop support for monolithic X.

* Tue Jan 22 2008 Patrice Dumas <pertusus[AT]free.fr> - 5.1.21-6
- don't add the grace fonts to the X server fonts. Instead use the
  urw fonts. Regenerate the FontDataBase based on the urw fonts.
- use xdg-utils instead of htmlview.
- use relative links.
- add links to doc and examples in GRACE_HOME to have correct help.
- use debian patch.
- clean docs.

* Fri Sep 28 2007 José Matos <jamatos[AT]fc.up.pt> - 5.1.21-4
- Correctly detect netcdf (signature has changed).
- Add libXmu-devel as BR.
- Add conditional dependency on chkfontpath for <= F8.

* Thu Sep 27 2007 José Matos <jamatos[AT]fc.up.pt> - 5.1.21-3
- Remove dependency on chkfontpath, thanks to ajax for the patch. (#252277)

* Tue Aug 28 2007 José Matos <jamatos[AT]fc.up.pt> - 5.1.21-2
- License fix, rebuild for devel (F8).

* Thu Mar  8 2007 José Matos <jamatos[AT]fc.up.pt> - 5.1.21-1
- Update to 5.1.21 (#231434).
- Fix typo in description (#231435).

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 5.1.20-6
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.20-5
- Fix incomplete change from pixmap to icons.

* Sun Sep 24 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.20-4
- Move icon from pixmaps to icons/highcolor/48x48/apps

* Sun Sep 24 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.20-3
- Use external xbae.
- Revert test for fedora macro so that it works by default for latest
  versions if the macro is not defined.

* Mon Sep 11 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.20-2
- Fix html documentation viewer. (#188696)

* Sun Jun 11 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.20-1
- New upstream version
- Do not ship debug files in -devel subpackage (#194769)

* Wed Apr 12 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.19-5
- Add htmlview as help viewer.

* Thu Feb 16 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.19-4
- Remove stripping option from Makefiles to have meaningfull debuginfo packages.
- Thanks to Ville Skyttä for the fix. (bz#180106)

* Thu Feb 16 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.19-3
- Unify spec file starting from FC-4.
- Rebuild for FC-5.

* Wed Feb  1 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.19-2
- Update BR from fftw to fftw2.
- Remove references to previous profile scripts.

* Fri Jan 13 2006 José Matos <jamatos[AT]fc.up.pt> - 5.1.19-1
- new upstream version
- remove name from Summary
- disable setting environment variable GRACE_HOME
- replace x11-xorg-devel by libXpm-devel in BuildRequires for FC-5.

* Mon Jan  9 2006 Patrice Dumas <dumas[AT]centre-cired.fr> - 5.1.18-7
- put config files in /etc
- licence is GPL and not BSD/GPL, as it is not dual licensed

* Wed Sep 14 2005 José Matos <jamatos[AT]fc.up.pt> - 5.1.18-6
- Require nedit as an explicit Require.

* Tue Sep 13 2005 José Matos <jamatos[AT]fc.up.pt> - 5.1.18-5
- Normalize buildroot and change default editor to nedit.

* Fri Sep  9 2005 José Matos <jamatos[AT]fc.up.pt> - 5.1.18-4
- Add license to cephes library as well as the original mail where permission is given.
- Move permission of profile.d files from 644 to 755.

* Sat Sep  3 2005 Patrice Dumas <dumas[AT]centre-cired.fr> - 5.1.18-3
- cleanup licences
- put examples/ and doc/ in %%doc
- remove duplicate manpages
- add patch to change fdf2fit path in graderc

* Sun Aug 21 2005 José Matos <jamatos[AT]fc.up.pt> - 5.1.18-2
- Add post and postun requires.

* Sat Aug 20 2005 José Matos <jamatos[AT]fc.up.pt> - 5.1.18-1

- Prepare for Fedora Extras submission, based on a previous spec file
  from Konstantin Ryabitsev (icon) and Seth Vidal from duke.edu
