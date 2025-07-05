%bcond bootstrap 0

Name:           stax2-api
Version:        4.2.2
Release:        %autorelease
Summary:        Streaming API for XML
License:        BSD-2-Clause
URL:            https://github.com/FasterXML/stax2-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{name}-%{version}.tar.gz

# From upstream commit 67d5988
Patch:          0001-Add-BSD-2-license-file.patch

%if %{without bootstrap}
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 4.2.2-6

BuildSystem:    maven
BuildOption:    usesJavapackagesBootstrap
BuildOption:    xmvnToolchain "openjdk25"
BuildOption:    mavenOptions {
BuildOption:        "-Djavac.src.version=8"
BuildOption:        "-Djavac.target.version=8"
BuildOption:    }
BuildOption:    transform ":stax2-api" {
BuildOption:        removeParent
BuildOption:        removePlugins {
BuildOption:            ":maven-javadoc-plugin"
BuildOption:        }
BuildOption:    }

%description
Stax2 API is an extension to standard Java Streaming API for XML
(StAX) added in JDK 6.

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
%autochangelog
