%global giturl  https://github.com/OCamlPro/ocp-indent

Name:           ocaml-ocp-indent
Version:        1.10.0
Release:        %autorelease
Summary:        A simple tool to indent OCaml programs

# The entire source code is LGPL with the OCaml linking exception except
# src/approx_tokens.ml is QPL-1.0
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND QPL-1.0
URL:            https://www.typerex.org/ocp-indent.html
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/ocp-indent-%{version}.tar.gz
# Fix use of ISO8859-1 characters at the beginnings of lines
# https://github.com/OCamlPro/ocp-indent/issues/318
Patch:          %{name}-nonbreaking-space.patch
# Fix a test that fails because files in mock builds have security contexts
Patch:          %{name}-security-context.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildRequires:  emacs-nw
BuildRequires:  emacs-tuareg
BuildRequires:  ocaml >= 4.11
BuildRequires:  ocaml-cmdliner-devel >= 2.0.0
BuildRequires:  ocaml-dune >= 3.20
BuildRequires:  ocaml-findlib-devel
BuildRequires:  vim-enhanced

Requires:       emacs-filesystem >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       vim-filesystem

%description
Ocp-indent is a simple tool and library to indent OCaml code.  It is based on
an approximate, tolerant OCaml parser and a simple stack machine; this is much
faster and more reliable than using regexps.  Presets and configuration
options are available, with the possibility to set them project-wide.
Ocp-indent supports most common syntax extensions, and is extensible for
others.

Includes:

- An indentor program, callable from the command-line or from within editors
- Bindings for popular editors
- A library that can be directly used by editor writers, or just for
  fault-tolerant/approximate parsing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-findlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ocp-indent-%{version} -p1

%install -a
sed -i '\@%{_datadir}/ocp-indent@d' .ofiles .ofiles-devel

# Reinstall vim files to Fedora default location
mkdir -p %{buildroot}%{vimfiles_root}
mv %{buildroot}%{_datadir}/ocp-indent/vim/* %{buildroot}%{vimfiles_root}
rm -fr %{buildroot}%{_datadir}/ocp-indent

# Generate the autoload file for the Emacs interface and byte compile
cd %{buildroot}%{_emacs_sitelispdir}
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/ocp-indent-loaddefs.el\"))"
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv ocp-indent-loaddefs.el %{buildroot}%{_emacs_sitestartdir}
%_emacs_bytecompile ocp-indent.el
cd -

%files -f .ofiles
%doc README.md CHANGELOG.md
%license LICENSE
%{_emacs_sitelispdir}/ocp-indent.elc
%{_emacs_sitestartdir}/ocp-indent-loaddefs.el
%{vimfiles_root}/indent/ocaml.vim

%files devel -f .ofiles-devel

%changelog
%autochangelog
