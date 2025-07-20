##Documents generation and Octave binding look not available yet

%global with_python  1
%global with_ruby    0
%global with_java    0

%global with_octave  0
%global with_perl    0
%global with_r       0

%ifarch %{mono_arches}
%global with_mono    0
%else
%global with_mono    0
%endif

%global with_doc     1

# No tests?
%global with_check   0

%global octpkg NUML
%if 0%{?with_octave}
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$
%endif

%global _docdir_fmt %{name}

%global commit 50815eb877aaa42bf9428cfa32f6ea33fc101e3f
%global date 20201214
%global shortcommit %(c=%{commit}; echo ${c:0:7})

ExcludeArch:    %{ix86}

Name:           libnuml
Summary:        Numerical Markup Language
Version:        1.1.7
Release:        %autorelease
URL:            https://github.com/NuML/NuML
Source0:        https://github.com/NuML/NuML/archive/%{commit}/NuML-%{version}.tar.gz
License:        LGPL-2.0-or-later

BuildRequires: cmake
BuildRequires: gcc, gcc-c++
BuildRequires: zlib-devel
BuildRequires: swig
BuildRequires: libsbml-devel
BuildRequires: libxml2-devel
BuildRequires: bzip2-devel
BuildRequires: xerces-c-devel
BuildRequires: minizip-ng-compat-devel

%if 0%{?with_check}
BuildRequires: check-devel
%endif

Obsoletes:     python2-libnuml < 0:1.1.4
Obsoletes:     java-%{octpkg} < 0:1.1.4

%description
LibNuML is a library for reading/writing documents describing numerical
results in an XML dialect.
This release includes a number of improvements especially:

 * improved object structure matching the specification document
 * ability to add notes and annotations
 * improved python support

%package devel
Summary: Library that fully supports NUML
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides header and library files of libnuml.

%package static
Summary: Library that fully supports NUML
Provides: libNuML-static = %{version}-%{release}
%description static
This package provides static library of libnuml.

%if 0%{?with_python}
%package -n python3-libnuml
Summary: Python3 library that fully supports NUML
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-libnuml
The %{octpkg} python package contains the libraries to 
develop applications with libNUML Python3 bindings.
%endif

%if 0%{?with_java}
%package -n java-%{octpkg}
Summary: Java library that fully supports NUML
BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  java-devel, javapackages-tools
Requires:       java-headless
Requires:       jpackage-utils
%description -n java-%{octpkg}
The %{octpkg} java package contains the libraries to 
develop applications with libNUML Java bindings.
%endif

%if 0%{?with_octave}
%package -n octave-%{octpkg}
Summary: Octave library that fully supports NUML
BuildRequires:  octave-devel
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
%description -n octave-%{octpkg}
The %{octpkg} octave package contains the libraries to 
develop applications with libNUML Octave bindings.
%endif

%if 0%{?with_perl}
%package -n perl-%{octpkg}
Summary: Perl library that fully supports NUML
BuildRequires: perl-interpreter
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
%description -n perl-%{octpkg}
The %{octpkg} perl package contains the libraries to 
develop applications with libNUML Perl bindings.
%endif

%if 0%{?with_ruby}
%package -n ruby-%{octpkg}
Summary: Ruby library that fully supports NUML
BuildRequires: ruby-devel
Requires: ruby(release)
Provides: ruby(NUML) = %{version}
%description -n ruby-%{octpkg}
The %{octpkg} ruby package contains the libraries to 
develop applications with libNUML Ruby bindings.
%endif

%if 0%{?with_r}
%package -n R-%{octpkg}
Summary: R library that fully supports NUML
BuildRequires: R-devel, R-core-devel, tex(latex)
Requires:      R-core
%description -n R-%{octpkg}
The %{octpkg} R package contains the libraries to 
develop applications with libNUML R bindings.
%endif

%if 0%{?with_mono}
%package sharp
Summary: Mono library that fully supports NUML
BuildRequires: xerces-c-devel, libxml2-devel, expat-devel
BuildRequires: mono-core
Requires: mono-core
%description sharp
The %{octpkg} csharp package contains the libraries to 
develop applications with libNUML C# bindings.
%endif

%if 0%{?with_doc}
%package doc
Summary: Library that fully supports NUML
BuildRequires: doxygen
BuildRequires: make
BuildArch: noarch
%description doc
The %{octpkg} doc package contains the HTML documentation
of libNUML libraries.
%endif

%prep
%autosetup -n NuML-%{version}

%build
pushd libnuml
%cmake -Wno-dev \
 -DEXTRA_INCLUDE_DIRS:STRING=%{_includedir}/minizip \
%if 0%{?with_python}
 -DWITH_PYTHON:BOOL=ON \
 -DWITH_SWIG:BOOL=ON \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python%{python3_version} \
 -DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{python3_version}.so \
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
 -DWITH_EXAMPLES:BOOL=ON \
%endif
 -DLIBSBML_LIBRARY:FILEPATH=%{_libdir}/libsbml.so -DLIBSBML_INCLUDE_DIR:PATH=%{_includedir} \
 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DLIBNUML_SHARED_VERSION:BOOL=ON \
 -DEXTRA_LIBS:STRING="sbml;xml2;bz2;z;m;dl" -DLIBSBML_STATIC:BOOL=OFF \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="-I%{_includedir}/libxml2" \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCPACK_BINARY_TZ:BOOL=OFF -DCPACK_BINARY_TGZ:BOOL=OFF \
 -DCPACK_SOURCE_TBZ2:BOOL=OFF -DCPACK_SOURCE_TGZ:BOOL=OFF \
 -DCPACK_SOURCE_TZ:BOOL=OFF -DWITH_ZLIB:BOOL=ON -DWITH_CPP_NAMESPACE:BOOL=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES
%cmake_build

%if 0%{?with_doc}
doxygen
%endif
popd

####################################################################################################

%install
pushd libnuml
%cmake_install
popd

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

##Only for R library
%if 0%{?with_r}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library build/bindings/r/libNUML_%{version}_R_*.tar.gz
test -d %{octpkg}/src && (cd %{octpkg}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/%{octpkg}/R.css

# Make symlink instead hard-link
ln -sf %{_libdir}/libNUML.so $RPM_BUILD_ROOT%{_libdir}/R/library/libNUML/libs/libNUML.so
%endif
##

%if 0%{?with_octave}
mkdir -p $RPM_BUILD_ROOT%{octpkgdir}/packinfo
install -pm 644 LICENSE.txt *.md $RPM_BUILD_ROOT%{octpkgdir}/packinfo
%endif

%if 0%{?with_java}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_jnidir}
mv $RPM_BUILD_ROOT%{_libdir}/libnumlj.so $RPM_BUILD_ROOT%{_libdir}/%{name}/
ln -sf %{_libdir}/%{name}/libnumlj.so $RPM_BUILD_ROOT%{_jnidir}/libnumlj.so
%endif

## Remove libtool archives
find $RPM_BUILD_ROOT -name '*.la' -delete

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
pushd libnuml
%ctest
%endif

%files
%doc libnuml/*.md
%license libnuml/LICENSE.txt
%{_libdir}/libnuml.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/cmake/numl-*.cmake
%{_includedir}/numl/
%{_datadir}/cmake/Modules/FindLIBNUML.cmake

%files static
%doc libnuml/*.md
%license libnuml/LICENSE.txt
%{_libdir}/%{name}-static.a
%{_libdir}/cmake/numl-static-config*.cmake

%if 0%{?with_python}
%files -n python3-%{name}
%doc libnuml/*.md
%license libnuml/LICENSE.txt
%{python3_sitearch}/%{name}/
%{python3_sitearch}/*.pth
%endif

%if 0%{?with_java}
%files -n java-%{octpkg}
%{_javadir}/libnumlj.jar
%{_jnidir}/libnumlj.so
%{_libdir}/%{name}/
%endif

%if 0%{?with_octave}
%files -n octave-%{octpkg}
%{octpkgdir}/packinfo
%{octpkglibdir}/
%endif

%if 0%{?with_perl}
%files -n perl-%{octpkg}
%doc libnuml/*.md
%license libnuml/LICENSE.txt
%{perl_vendorarch}/LibNUML.*
%exclude %dir %{perl_vendorarch}/auto/
%{perl_vendorarch}/auto/libNUML/
%endif

%if 0%{?with_ruby}
%files -n ruby-%{octpkg}
%doc libnuml/*.md
%license libnuml/LICENSE.txt
%{ruby_vendorarchdir}/*.so
%endif

%if 0%{?with_r}
%files -n R-%{octpkg}
%doc libnuml/*.md
%license libnuml/LICENSE.txt
%{_libdir}/R/library/libNUML/
%{_libdir}/libNUML.so
%endif

%if 0%{?with_mono}
%files sharp
%doc libnuml/*.md
%license libnuml/LICENSE.txt
#%%{_monogacdir}/libnumlcsP
%{_monodir}/LibnumlcsP/
%endif

%if 0%{?with_doc}
%files doc
%license libnuml/LICENSE.txt
%doc libnuml/doc/html *.pdf
%endif

%changelog
%autochangelog
