Summary:	Java GNOME bindings
Name:		java-gnome
Version:	4.1.3
Release:	32%{?dist}
URL:		http://java-gnome.sourceforge.net
Source0:	http://ftp.gnome.org/pub/gnome/sources/java-gnome/4.1/java-gnome-%{version}.tar.xz
# Workaround for brp-java-repack-jars skipping top-level dot-files
Patch0:		java-gnome-4.1.3-libdir.patch
# Disable strict java 8 doclint
Patch1:		java-gnome-doclint.patch
# Argument -client not supported everywhere.
Patch2:		java-gnome-4.1.3-javaargs.patch
# Use "javac -h" instead of "javah" for JDK 11 compatibility
Patch3:		java-gnome-4.1.3-javah.patch
# Fix build script for Python 3
Patch4:		java-gnome-4.1.3-py3.patch
# This is the "Classpath" exception.
License:	GPLv2 with exceptions
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(cairo-svg)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk+-unix-print-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
#BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	gettext
BuildRequires:	junit
BuildRequires:	python3
BuildRequires:	java-devel >= 1:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	perl
BuildRequires: make
Requires:	java-headless >= 1:1.6.0
Requires:	jpackage-utils

%description
These are the Java bindings for GTK and GNOME! Featuring a robust 
engineering design, completely generated internals, a lovingly 
crafted layer presenting the public API, and steadily increasing 
coverage of the underlying libraries.

You can use java-gnome to develop sophisticated user interfaces 
for Linux applications so that they richly integrate with the 
GNOME Desktop while leveraging the power of the Java language 
and your expertise with it.

%package	javadoc
Summary:	Javadoc for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch:	noarch

%description	javadoc
This package contains the API documentation for %{name}, along with
design documentation and sample code.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Remove all binaries
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

# JDK 11 does not generate pointless empty headers for classes with no native methods
# so we have to fool the java-gnome build
mkdir -p tmp/include
for c in atk_AtkRegistry atk_AtkUtil glib_GBoxed gdk_GdkWindowAttr gdk_GdkPixbufSimpleAnimIter gtk_GtkPlug gtk_GtkFilePath sourceview_GtkSourceViewSearchFlags \
pango_PangoAnalysis pango_PangoEngine pango_PangoEngineShape pango_PangoEngineLang pango_PangoGlyphGeometry pango_PangoGlyphInfo pango_PangoCairoFcFont pango_PangoFcFont ; do
	touch tmp/include/org_gnome_${c}.h
done

%build
# It'll get two conflicting --libdir parameters, but the last one
# happens to win which is what we want.
%configure --jardir=%{_jnidir} --libdir=%{_libdir}/%{name}

# The build system does not support parallell builds, so no
# _smp_mflags.
make V=1 build-java doc

%install
make install DESTDIR=%{buildroot}

# Remove the versioned jar
rm -rf %{buildroot}%{_jnidir}/gtk.jar
mv %{buildroot}%{_jnidir}/gtk-*.jar %{buildroot}%{_jnidir}/gtk.jar
# for backwards compatibility
mkdir -p %{buildroot}%{_libdir}/%{name}
ln -s %{_jnidir}/gtk.jar %{buildroot}%{_libdir}/%{name}/gtk.jar

# Install javadoc
mkdir -p %{buildroot}%{_javadocdir}
cp -rp doc/api %{buildroot}%{_javadocdir}/%{name}

%files
%doc AUTHORS* COPYING* README* NEWS* LICENCE*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.jar
%{_libdir}/%{name}/*.so
%{_jnidir}/gtk.jar

%files javadoc
# Note that not all here is javadoc. Two subpackages for documentation
# seems silly.
%doc doc/design doc/examples
%{_javadocdir}/%{name}

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 4.1.3-30
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 09 2020 Alexander Boström <abo@root.snowtree.se> - 4.1.3-26
- Fix date in changelog

* Sun Aug 09 2020 Alexander Boström <abo@root.snowtree.se> - 4.1.3-25
- Switch to Python 3 for build

* Wed Jul 29 2020 Mat Booth <mat.booth@redhat.com> - 4.1.3-24
- Fix javah usage for JDK 11 compatibility

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 4.1.3-22
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Alexander Boström <abo@root.snowtree.se> - 4.1.3-18
- Add perl build requirement

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.1.3-16
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Alexander Boström <abo@root.snowtree.se> - 4.1.3-12
- Remove old rpm workaround

* Mon Jun 26 2017 Alexander Boström <abo@root.snowtree.se> - 4.1.3-11
- Make java arguments ppc compatible (java-gnome-4.1.3-javaargs.patch)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mat Booth <mat.booth@redhat.com> - 4.1.3-8
- Fix FTBFS by disabling javadoc linting

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 4.1.3-5
- Install jar into %%_jnidir per latest guidelines (#1101069)
- Workaround for brp-java-repack-jars skipping top-level dot-files
- Remove obsolete gtkspell BR

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 4.1.3-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Mat Booth <fedora@matbooth.co.uk> - 4.1.3-1
- Update to latest upstream, rhbz #852985
- Drop no longer needed JDK7 patch
- Minor changes for newer guidelines

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 4.1.1-7
- Rebuilt for gtksourceview3 soname bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Alexander Boström <abo@root.snowtree.se> - 4.1.1-3
- Add java-gnome-4.1.1-extendsboxed.patch: Java 1.7 compat.

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 4.1.1-2
- Rebuild for new libpng

* Tue Jul 12 2011 Alexander Boström <abo@root.snowtree.se> - 4.1.1-1
- Upgrade to 4.1.1, GNOME 3 deps, remove libnotify patch.
- Remove javadocbuild patch.
- Remove BuildRoot and an obsolete conditional.

* Mon Jul 11 2011 Alexander Boström <abo@root.snowtree.se> - 4.0.20-1
- Upgrade to 4.0.20
- reapply libnotify patch

* Thu Jul 07 2011 Alexander Boström <abo@root.snowtree.se> - 4.0.19-5
- Rebuild

* Wed Jul 06 2011 Alexander Boström <abo@root.snowtree.se> - 4.0.19-4
- remove confusingly named .libnotify07 file from example code
- add workaround for javadoc build problem (rhbz bug 715804)

* Sun Apr 03 2011 Alexander Boström <abo@root.snowtree.se> - 4.0.19-3
- https://fedoraproject.org/wiki/Packaging:Java#Filenames does not
  apply to JNI JAR files. Avoid needless symlinking in new branches.

* Sun Apr 03 2011 Alexander Boström <abo@root.snowtree.se> - 4.0.19-2
- Make the libnotify patch conditional.

* Sat Apr 02 2011 Alexander Boström <abo@root.snowtree.se> - 4.0.19-1
- Update to the latest release.
- Patch for libnotify 0.7 compatibility.
- Add missing buildreqs.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 19 2010 Alexander Boström <abo@root.snowtree.se> - 4.0.16-3
- remove Xvfb buildreq (not used)

* Sat Jul 17 2010 Alexander Boström <abo@root.snowtree.se> - 4.0.16-2
- rebase configure patch

* Tue Jun 22 2010 Alexander Boström <abo@root.snowtree.se> - 4.0.16-1
- update to 4.0.16
- simplify the configure script patch
- pull configure patch from upstream bzr

* Sun Apr 18 2010 Alexander Boström <abo@root.snowtree.se> - 4.0.15-3
- add back the jar symlink

* Sat Apr 17 2010 Alexander Boström <abo@root.snowtree.se> - 4.0.15-2
- make the javadoc subpackage noarch
- add an unversioned symlink to the javadoc

* Fri Mar 19 2010 Alexander Boström <abo@root.snowtree.se> - 4.0.15-1
- upgrade to 4.0.15
- remove jar symlink that's not actually required

* Sat Jan  2 2010 Alexander Boström <abo@root.snowtree.se> - 4.0.14-3
- rearrange jar symlinks

* Fri Jan  1 2010 Alexander Boström <abo@root.snowtree.se> - 4.0.14-2
- fix license
- fix .jar, .class check

* Thu Dec 31 2009 Alexander Boström <abo@root.snowtree.se> - 4.0.14-1
- upgrade to 4.0.14
- add lots of BuildRequires
- use pkg-config to get values for CFLAGS and LDFLAGS
- rename jar
- various little fixes

* Fri Jul  3 2009 Alexander Boström <abo@root.snowtree.se> - 4.0.11-1
- upgrade to 4.0.11
- make jpackagecompatible patch apply cleanly
- remove jnipath patch, it won't apply and it looks like it's not
  needed anymore
- move JARs and JNI .so according to guidelines
- install javadoc and put it in a subpackage

* Wed May 14 2008 Colin Walters <walters@redhat.com> - 4.0.7-1
- Initial version
