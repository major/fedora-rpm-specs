Name:           tree-sitter-css
Version:        0.25.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-python-Drop-C-source-from-installed-package.patch
BuildSystem:    tree_sitter

%{tree_sitter -P -l CSS}

%changelog
%autochangelog
