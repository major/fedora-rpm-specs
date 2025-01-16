# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global ocamlver 503
%global giturl  https://github.com/ocaml/merlin

Name:           ocaml-merlin
Version:        5.4.1
Release:        %autorelease
Summary:        Context sensitive completion for OCaml

# The entire source is MIT except:
# QPL-1.0:
# - src/ocaml/driver/pparse.ml{,i}
# - src/ocaml/preprocess/lexer_ident.mll
# - src/ocaml/preprocess/lexer_raw.ml{i,l}
# LGPL-2.1-only WITH OCaml-LGPL-linking-exception
# - src/ocaml/preprocess/parser_raw.mly
# - upstream/ocaml_413/parsing/parser.mly
# - upstream/ocaml_413/utils/domainstate.ml{,i}.c
# - upstream/ocaml_414/parsing/parser.mly
# - upstream/ocaml_414/utils/domainstate.ml{,i}.c
License:        MIT AND QPL-1.0 AND LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://ocaml.github.io/merlin/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}-%{ocamlver}/merlin-%{version}-%{ocamlver}.tbz

# Fix the tests to work with /usr/lib64 as well as /usr/lib
Patch:          0001-Use-usr-lib64-for-Fedora.patch

BuildRequires:  emacs
BuildRequires:  emacs-auto-complete
BuildRequires:  emacs-company-mode
BuildRequires:  emacs-iedit
BuildRequires:  jq
BuildRequires:  ocaml >= 5.3
BuildRequires:  ocaml-alcotest-devel >= 1.3.0
BuildRequires:  ocaml-caml-mode
BuildRequires:  ocaml-csexp-devel >= 1.5.1
BuildRequires:  ocaml-dune >= 3.0.0
BuildRequires:  ocaml-findlib-devel >= 1.6.0
BuildRequires:  ocaml-menhir >= 20201216
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-source
BuildRequires:  ocaml-yojson-devel >= 2.0.0
BuildRequires:  vim-enhanced

Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
Requires:       dot-merlin-reader%{?_isa} = %{version}-%{release}
Requires:       ocaml-index%{?_isa} = %{version}-%{release}

Recommends:     ocaml-source

%global _desc %{expand:
Merlin is an assistant for editing OCaml code.  It aims to provide the
features available in modern IDEs: error reporting, auto completion,
source browsing and much more.}

%description %_desc

You should also install a package that integrates with your editor of
choice, such as emacs-merlin or vim-merlin.

%package        lib
Summary:        Library access to the merlin protocol
Requires:       ocaml-csexp-devel%{?_isa}

%description    lib
These libraries provides access to low-level compiler interfaces and the
standard higher-level merlin protocol.  The library is provided as-is,
is not thoroughly documented, and its public API might break with any
new release.

%package     -n dot-merlin-reader
License:        MIT
Summary:        Merlin configuration file reader
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}

%description -n dot-merlin-reader
This package contains a helper process that reads .merlin files and gives
the normalized content to merlin.

%package     -n ocaml-index
License:        MIT
Summary:        Tool that indexes value usages from cmt files
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}

%description -n ocaml-index
This package contains a tool that indexes value usages from cmt files.
It should integrate with the build system to index a codebase and allow
tools such as Merlin to perform project-wide occurrence queries.

%package     -n emacs-merlin
License:        MIT
Summary:        Context sensitive completion for OCaml in Emacs
BuildArch:      noarch
Requires:       ocaml-merlin = %{version}-%{release}
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       emacs-caml-mode

Recommends:     emacs-auto-complete
Recommends:     emacs-company-mode
Recommends:     emacs-iedit

%description -n emacs-merlin %_desc

This package contains the Emacs interface to merlin.

%package     -n vim-merlin
License:        MIT
Summary:        Context sensitive completion for OCaml in Vim
BuildArch:      noarch
Requires:       ocaml-merlin = %{version}-%{release}
Requires:       vim-filesystem

%description -n vim-merlin %_desc

This package contains the Vim interface to merlin.

%prep
%autosetup -n merlin-%{version}-%{ocamlver} -p1

%build
%dune_build @install

%install
%dune_install -s -n

# Reinstall vim files to Fedora default location
mkdir -p %{buildroot}%{vimfiles_root}
mv %{buildroot}%{_datadir}/merlin/vim/* %{buildroot}%{vimfiles_root}
rm -fr %{buildroot}%{_datadir}/merlin

# Generate the autoload file for the Emacs interface and byte compile
cd %{buildroot}%{_emacs_sitelispdir}
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/merlin-loaddefs.el\"))"
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv merlin-loaddefs.el %{buildroot}%{_emacs_sitestartdir}
%_emacs_bytecompile *.el
cd -

%check
%dune_check

%files
%doc featuremap.* CHANGES.md README.md
%{_bindir}/ocamlmerlin
%{_bindir}/ocamlmerlin-server
%{ocamldir}/merlin/

%files lib -f .ofiles-merlin-lib
%license LICENSE

%files -n dot-merlin-reader -f .ofiles-dot-merlin-reader

%files -n emacs-merlin
%{_emacs_sitelispdir}/merlin*
%{_emacs_sitestartdir}/merlin-loaddefs.el

%files -n ocaml-index -f .ofiles-ocaml-index

%files -n vim-merlin
%{vimfiles_root}/*/*

%changelog
%autochangelog
