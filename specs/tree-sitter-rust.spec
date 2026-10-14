Name:           tree-sitter-rust
Version:        0.24.2
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-python-Drop-C-source-from-installed-package.patch
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-cli >= 0.25.0

%{tree_sitter -P -l Rust}

%changelog
%{autochangelog}
