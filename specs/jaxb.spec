%bcond_with bootstrap

Name:           jaxb
Version:        4.0.6
Release:        %autorelease
Summary:        JAXB Reference Implementation
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-ri
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}-RI/%{name}-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.github.relaxng:relaxngDatatype)
BuildRequires:  mvn(com.sun.istack:istack-commons-maven-plugin)
BuildRequires:  mvn(com.sun.istack:istack-commons-runtime)
BuildRequires:  mvn(com.sun.istack:istack-commons-tools)
BuildRequires:  mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(net.java.dev.msv:xsdlib)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
%endif

%description
GlassFish JAXB Reference Implementation.

%package codemodel
Summary:        Codemodel Core

%description codemodel
The core functionality of the CodeModel java source code generation library.

%package codemodel-annotation-compiler
Summary:        Codemodel Annotation Compiler

%description codemodel-annotation-compiler
The annotation compiler ant task for the CodeModel java source code generation
library.

%package relaxng-datatype
Summary:        RelaxNG Datatype

%description relaxng-datatype
RelaxNG Datatype library.

%package xsom
Summary:        XML Schema Object Model

%description xsom
XML Schema Object Model (XSOM) is a Java library that allows applications to
easily parse XML Schema documents and inspect information in them. It is
expected to be useful for applications that need to take XML Schema as an
input.

%package core
Summary:        JAXB Core

%description core
JAXB Core module. Contains sources required by XJC, JXC and Runtime modules.

%package rngom
# pom.xml and module-info.java are under BSD, rest is MIT
License:        MIT AND BSD-3-Clause
Summary:        RELAX NG Object Model/Parser

%description rngom
This package contains RELAX NG Object Model/Parser.

%package runtime
Summary:        JAXB Runtime

%description runtime
JAXB (JSR 222) Reference Implementation

%package txw2
Summary:        TXW2 Runtime

%description txw2
TXW is a library that allows you to write XML documents.

%package xjc
# jaxb-ri/xjc/src/main/java/com/sun/tools/xjc/reader/internalizer/NamespaceContextImpl.java is under Apache-2.0
License:        BSD-3-Clause AND Apache-2.0
Summary:        JAXB XJC

%description xjc
JAXB Binding Compiler. Contains source code needed for binding customization
files into java sources. In other words: the tool to generate java classes for
the given xml representation.

%package txwc2
Summary:        TXW2 Compiler

%description txwc2
JAXB schema generator. The tool to generate XML schema based on java classes.

%prep
%autosetup -p1 -C

pushd jaxb-ri

# Remove ee4j parent
%pom_remove_parent boms/bom codemodel external xsom

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# Skip docs generation because of missing dependencies
%pom_xpath_remove "pom:profiles/pom:profile[pom:id='default-profile']/pom:modules"

# Disable unneeded extra OSGi bundles
%pom_disable_module bundles

# Missing dependency on org.checkerframework:compiler
%pom_disable_module jxc

%pom_remove_dep org.eclipse.angus:angus-activation core

# Don't install aggregator and parent poms
%mvn_package :jaxb-bom __noinstall
%mvn_package :jaxb-bom-ext __noinstall
%mvn_package :jaxb-bundles __noinstall
%mvn_package :jaxb-codemodel-parent __noinstall
%mvn_package :jaxb-docs-parent __noinstall
%mvn_package :jaxb-external-parent __noinstall
%mvn_package :jaxb-parent __noinstall
%mvn_package :jaxb-runtime-parent __noinstall
%mvn_package :jaxb-samples __noinstall
%mvn_package :jaxb-txw-parent __noinstall
%mvn_package :jaxb-www __noinstall

%if %{with bootstrap}
%pom_disable_module core
%pom_disable_module codemodel-annotation-compiler codemodel
%pom_disable_module runtime
%pom_disable_module relaxng-datatype external
%pom_disable_module rngom external
%pom_disable_module xjc
%pom_disable_module xsom
%pom_disable_module txw
%endif
popd

%build
pushd jaxb-ri
%mvn_build -s -f -j -- -Dproject.build.sourceEncoding=UTF-8
popd

%install
pushd jaxb-ri
%mvn_install
popd

%files codemodel -f jaxb-ri/.mfiles-codemodel
%license LICENSE.md NOTICE.md

%if %{without bootstrap}
%files codemodel-annotation-compiler -f jaxb-ri/.mfiles-codemodel-annotation-compiler
%files core -f jaxb-ri/.mfiles-jaxb-core
%files relaxng-datatype -f jaxb-ri/.mfiles-relaxng-datatype
%license LICENSE.md NOTICE.md
%files xsom -f jaxb-ri/.mfiles-xsom
%files rngom -f jaxb-ri/.mfiles-rngom
%files txw2 -f jaxb-ri/.mfiles-txw2
%license LICENSE.md NOTICE.md
%files txwc2 -f jaxb-ri/.mfiles-txwc2
%files runtime -f jaxb-ri/.mfiles-jaxb-runtime
%files xjc -f jaxb-ri/.mfiles-jaxb-xjc
%endif

%changelog
%autochangelog
