Name:           janino
Version:        3.1.7
Release:        3%{?dist}
Summary:        Super-small, super-fast Java compiler
License:        BSD
URL:            http://janino-compiler.github.io/janino
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/janino-compiler/janino/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)

Requires:       javapackages-tools
Requires:       commons-compiler = %{version}-%{release}

%description
Janino is a super-small, super-fast Java compiler.

The "JANINO" implementation of the "commons-compiler" API: Super-small,
super-fast, independent from the JDK's "tools.jar".

%package -n commons-compiler
Summary:        Commons Compiler
%description -n commons-compiler
The "commons-compiler" API, including the "IExpressionEvaluator",
"IScriptEvaluator", "IClassBodyEvaluator" and "ISimpleCompiler" interfaces.

%package -n commons-compiler-jdk
Summary:        Commons Compiler JDK
%description -n commons-compiler-jdk
The "JDK" implementation of the "commons-compiler" API that uses the
JDK's Java compiler (JAVAC) in "tools.jar".

%package javadoc
Summary:        API documentation for %{name}
%description javadoc
API documentation for %{name}.

%prep
%autosetup
# delete precompiled jar and class files
find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

cd %{name}-parent
# remove maven.compiler.* properties
  %pom_xpath_remove pom:maven.compiler.source
  %pom_xpath_remove pom:maven.compiler.target
  %pom_xpath_remove pom:maven.compiler.executable
  %pom_xpath_remove pom:maven.compiler.fork
# remove staging maven plugin
  %pom_remove_plugin :nexus-staging-maven-plugin
# remove jarsigner plugin
  %pom_remove_plugin :maven-jarsigner-plugin
# remove javadoc plugin:
# - don't build *-javadoc.jar
  %pom_remove_plugin :maven-javadoc-plugin
# remove source plugin:
# - don't build *-sources.jar
  %pom_remove_plugin :maven-source-plugin
# disable tests module
  %pom_disable_module ../commons-compiler-tests
# don't install parent
  %mvn_package :%{name}-parent __noinstall
cd -

%build

cd %{name}-parent
  %mvn_build -s -- -Dmaven.compiler.source=8 -Dmaven.compiler.target=8
cd -

%install

cd %{name}-parent
  %mvn_install
# create janinoc script
  %jpackage_script org.codehaus.commons.compiler.samples.CompilerDemo "" "" %{name}/janino:%{name}/commons-compiler janinoc true
cd -

%files -f %{name}-parent/.mfiles-%{name}
%license LICENSE
%{_bindir}/janinoc

%files -n commons-compiler -f %{name}-parent/.mfiles-commons-compiler
%license LICENSE
%files -n commons-compiler-jdk -f %{name}-parent/.mfiles-commons-compiler-jdk
%license LICENSE
%files javadoc -f %{name}-parent/.mfiles-javadoc
%license LICENSE

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.1.7-2
- Rebuilt for Drop i686 JDKs

* Thu Apr 21 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 3.1.7-1
- New upstream release 3.1.7

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 01 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 3.1.6-2
- Add Requires: commons-compiler = %%{version}-%%{release} to janino package
- Remove bundled jar/classes

* Fri Dec 31 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 3.1.6-1
- Initial package
