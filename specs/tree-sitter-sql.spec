Name:           tree-sitter-sql
Version:        0.3.13
Release:        %autorelease
License:        MIT
URL:            https://github.com/DerekStride/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# See https://github.com/DerekStride/tree-sitter-sql/pull/407
Patch1:         0001-build-Only-pass-grammar.js-to-tree-sitter-generate.patch
Patch2:         0002-build-Generate-the-parser-before-building-the-object.patch
Patch3:         0003-build-Bump-the-Makefile-version-to-0.3.13.patch
Patch4:         0004-build-Remove-the-Requires-field-from-the-pkg-config-.patch
Patch5:         0005-python-Drop-C-source-from-installed-package.patch
BuildRequires:  nodejs
BuildSystem:    tree_sitter

%{tree_sitter -P -l SQL}

%changelog
%autochangelog
