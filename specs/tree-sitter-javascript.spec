Name:           tree-sitter-javascript
Version:        0.25.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# See https://github.com/tree-sitter/tree-sitter-javascript/pull/390
Patch1:         0001-python-Drop-C-source-from-installed-package.patch
BuildSystem:    tree_sitter

%{tree_sitter -P -l JavaScript}

%changelog
%autochangelog
