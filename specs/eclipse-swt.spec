# Version available in bundles/org.eclipse.swt
%global swt_bundle_version 3.132.0
%global major_version   4
%global minor_version   38
%global forgeurl https://github.com/eclipse-platform/eclipse.platform.swt
%global tag R%{major_version}_%{minor_version}
Epoch:                  1

%global swtsrcdir       bundles/org.eclipse.swt
%global eclipse_arch    %{_arch}

Name:           eclipse-swt
Version:        %{major_version}.%{minor_version}
Release:        1%{?dist}
Summary:        Eclipse SWT: The Standard Widget Toolkit for GTK+
%forgemeta

License:        EPL-2.0
URL:            %{forgeurl}

Source0:        %{forgesource}

# Add fedora cflags to build native libs
Patch0:         eclipse-swt-fedora-build-native.patch

ExclusiveArch:  %{java_arches} 

Requires:       java-25-headless
Requires:       webkit2gtk4.1

BuildRequires:  javapackages-tools
BuildRequires:  java-25-devel
BuildRequires:  maven-local-openjdk25
BuildRequires:  ant-openjdk25
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  webkit2gtk4.1-devel
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
%forgesetup
# Patch doesn't support path with spaces, renaming and back to apply patch
mv %{swtsrcdir}/Eclipse\ SWT\ PI %{swtsrcdir}/Eclipse-SWT-PI
%patch -p1 0
mv %{swtsrcdir}/Eclipse-SWT-PI %{swtsrcdir}/Eclipse\ SWT\ PI

# This part generates secondary fragments using primary fragments
%pom_xpath_inject "pom:profiles/pom:profile[pom:id='unix']/pom:build/pom:plugins/pom:plugin[pom:artifactId='target-platform-configuration']/pom:configuration/pom:environments" \
  "<environment><os>linux</os><ws>gtk</ws><arch>s390x</arch></environment>" .
# Prepare native build
cp %{swtsrcdir}/Eclipse\ SWT/common/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT/common/version.txt %{swtsrcdir}/
cp %{swtsrcdir}/Eclipse\ SWT\ PI/{common,cairo}/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ OpenGL/glx/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ WebKit/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ AWT/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
# Prepare java build
mkdir -p bundles/org.eclipse.swt/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT/{common,gtk,cairo,emulated/bidi,emulated/coolbar,emulated/taskbar}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Accessibility/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ AWT/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Browser/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Custom\ Widgets/common/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Drag\ and\ Drop/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ OpenGL/{common,gtk,glx}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ PI/{common,gtk,cairo}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Printing/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Program/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ WebKit/gtk/org/* %{swtsrcdir}/src/main/java/org
# Prepare maven build for fedora
%pom_remove_parent
%pom_remove_plugin org.eclipse.tycho:
%pom_remove_plugin org.eclipse.tycho: bundles/org.eclipse.swt
%pom_remove_plugin org.eclipse.tycho: local-build/local-build-parent
%pom_disable_module binaries
%pom_disable_module examples/org.eclipse.swt.examples
%pom_disable_module examples/org.eclipse.swt.examples.browser.demos
%pom_disable_module examples/org.eclipse.swt.examples.launcher
%pom_disable_module examples/org.eclipse.swt.examples.ole.win32
%pom_disable_module examples/org.eclipse.swt.examples.views
%pom_disable_module tests/org.eclipse.swt.tests
rm .mvn/extensions.xml

%pom_xpath_replace "//pom:packaging" "<packaging>jar</packaging>" bundles/org.eclipse.swt
%pom_xpath_inject "//pom:artifactId[text()='eclipse.platform.swt']/.." "<version>%{major_version}.%{minor_version}.0</version>"

%pom_add_plugin :maven-compiler-plugin bundles/org.eclipse.swt
%pom_xpath_inject "//pom:plugin[pom:artifactId='maven-compiler-plugin']" \
"<configuration>
    <source>25</source>
    <target>25</target>
    <compilerArgs>
		<arg>-classpath</arg>
		<arg>\${project.build.outputDirectory}</arg>
	</compilerArgs>
</configuration>" bundles/org.eclipse.swt
# Remove -SNAPSHOT in version
%pom_xpath_set "//pom:project/pom:version" "%{major_version}.%{minor_version}.0" pom.xml
%pom_xpath_set "//pom:project/pom:version" "%{swt_bundle_version}" bundles/org.eclipse.swt/pom.xml
%pom_xpath_set "//pom:parent/pom:version" "%{major_version}.%{minor_version}.0" bundles/org.eclipse.swt/pom.xml
%pom_xpath_set "//pom:parent/pom:version" "%{major_version}.%{minor_version}.0" local-build/local-build-parent/pom.xml

%build

cd %{swtsrcdir}

# Build native part
export SWT_LIB_DEBUG=1
export SWT_JAVA_HOME=/usr/lib/jvm/java-25-openjdk
export CFLAGS="${RPM_OPT_FLAGS} -std=gnu17 -Wno-deprecated-declarations"
export LFLAGS="${RPM_LD_FLAGS}"
cd Eclipse\ SWT\ PI/gtk/library/
sh build.sh -gtk3

# Build Java part
cd ../../..
%mvn_build

%install
# Generate addition Maven metadata
rm -rf .xmvn/ .xmvn-reactor

# Install Maven metadata for SWT
JAR="$(ls -1 %{swtsrcdir}/target/org.eclipse.swt-*.jar | head -n1)"
VER="$(basename "$JAR" | sed -E 's/^org\.eclipse\.swt-([0-9][0-9.]*(-SNAPSHOT)?)\.jar/\1/')"
%mvn_artifact "org.eclipse.swt:org.eclipse.swt:jar:$VER" "$JAR"
%mvn_alias "org.eclipse.swt:org.eclipse.swt" "org.eclipse.swt:swt"
%mvn_file "org.eclipse.swt:org.eclipse.swt" swt

%mvn_install -J %{swtsrcdir}/target/xmvn-apidocs

# fix so permissions
find %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/*.so -name *.so -exec chmod a+x {} \;

install -d 755 %{buildroot}/%{_libdir}/%{name}
cp -a %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/*.so %{buildroot}/%{_libdir}/%{name}

%files -f .mfiles
%{_libdir}/%{name}
%license LICENSE
%license NOTICE

%changelog
* Thu Feb 05 2026 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.38-1
- Bump to 4.38 and fix FTBFS(2434004)

* Thu Feb 27 2025 Sérgio Basto <sergio@serjux.com> - 1:4.29-8
- Fix GCC build, compiling with -std=gnu17

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 06 2024 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.29-6
- Rebuilt for java-21-openjdk as system jdk

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1:4.29-4
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.29-1
- Bump to 4.29

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.28-1
- Bump to 4.28

* Thu May 11 2023 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.27-2
- Change dependency to webkit2gtk-4.1 due to removal of webkit2gtk-3

* Tue Apr 04 2023 Nicolas De Amicis <deamicis@bluewin.ch> - 1:4.27-1
- Bump to 4.27

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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


