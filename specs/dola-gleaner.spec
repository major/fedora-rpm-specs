%bcond bootstrap 0

Name:           dola-gleaner
Version:        1.1.1
Release:        %autorelease
Summary:        Maven 4 extension for extracting build dependencies
License:        Apache-2.0
URL:            https://github.com/mizdebsk/dola-gleaner
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source:         https://github.com/mizdebsk/dola-gleaner/releases/download/%{version}/dola-gleaner-%{version}.tar.zst

BuildSystem:    maven
BuildOption:    usesJavapackagesBootstrap
BuildOption:    xmvnToolchain "openjdk25"
BuildOption:    buildRequireVersion "org.apache.maven:" "4.0.0-rc-4"

%description
Dola Gleaner is an extension for Apache Maven 4 that extracts build
dependencies without actually executing the build.  Instead of running
plugins (MOJOs), it analyzes the project and prints the dependencies
that would be required to complete the specified build.

This tool is especially useful for tools and environments that need to
understand build requirements without performing the build itself.

%files -f .mfiles
%license LICENSE NOTICE
%doc README.md

%changelog
%autochangelog
