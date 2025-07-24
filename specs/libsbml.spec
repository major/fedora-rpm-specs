%bcond perl   1
%bcond ruby   1
%bcond octave 0
%bcond r      1
%bcond java   0
%bcond python 1
%bcond check  1

# The build result of docs is different between architectures.
# Also, something is wrong with javascript, so the page is unusable anyway.
# Let's not build the subpackage until the issue is fixed upstream.
%bcond doc    0

# Exclude sharp binding (Error CS0246)
Obsoletes:      libsbml-sharp < 0:5.18.0-20
%bcond mono   0

# those have special requirements, the rest follows main package name
%global octpkg  SBML
%global perlpkg LibSBML
%global rubypkg SBML
%global rpkg    libSBML

%if %{with octave}
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$
%endif

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

Name:           libsbml
Version:        5.20.5
Release:        %autorelease
Summary:        Systems Biology Markup Language library
License:        LGPL-2.1-or-later
URL:            https://sbml.org/Software/libSBML
Source:         https://github.com/sbmlteam/libsbml/archive/v%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=1632190
Patch:          0001-Use-system-minizip-cmake.patch
Patch:          0002-Fix-install-libpaths.patch
Patch:          0003-Fix-jsfile-globs.patch
Patch:          0004-Add-missing-include-to-fix-build-with-newer-gcc.patch
# Fix build failure with libsbml-5.20.4
Patch:          0005-cmake-do-not-skip-building-of-static-libs.patch

BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  libxml2-devel
BuildRequires:  expat-devel
BuildRequires:  check-devel
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  swig
BuildRequires:  hostname
BuildRequires:  gcc-c++

# Python2 is no longer supported
Obsoletes:      python2-%{name} < 0:5.18
# Disable Java support
Obsoletes:      java-%{name} < 0:5.19.0-18

%if %{without doc}
Obsoletes:      %{name}-doc < 0:5.18.0-21
%endif

%description
LibSBML is an open-source programming library designed to
read, write, manipulate, translate, and validate SBML files and data
streams.  It is not an application itself (though it does come with
example programs), but rather a library you can embed in other
applications.

LibSBML %{version} understands SBML Level 3 Version 1 and older,
as well as the draft SBML Level 2 Layout proposal by Gauges, Rost,
Sahle and Wegner.  It’s written in ISO C and C++ but can also be
used from C#, Java, MATLAB, Octave, PERL, Python, and Ruby.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use libSBML.

%if %{with python}
%package -n python3-%{name}
BuildRequires:  python3-devel
Summary:        Python bindings for libSBML
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package contains %{summary}.
%endif

%if %{with perl}
%package -n perl-%{perlpkg}
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-Test
Summary:        PERL bindings for libSBML
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n perl-%{perlpkg}
This package contains %{summary}.
%endif

%if %{with ruby}
%package -n ruby-%{rubypkg}
BuildRequires:  ruby-devel
Requires:       ruby(release)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       ruby(%{rubypkg}) = %{version}
Summary:        Ruby bindings for libSBML

%description -n ruby-%{rubypkg}
This package contains %{summary}.
%endif

%if %{with java}
%package -n java-%{name}
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
Requires:       java-headless
Requires:       jpackage-utils
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Java bindings for libSBML

%description -n java-%{name}
This package contains %{summary}.
%endif

%if %{with octave}
%package -n octave-%{octpkg}
BuildRequires:  octave-devel
Requires:       octave(api) = %{octave_api}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Octave bindings for libSBML

%description -n octave-%{octpkg}
This package contains %{summary}.
%endif

%if %{with r}
%package -n R-%{rpkg}
BuildRequires:  R-devel
BuildRequires:  R-core-devel
BuildRequires:  tex(latex)
Requires:       R-core
Summary:        R bindings for libSBML
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n R-%{rpkg}
This package contains %{summary}.
%endif

%if %{with mono}
%package sharp
BuildRequires:  mono-core
BuildRequires:  xerces-c-devel, libxml2-devel, expat-devel
Summary:        C# bindings for libSBML
Requires:       mono-core
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description sharp
This package contains %{summary}.
%endif

%if %{with doc}
%package        doc
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
BuildRequires:  graphviz
BuildRequires:  make
Summary:        API documentation for %{name}
Requires:       %{name} = %{version}-%{release}

##Granted  exception temporarily
##http://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries
Provides:       bundled(jquery)
BuildArch:      noarch

%description    doc
This package contains %{summary}.
%endif

%prep
%autosetup -p1

%if %{with python}
find . -type f -name '*.py' -exec %{python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{python3}"  {} \;
%endif

grep -e 'This file was automatically generated by SWIG' -r -l . | xargs --no-run-if-empty rm -v

%if %{with doc}
mkdir build-docs
cp -a $(ls -1|grep -v build-docs) build-docs/
%endif

sed -r -i 's|(set\(PERL_PACKAGE_INSTALL_DIR.*/perl5)/site_perl.*\)|\1/vendor_perl)|' src/bindings/perl/CMakeLists.txt
sed -r -i 's|(set\(RUBY_PACKAGE_INSTALL_DIR.*/ruby)/site_ruby.*\)|\1/vendor_ruby)|' src/bindings/ruby/CMakeLists.txt

%build
# silence some warnings which are only relevant to upstream developers
export CXXFLAGS="$CXXFLAGS -Wno-overloaded-virtual -Wno-unused-variable -Wno-unused-but-set-variable -Wno-switch"

%cmake -DENABLE_{LAYOUT,QUAL,COMP,FBC,RENDER,GROUPS,MULTI}=ON \
       -DCSHARP_COMPILER:FILEPATH=%{_bindir}/mcs \
%if %{with python}
       -DWITH_PYTHON:BOOL=ON \
       -DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python%{python3_version}$(python3-config --abiflags) \
       -DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{python3_version}$(python3-config --abiflags).so \
       -DPYTHON_EXECUTABLE:FILEPATH=%{python3} \
       -DPYTHON_USE_DYNAMIC_LOOKUP:BOOL=ON \
%endif
%if %{with perl}
       -DWITH_PERL:BOOL=ON \
       -DPERL_EXECUTABLE:FILEPATH=%{_bindir}/perl \
       -DPERL_INCLUDE_PATH:PATH=%{_libdir}/perl5/CORE \
       -DPERL_LIBRARY:FILEPATH=%{_libdir}/libperl.so \
%endif
%if %{with ruby}
       -DWITH_RUBY:BOOL=ON \
       -DRUBY_SITEARCH_DIR:PATH=%{ruby_sitearchdir} \
       -DRUBY_SITELIB_DIR:PATH=%{ruby_sitelibdir} \
       -DRUBY_VENDORARCH_DIR:PATH=%{ruby_vendorarchdir} \
       -DRUBY_VENDORLIB_DIR:PATH=%{ruby_vendorlibdir} \
       -DRUBY_HAS_VENDOR_RUBY:BOOL=ON \
%endif
%if %{with java}
       -DWITH_JAVA:BOOL=ON \
       -DWITH_JAVASCRIPT:BOOL=OFF \
       -DWITH_SWIG:BOOL=ON \
       -DJAVA_COMPATIBILITY=1.7 \
%endif
%if %{with octave}
       -DWITH_OCTAVE:BOOL=ON \
%endif
%if %{with r}
       -DWITH_R:BOOL=ON \
       -DR_INCLUDE_DIRS:PATH=%{_includedir}/R \
%endif
%if %{with mono}
       -DWITH_CSHARP:BOOL=ON \
       -DWITH_XERCES:BOOL=OFF \
       -DWITH_LIBXML:BOOL=ON \
       -DWITH_EXPAT:BOOL=OFF \
       -DWITH_SWIG:BOOL=ON \
%endif
%if %{with check}
       -DWITH_CHECK=ON \
%endif
       -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
       -DCMAKE_BUILD_TYPE:STRING=Release \
       -DCMAKE_SKIP_RPATH:BOOL=YES \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
       -DWITH_MATLAB:BOOL=OFF \
       -Wno-dev -DEXIT_ON_ERROR:BOOL=ON

%cmake_build

%if %{with doc}
pushd build-docs
%configure --disable-static \
           --with-expat=no \
           --with-libxml=yes \
%if %{with doc}
           --with-doxygen \
%endif
%if %{with python}
           --with-python --with-python-interpreter=%{python3} \
%endif
           --enable-layout --enable-comp --enable-fbc --enable-qual

cp -p src/bindings/python/libsbml-doxygen.py src/bindings/python/
# build is internally parallelized
make docs
%endif

%install
%cmake_install

##This directory provides just some txt documentation files
rm -rf %{buildroot}%{_datadir}/%{name}

%if %{with octave}
chmod 0755 %{buildroot}%{octpkglibdir}/*.mex
mkdir -p %{buildroot}%{octpkgdir}/packinfo
install -pm 644 COPYING.txt README* %{buildroot}%{octpkgdir}/packinfo
%endif

%if %{with java}
mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_jnidir}
mv %{buildroot}%{_javadir}/libsbmlj.jar %{buildroot}%{_jnidir}/
mv %{buildroot}%{_libdir}/libsbmlj.so %{buildroot}%{_libdir}/%{name}/
%endif

%if %{with r}
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL -l %{buildroot}%{_libdir}/R/library %_vpath_builddir/src/bindings/r/%{rpkg}_%{version}_R_*.tar.gz
rm -rf %{buildroot}%{_libdir}/R/library/%{rpkg}/R.css
%endif

%if %{with doc}
make -C build-docs install-docs DESTDIR=%{buildroot}
mv %{buildroot}%{_pkgdocdir}-%{version} %{buildroot}%{_pkgdocdir}
%endif

%if %{with ruby}
install -Dm0644 src/bindings/ruby/README.txt %{buildroot}%{_pkgdocdir}/README-ruby.txt
%endif

# WTF?
rm -fv %buildroot/%{_datadir}/cmake/Modules/Find{BZ2,LIBXML,ZLIB}.cmake

%if %{with check}
%check
# See https://github.com/sbmlteam/libsbml/issues/234
%ctest -E "test_ruby_binding|test_perl_binding"
%endif

%files
%license COPYING.txt LICENSE.txt
%doc README* NEWS.txt FUNDING.txt
%{_libdir}/*.so.*
%if %{with doc}
%exclude %{_pkgdocdir}/*-api
%endif

%files devel
%{_includedir}/sbml/
%{_libdir}/*.so
%{_libdir}/libsbml-static.a
%{_libdir}/cmake/sbml-*.cmake
%{_datadir}/cmake/Modules/FindLIBSBML.cmake
%{_libdir}/pkgconfig/%{name}.pc

%if %{with python}
%files -n python3-%{name}
%license COPYING.txt LICENSE.txt
%{python3_sitearch}/%{name}.pth
%{python3_sitearch}/%{name}
%endif

%if %{with perl}
%files -n perl-%{perlpkg}
%license COPYING.txt LICENSE.txt
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%endif

%if %{with ruby}
%files -n ruby-%{rubypkg}
%license COPYING.txt LICENSE.txt
%doc %{_pkgdocdir}/README-ruby.txt
%{ruby_vendorarchdir}/*.so
%endif

%if %{with java}
%files -n java-%{name}
%license COPYING.txt LICENSE.txt
%{_jnidir}/libsbmlj.jar
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libsbmlj.so
%endif

%if %{with octave}
%files -n octave-%{octpkg}
%dir %{octpkgdir}
%{octpkgdir}/packinfo/COPYING.txt
%{octpkgdir}/packinfo/README*
%{octpkglibdir}/
%endif

%if %{with r}
%files -n R-%{rpkg}
%license COPYING.txt LICENSE.txt
%{_libdir}/R/library/%{rpkg}/
%endif

%if %{with mono}
%files sharp
%license COPYING.txt LICENSE.txt
%{_monodir}/libsbmlcsP/
%endif

%if %{with doc}
%files doc
%{_pkgdocdir}/cpp-api
# Binding docs are here too, as a compromise. Making a separate
# python-libsbml-doc seems overkill, but including them in an arched
# package is not nice.
%{_pkgdocdir}/python-api
%endif

%changelog
%autochangelog
