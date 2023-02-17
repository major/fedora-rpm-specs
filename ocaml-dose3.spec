%undefine _package_note_flags
# There is also a separate test data repository for a different set of tests
# that is distributed separately.

Name:           ocaml-dose3
Version:        7.0.0
Release:        %autorelease
Summary:        Framework for managing distribution packages and dependencies

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            http://www.mancoosi.org/software/

Source0:        https://gitlab.com/irill/dose3/-/archive/%{version}/%{libname}-%{version}.tar.gz

# Use oUnit2 instead of oUnit
Patch0:         0001-Use-ounit2.patch
# We do not need stdlib-shims, which provides backwards compatibility
Patch1:         0002-Do-not-depend-on-stdlib-shims.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-parmap-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-camlbz2-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-base64-devel >= 3.4.0-1

BuildRequires:  rpm-devel
BuildRequires:  zlib-devel

BuildRequires:  perl, perl-generators

# Test dependencies
BuildRequires:  dpkg
BuildRequires:  %{py3_dist pyyaml}

# Needs latex for documentation.
BuildRequires:  tex(latex)
BuildRequires:  tex(comment.sty)
BuildRequires:  pandoc
BuildRequires:  graphviz
BuildRequires:  poetry
BuildRequires:  /usr/bin/python
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist wheel}

# Depend on pod2man, pod2html.
BuildRequires:  /usr/bin/pod2man
BuildRequires:  /usr/bin/pod2html

%description
Dose3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

Though not tied to any particular distribution, dose3 constitutes a pool of
libraries which enable analyzing packages coming from various distributions.

Besides basic functionalities for querying and setting package properties,
dose3 also implements algorithms for solving more complex problems
(monitoring package evolutions, correct and complete dependency resolution,
repository-wide uninstallability checks).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cudf-devel%{?_isa}
Requires:       ocaml-extlib-devel%{?_isa}
Requires:       ocaml-ocamlgraph-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

# Since these are applications, I think the correct name is "dose3-tools"
# and not "ocaml-dose3-tools", but I'm happy to change it if necessary.

%package -n dose3-tools
Summary:        Tools suite from the dose3 framework

%description -n dose3-tools
Dose3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

This package contains the tools shipped with the dose3 framework
for manipulating packages of various formats.

%prep
%autosetup -p1 -n %{libname}-%{version}

# Do not run linkcheck; the koji builders have no network access
sed -i 's/html linkcheck/html/' doc/rtd/Makefile

%build
dune build %{?_smp_mflags} --display=verbose @install --release
dune build %{?_smp_mflags} @doc --release
# FIXME: parallel build does not work
make -C doc

%install
dune install --destdir=%{buildroot} --release

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

# Install manpages.
mkdir -p %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_mandir}/man8/
cp -a doc/manpages/*.8 %{buildroot}%{_mandir}/man8/
cp -a doc/manpages/*.5 %{buildroot}%{_mandir}/man5/
cp -a doc/manpages/*.1 %{buildroot}%{_mandir}/man1/

%check
dune runtest --release

%files
%license COPYING
%doc CHANGES CREDITS README.architecture
%dir %{_libdir}/ocaml/%{libname}/
%dir %{_libdir}/ocaml/%{libname}/algo/
%dir %{_libdir}/ocaml/%{libname}/common/
%dir %{_libdir}/ocaml/%{libname}/versioning/
%dir %{_libdir}/ocaml/%{libname}-extra/
%dir %{_libdir}/ocaml/%{libname}-extra/debian/
%dir %{_libdir}/ocaml/%{libname}-extra/doseparse/
%dir %{_libdir}/ocaml/%{libname}-extra/npm/
%dir %{_libdir}/ocaml/%{libname}-extra/opam2/
%dir %{_libdir}/ocaml/%{libname}-extra/opencsw/
%dir %{_libdir}/ocaml/%{libname}-extra/pef/
%{_libdir}/ocaml/%{libname}{,-extra}/META
%{_libdir}/ocaml/%{libname}{,-extra}{,/*}/*.cma
%{_libdir}/ocaml/%{libname}{,-extra}{,/*}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}{,-extra}{,/*}/*.cmxs
%endif

%files devel
%license COPYING
%doc _build/default/_doc/_html/*
%{_libdir}/ocaml/%{libname}{,-extra}/dune-package
%{_libdir}/ocaml/%{libname}{,-extra}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}{,-extra}{,/*}/*.a
%{_libdir}/ocaml/%{libname}{,-extra}{,/*}/*.cmx
%{_libdir}/ocaml/%{libname}{,-extra}{,/*}/*.cmxa
%endif
%{_libdir}/ocaml/%{libname}{,-extra}{,/*}/*.cmt
%{_libdir}/ocaml/%{libname}{,-extra}{,/*}/*.cmti
%{_libdir}/ocaml/%{libname}{,-extra}{,/*}/*.mli

%files -n dose3-tools
%license COPYING
%doc doc/debcheck.primer/*.pdf
%doc doc/apt-external-solvers.primer/*.pdf
%doc doc/apt-cudf/
%{_bindir}/apt-cudf
%{_bindir}/dose-builddebcheck
%{_bindir}/dose-ceve
%{_bindir}/dose-challenged
%{_bindir}/dose-deb-coinstall
%{_bindir}/dose-distcheck
%{_bindir}/dose-outdated
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%changelog
%autochangelog
