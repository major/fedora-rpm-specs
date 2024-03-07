Name:           tomcat-jakartaee-migration
Version:        1.0.8
Release:        1%{?dist}
Summary:        Tomcat Migration Tool for Jakarta EE

License:        Apache-2.0
URL:            http://tomcat.apache.org/
Source0:        http://www.apache.org/dist/tomcat/jakartaee-migration/v%{version}/source/jakartaee-migration-%{version}-src.tar.gz
Patch0:         pom.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  bcel
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-io
BuildRequires:  ant
BuildRequires:  java-devel
	
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin) 
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin) 
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin) 
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin) 

%description
The purpose of the tool is to take a web application written for Java EE 8 that runs on Apache Tomcat 9 and convert it automatically so it runs on Apache Tomcat 10 which implements Jakarta EE 9.

%package javadoc
Summary:        Javadoc for %{name}
 
%description javadoc
API documentation for %{name}.

%prep
%setup -q -n jakartaee-migration-%{version}
%patch -P0 -p0

%build
%mvn_build 

%install
%mvn_install

%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_datarootdir}/licenses/%{name}-javadoc
%{__mv} ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}/legal/ADDITIONAL_LICENSE_INFO ${RPM_BUILD_ROOT}%{_datarootdir}/licenses/%{name}-javadoc/

%files -f .mfiles
%license LICENSE.txt
%doc CHANGES.md README.md
 
%files javadoc -f .mfiles-javadoc
%{_datarootdir}/licenses/%{name}-javadoc/ADDITIONAL_LICENSE_INFO
%license LICENSE.txt

%changelog
* Fri Feb 09 2024 Hui Wang <huwang@redhat.com> - 1.0.8-1
- First build

