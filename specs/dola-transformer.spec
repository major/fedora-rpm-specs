%bcond bootstrap 0

Name:           dola-transformer
Version:        1.0.2
Release:        %autorelease
Summary:        Maven 4 extension for dynamic POM transformation
License:        Apache-2.0
URL:            https://github.com/mizdebsk/dola-transformer
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source:         https://github.com/mizdebsk/dola-transformer/releases/download/%{version}/dola-transformer-%{version}.tar.zst

BuildSystem:    maven
BuildOption:    usesJavapackagesBootstrap
BuildOption:    xmvnToolchain "openjdk25"
BuildOption:    buildRequireVersion "org.apache.maven:" "4.0.0-rc-4"

%description
Dola Transformer is an extension for Apache Maven 4 that enables
dynamic, in-memory transformation of project models (POMs) without
modifying them on disk.  It supports a range of transformations,
including adding or removing plugins, dependencies, and parent POMs.

Unlike traditional POM modification tools from the Javapackages
project, Dola Transformer works with a variety of model formats and is
not limited to XML.  This makes it especially useful in environments
where custom Maven builds are needed without manually editing POM
files.

%files -f .mfiles
%license LICENSE NOTICE
%doc README.md

%changelog
%autochangelog
