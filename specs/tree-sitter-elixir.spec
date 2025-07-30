Name:           tree-sitter-elixir
Version:        0.3.4
Release:        %{autorelease}
License:        Apache-2.0
URL:            https://github.com/elixir-lang/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  tree-sitter-srpm-macros >= 0.4.2
BuildSystem:    tree_sitter
BuildOption(build): PARSER_NAME=elixir
BuildOption(install): PARSER_NAME=elixir

%{tree_sitter -l Elixir}


%install
%{buildsystem_tree_sitter_install PARSER_NAME=elixir}
mv $RPM_BUILD_ROOT/%{_includedir}/tree_sitter/elixir.h \
   $RPM_BUILD_ROOT/%{_includedir}/tree_sitter/%{name}.h \


%changelog
%{autochangelog}
