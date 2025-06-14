Name:           tree-sitter-lua
Version:        0.4.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l Lua}

%changelog
%autochangelog
