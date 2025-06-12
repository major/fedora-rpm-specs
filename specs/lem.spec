Name:           lem
Version:        2025.03.13
Release:        %autorelease
Summary:        A tool for semantic definition language

License:        LGPL-2.0-only
URL:            https://github.com/rems-project/%{name}
Source0:        https://github.com/rems-project/%{name}/archive/2025-03-13/%{name}-2025-03-13.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  help2man
BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-zarith-devel
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-rpm-macros

%global debug_package %{nil}

%description
Lem is a tool for lightweight executable mathematics, 
for writing, managing, and publishing large-scale 
portable semantic definitions. It exports to LaTeX, 
OCaml code, and theorem proves (Coq, HOL4, Isabelle/HOL). 
Generated Coq code may not be idiomatic. It acts as 
an intermediate language for domain-specific tools 
and for porting definitions between theorem proves.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n lem-2025-03-13 -p1

%build
make

%install
# INSTALL_DIR variable is in Makefile
# but INSTALLDIR is in ocaml-lib/ocamlbuild.mk 
mkdir -p %{buildroot}%{ocamldir}
make install INSTALLDIR=%{buildroot}%{ocamldir} INSTALL_DIR=%{buildroot}/usr

mkdir -p %{buildroot}%{_mandir}/man1
help2man -N --version-string=%{version} -o %{buildroot}%{_mandir}/man1/lem.1 \
  -n 'Convert markdown to HTML' %{buildroot}%{_bindir}/lem

%files
%{_bindir}/lem
%{_mandir}/man1/lem.1*
%license LICENSE
%doc README.md

%files devel
%{ocamldir}/lem/*
%{ocamldir}/lem_num/*
%{ocamldir}/lem_zarith/*
%attr(644, root, root)%{_datadir}/lem/coq-lib/*
%attr(644, root, root)%{_datadir}/lem/hol-lib/*
%attr(644, root, root)%{_datadir}/lem/isabelle-lib/*
%attr(644, root, root)%{_datadir}/lem/library/*

%changelog
%autochangelog
