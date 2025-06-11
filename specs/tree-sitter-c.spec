Name:           tree-sitter-c
Version:        0.24.1
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-srpm-macros >= 0.2.1

%{tree_sitter -l C}


# Required until Makefile is regenerated to incorporate
# https://github.com/tree-sitter/tree-sitter/commit/8eb44072006ac0bb7bfeb0004355ccca3a5dcf57
%install
%buildsystem_tree_sitter_install
install -m644 queries/*.scm $RPM_BUILD_ROOT%{_datadir}/tree-sitter/queries/c


%changelog
%{autochangelog}
