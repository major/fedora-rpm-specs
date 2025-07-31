%bcond_without tests
%global nwname classloader-leak-prevention-parent

Name:           classloader-leak-test-framework
Version:        2.7.0
Release:        %autorelease
Summary:        Detection and verification of Java ClassLoader leaks
License:        Apache-2.0
URL:            https://github.com/mjiderhamn/classloader-leak-prevention/tree/master/%{name}
Source0:        https://github.com/mjiderhamn/classloader-leak-prevention/archive/%{nwname}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.bcel:bcel)

%description
Stand-alone test framework for detecting and/or verifying the existence or
non-existence of Java ClassLoader leaks. It is also possible to test leak
prevention mechanisms to confirm that the leak really is avoided. The framework
is an built upon JUnit.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n classloader-leak-prevention-%{nwname}-%{version}

rm -r classloader-leak-prevention
cp -r %{name}/* .

%pom_remove_dep com.sun.faces:jsf-api
%pom_remove_dep com.sun.faces:jsf-impl
%pom_remove_dep javax.el:el-api

%pom_xpath_set 'pom:properties/pom:maven.compiler.source' '8'
%pom_xpath_set 'pom:properties/pom:maven.compiler.target' '8'

%pom_remove_plugin -r :maven-javadoc-plugin

%build
%if %{with tests}
%mvn_build --xmvn-javadoc
%else
%mvn_build -f --xmvn-javadoc
%endif

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
