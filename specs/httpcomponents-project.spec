%bcond_with bootstrap

Name:           httpcomponents-project
Summary:        Common POM file for HttpComponents
Version:        13
Release:        %autorelease
License:        Apache-2.0
URL:            https://hc.apache.org/
Source0:        https://archive.apache.org/dist/httpcomponents/httpcomponents-parent/httpcomponents-parent-%{version}-source-release.zip
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

%description
Common Maven POM file for HttpComponents. This project should be
required only for building dependant packages with Maven. Please don't
use it as runtime requirement.

%prep
%autosetup -p1 -n httpcomponents-parent-%{version}

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :apache-rat-plugin

# Version <= 8 had this AID
%mvn_alias : :project

%build
%mvn_file  : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%changelog
%autochangelog