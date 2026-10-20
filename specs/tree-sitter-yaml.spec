Name:           tree-sitter-yaml
Version:        0.7.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  tree-sitter-srpm-macros >= 0.2.1
Patch1:         0001-python-Drop-C-source-from-installed-package.patch
BuildSystem:    tree_sitter

%{tree_sitter -P -l YAML}

%changelog
%{autochangelog}
