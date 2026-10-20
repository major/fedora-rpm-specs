Name:           tree-sitter-bash
Version:        0.25.1
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-python-Drop-C-source-from-installed-package.patch
BuildSystem:    tree_sitter

%{tree_sitter -P -l Bash}

%changelog
%autochangelog
