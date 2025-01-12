# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# The OCaml code is byte compiled, not native compiled, so there are no ELF
# objects in the binary RPM.
%global debug_package %{nil}

%global giturl  https://github.com/ocaml-community/utop

Name:           utop
Version:        2.15.0
Release:        %autorelease
Summary:        Improved toplevel for OCaml

License:        BSD-3-Clause
URL:            https://ocaml-community.github.io/utop/
VCS :           git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.11.0
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-cppo >= 1.1.2
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-findlib >= 1.7.2
BuildRequires:  ocaml-lambda-term-devel >= 3.1.0
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-lwt-react-devel
BuildRequires:  ocaml-react-devel >= 1.0.0
BuildRequires:  ocaml-xdg-devel >= 3.9.0
BuildRequires:  ocaml-zed-devel >= 3.2.0

# for utop.el
BuildRequires:  emacs-nw
BuildRequires:  emacs-tuareg

Provides:       ocaml-%{name}%{?_isa} = %{version}-%{release}

%description
utop is an improved toplevel (i.e., Read-Eval-Print Loop) for
OCaml. It can run in a terminal or in Emacs. It supports line
editing, history, real-time and context sensitive completion,
colors, and more.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-findlib%{?_isa}
Requires:       ocaml-lambda-term-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-zed-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package -n emacs-utop
Summary:        Emacs front end for utop
BuildArch:      noarch
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       emacs-tuareg
Recommends:     emacs-company

%description -n emacs-utop
This package contains an Emacs front end for utop, an improved toplevel
for OCaml.

%prep
%autosetup

%build
%dune_build

cd src/top
emacs -batch --no-init-file --no-site-file \
    --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/utop-loaddefs.el\"))"
%_emacs_bytecompile utop.el
cd -

%install
%dune_install

# Install the Emacs interface
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cp -p src/top/utop-loaddefs.* %{buildroot}%{_emacs_sitestartdir}
cp -p src/top/utop.elc %{buildroot}%{_emacs_sitelispdir}

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%files -n emacs-utop
%{_emacs_sitelispdir}/%{name}.el*
%{_emacs_sitestartdir}/%{name}-loaddefs.el*

%changelog
%autochangelog
