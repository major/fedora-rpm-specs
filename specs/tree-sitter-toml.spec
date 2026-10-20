Name:           tree-sitter-toml
Version:        0.7.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-python-Drop-C-source-from-installed-package.patch
BuildSystem:    tree_sitter

%{tree_sitter -P -l TOML}

%changelog
%{autochangelog}
