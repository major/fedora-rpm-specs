Name:           tree-sitter-c-sharp
Version:        0.23.1
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l C#}

%changelog
%autochangelog
