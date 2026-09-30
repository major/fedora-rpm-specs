Name:           tree-sitter-html
Version:        0.23.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# See https://github.com/tree-sitter/tree-sitter-html/pull/144
Patch1:         0001-python-Drop-C-source-from-installed-package.patch
BuildSystem:    tree_sitter

%{tree_sitter -P -l HTML}

%changelog
%autochangelog
