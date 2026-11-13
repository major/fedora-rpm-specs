Name:           tree-sitter-xml
Version:        0.7.0
Release:        %autorelease
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/tree-sitter-grammars/tree-sitter-xml/commit/2128a0b249263e238d88cb894dad00c3168fea37
Patch1:         0001-build-c-fix-makefile.patch
Patch2:         0002-python-Drop-C-source-from-installed-package.patch
BuildSystem:    tree_sitter

%{tree_sitter -P -l %{quote:XML and DTD}}

%changelog
%autochangelog
