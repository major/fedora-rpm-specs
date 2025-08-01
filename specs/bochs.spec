%define _hardened_build 1
Name:           bochs
Version:        3.0
Release:        2%{?dist}
Summary:        Portable x86 PC emulator
License:        LGPL-2.0-or-later
URL:            http://bochs.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: %{name}-0001_bx-qemu.patch
Patch7: %{name}-nonet-build.patch
# Update configure for aarch64 (bz #925112)
Patch8: bochs-aarch64.patch
Patch10: bochs-usb.patch
Patch11: bochs-2.6.10-slirp-include.patch

ExcludeArch:    s390x i686

BuildRequires:  gcc-c++
BuildRequires:  libXt-devel libXpm-devel SDL2-devel readline-devel byacc
BuildRequires:  docbook-utils
BuildRequires:  gtk2-devel
BuildRequires: make
%ifarch %{ix86} x86_64
BuildRequires:  dev86 iasl
%endif
Requires:       %{name}-bios = %{version}-%{release}
Requires:       seavgabios-bin

%description
Bochs is a portable x86 PC emulation software package that emulates
enough of the x86 CPU, related AT hardware, and BIOS to run DOS,
Windows '95, Minix 2.0, and other OS's, all on your workstation.


%package        debugger
Summary:        Bochs with builtin debugger
Requires:       %{name} = %{version}-%{release}

%description    debugger
Special version of bochs compiled with the builtin debugger.


%package        gdb
Summary:        Bochs with support for debugging with gdb
Requires:       %{name} = %{version}-%{release}

%description    gdb
Special version of bochs compiled with a gdb stub so that the software running
inside the emulator can be debugged with gdb.

%ifarch %{ix86} x86_64
# building firmwares are quite tricky, because they often have to be built on
# their native architecture (or in a cross-capable compiler, that we lack in
# koji), and deployed everywhere. Recent koji builders support a feature
# that allow us to build packages in a single architecture, and create noarch
# subpackages that will be deployed everywhere. Because the package can only
# be built in certain architectures, the main package has to use
# BuildArch: <nativearch>, or something like that.
# Note that using ExclusiveArch is _wrong_, because it will prevent the noarch
# packages from getting into the excluded repositories.
%package	bios
Summary:        Bochs bios
BuildArch:      noarch
Provides:       bochs-bios-data = 2.3.8.1
Obsoletes:      bochs-bios-data < 2.3.8.1


%description bios
Bochs BIOS is a free implementation of a x86 BIOS provided by the Bochs project.
It can also be used in other emulators, such as QEMU
%endif

%package        devel
Summary:        Bochs header and source files
Requires:       %{name} = %{version}-%{release}

%description    devel
Header and source files from bochs source.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 7 -p0 -z .nonet

# Fix up some man page paths.
sed -i -e 's|/usr/local/share/|%{_datadir}/|' doc/man/*.*

# remove executable bits from sources to make rpmlint happy with the debuginfo
chmod -x `find -name '*.cc' -o -name '*.h' -o -name '*.inc'`
# Fix CHANGES encoding
iconv -f ISO_8859-2 -t UTF8 CHANGES > CHANGES.tmp
mv CHANGES.tmp CHANGES


%build
# Note: the CPU level, MMX et al affect what the emulator will emulate, they
# are not properties of the build target architecture.
# Note2: passing --enable-pcidev will change bochs license from LGPLv2+ to
# LGPLv2 (and requires a kernel driver to be usefull)
CONFIGURE_FLAGS=" \
  --enable-ne2000 \
  --enable-pci \
  --enable-all-optimizations \
  --enable-clgd54xx \
  --enable-sb16=linux \
  --enable-3dnow \
  --with-x11 \
  --with-nogui \
  --with-term \
  --with-rfb \
  --with-sdl2 \
  --without-wx \
  --with-svga=no \
  --enable-cpu-level=6 \
  --enable-disasm \
  --enable-e1000 \
  --enable-x86-64 \
  --enable-smp"
export CXXFLAGS="$RPM_OPT_FLAGS -DPARANOID"

%configure $CONFIGURE_FLAGS --enable-x86-debugger --enable-debugger
make %{?_smp_mflags}
mv bochs bochs-debugger
#make dist-clean

%configure $CONFIGURE_FLAGS --enable-x86-debugger --enable-gdb-stub --enable-smp=no
make %{?_smp_mflags}
mv bochs bochs-gdb
#make dist-clean

%configure $CONFIGURE_FLAGS
make %{?_smp_mflags}

%ifarch %{ix86} x86_64
cd bios
make bios
cp BIOS-bochs-latest BIOS-bochs-kvm
%endif

%install
rm -rf $RPM_BUILD_ROOT _installed-docs
make install DESTDIR=$RPM_BUILD_ROOT
ln -s %{_prefix}/share/seavgabios/vgabios-cirrus.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-cirrus
ln -s %{_prefix}/share/seavgabios/vgabios-isavga.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-isavga
ln -s %{_prefix}/share/seavgabios/vgabios-qxl.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-qxl
ln -s %{_prefix}/share/seavgabios/vgabios-stdvga.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-stdvga
ln -s %{_prefix}/share/seavgabios/vgabios-vmware.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-vmware
%ifnarch %{ix86} x86_64
rm -rf $RPM_BUILD_ROOT%{_prefix}/share/bochs/*{BIOS,bios,i440fx}*
%endif
install -m 755 bochs-debugger bochs-gdb $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_docdir}/bochs _installed-docs
rm $RPM_BUILD_ROOT%{_mandir}/man1/bochs-dlx.1*

mkdir -p $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm
#cp -pr disasm/*.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm/
#cp -pr disasm/*.cc $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm/
#cp -pr disasm/*.inc $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm/
cp -pr config.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu
cp -pr cpu/*.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/
cp -pr cpu/*.cc $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/decoder
cp -pr cpu/decoder/*.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/decoder/
cp -pr cpu/decoder/*.cc $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/decoder/
# Install osdep.h BZ 1786771
cp -pr osdep.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm/
rm -f $RPM_BUILD_ROOT%{_datadir}/bochs/SeaVGABIOS-README

%files
%doc _installed-docs/* README-* bios/SeaVGABIOS-README
%{_bindir}/bochs
%{_bindir}/bximage
%{_bindir}/bxhub
# Note: must include *.la in %%{_libdir}/bochs/plugins/
#%%{_libdir}/bochs/
%{_mandir}/man1/bochs.1*
%{_mandir}/man1/bximage.1*
%{_mandir}/man5/bochsrc.5*
%dir %{_datadir}/bochs/
%{_datadir}/bochs/keymaps/

%ifarch %{ix86} x86_64
%files bios
%{_datadir}/bochs/BIOS*
%{_datadir}/bochs/vgabios*
%{_datadir}/bochs/VGABIOS*
%{_datadir}/bochs/bios.bin-1.13.0
%{_datadir}/bochs/SeaBIOS-README
%{_datadir}/bochs/README-i440fx
%{_datadir}/bochs/i440fx.bin
%endif


%files debugger
%{_bindir}/bochs-debugger

%files gdb
%{_bindir}/bochs-gdb

%files devel
%{_prefix}/include/bochs/

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Feb 17 2025 Gwyn Ciesla <gwync@protonmail.com> - 3.0-1
- 3.0

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.8-1
- 2.8

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.7-6
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Florian Weimer <fweimer@redhat.com> - 2.7-4
- Port configure script to C99

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.7-1
- 2.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.11-3
- Drop svgalib

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.11-1
- 2.6.11 + SMP/debugger and iasl patches.

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.6.10-2
- Install osdep.h BZ 1786771

* Mon Dec 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.6.10-1
- 2.6.10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Gwyn Ciesla <limburgher@gmail.com> - 2.6.9-12
- Fix debugger plugin.

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.9-11
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.6.9-9
- BR fix.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 06 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.6.9-6
- Enable SMP.

* Thu Oct 26 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.6.9-5
- Patch includes to fix FTBFS.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.6.9-2
- Enable e1000, x86-64.
- Add cpu includes to devel.

* Fri May 05 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.6.9-1
- 2.6.9

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.6.2-11
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.6.2-8
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jon Ciesla <limburgher@gmail.com> - 2.6.2-5
- Add back one of the man page munging lines.

* Tue Aug 13 2013 Jon Ciesla <limburgher@gmail.com> - 2.6.2-4
- Drop noop man page munging.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Cole Robinson <crobinso@redhat.com> - 2.6.2-2
- Update configure for aarch64 (bz #925112)

* Tue May 28 2013 Jon Ciesla <limburgher@gmail.com> - 2.6.2-1
- 2.6.2.

* Mon May 27 2013 Dan Horák <dan[at]danny.cz> - 2.6.1-4
- fix non-x86 build

* Sat May 25 2013 Jon Ciesla <limburgher@gmail.com> - 2.6.1-3
- Fix bios symlinks.

* Sat May 25 2013 Jon Ciesla <limburgher@gmail.com> - 2.6.1-2
- Require seavgabios-bin, vgabios has been retired.

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 2.6.1-1
- 2.6.1.
- pci patches upstreamed.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 04 2012 Jon Ciesla <limburgher@gmail.com> - 2.6-1
- Update to 2.6.
- eh_frame patch upstreamed.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 2.5.1-4
- Add hardened build.

* Tue Mar 13 2012 Jon Ciesla <limburgher@gmail.com> - 2.5.1-3
- Add devel package.

* Tue Feb 21 2012 Jon Ciesla <limburgher@gmail.com> - 2.5.1-2
- Compile with disasm, BZ 798437.

* Fri Jan 20 2012 Jon Ciesla <limburgher@gmail.com> - 2.5.1-1
- Update to 2.5.1.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 30 2011 Jon Ciesla <limburgher@gmail.com> - 2.5-1
- Update to 2.5.
- Disabled vbe, vesa bios extensions.

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.4.6-2
- Rebuild for new libpng

* Thu Feb 24 2011 Jon Ciesla <limb@jcomserv.net> 2.4.6-1
- Update to 2.4.6.

* Mon Feb 14 2011 Chris Lalancette <clalance@redhat.com> - 2.4.5-3
- Add patch so rombios builds with gcc 4.6.0.
- Cleanup spec file to get rid of old cruft.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 29 2010 Jon Ciesla <limb@jcomserv.net> 2.4.5-1
- Update to 2.4.5.
- Updated read additional tables patch.
- Using cvs checkout done 4/29/2010, see upstream bug 2994370.

* Tue Dec 08 2009 Jon Ciesla <limb@jcomserv.net> 2.4.2-1
- Update to 2.4.2.
- Removed patches 1-4, 9, upstreamed.
- Updated to included bios, as bios is no longer at old location.

* Fri Dec 04 2009 Jon Ciesla <limb@jcomserv.net> 2.3.8-0.9.git04387139e3b
- Include symlinks to VGABIOS in vgabios rpm, BZ 544310.
- Enable cpu level 6.

* Fri Jul 31 2009 Glauber Costa <glommer@redhat.com> - 2:0.10.50-14.kvm88
- replace kvm-bios with a more modern version, and refresh instructions on how to get it.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-0.7.git04387139e3b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 11 2009 Glauber Costa <glommer@redhat.com> 2.3.8-0.6.git04387139e3b
- Fix Obsoletes/Provides pair.

* Wed Mar 11 2009 Glauber Costa <glommer@redhat.com> 2.3.8-0.5.git04387139e3b
- kvm needs a slightly different bios due to irq routing, so build it too.
  from kvm source. This is not ideal, but avoids the creation of yet another
  noarch subpackage.

* Fri Mar 06 2009 Glauber Costa <glommer@redhat.com> 2.3.8-0.4.git04387139e3b
- Provide and Obsolete bochs-bios-data to make sure no one is harmed during
  updates.

* Thu Mar 05 2009 Glauber Costa <glommer@redhat.com> 2.3.8-0.3.git04387139e3b
- added patches ;-)

* Thu Mar 05 2009 Glauber Costa <glommer@redhat.com> 2.3.8-0.2.git04387139e3b
- this time with sources added.

* Thu Mar 05 2009 Glauber Costa <glommer@redhat.com> 2.3.8-0.1.git04387139e3b
- updated to git 04387139e3b, and applied qemu's patch ontop.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Hans de Goede <hdegoede@redhat.com> 2.3.7-2
- Remove dlxlinux sub package, we cannot build this from source (rh 476878)

* Mon Jun  9 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.7-1
- New upstream release 2.3.7

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.6-3
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.6-2
- Fix compilation with gcc 4.3

* Mon Dec 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.6-1
- New upstream release 2.3.6

* Sun Sep 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.5-1
- New upstream release 2.3.5

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-7
- Fix CVE-2007-2894 (really fix bz 241799)

* Sun Aug  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-6
- Update License tag for new Licensing Guidelines compliance

* Wed Jul 18 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-5
- Fix CVE-2007-2893 (bz 241799)

* Mon Dec 18 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-4
- rebuilt without wxGTK as wxGTK is even more broken with wxGTK 2.8 then it
  was with 2.6

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.3-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-2
- Add -debugger and -gdb sub packages which contain special versions of
  bochs compiled with the buildin debugger resp. the gdb-stub (bz 206508)

* Sun Aug 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-1
- New upstream version 2.3 (final)

* Thu Aug 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-0.1.pre3
- New upstream version 2.3.pre3

* Mon Jul 17 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3-0.1.pre2
- New upstream version 2.3.pre2
- Drop upstreamed wx26 patch

* Wed Feb 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> - 2.2.6-1
- New upstream version 2.2.6
- Rebuild for new gcc4.1 and glibc
- Remove --enable-pae as that requires a CPU level of 6 with the new version
- Remove a few configure switches which are identical to the
  upstream defaults and thus don't do anything
- Add --enable-clgd54xx
- Add --with-svga which adds support for svgalib as display (x86(_64) only)
- Fix compile with wxGTK-2.6 and unconditionalize wxGTK build

* Fri Dec 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.2.1-2
- Adapt to modular X.
- Fix build with g++ 4.1.0.
- Conditionalize wxGTK build and default it to off (build failures w/2.6.x).
- Use sed instead of dos2unix and perl during build.

* Sat Jul  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.2.1-1
- 2.2.1, precision patch applied upstream.

* Sun May 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.2-2
- Try to fix x86_64 build.

* Sat May 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.2-1
- 2.2, buildpaths and fpu-regparms patches applied upstream, pthread and
  ncurses linking hacks no longer needed.
- Use upstream default display library, wx is clunky with wxGTK2 2.4.x.
- Enable 3DNow! emulation and the SDL display library.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.1.1-3
- rebuild on all arches

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.1.1-2
- rebuilt

* Sun Dec  5 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.1.1-1
- Update to 2.1.1.
- Enable PAE and 4M pages support.
- Loosen version in dlxlinux to main dependency.
- BuildRequire ncurses-devel instead of ncurses-c++-devel for FC3.
- Apply upstream fpu-regparm patch to fix the build on FC3.

* Fri Jan 16 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.1-0.fdr.2
- Fix RFB linking, force pthreads.
- dos2unix some -dlxlinux files.

* Mon Jan 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.1-0.fdr.1
- Update to 2.1.
- Make sure everything is built with GTK2.
- Add "--with debugger" rpmbuild option.
- Put SDL build behind the "--with sdl" rpmbuild option due to startup crashes.

* Sun Nov 30 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.1-0.fdr.0.3.pre2
- Update to 2.1pre2.

* Tue Oct 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.1-0.fdr.0.2.pre1
- Remove .cvsignore from docs.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.1-0.fdr.0.1.pre1
- Update to 2.1pre1.
- Enable 3DNow! on athlon.
- Other cosmetic tweaks.

* Sat Jul 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0.2-0.fdr.3
- List wanted GUIs explicitly, exclude svgalib (bug 306).

* Wed May 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0.2-0.fdr.2
- Rebuild with wxGTK2.

* Tue May 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0.2-0.fdr.1
- First Fedora release, based on upstream SRPM.
