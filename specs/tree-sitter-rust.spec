Name:           tree-sitter-rust
Version:        0.24.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-cli >= 0.25.0

%{tree_sitter -l Rust}

%changelog
%{autochangelog}
