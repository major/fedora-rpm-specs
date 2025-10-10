ExclusiveArch: %{ocaml_native_compiler}

#OCamlMakefile does not work for parallel builds
%global _smp_ncpus_max 1

Name: ocaml-camlpdf
Version: 2.8.1
Release: %autorelease
Summary: OCaml library for reading, writing and modifying PDFs

#Entire source is LGPL-2.1-or-later WITH OCaml-LGPL-linking exception except
#rijndael-alg-fst* which is LicenseRef-Fedora-Public-Domain, sha2.* which is
#BSD-3-Clause, miniz.* which is MIT and Unlicense, and pdfafmdata.* which is
#APAFML
License: LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception and LicenseRef-Fedora-Public-Domain and BSD-3-Clause and MIT and Unlicense and APAFML
URL: https://github.com/johnwhitington/camlpdf
Source: https://github.com/johnwhitington/camlpdf/archive/v%{version}/camlpdf-%{version}.tar.gz

#This patch adds -g to CFLAGS, an OCamlMakefile variable. This ensures debug symbols are generated for C code.
Patch0: patch.patch

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: gcc
BuildRequires: make
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-rpm-macros

#These two files are not packaged in Fedora, but are bundled. They are unchanged from upstream.
Provides: bundled(sha2.c)
Provides: bundled(rijndael-alg-fst.c) = 3.0
#Miniz has been forked to deal with malformed PDFs. The later version packaged in Fedora would not work.
Provides: bundled(miniz) = 2.1.0

%description
OCaml library for reading, writing and modifying PDFs. The basis of the Cpdf
command line tools.

%package devel
Summary: Development files to %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n camlpdf-%{version}

%build
%make_build

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install
%ocaml_files

%check
cd examples
ocamlopt -I .. ../*.cmxa pdfhello.ml
./a.out
test -f hello.pdf
cd ..

%files -f .ofiles
%doc README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
%autochangelog
