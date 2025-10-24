ExclusiveArch: %{ocaml_native_compiler}

#OCamlMakefile does not work for parallel builds
%global _smp_ncpus_max 1

Name: ocaml-cpdf
Version: 2.8.1
Release: %autorelease
Summary: OCaml library and command line tool for processing PDFs

#All AGPL-3.0-only except cpdfxmlm.ml* which are ISC and cpdfyojson.ml* which
#are BSD-3-Clause and the textual Matterhorn protocol error descriptions in 
#cpdfua.ml which are CC-BY-4.0 and the files cpdfunicodedata.* which are
#Unicode-DFS-2015
License: AGPL-3.0-only and ISC and BSD-3-Clause and CC-BY-4.0 and Unicode-DFS-2015
URL: https://github.com/johnwhitington/cpdf-source
Source: https://github.com/johnwhitington/cpdf-source/archive/v%{version}/cpdf-source-%{version}.tar.gz

#This patch adds -g to CFLAGS, an OCamlMakefile variable. This ensures debug
#symbols are generated for C code.
Patch0: patch.patch

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: gcc
BuildRequires: make
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-rpm-macros
BuildRequires: ocaml-camlpdf-devel = %{version}

#These two modules have been modified upstream. The versions packaged in Fedora would not work.
Provides: bundled(ocaml-yojson)
Provides: bundled(ocaml-xmlm)

%description
OCaml library and command line tool for processing PDFs, for example
merging and splitting, adding text, or compressing.

%package devel
Summary: Development files to %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package -n cpdf
Summary: Command line tool for processing PDFs

%description -n cpdf
PDF command line tool for processing PDFs, for example merging and
splitting, adding text, or compressing.

%prep
%autosetup -n cpdf-source-%{version}

%build
%make_build

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install
%ocaml_files
mkdir -p %{buildroot}%{_bindir}
cp -a cpdf %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -a cpdf.1 %{buildroot}%{_mandir}/man1

%check
./cpdf -create-pdf -o out.pdf
test -f out.pdf

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%files -n cpdf
%doc cpdfmanual.pdf
%license LICENSE.md
%{_bindir}/cpdf
%{_mandir}/man1/cpdf.1*

%changelog
%autochangelog
