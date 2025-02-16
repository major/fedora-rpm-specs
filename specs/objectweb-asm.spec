%bcond_with bootstrap

Name:           objectweb-asm
Version:        9.7.1
Release:        %autorelease
Summary:        Java bytecode manipulation and analysis framework
License:        BSD-3-Clause
URL:            https://asm.ow2.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        aggregator.pom
Source2:        https://repo1.maven.org/maven2/org/ow2/asm/asm/%{version}/asm-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/ow2/asm/asm-analysis/%{version}/asm-analysis-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/ow2/asm/asm-commons/%{version}/asm-commons-%{version}.pom
Source5:        https://repo1.maven.org/maven2/org/ow2/asm/asm-test/%{version}/asm-test-%{version}.pom
Source6:        https://repo1.maven.org/maven2/org/ow2/asm/asm-tree/%{version}/asm-tree-%{version}.pom
Source7:        https://repo1.maven.org/maven2/org/ow2/asm/asm-util/%{version}/asm-util-%{version}.pom
# The source contains binary jars that cannot be verified for licensing and could be proprietary
Source9:        generate-tarball.sh
Source10:       tools-retrofitter.pom

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif

%description
ASM is an all purpose Java bytecode manipulation and analysis
framework.  It can be used to modify existing classes or dynamically
generate classes, directly in binary form.  Provided common
transformations and analysis algorithms allow to easily assemble
custom complex transformations and code analysis tools.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C

# A custom pom to aggregate the build
cp -p %{SOURCE1} pom.xml

cp -p %{SOURCE10} tools/retrofitter/pom.xml

# Insert poms into modules
for pom in asm asm-analysis asm-commons asm-test asm-tree asm-util; do
  cp -p ${RPM_SOURCE_DIR}/${pom}-%{version}.pom ${pom}/pom.xml
  %pom_add_dep org.fedoraproject.xmvn.objectweb-asm:tools-retrofitter::provided ${pom}
  %pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin ${pom}
  %pom_set_parent org.fedoraproject.xmvn.objectweb-asm:aggregator:any ${pom}
  %pom_xpath_inject pom:parent '<relativePath>..</relativePath>' ${pom}
done

# Don't ship poms used for build only
%mvn_package :aggregator __noinstall
%mvn_package :tools-retrofitter __noinstall

# Don't ship the test framework to avoid runtime dep on junit
%mvn_package :asm-test __noinstall

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%jpackage_script org.objectweb.asm.xml.Processor "" "" %{name}/asm:%{name}/asm-attrs:%{name}/asm-util %{name}-processor true

%files -f .mfiles
%license LICENSE.txt
%{_bindir}/%{name}-processor

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
