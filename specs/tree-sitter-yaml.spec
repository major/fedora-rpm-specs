Name:           tree-sitter-yaml
Version:        0.7.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  tree-sitter-srpm-macros >= 0.2.1
BuildSystem:    tree_sitter

%{tree_sitter -l YAML}

%changelog
%{autochangelog}
