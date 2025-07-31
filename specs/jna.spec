# Allow conditionally building without the reflections library
%if %{defined rhel}
%bcond_with reflections
%else
%bcond_without reflections
%endif

Name:           jna
Version:        5.17.0
Release:        %autorelease
Summary:        Pure Java access to native libraries
# Most of code is dual-licensed under either LGPL 2.1+ only or Apache
# License 2.0.  WeakIdentityHashMap.java was taken from Apache CXF,
# which is pure Apache License 2.0.
License:        Apache-2.0 OR LGPL-2.1-or-later

URL:            https://github.com/java-native-access/jna/
# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.zst
Source1:        package-list
Source2:        generate-tarball.sh

Patch0:         0001-Adapt-build.patch
# This patch is Fedora-specific for now until we get the huge
# JNI library location mess sorted upstream
Patch1:         0002-Load-system-library.patch
# The X11 tests currently segfault; overall I think the X11 JNA stuff is just a
# Really Bad Idea, for relying on AWT internals, using the X11 API at all,
# and using a complex API like X11 through JNA just increases the potential
# for problems.
Patch2:         0003-Tests-headless.patch
# Adds --allow-script-in-comments arg to javadoc to avoid error
Patch3:         0004-Fix-javadoc-build.patch
# Avoid generating duplicate manifest entry
# See https://bugzilla.redhat.com/show_bug.cgi?id=1469022
Patch4:         0005-Fix-duplicate-manifest-entry.patch
# We don't want newly added warnings to break our build
Patch5:         0006-Remove-Werror.patch

Patch6:         0007-Support-openjdk-17.patch

ExclusiveArch:  %{java_arches}

# We manually require libffi because find-requires doesn't work
# inside jars.
Requires:       libffi
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  libffi-devel
BuildRequires:  ant-openjdk25 
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  objectweb-asm
BuildRequires:  hamcrest
%if %{with reflections}
BuildRequires:  reflections
%endif

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 5.15.0-4

%description
JNA provides Java programs easy access to native shared libraries
(DLLs on Windows) without writing anything but Java code. JNA's
design aims to provide native access in a natural way with a
minimum of effort. No boilerplate or generated code is required.
While some attention is paid to performance, correctness and ease
of use take priority.

%package        contrib
Summary:        Contrib for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    contrib
This package contains the contributed examples for %{name}.

%prep
%autosetup -p1
cp %{SOURCE1} .

chmod -Rf a+rX,u+w,g-w,o-w .
sed -i 's|@LIBDIR@|%{_libdir}/%{name}|' src/com/sun/jna/Native.java

# TEMPLATE has to be changed to %%version in the pom files
# in order to generate correct provides
sed -i 's/TEMPLATE/%{version}/' \
 pom-jna-jpms.xml \
 pom-jna-platform.xml \
 pom-jna.xml \
 pom-jna-platform-jpms.xml \
;

# clean LICENSE.txt
sed -i 's/\r//' LICENSE

chmod -c 0644 LICENSE OTHERS CHANGES.md

%if %{with reflections}
sed s,'<include name="junit.jar"/>,&<include name="reflections.jar"/>,' -i build.xml
build-jar-repository -s -p lib junit reflections
%else
build-jar-repository -s -p lib junit
rm test/com/sun/jna/StructureFieldOrderInspector.java
rm test/com/sun/jna/StructureFieldOrderInspectorTest.java
%endif
ln -s $(xmvn-resolve ant:ant:1.10.5) lib/ant.jar
ln -s $(xmvn-resolve org.ow2.asm:asm) lib/asm-8.0.1.jar
ln -s $(xmvn-resolve org.hamcrest:hamcrest-all) lib/hamcrest-core-1.3.jar
ln -s $(xmvn-resolve org.reflections:reflections) lib/test/reflections.jar

cp lib/native/aix-ppc64.jar lib/clover.jar

%build
# We pass -Ddynlink.native which comes from our patch because
# upstream doesn't want to default to dynamic linking.
# -Drelease removes the .SNAPSHOT suffix from maven artifact names
#ant -Dcflags_extra.native="%{optflags}" -Ddynlink.native=true native compile javadoc jar contrib-jars
ant -Drelease -Dcompatibility=1.8 -Dplatform.compatibility=1.8\
 -Dcflags_extra.native="%{optflags}" -Ddynlink.native=true -DCC=%{__cc} native dist
# remove compiled contribs
find contrib -name build -exec rm -rf {} \; || :

%install
# NOTE: JNA has highly custom code to look for native jars in this
# directory.  Since this roughly matches the jpackage guidelines,
# we'll leave it unchanged.
install -d -m 755 %{buildroot}%{_libdir}/%{name}
install -m 755 build/native*/libjnidispatch*.so %{buildroot}%{_libdir}/%{name}/

%mvn_file :jna jna jna/jna %{_javadir}/jna

%mvn_package :jna-platform contrib
%mvn_alias :jna-platform :platform

%mvn_artifact pom-jna.xml build/jna-min.jar
%mvn_artifact pom-jna-platform.xml contrib/platform/dist/jna-platform.jar

%mvn_install

%files -f .mfiles
%doc OTHERS README.md CHANGES.md TODO
%license LICENSE LGPL2.1 AL2.0
%{_libdir}/%{name}

%files contrib -f .mfiles-contrib

%changelog
%autochangelog
