Name:           tree-sitter-phpdoc
Version:        0.1.8
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/claytonrcarter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l PHPDoc}

%changelog
%{autochangelog}
