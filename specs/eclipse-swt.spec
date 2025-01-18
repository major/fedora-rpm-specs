%global major_version   4
%global minor_version   29
%global forgeurl https://github.com/eclipse-platform/eclipse.platform.swt
%global tag R%{major_version}_%{minor_version}
Epoch:                  1

%global swtsrcdir       bundles/org.eclipse.swt
%global eclipse_arch    %{_arch}

Name:           eclipse-swt
Version:        %{major_version}.%{minor_version}
Release:        7%{?dist}
Summary:        Eclipse SWT: The Standard Widget Toolkit for GTK+
%forgemeta

License:        EPL-2.0
URL:            %{forgeurl}

Source0:        %{forgesource}
Source1:        classpath.xls

# Avoid the need for a javascript interpreter at build time
Patch0:         eclipse-swt-avoid-javascript-at-build.patch
# Remove eclipse tasks and modify build tasks to generate jar like expected
Patch1:         eclipse-swt-rm-eclipse-tasks-and-customize-build.patch
# Add fedora cflags to build native libs
Patch2:         eclipse-swt-fedora-build-native.patch

ExclusiveArch:  %{java_arches} 

Requires:       java-headless
Requires:       webkit2gtk4.1

BuildRequires:  javapackages-tools
BuildRequires:  java-devel
BuildRequires:  maven-local
BuildRequires:  ant
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
%patch -p1 0
%patch -p1 1
# Patch doesn't support path with spaces, renaming and back to apply patch
mv %{swtsrcdir}/Eclipse\ SWT\ PI %{swtsrcdir}/Eclipse-SWT-PI
%patch -p1 2
mv %{swtsrcdir}/Eclipse-SWT-PI %{swtsrcdir}/Eclipse\ SWT\ PI
mkdir %{swtsrcdir}/tasks
cp %{SOURCE1} %{swtsrcdir}/tasks

# This part generates secondary fragments using primary fragments
%pom_xpath_inject "pom:profiles/pom:profile[pom:id='unix']/pom:build/pom:plugins/pom:plugin[pom:artifactId='target-platform-configuration']/pom:configuration/pom:environments" \
  "<environment><os>linux</os><ws>gtk</ws><arch>s390x</arch></environment>" .

cp %{swtsrcdir}/Eclipse\ SWT/common/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT/common/version.txt %{swtsrcdir}/
cp %{swtsrcdir}/Eclipse\ SWT\ PI/{common,cairo}/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ OpenGL/glx/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ WebKit/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ AWT/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/

%build

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

# fix so permissions
find %{swtsrcdir}/*.so -name *.so -exec chmod a+x {} \;

install -d 755 %{buildroot}/%{_libdir}/%{name}
cp -a %{swtsrcdir}/*.so %{buildroot}/%{_libdir}/%{name}

%files -f .mfiles
%{_libdir}/%{name}
%license LICENSE
%license NOTICE

%changelog
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


