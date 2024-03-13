Name:           janino
Version:        3.1.10
Release:        %autorelease
Summary:        Super-small, super-fast Java compiler
License:        BSD-3-Clause
URL:            http://janino-compiler.github.io/janino
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/janino-compiler/janino/archive/v%{version}/%{name}-%{version}.tar.gz

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
cd %{name}-parent
# remove maven.compiler.* properties
  %pom_xpath_remove pom:maven.compiler.executable
  %pom_xpath_remove pom:maven.compiler.fork
# remove staging maven plugin
  %pom_remove_plugin :nexus-staging-maven-plugin
# remove jarsigner plugin
  %pom_remove_plugin :maven-jarsigner-plugin
# remove javadoc plugin:
  %pom_remove_plugin :maven-javadoc-plugin
# remove source plugin:
  %pom_remove_plugin :maven-source-plugin
# disable tests module
  %pom_disable_module ../commons-compiler-tests
# don't install parent
  %mvn_package :%{name}-parent __noinstall
cd -

%build

cd %{name}-parent
# de.unkrig.jdisasm:jdisasm is missing
  %mvn_build -s -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
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
%autochangelog
