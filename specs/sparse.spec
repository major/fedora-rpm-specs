Name:       sparse
# snapshot of the upstream master branch, taken after the v0.6.5-rc1
# pre-release; the snapshot information field after the caret contains
# the commit date and the abbreviated commit hash
Version:    0.6.5~rc1^20261022.84ec0658c8

# git snapshot of upstream sparse
%global commit 84ec0658c81db4ccc4aabc420d3dc118c2c6a310

Release:    %autorelease
Summary:    A semantic parser of source files
License:    MIT
URL:        https://sparse.wiki.kernel.org
Source0:    https://git.kernel.org/pub/scm/devel/sparse/sparse.git/snapshot/sparse-%{commit}.tar.gz

# test-inspect was part of the main package before it was split into the
# sparse-test-inspect subpackage. Both packages obsolete the pre-split
# sparse so that an upgrade pulls in the subpackage instead of silently
# dropping the tool ("One-to-Many Replacement" in the packaging
# guidelines). Drop these tags once no supported Fedora release ships
# a pre-split sparse.
Obsoletes:  sparse < 0.6.5~rc1^20261022.84ec0658c8

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  sqlite-devel

%description
Sparse is a semantic parser of source files: it's neither a compiler
(although it could be used as a front-end for one) nor is it a
preprocessor (although it contains as a part of it a preprocessing
phase).

It is meant to be a small - and simple - library.  Scanty and meager,
and partly because of that easy to use.  It has one mission in life:
create a semantic parse tree for some arbitrary user for further
analysis.  It's not a tokenizer, nor is it some generic context-free
parser.  In fact, context (semantics) is what it's all about - figuring
out not just what the grouping of tokens are, but what the _types_ are
that the grouping implies.

Sparse is primarily used in the development and debugging of the Linux kernel.

%package test-inspect
Summary:    GTK tool to inspect sparse's abstract syntax trees
Obsoletes:  sparse < 0.6.5~rc1^20261022.84ec0658c8

%description test-inspect
test-inspect parses source files with sparse and displays the
resulting abstract syntax tree in a GTK+ tree view. It is mainly
useful for debugging sparse itself. Installing it pulls in the
GTK libraries, which the main sparse package does not require.

%prep
%autosetup -p1 -n sparse-%{commit}

%build
%make_build CFLAGS="%{optflags}" HAVE_LLVM=no

%install
%make_install PREFIX="%{_prefix}" BINDIR="%{_bindir}" MANDIR="%{_mandir}" HAVE_LLVM=no

%check
%make_build check HAVE_LLVM=no

%files
%license LICENSE
%doc README FAQ
%{_bindir}/sparse
%{_bindir}/semind
%{_bindir}/cgcc
%{_bindir}/c2xml
%{_mandir}/man1/*

%files test-inspect
%license LICENSE
%{_bindir}/test-inspect

%changelog
%autochangelog
