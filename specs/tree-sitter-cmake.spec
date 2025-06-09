Name:           tree-sitter-cmake
Version:        0.7.1
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/uyha/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-srpm-macros >= 0.2.4

%{tree_sitter -l CMake}

%changelog
%{autochangelog}
