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
Version:        2.0.32
Release:        14%{?dist}
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

Patch2: %{name}-2.0-Fixes-for-swig-4.1.0-macro-definition-correction.patch

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

# Needed for SWIG 4.1.0
%patch -P 2 -p1 -b .fix_macro_definition

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
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.32-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2:2.0.32-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.32-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2:2.0.32-11
- Rebuilt for Python 3.13

* Sun Feb 04 2024 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.32-10
- Exclude ix86 architectures

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2:2.0.32-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2:2.0.32-4
- Fixes for SWIG 4.1.0 macro definition correction (BZ#2127982)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2:2.0.32-2
- Rebuilt for Python 3.11

* Sat Jun 11 2022 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.32-1
- Release 2.0.32

* Fri Apr 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.31-1
- Release 2.0.31

* Thu Apr 07 2022 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.30-1
- Release 2.0.30

* Sat Mar 12 2022 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.29-1
- Release 2.0.29

* Thu Feb 17 2022 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.27-1
- Release 2.0.27

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.26-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.26-0.1
- Pre-Release 2.0.26

* Sat Aug 07 2021 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.25-0.1
- Pre-Release 2.0.25

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.22-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.22-0.1
- Pre-Release 2.0.22

* Sat Jun 26 2021 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.21-0.1
- Pre-Release 2.0.21

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2:2.0.20-0.2
- Rebuilt for Python 3.10

* Tue May 25 2021 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.20-0.1
- Pre-Release 2.0.20

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2:2.0.19-0.2
- Perl 5.34 rebuild

* Thu May 13 2021 Antonio Trande <sagitter@fedoraproject.org> - 2:2.0.19-0.1
- Pre-Release 2.0.19

* Wed Mar 31 2021 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-17
- Add gcc BR

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-15
- Rebuild for libnuml-1.1.3

* Thu Jan 07 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.4.4-14
- F-34: rebuild against ruby 3.0

* Fri Nov 13 2020 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-13
- Porting to Python-3.10 (rhbz#1897111)

* Tue Aug 04 2020 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Enable cmake_in_source_build
- Disable Java binding

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.4.4-11
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.4.4-10
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.4.4-8
- F-32: rebuild against ruby27

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.4.4-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.4.4-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.4.4-4
- Perl 5.30 rebuild

* Wed May 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-3
- Use Python3 abiflags

* Sun May 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-2
- Rebuild for libsbml-5.18.0
- Obsolete python2-libsedml

* Fri Mar 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-1
- Release 0.4.4
- Obsolete libsedml-sharp on fedora 30+/pp64* (rhbz#1588734,#1686738)
- Disable -Werror=format-security for ruby- builds (upstream bug #55)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.4.3-19
- F-30: rebuild against ruby26
- Disable parallel build for mono bindings (build fails randomly on s390x)

* Mon Sep 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-18
- Bundle minizip on fedora 30+ (rhbz#1632191) (upstream bug #466)

* Tue Sep 04 2018 Patrik Novotný <panovotn@redhat.com> - 1:0.4.3-17
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Sun Sep 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-16
- Deprecate python2 on fedora 30+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 1:0.4.3-14
- Perl 5.28 rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.4.3-13
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.4.3-12
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-11
- Rebuild for libsbml-5.17.0

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1:0.4.3-10
- add minizip-devel as explicit BR, probably a broken .pc file in something else though

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1:0.4.3-9
- rebuild for R 3.5.0

* Thu Feb 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-8
- Rebuild for libsbml-5.16.0
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.4.3-6
- F-28: rebuild for ruby25

* Sun Dec 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-5
- Rebuild for libsbml-5.16.0

* Wed Oct 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-4
- Split off the static library

* Wed Oct 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-3
- Fix dependency's Epoch

* Wed Oct 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-2
- Fix dependencies

* Sun Oct 01 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-1
- Update to 0.4.3
- Set new Epoch
- Add new dependency (libnuml)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-21
- Perl 5.26 rebuild

* Fri Apr 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-20
- Rebuild for libsbml-5.15.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-18
- F-26: rebuild for ruby24

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-17
- Rebuild for Python 3.6

* Tue Aug 16 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-16
- Rebuild for Python 3.5.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-15
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-14
- Perl 5.24 rebuild

* Tue Apr 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-13
- Rebuild for libSBML 5.13.0

* Sat Apr 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-12
- Fixed Python2 sub-package
- Documentation/License files moved to octpkgdir/packinfo
 -Added post/postun/preun scriptlets for Octave sub-package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Sat Dec 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-9
- Rebuilt with GCC-5.3
- Added python-provides

* Sat Nov 14 2015 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-8
- Rebuilt for libsbml-5.12.0 and Python3.5

* Wed Nov 11 2015 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-7
- Set manually CC/CXX variable

* Tue Nov 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-6
- Rebuilt again

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Nov 01 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.1-4
- Built with clang++ on aarch64

* Sun Nov 01 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.1-3
- Hardened builds on <F23

* Sat Sep 19 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.1-2
- Disabled C++ namespaces (Bug2188 on copasi bug tracker)

* Fri Sep 18 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.1-1
- Update to 0.3.1
- Enabled tests

* Sun Jul 26 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-13.20150422git235bb5
- Rebuild after libsbml update

* Fri Jun 19 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-12.20150422git235bb5
- Debug undefined references
- Built with clang on F23 64bit

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11.20150422git235bb5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-10.20150422git235bb5
- Fixed octpkg macro

* Thu Jun 11 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-9.20150422git235bb5
- Added missing linkage to libsbml
- Fixed Python variables

* Mon Jun 08 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-8.20150422git235bb5
- Python2 package is named python-libsedml
- Forced same documentation directory for all sub-packages
- Make symlink between R libraries

* Fri Jun 05 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-7.20150422git235bb5
- Description improved
- Sub-packages main name changed to libsedml for Python, Java
- Packaged Python3 bindings

* Fri Jun 05 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-6.20150422git235bb5
- Set CSHARP compiler on F23

* Fri May 29 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-5.20150422git235bb5
- Update to commit 235bb5

* Mon Feb 02 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-4.20141230gitb455cd
- Set installation directory of the java library

* Fri Jan 09 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-3.20141230gitb455cd
- Package name modified

* Wed Dec 31 2014 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-2.20141230gitb455cd
- Excluded packaging of static file

* Tue Dec 30 2014 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-1.20141230gitb455cd
- Update to the commit fb91ad (post-release 0.3.0)

* Sun Dec 28 2014 Antonio Trande <sagitter@fedoraproject.org> - 5.11.0-1
- First package

