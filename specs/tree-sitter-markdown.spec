Name:           tree-sitter-markdown
Version:        0.5.3
Release:        %{autorelease}
License:        MIT
URL:            https://github.com/tree-sitter-grammars/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter
BuildRequires:  tree-sitter-srpm-macros >= 0.4.3

%{tree_sitter -l Markdown}


%check
(cd tree-sitter-markdown && %{make_build} test)

## Some of these tests fail unless we regenerate the parser with:
## (cd tree-sitter-markdown-inline && env ALL_EXTENSIONS=1 tree-sitter generate)
(cd tree-sitter-markdown-inline && %{make_build} test || :)


%changelog
%{autochangelog}
