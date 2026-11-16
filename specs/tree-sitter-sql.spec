Name:           tree-sitter-sql
Version:        0.3.13
Release:        %autorelease
License:        MIT
URL:            https://github.com/DerekStride/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# tree-sitter generate holds the whole grammar in memory to build the
# parser tables, which doesn't fit in the address space of a 32-bit
# process. The release tarball ships the parser generated during the
# release process, but lacks the test suite and the README, so
# extract its src/ over the sources instead of building from it.
# See https://github.com/DerekStride/tree-sitter-sql/issues/234
Source1:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
# See https://github.com/DerekStride/tree-sitter-sql/pull/407
Patch1:         0001-build-Only-pass-grammar.js-to-tree-sitter-generate.patch
Patch2:         0002-build-Generate-the-parser-before-building-the-object.patch
Patch3:         0003-build-Bump-the-Makefile-version-to-0.3.13.patch
Patch4:         0004-build-Remove-the-Requires-field-from-the-pkg-config-.patch
Patch5:         0005-python-Drop-C-source-from-installed-package.patch
BuildRequires:  nodejs
BuildSystem:    tree_sitter

%{tree_sitter -P -l SQL}

%prep -a
# The extracted files are more recent than the archive ones, so make
# doesn't run tree-sitter generate
tar -xzf '%{SOURCE1}' --strip-components=1 ./src

%changelog
%autochangelog
