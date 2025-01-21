# Copyright (c) 2007 oc2pus <toni@links2linux.de>
# Copyright (c) 2007 Hans de Goede <j.w.r.degoede@hhs.nl>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to us at the above email addresses

Name:           sdljava
Version:        0.9.1
Release:        65%{?dist}
Summary:        Java binding to the SDL API
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sdljava.sourceforge.net/
# this is http://downloads.sourceforge.net/%%{name}/%%{name}-%%{version}.tar.gz
# with the included Microsoft Copyrighted Arial fonts removed
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-runtest.sh
Patch0:         sdljava-0.9.1-regen.patch
Patch1:         sdljava-0.9.1-ftgl213.patch
Patch2:         sdljava-0.9.1-ruby19.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ftgl-devel
BuildRequires:  glew-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  swig
BuildRequires:  jdom
BuildRequires:  xml-commons-apis
BuildRequires:  %{_bindir}/ruby
BuildRequires:  rubygems
# To generate the replacement font symlinks for the sdljava-demo testdata
BuildRequires:  font(dejavusans) fontconfig
# sdljava provides java bindings for SDL, so it can only run on java_arches
ExclusiveArch:  %{java_arches}

Requires:       java
Requires:       javapackages-filesystem
Requires:       jdom

%description
sdljava is a Java binding to the SDL API being developed by Ivan Ganza.

sdljava provides the ability to write games and other applications
from the java programming language. sdljava is designed to be fast,
efficient and easy to use.


%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
Javadoc for %{name}.


%package demo
Summary:        Some examples for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       font(dejavusans)
Requires:       javapackages-tools

%description demo
Demonstrations and samples for %{name}.


%prep
%autosetup -p1

find -name '*.jar' -or -name '*.class' -or -name '*.bat' -name '*.so' -delete
rm -r etc/build/gljava/windows etc/build/windows

# Newer ftgl no longer exports the FTFace class
rm src/org/gljava/opengl/ftgl/FTFace.java
iconv -f ISO_8859-2 -t UTF8 docs/CHANGES_0_9_1 > docs/CHANGES_0_9_1.tmp
touch -r docs/CHANGES_0_9_1 docs/CHANGES_0_9_1.tmp
mv docs/CHANGES_0_9_1.tmp docs/CHANGES_0_9_1

# patch in gcc include path so that swig can find it
GCC_PATH=`gcc -print-search-dirs | grep install | cut -f 2 -d " "`
sed -i "s#@GCC_INCLUDE_PATH@#$GCC_PATH/include#g" \
  etc/build/linux/Makefile \
  etc/build/gljava/linux/Makefile \
  etc/build/gljava/linux/ftgl/Makefile

# adjust testdata path in demos
find ./testsrc -name '*.java' | xargs sed -i \
  -e 's|testdata|%{_datadir}/%{name}/testdata|g'

# use system versions of jdom
build-jar-repository -p lib jdom

# copy the Linux Makefiles into place
cp etc/build/linux/Makefile src/sdljava/native
cp etc/build/gljava/linux/Makefile src/org/gljava/opengl/native
cp etc/build/gljava/linux/ftgl/Makefile src/org/gljava/opengl/native/ftgl

# and remove the swig generated code so that it gets regenerated
rm src/sdljava/native/SDL*_wrap.c src/sdljava/native/SDL_types.h
rm src/org/gljava/opengl/native/glew_wrap.c


%build
# We must add -D__%%{_arch}__ to swigs arguments as swig doesn't do that itself.
# Special case ppc as the define is powerpc not ppc and both ppc and ppc64
# must be set for ppc64, also add -D__LONG_DOUBLE_128__ which works around
# swig barfing on bits/stdlib-ldbl.h
%ifarch ppc
export ARCH_DEFINE="-D__powerpc__ -D__LONG_DOUBLE_128__"
%endif
%ifarch ppc64
export ARCH_DEFINE="-D__powerpc__ -D__powerpc64__ -D__LONG_DOUBLE_128__"
%endif
%ifarch ppc64le
export ARCH_DEFINE="-D__powerpc__ -D__powerpc64__ -D__LITTLE_ENDIAN__ -D\"__BYTE_ORDER__=1234\" -D\"_CALL_ELF=2\" -D__LONG_DOUBLE_128__"
%endif
%ifarch s390x
export ARCH_DEFINE="-D__s390x__ -D__LONG_DOUBLE_128__"
%endif
# special case ix86 as all of ix86 should define __i386__
%ifarch %{ix86}
export ARCH_DEFINE="-D__i386__"
%endif
# arm also needs a bunch of special defines
%ifarch %{arm}
export ARCH_DEFINE="-D__arm__ -D__ARMEL__ -D__ARM_EABI__"
%ifnarch armv5tel
export ARCH_DEFINE="$ARCH_DEFINE -D__ARM_PCS_VFP"
%endif
%endif
# All other archs
if [ -z "$ARCH_DEFINE" ]; then
  export ARCH_DEFINE="-D__%{_arch}__"
fi

export JAVA_HOME=%{_jvmdir}/java

pushd src/sdljava/native
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
make libsdljava_gfx.so CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
popd

pushd src/org/gljava/opengl/native
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
popd

pushd src/org/gljava/opengl/native/ftgl
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
popd

ant jar javadoc


%install
# dirs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_jnidir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# jars
install -m 644 lib/%{name}.jar \
  $RPM_BUILD_ROOT%{_jnidir}/%{name}.jar

# native libraries
install -m 755 lib/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}

# javadoc
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo scripts
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
pushd bin
rm runtest.sh
rm run-bsh.sh
for i in `ls -1 *.sh`; do
   sed -i -e 's|./runtest.sh|%{_bindir}/%{name}-runtest.sh|g' $i
   FN=`echo $i | awk 'BEGIN { FS="." }{ print $1 }'`
   install -m 755 $i $RPM_BUILD_ROOT%{_bindir}/%{name}-$FN.sh
done
popd

#test data
cp -a testdata $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s $(fc-match -f "%{file}" "sans") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/arial.ttf
ln -s $(fc-match -f "%{file}" "sans:bold") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/arialbd.ttf
ln -s $(fc-match -f "%{file}" "sans:italic") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/ariali.ttf
ln -s $(fc-match -f "%{file}" "sans:bold:italic") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/arialbi.ttf


%files
%doc README TODO docs/CHANGES_0_9_1
%{_jnidir}/%{name}.jar
%{_libdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo
%{_bindir}/%{name}-*.sh
%{_datadir}/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.1-64
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.9.1-62
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Hans de Goede <hdegoede@redhat.com> - 0.9.1-57
- sdljava provides java bindings for SDL and the JDK is no longer
  build on i686, disable i686 builds (rhbz#2104100)

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.9.1-56
- Rebuild for glew 2.2

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.9.1-55
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec  2 2021 Hans de Goede <hdegoede@redhat.com> - 0.9.1-53
- Drop sdljava-run-bsh.sh demo
- Drop now unnecessary bsh Requires

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.9.1-49
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Mar  9 2020 Hans de Goede <hdegoede@redhat.com> - 0.9.1-48
- Use fc-match to generate dejavu font file symlinks in -demo in case the
  file-paths or names change again in the future

* Fri Mar  6 2020 Hans de Goede <hdegoede@redhat.com> - 0.9.1-47
- Replace path requires on dejavu with Requires: font(dejavusans) (rhbz#1731701)
- Adjust -demo font paths for F32+ font path changes (rhbz#1806272)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Hans de Goede <hdegoede@redhat.com> - 0.9.1-45
- Replace unnecessary BuildRequires: jruby with BuildRequires: rubygems
- Drop version prefix from javadocs installation the ghosted symlink
  blocking us from doing this has last shipped in Fedora 16
- Update to match latest java packaging guidelines

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.9.1-42
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Michael Simacek <msimacek@redhat.com> - 0.9.1-40
- Add BR on gcc and make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 26 2017 Vít Ondruch <vondruch@redhat.com> - 0.9.1-38
- Prefer dependency on "%%{_bindir}/ruby".

* Mon Sep 04 2017 Michael Simacek <msimacek@redhat.com> - 0.9.1-37
- Fix build on s390x

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-33
- Rebuild for glew 2.0.0

* Sun Jul 17 2016 Michael Simacek <msimacek@redhat.com> - 0.9.1-32
- Fix FTBFS
- Specfile cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.9.1-30
- Rebuild for glew 1.13

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 01 2014 Karsten Hopp <karsten@redhat.com> 0.9.1-28
- fix ppc64le build

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 0.9.1-26
- Rebuild for new SDL_gfx

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.9.1-24
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Hans de Goede <hdegoede@redhat.com> - 0.9.1-22
- Fix FTBFS on ARM (rhbz#893157)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.9.1-20
- Rebuild for glew 1.9.0

* Thu Jul 26 2012 Hans de Goede <hdegoede@redhat.com> - 0.9.1-19
- Fix building with ruby 1.9
- Rebuilt for new GLEW

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Hans de Goede <hdegoede@redhat.com> - 0.9.1-16
- Rebuild for new SDL_gfx
- Drop gcj aot bits, Fedora has not been using these for a long long time
- Update to match latest java packaging guidelines

* Mon Jun 20 2011 ajax@redhat.com - 0.9.1-15
- Rebuild for new glew soname

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Hans de Goede <hdegoede@redhat.com> 0.9.1-12
- Rebuild for new ftgl (#501323)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  8 2008 Hans de Goede <hdegoede@redhat.com> 0.9.1-10
- Fixed unowned /usr/share/sdljava dir in the -demo package (bz 474604)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-9
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-8
- Rebuild for new glew

* Sun Dec  9 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-7
- And the dejavu-fonts fontfile names changed back again (what fun)
- The gcj bug causing us to not compile has been fixed, use gcj again
  and drop ExclusiveArch
- There is no reason for us to run ldconfig!
- Sigh we must now define __arch__ ourself as the newer swig doesn't

* Tue Nov 20 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-6
- Adjust font symlinks in sdljava-demo package for fontfile name changes in
  dejavu-fonts (bz 388861)

* Thu Sep 20 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-5
- BuildRequire icedtea as building with gcj fails (bug 297961)

* Wed Sep 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-4
- Make all doc files UTF-8

* Mon Sep 17 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-3
- Fix determination of gcc include path

* Tue Sep 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-2
- Dynamically determine gcc include path instead of hardcoding it, so that
  sdljava will build on other setups then devel-x86_64 too (oops).

* Sat Sep  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-1
- Adapted Packman spec file for Fedora

* Mon Jun 18 2007 Toni Graffy <toni@links2linux.de> - 0.9.1-0.pm.2
- rebuild with glew-1.3.6

* Sat Jun 16 2007 Toni Graffy <toni@links2linux.de> - 0.9.1-0.pm.1
- initial build 0.9.1
- repacked as tar.bz2
