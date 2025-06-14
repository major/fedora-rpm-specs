Name:           tree-sitter-heex
Version:        0.8.0
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/phoenixframework/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-srpm-macros >= 0.1.1

%{tree_sitter -l HEEx}

%changelog
%{autochangelog}
