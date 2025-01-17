# TODO: A Julia interface is now available, but requires
# https://github.com/JuliaInterop/libcxxwrap-julia, which is not currently
# available in Fedora.

# TODO: A JavaScript interface is now available.  Given the generally poor
# state of JavaScript in Fedora, I do not plan to add a subpackage for it
# unless somebody is really, really persuasive and available to help fix it
# if it breaks.

# Tests are off by default because some of the tests require more memory than
# the koji builders have available.
%bcond test 0

%global giturl  https://github.com/Z3Prover/z3

Name:           z3
Version:        4.13.4
Release:        %autorelease
Summary:        Satisfiability Modulo Theories (SMT) solver

License:        MIT
URL:            https://github.com/Z3Prover/z3/wiki
VCS :           git:%{giturl}.git
Source:         %{giturl}/archive/%{name}-%{version}.tar.gz
# Do not try to build or install native OCaml artifacts on bytecode-only arches
Patch:          %{name}-ocaml.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  help2man
%ifarch %{java_arches}
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
%endif
BuildRequires:  make
BuildRequires:  ninja-build
%ifnarch %{ix86}
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-zarith-devel
%endif
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%description
Z3 is a satisfiability modulo theories (SMT) solver; given a set of
constraints with variables, it reports a set of values for those
variables that would meet the constraints.  The Z3 input format is an
extension of the one defined by the SMT-LIB 2.0 standard.  Z3 supports
arithmetic, fixed-size bit-vectors, extensional arrays, datatypes,
uninterpreted functions, and quantifiers.

%package libs
Summary:        Library for applications that use z3 functionality

# This can be removed when F40 reaches EOL
%ifnarch %{java_arches}
Obsoletes:      java-z3 < 4.8.17-5
%endif

%description libs
Library for applications that use z3 functionality.

%package devel
Summary:        Header files for build applications that use z3
Requires:       z3-libs%{?_isa} = %{version}-%{release}

%description devel
Header files for build applications that use z3.

%package doc
# The content is MIT.
# Two files in examples are GPL-3.0-or-later WITH Bison-exception 2.2:
# examples/tptp/tptp5.tab.c
# examples/tptp/tptp5.tab.c
# Other licenses are due to files installed by doxygen.
# html/bc_s.png: GPL-1.0-or-later
# html/bdwn.png: GPL-1.0-or-later
# html/closed.png: GPL-1.0-or-later
# html/doc.png: GPL-1.0-or-later
# html/doxygen.css: GPL-1.0-or-later
# html/doxygen.svg: GPL-1.0-or-later
# html/dynsections.js: MIT
# html/folderclosed.png: GPL-1.0-or-later
# html/folderopen.png: GPL-1.0-or-later
# html/jquery.js: MIT
# html/nav_f.png: GPL-1.0-or-later
# html/nav_g.png: GPL-1.0-or-later
# html/nav_h.png: GPL-1.0-or-later
# html/open.png: GPL-1.0-or-later
# html/search/search.css: GPL-1.0-or-later
# html/search/search.js: MIT
# html/search/search_l.png: GPL-1.0-or-later
# html/search/search_m.png: GPL-1.0-or-later
# html/search/search_r.png: GPL-1.0-or-later
# html/splitbar.png: GPL-1.0-or-later
# html/sync_off.png: GPL-1.0-or-later
# html/sync_on.png: GPL-1.0-or-later
# html/tab_a.png: GPL-1.0-or-later
# html/tab_b.png: GPL-1.0-or-later
# html/tab_h.png: GPL-1.0-or-later
# html/tab_s.png: GPL-1.0-or-later
# html/tabs.css: GPL-1.0-or-later
License:        MIT AND GPL-3.0-or-later WITH Bison-exception-2.2 AND GPL-1.0-or-later
Summary:        API documentation for Z3
# FIXME: this should be noarch, but we end up with different numbers of inheritance
# graphs on different architectures.  Why?

%description doc
API documentation for Z3.

%ifarch %{java_arches}
%package -n java-z3
Summary:        Java interface to z3
Requires:       z3-libs%{?_isa} = %{version}-%{release}
Requires:       java
Requires:       javapackages-tools

%description -n java-z3
Java interface to z3.
%endif

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
%ifnarch %{ix86}
%package -n ocaml-z3
Summary:        Ocaml interface to z3
Requires:       z3-libs%{?_isa} = %{version}-%{release}

%description -n ocaml-z3
Ocaml interface to z3.

%package -n ocaml-z3-devel
Summary:        Files for building ocaml applications that use z3
Requires:       ocaml-z3%{?_isa} = %{version}-%{release}
Requires:       ocaml-zarith-devel%{?_isa}

%description -n ocaml-z3-devel
Files for building ocaml applications that use z3.
%endif

%package -n python3-z3
Summary:        Python 3 interface to z3
BuildArch:      noarch
Requires:       z3-libs = %{version}-%{release}

%description -n python3-z3
Python 3 interface to z3.

%prep
%autosetup -N -n %{name}-%{name}-%{version}
%ifnarch %{ocaml_native_compiler}
%patch -P0 -p1
%endif

%conf
# Enable verbose builds, use Fedora CFLAGS, preserve timestamps when installing,
# include the entire contents of the archives in the library, link the library
# with the correct flags, and build the ocaml files with debuginfo.
sed \
  -e 's/@$(CXX)/$(CXX)/' \
  -e '/O3/d' \
  -e "s/\(['\"]\)cp\([^[:alnum:]]\)/\1cp -p\2/" \
  -e "s/\(SLIBEXTRAFLAGS = '\)'/\1-Wl,--no-whole-archive'/" \
  -e '/SLIBFLAGS/s|-shared|& %{build_ldflags} -Wl,--whole-archive|' \
  -e 's/\(libz3$(SO_EXT)\)\(\\n\)/\1 -Wl,--no-whole-archive\2/' \
  -e "s/OCAML_FLAGS = ''/OCAML_FLAGS = '-g'/" \
  -i scripts/mk_util.py

# Comply with the Java packaging guidelines and fill in the version for python
majver=$(cut -d. -f-2 <<< %{version})
sed -e '/libz3java/s,\(System\.load\)Library("\(.*\)"),\1("%{_libdir}/z3/\2.so"),' \
    -e "s/'so'/'so.$majver'/" \
    -i scripts/update_api.py

# Turn off HTML timestamps for reproducible builds
sed -i '/HTML_TIMESTAMP/s/YES/NO/' doc/z3api.cfg.in doc/z3code.dox

%build
export PYTHON=%{python3}

%cmake -G Ninja \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/z3 \
  -DCMAKE_JAVA_COMPILE_FLAGS="-source;1.8;-target;1.8" \
  -DZ3_BUILD_DOCUMENTATION:BOOL=ON \
%ifarch %{java_arches}
  -DZ3_BUILD_JAVA_BINDINGS:BOOL=ON \
%endif
  -DZ3_BUILD_PYTHON_BINDINGS:BOOL=ON \
  -DZ3_INCLUDE_GIT_HASH:BOOL=OFF \
  -DZ3_INCLUDE_GIT_DESCRIBE:BOOL=OFF \
  -DZ3_USE_LIB_GMP:BOOL=ON

%cmake_build

%ifnarch %{ix86}
# The cmake build system does not build the OCaml interface.  Do that manually.
#
# First, run the configure script to generate several files.
# This is NOT an autoconf-generated configure script.
./configure -p %{_prefix} --gmp --ml

# Second, to prevent make from rebuilding the entire library, copy the
# cmake-built library to where make expects it.
cp -dp %{_vpath_builddir}/libz3.so* build

# Third, make wants to rebuild libz3.so since its dependencies do not exist.
# Do selective Makefile surgery to prevent this.
sed -i '/^api/s/ libz3\$(SO_EXT)//g' build/Makefile

# Fourth, build the OCaml interface
%make_build -C build ml
%endif

%install
# Install the C++, python3, and Java interfaces
%cmake_install

%ifarch %{java_arches}
# Move the Java interface to its correct location
mkdir -p %{buildroot}%{_libdir}/z3
mkdir -p %{buildroot}%{_jnidir}
mv %{buildroot}%{_javadir}/*.jar %{buildroot}%{_jnidir}
ln -s %{_jnidir}/com.microsoft.z3.jar %{buildroot}%{_libdir}/z3
mv %{buildroot}%{_libdir}/libz3java.so %{buildroot}%{_libdir}/z3
%endif

%ifnarch %{ix86}
# Install the OCaml interface
cd build/api/ml
mkdir -p %{buildroot}%{ocamldir}/Z3
%ifarch %{ocaml_native_compiler}
cp -p *.cmx{,a,s} %{buildroot}%{ocamldir}/Z3
%endif
cp -p META *.{a,cma,cmi,mli} %{buildroot}%{ocamldir}/Z3
mkdir -p %{buildroot}%{ocamldir}/stublibs
cp -p *.so %{buildroot}%{ocamldir}/stublibs
cd -
%endif

# We handle the documentation files below
rm -rf %{buildroot}%{_docdir}/Z3

# Make a man page
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -o %{buildroot}%{_mandir}/man1/z3.1 \
  -n 'Satisfiability Modulo Theories (SMT) solver' %{_vpath_builddir}/z3

# Fix the pkgconfig file
sed -i 's,//usr,,' %{buildroot}%{_libdir}/pkgconfig/z3.pc

%if %{with test}
%check
cd build
make test-z3
./test-z3 /a
cd -
%endif

%files
%doc README.md RELEASE_NOTES.md
%{_bindir}/z3
%{_mandir}/man1/z3.1*

%files libs
%license LICENSE.txt
%{_libdir}/libz3.so.4.13*

%files devel
%{_includedir}/z3/
%{_libdir}/libz3.so
%{_libdir}/cmake/z3/
%{_libdir}/pkgconfig/z3.pc

%files doc
%doc %{_vpath_builddir}/doc/api/html examples
%license LICENSE.txt

%ifarch %{java_arches}
%files -n java-z3
%{_libdir}/z3/
%{_jnidir}/com.microsoft.z3*jar
%endif

%ifnarch %{ix86}
%files -n ocaml-z3
%dir %{ocamldir}/Z3/
%{ocamldir}/Z3/META
%{ocamldir}/Z3/*.cma
%{ocamldir}/Z3/*.cmi
%ifarch %{ocaml_native_compiler}
%{ocamldir}/Z3/*.cmxs
%endif
%{ocamldir}/stublibs/*.so

%files -n ocaml-z3-devel
%{ocamldir}/Z3/*.a
%ifarch %{ocaml_native_compiler}
%{ocamldir}/Z3/*.cmx
%{ocamldir}/Z3/*.cmxa
%endif
%{ocamldir}/Z3/*.mli
%endif

%files -n python3-z3
%{python3_sitelib}/z3/

%changelog
%autochangelog
