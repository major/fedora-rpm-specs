Name:           tree-sitter-cpp
Version:        0.23.4
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-srpm-macros >= 0.3.0

%{tree_sitter -l C++}

%changelog
%{autochangelog}
