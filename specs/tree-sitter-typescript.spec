Name:           tree-sitter-typescript
Version:        0.23.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l %{quote:TypeScript and TSX}}

%changelog
%{autochangelog}
