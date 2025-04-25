# Documents generation and Octave binding look not available yet
%global with_python  1
%global with_ruby    0
%global with_java    0
%global with_octave  0
%global with_perl    0
%global with_r       0
%global with_mono    0
#

%global with_doc     0
%global with_check   1

%global octpkg SEDML
%if 0%{?with_octave}
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$
%endif

%global _docdir_fmt %{name}

ExcludeArch:    %{ix86}

Name:           libsedml
Summary:        Library that fully supports SED-ML for SBML
Version:        2.0.33
Release:        %autorelease
Epoch:          2
URL:            https://github.com/fbergmann/libSEDML
Source0:        https://github.com/fbergmann/libSEDML/archive/v%{version}/libSEDML-%{version}.tar.gz
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: swig
BuildRequires: libsbml-devel
BuildRequires: libnuml-devel
BuildRequires: libxml2-devel
BuildRequires: bzip2-devel
BuildRequires: xerces-c-devel
BuildRequires: minizip-devel

%if 0%{?with_check}
BuildRequires: check-devel
%endif

Obsoletes:     python2-libsedml < 2:%{version}-1
Obsoletes:     java-%{octpkg} < 2:%{version}-1
Obsoletes:     libsedml-sharp < 2:%{version}-1
Obsoletes:     octave-%{octpkg} < 2:%{version}-1
Obsoletes:     perl-%{octpkg} < 2:%{version}-1
Obsoletes:     ruby-%{octpkg} < 2:%{version}-1
Obsoletes:     R-%{octpkg} < 2:%{version}-1

##This patch sets libraries' installation paths
Patch0: %{name}-2.0-fix_install_libpaths.patch

Patch1: %{name}-2.0-porting_to_python310.patch

%description
C++ library that fully supports SED-ML 
(Simulation Experiment Description Markup Language) for SBML as well as 
CellML models for creation of the description just as for
the execution of Simulation Experiments. 
This project makes use of libSBML XML layer as well as code generation 
as starting point to produce a library for reading and writing of SED-ML models.
This package provides header and library files of libsedml.

%package devel
Summary: Library that fully supports SED-ML for SBML
Requires: %{name}%{?_isa} = 2:%{version}-%{release}
%description devel
This package provides header and library files of libsedml.

%package static
Summary: Library that fully supports SED-ML for SBML
Provides: %{name}-static = 2:%{version}-%{release}
%description static
This package provides static library of libsedml.

%if 0%{?with_python}
%package -n python3-libsedml
Summary: Python3 library that fully supports SED-ML for SBML
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-libsedml
The %{octpkg} python package contains the libraries to 
develop applications with libSEDML Python3 bindings.
%endif

%if 0%{?with_java}
%package -n java-%{octpkg}
Summary: Java library that fully supports SED-ML for SBML
BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  java-devel
Requires:       java-headless
Requires:       jpackage-utils
%description -n java-%{octpkg}
The %{octpkg} java package contains the libraries to 
develop applications with libSEDML Java bindings.
%endif

%if 0%{?with_octave}
%package -n octave-%{octpkg}
Summary: Octave library that fully supports SED-ML for SBML
BuildRequires:  octave-devel
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
%description -n octave-%{octpkg}
The %{octpkg} octave package contains the libraries to 
develop applications with libSEDML Octave bindings.
%endif

%if 0%{?with_perl}
%package -n perl-%{octpkg}
Summary: Perl library that fully supports SED-ML for SBML
BuildRequires: perl-interpreter
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
%description -n perl-%{octpkg}
The %{octpkg} perl package contains the libraries to 
develop applications with libSEDML Perl bindings.
%endif

%if 0%{?with_ruby}
%package -n ruby-%{octpkg}
Summary: Ruby library that fully supports SED-ML for SBML
BuildRequires: ruby-devel
Requires: ruby(release)
Provides: ruby(SBML) = %{version}
%description -n ruby-%{octpkg}
The %{octpkg} ruby package contains the libraries to 
develop applications with libSEDML Ruby bindings.
%endif

%if 0%{?with_r}
%package -n R-%{octpkg}
Summary: R library that fully supports SED-ML for SBML
BuildRequires: R-devel, R-core-devel, tex(latex)
Requires:      R-core
%description -n R-%{octpkg}
The %{octpkg} R package contains the libraries to 
develop applications with libSEDML R bindings.
%endif

%if 0%{?with_mono}
%package sharp
Summary: Mono library that fully supports SED-ML for SBML
BuildRequires: xerces-c-devel, libxml2-devel, expat-devel
BuildRequires: mono-core
Requires: mono-core
%description sharp
The %{octpkg} csharp package contains the libraries to 
develop applications with libSEDML C# bindings.
%endif

%if 0%{?with_doc}
%package -n libsedml-javadoc
Summary: Library that fully supports SED-ML for SBML
BuildRequires: doxygen
BuildRequires: make
BuildArch: noarch
%description -n libsedml-javadoc
The %{octpkg} doc package contains the documentation
of libSEDML libraries.
%endif

%prep
%autosetup -n libSEDML-%{version} -N

# Fix where CMake config files are installed
sed -e 's| lib/cmake | %{_lib}/cmake |g' -i CMakeLists.txt
sed -e 's| /usr/lib/cmake | %{_libdir}/cmake |g' -i CMakeModules/FindLIBNUML.cmake
sed -e 's| /usr/lib/cmake | %{_libdir}/cmake |g' -i CMakeModules/FindLIBSBML.cmake

# Needed by bindings
%patch -P 0 -p1 -b .fix_install_libpaths

%if %{with python}
%if 0%{?python3_version_nodots} > 39
%patch -P 1 -p1 -b .porting_to_python310
%endif
%endif

%build
######################################################################################################
## ----> Move to build directory ##

mkdir -p build
export LDFLAGS="$RPM_LD_FLAGS -lpthread"
%cmake3 -B build -Wno-dev \
%if 0%{?with_python}
 -DWITH_PYTHON:BOOL=ON \
 -DWITH_SWIG:BOOL=ON \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python%{python3_version}%(python3-config --abiflags) \
 -DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{python3_version}%(python3-config --abiflags).so \
%endif
%if 0%{?with_java}
 -DWITH_JAVA:BOOL=ON \
 -DWITH_SWIG:BOOL=ON \
%endif
%if 0%{?with_octave}
 -DWITH_OCTAVE:BOOL=ON \
%endif
%if 0%{?with_perl}
 -DWITH_PERL:BOOL=ON \
%endif
%if 0%{?with_ruby}
 -DWITH_RUBY:BOOL=ON \
%endif
%if 0%{?with_r}
 -DWITH_R:BOOL=ON \
 -DR_INCLUDE_DIRS:PATH=%{_includedir}/R \
%endif
%if 0%{?with_mono}
 -DWITH_CSHARP:BOOL=ON \
 -DWITH_SWIG:BOOL=ON \
%endif
 -DCSHARP_COMPILER:FILEPATH=%{_bindir}/mcs \
%if 0%{?with_doc}
 -DWITH_DOXYGEN:BOOL=ON \
%endif
%if 0%{?with_check}
 -DWITH_CHECK:BOOL=ON \
 -DWITH_EXAMPLES:BOOL=OFF \
%endif
 -DLIBSBML_LIBRARY:FILEPATH=%{_libdir}/libsbml.so -DLIBSBML_INCLUDE_DIR:PATH=%{_includedir} \
 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DLIBSEDML_SHARED_VERSION:BOOL=ON \
 -DEXTRA_LIBS:STRING="numl;sbml;xml2;bz2;z;m;dl" -DLIBSBML_STATIC:BOOL=OFF \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="`pkg-config --cflags libxml-2.0`" \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCPACK_BINARY_TZ:BOOL=OFF -DCPACK_BINARY_TGZ:BOOL=OFF \
 -DCPACK_SOURCE_TBZ2:BOOL=OFF -DCPACK_SOURCE_TGZ:BOOL=OFF \
 -DCPACK_SOURCE_TZ:BOOL=OFF -DWITH_ZLIB:BOOL=ON -DWITH_CPP_NAMESPACE:BOOL=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES

##'Parallel make' breaks Java library's building
## And mono build seems no good on s390x with parallel build
%if 0%{?with_java} || 0%{?with_mono}
make -j1 -C build
%else
%make_build -C build
%endif

####################################################################################################

%install
%make_install -C build

mkdir -p $RPM_BUILD_ROOT%{_datadir}/libsedml

##Only for R library
%if 0%{?with_r}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library build/bindings/r/libSEDML_%{version}_R_*.tar.gz
test -d %{octpkg}/src && (cd %{octpkg}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/%{octpkg}/R.css

# Make symlink instead hard-link
ln -sf %{_libdir}/libSEDML.so $RPM_BUILD_ROOT%{_libdir}/R/library/libSEDML/libs/libSEDML.so
%endif
##

%if 0%{?with_octave}
mkdir -p $RPM_BUILD_ROOT%{octpkgdir}/packinfo
install -pm 644 LICENSE.txt *.md $RPM_BUILD_ROOT%{octpkgdir}/packinfo
%endif

## Remove libtool archives
find $RPM_BUILD_ROOT -name '*.la' -delete

rm -rf %{buildroot}%{_datadir}/cmake

%if 0%{?with_r}
%ldconfig_scriptlets -n R-%{octpkg}
%endif

%if 0%{?with_octave}
%post -n octave-%{octpkg}
%octave_cmd pkg rebuild

%postun -n octave-%{octpkg}
%octave_cmd pkg rebuild

%preun -n octave-%{octpkg}
%octave_pkg_preun
%endif

%if 0%{?with_check}
%check
make test -C build
%endif

%files
%doc *.md
%license LICENSE.txt
%{_libdir}/libsedml.so.*

%files devel
%{_libdir}/libsedml.so
%{_libdir}/cmake/sedml*.cmake
%{_includedir}/sedml/

%files static
%doc *.md
%license LICENSE.txt
%{_libdir}/%{name}-static.a

%if 0%{?with_python}
%files -n python3-libsedml
%doc *.md
%license LICENSE.txt
%{python3_sitearch}/libsedml/
%{python3_sitearch}/*.pth
%endif

%if 0%{?with_java}
%files -n java-%{octpkg}
%{_javadir}/libsedmlj.jar
%{_libdir}/libsedml/
%endif

%if 0%{?with_octave}
%files -n octave-%{octpkg}
%{octpkgdir}/packinfo
%{octpkglibdir}/
%endif

%if 0%{?with_perl}
%files -n perl-%{octpkg}
%doc *.md
%license LICENSE.txt
%{perl_vendorarch}/LibSEDML.*
%exclude %dir %{perl_vendorarch}/auto/
%{perl_vendorarch}/auto/libSEDML/
%endif

%if 0%{?with_ruby}
%files -n ruby-%{octpkg}
%doc *.md
%license LICENSE.txt
%{ruby_vendorarchdir}/*.so
%endif

%if 0%{?with_r}
%files -n R-%{octpkg}
%doc *.md
%license LICENSE.txt
%{_libdir}/R/library/libSEDML/
%{_libdir}/libSEDML.so
%endif

%if 0%{?with_mono}
%files sharp
%doc *.md
%license LICENSE.txt
##DLL library cannot be registered because not signed
##https://github.com/fbergmann/libSEDML/issues/10
#%%{_monogacdir}/libsedmlcsP
%{_monodir}/libsedmlcsP/
%endif

%if 0%{?with_doc}
%files -n libsedml-javadoc
%doc *.md
%license LICENSE.txt
%doc 00README*
%doc index.html src formatted
%endif

%changelog
%autochangelog
