# TODO: A Julia interface is now available, but requires
# https://github.com/JuliaInterop/libcxxwrap-julia, which is not currently
# available in Fedora.

# TODO: A JavaScript interface is now available.  Given the generally poor
# state of JavaScript in Fedora, I do not plan to add a subpackage for it
# unless somebody is really, really persuasive and available to help fix it
# if it breaks.

# A Go interface is now available, but Fedora no longer builds Go library
# packages (https://docs.fedoraproject.org/en-US/packaging-guidelines/Golang/).

# Tests are off by default because some of the tests require more memory than
# the koji builders have available.
%bcond test 0

Name:           z3
Version:        5.3.2
Release:        %autorelease
Summary:        Satisfiability Modulo Theories (SMT) solver

%global giturl  https://github.com/Z3Prover/z3
%global majver  %{gsub %version ^(%d*%.%d*)%..*$ %1}

License:        MIT
URL:            https://github.com/Z3Prover/z3/wiki
VCS :           git:%{giturl}.git
Source:         %{giturl}/archive/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): -G Ninja
BuildOption(conf): -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/z3
BuildOption(conf): -DZ3_BUILD_DOCUMENTATION:BOOL=ON
%ifarch %{java_arches}
BuildOption(conf): -DZ3_BUILD_JAVA_BINDINGS:BOOL=ON
%endif
BuildOption(conf): -DZ3_BUILD_OCAML_BINDINGS:BOOL=ON
BuildOption(conf): -DZ3_BUILD_PYTHON_BINDINGS:BOOL=ON
BuildOption(conf): -DCMAKE_INSTALL_PYTHON_PKG_DIR=%{python3_sitelib}
BuildOption(conf): -DZ3_INCLUDE_GIT_HASH:BOOL=OFF
BuildOption(conf): -DZ3_INCLUDE_GIT_DESCRIBE:BOOL=OFF
BuildOption(conf): -DZ3_USE_LIB_GMP:BOOL=ON

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
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-zarith-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%description
Z3 is a satisfiability modulo theories (SMT) solver; given a set of
constraints with variables, it reports a set of values for those variables
that would meet the constraints.  The Z3 input format is an extension of the
one defined by the SMT-LIB 2.0 standard.  Z3 supports arithmetic, fixed-size
bit-vectors, extensional arrays, datatypes, uninterpreted functions, and
quantifiers.

%package libs
Summary:        Library for applications that use z3 functionality

%description libs
Library for applications that use z3 functionality.

%package devel
Summary:        Header files for building applications that use z3
Requires:       z3-libs%{?_isa} = %{version}-%{release}

%description devel
Header files for building applications that use z3.

%package doc
# The content is MIT.
# Two files in examples are GPL-3.0-or-later WITH Bison-exception 2.2:
# examples/tptp/tptp5.tab.c
# examples/tptp/tptp5.tab.c
# Other licenses are due to files installed by doxygen.
# html/clipboard.js: MIT
# html/cookie.js: MIT
# html/doxygen.css: GPL-1.0-or-later
# html/doxygen.svg: GPL-1.0-or-later
# html/dynsections.js: MIT
# html/jquery.js: MIT
# html/navtree.css: GPL-1.0-or-later
# html/search/search.css: GPL-1.0-or-later
# html/search/search.js: MIT
# html/tabs.css: GPL-1.0-or-later
License:        MIT AND GPL-3.0-or-later WITH Bison-exception-2.2 AND GPL-1.0-or-later
Summary:        API documentation for Z3
BuildArch:      noarch

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

%package -n ocaml-z3
Summary:        Ocaml interface to z3
Requires:       z3-libs%{?_isa} = %{version}-%{release}

%description -n ocaml-z3
Ocaml interface to z3.

%package -n ocaml-z3-devel
Summary:        Files for building ocaml applications that use z3
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-z3%{?_isa} = %{version}-%{release}
Requires:       ocaml-zarith-devel%{?_isa}

%description -n ocaml-z3-devel
Files for building ocaml applications that use z3.

%package -n python3-z3
Summary:        Python 3 interface to z3
BuildArch:      noarch
Requires:       z3-libs = %{version}-%{release}

# Provide the PyPI name
%py_provides python3-z3-solver

%description -n python3-z3
Python 3 interface to z3.

%prep
%autosetup -N -n %{name}-%{name}-%{version}

# Comply with the Java packaging guidelines and fill in the version for python
sed -e '/libz3java/s,\(System\.load\)Library("\(.*\)"),\1("%{_libdir}/z3/\2.so"),' \
    -e "s/'so'/'so.%{majver}'/" \
    -i scripts/update_api.py

# Turn off HTML timestamps for reproducible builds
sed -i '/HTML_TIMESTAMP/s/YES/NO/' doc/z3api.cfg.in doc/z3code.dox

# We are Linux, not OS X
sed -i 's/DYLD_LIBRARY_PATH/LD_LIBRARY_PATH/g' src/api/ml/CMakeLists.txt

%build -p
export PYTHON=%{python3}

%build -a
# Remove meaningless memory addresses from the pydoc documentation
# See https://github.com/python/cpython/issues/83572
sed -ri 's/, handle [0-9a-fA-F]+//' \
    %{_vpath_builddir}/doc/api/html/z3{,.z3{,num,poly,printer,rcf,util}}.html
sed -ri 's/ at 0x[0-9a-fA-F]+//g' \
    %{_vpath_builddir}/doc/api/html/z3.z3core.html

%install -a
%ifarch %{java_arches}
# Move the Java interface to its correct location
mkdir -p %{buildroot}%{_libdir}/z3
mkdir -p %{buildroot}%{_jnidir}
mv %{buildroot}%{_javadir}/*.jar %{buildroot}%{_jnidir}
ln -s %{_jnidir}/com.microsoft.z3.jar %{buildroot}%{_libdir}/z3
mv %{buildroot}%{_libdir}/libz3java.so %{buildroot}%{_libdir}/z3
%endif

# Fix permissions
chmod 0755 %{buildroot}%{ocamldir}/stublibs/dllz3ml.so
%ifarch %{ocaml_native_compiler}
chmod 0755 %{buildroot}%{ocamldir}/z3/z3ml.cmxs
%endif

# Fix the python symlink
rm %{buildroot}%{python3_sitelib}/z3/libz3.so.%{majver}
ln -s %{_libdir}/libz3.so.%{majver} \
      %{buildroot}%{python3_sitelib}/z3/libz3.so.%{majver}

# We handle the documentation files below
rm -rf %{buildroot}%{_docdir}/Z3
rm -f examples/ml/*.{cmi,cmo,cmx,o}

# Make a man page
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -o %{buildroot}%{_mandir}/man1/z3.1 \
  -n 'Satisfiability Modulo Theories (SMT) solver' %{_vpath_builddir}/z3

# Fix the pkgconfig file
sed -i 's,//usr,,' %{buildroot}%{_libdir}/pkgconfig/z3.pc

%check
%if %{with test}
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
%{_libdir}/libz3.so.5.3{,.*}

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
%{_jnidir}/com.microsoft.z3.jar
%endif

%files -n ocaml-z3
%dir %{ocamldir}/z3/
%{ocamldir}/z3/META
%{ocamldir}/z3/*.cma
%{ocamldir}/z3/*.cmi
%ifarch %{ocaml_native_compiler}
%{ocamldir}/z3/*.cmxs
%endif
%{ocamldir}/stublibs/dllz3ml.so

%files -n ocaml-z3-devel
%{ocamldir}/z3/*.a
%ifarch %{ocaml_native_compiler}
%{ocamldir}/z3/*.cmx
%{ocamldir}/z3/*.cmxa
%endif
%{ocamldir}/z3/*.mli

%files -n python3-z3
%{python3_sitelib}/z3/

%changelog
%autochangelog
