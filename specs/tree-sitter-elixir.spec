Name:           tree-sitter-elixir
Version:        0.3.5
Release:        %{autorelease}
License:        Apache-2.0
URL:            https://github.com/elixir-lang/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  tree-sitter-srpm-macros >= 0.4.2
BuildSystem:    tree_sitter

# https://github.com/elixir-lang/tree-sitter-elixir/issues/88
Patch: 5c22791c9836d436ce31de5e454fbad0e706ea96.patch

# https://github.com/elixir-lang/tree-sitter-elixir/pull/91
Patch: 0001-Regenerate-tree-sitter-elixir.pc.in.patch

%{tree_sitter -l Elixir}


%changelog
%{autochangelog}
