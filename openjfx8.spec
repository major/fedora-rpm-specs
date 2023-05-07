%global openjfxdir %{_jvmdir}/%{name}

Name:           openjfx8
Version:        8.0.202
Release:        35.b07%{?dist}
Summary:        Rich client application platform for Java

#fxpackager is BSD
License:        GPL v2 with exceptions and BSD
URL:            http://openjdk.java.net/projects/openjfx/

Source0:        http://hg.openjdk.java.net/openjfx/8u-dev/rt/archive/8u202-b07.tar.bz2
Source1:        README.fedora
Source2:        pom-base.xml
Source3:        pom-builders.xml
Source4:        pom-controls.xml
Source5:        pom-fxml.xml
Source6:        pom-fxpackager.xml
Source7:        pom-graphics.xml
Source8:        pom-graphics_compileDecoraCompilers.xml
Source9:        pom-graphics_compileDecoraJavaShaders.xml
Source10:       pom-graphics_compileJava.xml
Source11:       pom-graphics_compilePrismCompilers.xml
Source12:       pom-graphics_compilePrismJavaShaders.xml
Source13:       pom-graphics_libdecora.xml
Source14:       pom-graphics_libglass.xml
Source15:       pom-graphics_libglassgtk2.xml
Source16:       pom-graphics_libglassgtk3.xml
Source17:       pom-graphics_libjavafx_font.xml
Source18:       pom-graphics_libjavafx_font_freetype.xml
Source19:       pom-graphics_libjavafx_font_pango.xml
Source20:       pom-graphics_libjavafx_iio.xml
Source21:       pom-graphics_libprism_common.xml
Source22:       pom-graphics_libprism_es2.xml
Source23:       pom-graphics_libprism_sw.xml
Source24:       pom-jmx.xml
Source25:       pom-media.xml
Source26:       pom-openjfx.xml
Source27:       pom-swing.xml
Source28:       pom-web.xml
Source29:       shade.xml
Source30:       build.xml
Source31:       buildSrc.xml
Source32:       fxpackager-native.xml
Source33:       fxpackager-so.xml
Source34:       build-sources.xml

Patch0:         0000-Fix-wait-call-in-PosixPlatform.patch
Patch1:         0003-fix-cast-between-incompatible-function-types.patch
Patch2:         0004-Fix-Compilation-Flags.patch
Patch3:         0005-fxpackager-extract-jre-accept-symlink.patch
Patch4:         openjfx8-c99.patch

ExclusiveArch:  x86_64

Requires:       java-1.8.0-openjdk

BuildRequires:  maven-local-openjdk8
BuildRequires:	ant
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-static
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.codehaus.mojo:native-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(gl)

Provides:       openjfx = 2:%{version}-%{release}
Obsoletes:      openjfx <= 2:8.0.202-13

%description
JavaFX/OpenJFX is a set of graphics and media APIs that enables Java
developers to design, create, test, debug, and deploy rich client
applications that operate consistently across diverse platforms.

The media and web module have been removed due to missing dependencies.
The swt module has been removed due to incompatible runtime version 
(openjdk 11).

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: java-devel
Summary: OpenJFX development tools and libraries

%description devel
%{summary}.

%package src
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: OpenJFX Source Bundle

%description src
%{summary}.

%global debug_package %{nil}

%prep
%setup -q -n rt-8u202-b07
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
 
cp %{SOURCE1} .

#prep for graphics
cp -a modules/graphics/src/main/resources/com/sun/javafx/tk/quantum/*.properties modules/graphics/src/main/java/com/sun/javafx/tk/quantum

#prep for base
cp -a modules/base/src/main/java8/javafx modules/base/src/main/java

#prep for swt (removal)
rm -rf modules/graphics/src/main/java/com/sun/glass/ui/swt/
rm -rf modules/builders/src/main/java/javafx/embed/swt

find -name '*.class' -delete
find -name '*.jar' -delete

#copy maven files
cp -a %{_sourcedir}/pom-*.xml .
mv pom-openjfx.xml pom.xml

for MODULE in base graphics controls swing fxml media web builders fxpackager jmx
do
	mv pom-$MODULE.xml ./modules/$MODULE/pom.xml
done

#shade
mkdir shade
cp -a %{_sourcedir}/shade.xml ./shade/pom.xml

#fxpackager native exe
mkdir ./modules/fxpackager/native
cp -a %{_sourcedir}/fxpackager-native.xml ./modules/fxpackager/native/pom.xml
#fxpackager libpackager.so
mkdir ./modules/fxpackager/so
cp -a %{_sourcedir}/fxpackager-so.xml ./modules/fxpackager/so/pom.xml

cp -a %{_sourcedir}/buildSrc.xml ./buildSrc/pom.xml

mkdir ./modules/graphics/{compileJava,compilePrismCompilers,compilePrismJavaShaders,compileDecoraCompilers,compileDecoraJavaShaders,libdecora,libjavafx_font,libjavafx_font_freetype,libjavafx_font_pango,libglass,libglassgtk2,libglassgtk3,libjavafx_iio,libprism_common,libprism_es2,libprism_sw}
for GRAPHMOD in compileJava compilePrismCompilers compilePrismJavaShaders compileDecoraCompilers compileDecoraJavaShaders libdecora libjavafx_font libjavafx_font_freetype libjavafx_font_pango libglass libglassgtk2 libglassgtk3 libjavafx_iio libprism_common libprism_es2 libprism_sw
do
	mv pom-graphics_$GRAPHMOD.xml ./modules/graphics/$GRAPHMOD/pom.xml
done

#set VersionInfo
cp -a %{_sourcedir}/build.xml .
ant -f build.xml

cp -a %{_sourcedir}/build-sources.xml .

%build

#set openjdk8 for build
#export JAVA_HOME=%{_jvmdir}/java-1.8.0-openjdk
%mvn_build -f --skip-javadoc

ant -f build-sources.xml

%install
install -d -m 755 %{buildroot}%{openjfxdir}
mkdir -p %{buildroot}%{openjfxdir}/bin
mkdir -p %{buildroot}%{openjfxdir}/lib
mkdir -p %{buildroot}%{openjfxdir}/rt/lib/{amd64,ext}

cp -a shade/target/jfxrt.jar %{buildroot}%{openjfxdir}/rt/lib/ext
cp -a modules/graphics/libdecora/target/libdecora_sse.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libglass/target/libglass.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libglassgtk2/target/libglassgtk2.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libglassgtk3/target/libglassgtk3.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libjavafx_font/target/libjavafx_font.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libjavafx_font_freetype/target/libjavafx_font_freetype.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libjavafx_font_pango/target/libjavafx_font_pango.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libjavafx_iio/target/libjavafx_iio.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libprism_common/target/libprism_common.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libprism_es2/target/libprism_es2.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/graphics/libprism_sw/target/libprism_sw.so %{buildroot}%{openjfxdir}/rt/lib/amd64
cp -a modules/jmx/target/javafx-mx.jar %{buildroot}%{openjfxdir}/lib
cp -a modules/fxpackager/target/fxpackager-ant-javafx.jar %{buildroot}%{openjfxdir}/lib/ant-javafx.jar
cp -a modules/fxpackager/target/fxpackager-packager.jar %{buildroot}%{openjfxdir}/lib/packager.jar
install -m 755 modules/fxpackager/src/main/native/javapackager/shell/javapackager %{buildroot}%{openjfxdir}/bin
install -m 755 modules/fxpackager/src/main/native/javapackager/shell/javapackager %{buildroot}%{openjfxdir}/bin/javafxpackager

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 modules/fxpackager/src/main/man/man1/* %{buildroot}%{_mandir}/man1

install -d -m 755 %{buildroot}%{_mandir}/ja_JP/man1
install -m 644 modules/fxpackager/src/main/man/ja_JP.UTF-8/man1/* %{buildroot}%{_mandir}/ja_JP/man1

install -m 644 javafx-src.zip %{buildroot}%{openjfxdir}/javafx-src.zip

mkdir -p %{buildroot}%{_bindir}
ln -s %{openjfxdir}/bin/javafxpackager %{buildroot}%{_bindir}
ln -s %{openjfxdir}/bin/javapackager %{buildroot}%{_bindir}

%files
%dir %{openjfxdir}
%{openjfxdir}/rt
%license LICENSE
%doc README
%doc README.fedora

%files devel
%{openjfxdir}/lib
%{openjfxdir}/bin
%{_bindir}/javafxpackager
%{_bindir}/javapackager
%{_mandir}/man1/javafxpackager.1*
%{_mandir}/man1/javapackager.1*
%{_mandir}/ja_JP/man1/javafxpackager.1*
%{_mandir}/ja_JP/man1/javapackager.1*
%license LICENSE
%doc README
%doc README.fedora

%files src
%{openjfxdir}/javafx-src.zip

%changelog
* Fri May 05 2023 Florian Weimer <fweimer@redhat.com> - 8.0.202-35.b07
- C99 compatibility fix

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-34.b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-33.b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 09 2022 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-32.b07
- Change to 'exec' goals of exec-maven-plugin tasks.

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 8.0.202-31.b07
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-30.b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-29.b07
- The swt module has been removed due to incompatible runtime version (openjdk
  11)

* Thu Aug 05 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-28.b07
- Fix FTBFS in Fedora rawhide see bug 1987773 and fix bug 1962258. Package javadoc is removed because xmvn couldn't build javadoc for java 8

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-27.b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-26.b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 23 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-25.b07
- Add package migration from previous openjfx to openjfx8 (see bug 1890805)

* Tue Aug 04 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-24.b07
- Fix FTBFS in Fedora rawhide see bug 1865157

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-23.b07
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-22.b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-21.b07
- Added openjfx-src package (see bug 1836908)

* Tue May 12 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-20.b07
- renaming package from openjfx to openjfx8

* Tue May 12 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-11.b07
- wrong value returned by javafx.runtime.version

* Wed Feb 12 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-10.b07
- Replace gradle build with maven build

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-9.b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Nicolas De Amicis - 8.0.202-8.b07
- fxpackager extracts jre with symlinks (see bug 1700884) + drop SWT support for
  32 bits architectures (FTBFS in Fedora rawhide see bug 1736382)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-7.b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Nicolas De Amicis - 8.0.202-6.b07
- Remove orphaned dependency (javapackages-tools)

* Mon Feb 04 2019 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-5.b07
- Fix compilation flags (see bug 1667675)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.202-4.b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-3.b07
- Update to upstream version 8.0.202b07 and adding gtk3 support
  (libglassgtk3.so)

* Tue Nov 27 2018 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.202-2.b02
- Update to upstream version 8.0.202b02

* Mon Nov 12 2018 Nicolas De Amicis <deamicis@bluewin.ch> - 8.0.152-19.b05
- Fix missing java packages in openjfx

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.152-18.b05
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Mat Booth <mat.booth@redhat.com> - 8.0.152-17.b05
- Fix failure to build from source

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.152-16.b05
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.152-15.b05
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.152-14.b05
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-13.b05
- Update to upstream version 8.0.152b05

* Thu Jun 15 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-12.b04
- Removed BuildArch: noarch for subpackages that requires the parent package

* Thu Jun 15 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-11.b04
- Build on i686 too

* Wed May 31 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-10.b04
- Update to upstream version 8.0.152b04

* Wed May 31 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-9.b03
- Added requires on java and java-devel
- Updated license

* Thu May 18 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-8.b03
- Added requires on javapackages-tools
- Added requires on parent package for subpackages devel and src

* Fri May 12 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-7.b03
- Introduce sub-package devel

* Mon May 08 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-6.b03
- Update to upstream version 8.0.152b03

* Mon May 01 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-5.b02
- Update to upstream version 8.0.152b02

* Wed Apr 05 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-4.b00
- Only build for x86 and x86_64, will fail to build on other platforms

* Thu Jan 19 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-3.b00
- Include javadoc sub-package

* Tue Jan 17 2017 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-2.b00
- Include src sub-package

* Fri Dec 30 2016 Jonny Heggheim <hegjon@gmail.com> - 8.0.152-1.b00
- Update to upstream version 8.0.152b00

* Tue Apr 26 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.0.91-1
- Update to upstream version 8.0.91

* Tue Apr 26 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.0.60-1
- Update to upstream version 8.0.60

* Mon Jul  6 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.0.40-1
- Initial packaging
