Name:           tree-sitter-php
Version:        0.23.12
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-srpm-macros >= 0.1.1

%{tree_sitter -l PHP}

%changelog
%{autochangelog}
