Epoch:                  1

%global swtdir          eclipse-platform-sources-I20221123-1800
%global eclipse_rel     %{version}
%global eclipse_tag     R-%{eclipse_rel}-202211231800
%global swtsrcdir       eclipse.platform.swt/bundles/org.eclipse.swt
%global eclipse_arch    %{_arch}

Name:           eclipse-swt
Version:        4.26
Release:        1%{?dist}
Summary:        Eclipse SWT: The Standard Widget Toolkit for GTK+

License:        EPL-2.0
URL:            https://www.eclipse.org/swt/

Source0:        https://download.eclipse.org/eclipse/downloads/drops4/%{eclipse_tag}/eclipse-platform-sources-%{eclipse_rel}.tar.xz
# Copy of the script https://git.eclipse.org/c/linuxtools/org.eclipse.linuxtools.eclipse-build.git/tree/utils/ensure_arch.sh. Need for create secondary arch for s390x
Source1:        ensure_arch.sh

# Avoid the need for a javascript interpreter at build time
Patch0:         eclipse-swt-avoid-javascript-at-build.patch
# Remove eclipse tasks and modify build tasks to generate jar like expected
Patch1:         eclipse-swt-rm-eclipse-tasks-and-customize-build.patch
# Add fedora cflags to build native libs
Patch2:         eclipse-swt-fedora-build-native.patch

ExclusiveArch:  %{java_arches} 

Requires:       java-11-openjdk
Requires:       webkit2gtk3

BuildRequires:  java-11-openjdk-devel
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  webkit2gtk3-devel
BuildRequires:  cairo-devel
BuildRequires:  gtk3-devel
BuildRequires:  mesa-libGLU-devel

Provides:       eclipse-swt = 1:%{version}-%{release}
Obsoletes:      eclipse-swt <= 1:4.19-3

%description
SWT is an open source widget toolkit for Java designed to provide 
efficient, portable access to the user-interface facilities of the 
operating systems on which it is implemented.

%javadoc_package

%prep
%setup -q -n %{swtdir}
%patch0 -p1
%patch1 -p1

# Remove pre-compiled native launchers	
rm -rf rt.equinox.binaries/org.eclipse.equinox.executable/{bin,contributed}/

# Delete pre-built binary artifacts except some test data that cannot be generated
rm -rf rt.equinox.p2/
rm -rf eclipse.jdt.core/org.eclipse.jdt.core.tests.model/
find . ! -path "*/JCL/*" ! -name "rtstubs*.jar" ! -name "javax15api.jar" ! -name "j9stubs.jar" ! -name "annotations.jar" \
-type f -name *.jar -delete
find -name '*.class' -delete
find -name '*.jar' -delete
find -name '*.so' -delete
find -name '*.dll' -delete
find -name '*.jnilib' -delete

# Patch doesn't support path with spaces, renaming and back to apply patch
mv %{swtsrcdir}/Eclipse\ SWT\ PI %{swtsrcdir}/Eclipse-SWT-PI
%patch2 -p1
mv %{swtsrcdir}/Eclipse-SWT-PI %{swtsrcdir}/Eclipse\ SWT\ PI

# This part generates secondary fragments using primary fragments
%pom_xpath_inject "pom:plugin[pom:artifactId='target-platform-configuration']/pom:configuration/pom:environments" \
  "<environment><os>linux</os><ws>gtk</ws><arch>s390x</arch></environment>" eclipse-platform-parent
rm -rf eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.s390x
rm -rf rt.equinox.framework/bundles/org.eclipse.equinox.launcher.gtk.linux.s390x
for dir in rt.equinox.binaries equinox/bundles eclipse.platform.swt.binaries/bundles ; do
  %{_sourcedir}/ensure_arch.sh "$dir" x86_64 s390x	
done

cp %{swtsrcdir}/Eclipse\ SWT/common/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT/common/version.txt %{swtsrcdir}/
cp %{swtsrcdir}/Eclipse\ SWT\ PI/{common,cairo}/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ OpenGL/glx/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ WebKit/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ AWT/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.%{eclipse_arch}/about_files/*.txt %{swtsrcdir}/about_files/

%build

export JAVA_HOME=%{_jvmdir}/java-11-openjdk

cd %{swtsrcdir}

# Build native part
export SWT_LIB_DEBUG=1
export CFLAGS="${RPM_OPT_FLAGS}"
export LFLAGS="${RPM_LD_FLAGS}"
ant -f buildSWT.xml build_local -Dbuild_dir=Eclipse\ SWT\ PI/gtk/library -Dtargets="-gtk3 install" -Dclean= -Dcflags="${RPM_OPT_FLAGS}" -Dlflags="${RPM_LD_FLAGS}"

# Build Java part
ant -f buildSWT.xml check_compilation_all_platforms -Drepo.src=../../

# Build Jar file
ant -f build.xml

%install
# Generate addition Maven metadata
rm -rf .xmvn/ .xmvn-reactor

# Install Maven metadata for SWT
JAR=%{swtsrcdir}/org.eclipse.swt_*.jar
VER=$(echo $JAR | sed -e "s/.*_\(.*\)\.jar/\1/")
%mvn_artifact "org.eclipse.swt:org.eclipse.swt:jar:$VER" %{swtsrcdir}/org.eclipse.swt_*.jar
%mvn_alias "org.eclipse.swt:org.eclipse.swt" "org.eclipse.swt:swt"
%mvn_file "org.eclipse.swt:org.eclipse.swt" swt

%mvn_install -J %{swtsrcdir}/docs/api/

#fix so permissions
find %{swtsrcdir}/*.so -name *.so -exec chmod a+x {} \;

install -d 755 %{buildroot}/%{_libdir}/%{name}
cp -a %{swtsrcdir}/*.so %{buildroot}/%{_libdir}/%{name}

%files -f .mfiles
%{_libdir}/%{name}
%license LICENSE
%license NOTICE

%changelog
* Wed Dec 07 2022 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.26-1
- Bump to 4.26

* Thu Sep 22 2022 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.25-1
- Bump to 4.25

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.24-2
- Rebuilt for Drop i686 JDKs (use new macro %{java_arches})

* Thu Jun 23 2022 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.24-1
- Bump to 4.24

* Wed Mar 16 2022 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.23-1
- Bump to 4.23

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:4.22-4
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 29 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.22-2
- 4.22 release compile only with openjdk-11, cleanup spec file

* Thu Dec 09 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.22-1
- Bump to 4.22 release and change compilation to openjdk-1.8

* Wed Sep 22 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.21-1
- Initial packaging


