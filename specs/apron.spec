%global giturl  https://github.com/antoinemine/apron

Name:           apron
Version:        0.9.15
Summary:        Numerical abstract domain library
Release:        %autorelease

# The entire package is LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
# except newpolka/mf_qsort.c and ppl/*, all of which are GPL-2.0-or-later.
# This means that libpolkaMPQ.so.*, libpolkaRll.so.*, and libap_ppl.so.* are
# GPL-2.0-or-later, and the other libraries are all LGPL-2.1-or-later WITH
# OCaml-LGPL-linking-exception.
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND GPL-2.0-or-later
URL:            https://antoinemine.github.io/Apron/doc/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# This patch has not been sent upstream as it is GCC-specific.  Certain
# symbols are defined in both libpolkaMPQ and libpolkaRll, with different
# implementations.  This patch makes references to those symbols in
# libap_pkgrid be weak references, since that library can be combined with
# either of the 2 implementations.
Patch0:         %{name}-weak.patch
# Fix the OCaml build on bytecode-only architectures
Patch1:         %{name}-ocaml-bytecode.patch
# Update CSDP support for CSDP 6.2.0
Patch2:         %{name}-csdp.patch
# Since the jgmp library is not installed in a normal search path, add an rpath
# to the japron library so it can find jgmp
Patch3:         %{name}-japron-link.patch
# Fix a japron hasVar bug
# https://github.com/antoinemine/apron/issues/94
# https://github.com/antoinemine/apron/pull/95
Patch4:         %{name}-hasvar.patch
# Add a missing flint #include
Patch5:         %{name}-flint.patch
# Prevent segfaults in the OCaml garbage collector
# https://github.com/antoinemine/apron/pull/112
Patch6:         %{name}-ocaml-gc.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  csdp-devel
BuildRequires:  doxygen-latex
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  glpk-devel
%ifarch %{java_arches}
BuildRequires:  java-devel
BuildRequires:  javapackages-local
%endif
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  ppl-devel
BuildRequires:  pplite-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-mlgmpidl-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  perl-interpreter
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(etoc.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(listofitems.sty)
BuildRequires:  tex(newunicodechar.sty)
BuildRequires:  tex(stackengine.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(ulem.sty)
BuildRequires:  texinfo-tex

%global sover %(cut -d. -f 1 <<< %{version})

# Do not Require symbols we do not Provide
%global __ocaml_requires_opts -i Coeff -i Dim -i Interval -i Lincons0 -i Linexpr0 -i Scalar -i Tcons0 -i Texpr0

# This can be removed when F40 reaches EOL
%ifnarch %{java_arches}
Obsoletes:      japron < 0.9.13-12
%endif

%description
The APRON library is dedicated to the static analysis of the numerical
variables of a program by Abstract Interpretation.  The aim of such an
analysis is to infer invariants about these variables, like 1<=x+y<=z,
which holds during any execution of the program.

The APRON library is intended to be a common interface to various
underlying libraries/abstract domains and to provide additional services
that can be implemented independently from the underlying
library/abstract domain.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glpk-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Provides:       bundled(js-jquery)

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package -n     ocaml-%{name}
Summary:        Ocaml interface to APRON
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}
Ocaml interface to the APRON library.

%package -n     ocaml-%{name}-devel
Summary:        Development files for the Ocaml interface to APRON
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Requires:       ocaml-%{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}-devel
Development files for the Ocaml interface to the APRON library.

%ifarch %{java_arches}
%package -n     japron
Summary:        Java interface to APRON
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       javapackages-filesystem

%description -n japron
Java interface to the APRON library.
%endif

%prep
%autosetup -N -n %{name}-%{version}
%patch -P0 -p0
%ifnarch %{ocaml_native_compiler}
%patch -P1 -p0
%endif
%autopatch -m2 -p0

%conf
# Fix library path for 64-bit installs
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's,\${apron_prefix}/lib,&64,' configure
  sed -i 's,/lib,&64,' vars.mk
fi

# Fix encodings
iconv -f iso8859-1 -t utf-8 Changes > Changes.utf8
touch -r Changes Changes.utf8
mv -f Changes.utf8 Changes

# Preserve timestamps when copying
sed -i 's/^\([[:blank:]]*cp[[:blank:]]\)/\1-p /' Makefile */Makefile

# Build with debuginfo
sed -i 's/^OCAMLOPTFLAGS =/& -g/' configure
sed -i 's|\$(OCAMLMKLIB) -L.*|& -g|' vars.mk

# Give the C++ library an soname
sed -i '/shared/s/\$(CXX)/$(CXX_APRON_DYLIB)/' apronxx/Makefile

# For reproducibility, omit timestamps from generated documentation
sed -i '/HTML_TIMESTAMP/s/= YES/= NO/' apronxx/doc/Doxyfile

%build
# This is NOT an autoconf-generated script.  Do not use %%configure
export CPPFLAGS='-D_GNU_SOURCE -I%{_includedir}/csdp'
export CFLAGS='%{build_cflags} -fsigned-char'
export CXXFLAGS='%{build_cxxflags} -fsigned-char'
export CSDP_PATH=%{_prefix}
%ifarch %{java_arches}
export JAVA_HOME='%{_jvmdir}/java'
export JAVA_TOOL_OPTIONS='-Dfile.encoding=UTF8'
./configure -prefix %{_prefix} -pplite-prefix %{_prefix} -no-strip -java-prefix %{_jvmdir}/java
%else
./configure -prefix %{_prefix} -pplite-prefix %{_prefix} -no-strip
%endif

# Put back a flag that the configure script strips out
sed -i 's/-Wall/& -Werror=format-security/' Makefile.config

# Generate dependency lists
touch apron/depend
make -C apron depend

# Parallel builds fail intermittently
make
make doc

# for some reason this is no longer built in `make doc`
make -C mlapronidl mlapronidl.pdf

%install
# Install the ocaml bits into the buildroot
sed -i 's, install ,&-destdir %{buildroot}%{ocamldir} -ldconf ignore ,' \
    Makefile

# Install
mkdir -p %{buildroot}%{ocamldir}/stublibs
mkdir -p %{buildroot}%{_jnidir}
%ifarch %{java_arches}
make install INSTALL="install -p" APRON_PREFIX=%{buildroot}%{_prefix} \
  JAVA_PREFIX=%{buildroot}%{_jnidir}

# Move the JNI shared objects
mv %{buildroot}%{_libdir}/libj*.so %{buildroot}%{_jnidir}
%else
make install INSTALL="install -p" APRON_PREFIX=%{buildroot}%{_prefix}
%endif

# We don't really want the test binaries
rm -fr %{buildroot}%{_bindir}

# Move the header files into a subdirectory
mkdir %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/apronxx \
   %{buildroot}%{_includedir}/oct %{buildroot}%{_includedir}/%{name}

# Remove extraneous executable bits
find %{buildroot}%{_includedir} \( -name \*.h -o -name \*.hh \) \
     -perm /0111 -execdir chmod a-x {} +

# Erase the static libraries
rm -f %{buildroot}%{_libdir}/*.a

# Fix up the shared library names
pushd %{buildroot}%{_libdir}
for f in lib*.so; do
  mv $f $f.%{version}
  ln -s $f.%{sover} $f
  ln -s $f.%{version} $f.%{sover}
done
popd

# Don't have two sets of documentation both named html
mkdir doc
mv apron/html doc/apron
mv apronxx/doc/html doc/apronxx

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make -C test APRON_INCLUDE=%{buildroot}%{_includedir}/%{name} \
  APRON_LIB=%{buildroot}%{ocamldir}/%{name} \
  CAMLIDL_PREFIX=%{buildroot}%{_libdir}
test/ctest1

%files
%doc AUTHORS Changes README.md apron/apron.pdf
%license COPYING
%{_libdir}/lib*.so.0
%{_libdir}/lib*.so.0.*

%files devel
%doc doc/apron doc/apronxx
%{_libdir}/lib*.so
%{_includedir}/%{name}/
%{_includedir}/avo/
%{_includedir}/fpp/

%files -n ocaml-%{name}
%doc mlapronidl/mlapronidl.pdf
%dir %{ocamldir}/%{name}/
%{ocamldir}/%{name}/META
%{ocamldir}/%{name}/*.cma
%{ocamldir}/%{name}/*.cmi
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}/*.cmxs
%endif
%{ocamldir}/stublibs/dll*

%files -n ocaml-%{name}-devel
%doc mlapronidl/html/*
%{ocamldir}/%{name}/*.a
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}/*.cmxa
%{ocamldir}/%{name}/*.cmx
%endif
%{ocamldir}/%{name}/*.h
%{ocamldir}/%{name}/*.idl
%{ocamldir}/%{name}/*.mli

%ifarch %{java_arches}
%files -n japron
%doc japron/README
%license japron/COPYING
%{_jnidir}/*.jar
%{_jnidir}/*.so
%endif

%changelog
%autochangelog
