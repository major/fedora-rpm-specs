Name:           tree-sitter-yaml
Version:        0.7.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  tree-sitter-srpm-macros >= 0.2.1
BuildSystem:    tree_sitter

# https://github.com/tree-sitter-grammars/tree-sitter-yaml/pull/18
Patch:          18.patch

%{tree_sitter -l YAML}

%changelog
%{autochangelog}
