%global forgeurl https://github.com/TooTallNate/Java-WebSocket

Name:       Java-WebSocket
Version:    1.6.0
Release:    %autorelease
Summary:    A barebones WebSocket client and server implementation written in 100% Java

%forgemeta
# bundled iharder code is Public Domain, see below
License:    MIT AND LicenseRef-Fedora-Public-Domain
URL:        %{forgeurl}
Source:     %{forgesource}

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Requires:   java-headless
Requires:   javapackages-filesystem

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

# In package org.java_websocket.util
# Public Domain Java class from http://iharder.net/base64
Provides:   bundled(net.iharder:base64) = 2.3.7

%description
A barebones WebSocket server and client implementation written in 100% Java.
The underlying classes are implemented java.nio, which allows for a non-blocking
event-driven model (similar to the WebSocket API for web browsers).

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%forgesetup

sed -i -e s#\<release\>7\</release\>#\<release\>21\</release\># pom.xml

%pom_remove_plugin :maven-checkstyle-plugin

%build
#missing dependencies
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.markdown
%doc CHANGELOG.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.markdown
%doc CHANGELOG.md
%license LICENSE


%changelog
%autochangelog
