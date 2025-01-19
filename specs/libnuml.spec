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
Version:        1.1.4
Release:        20%{?dist}
URL:            https://github.com/NuML/NuML
Source0:        https://github.com/NuML/NuML/archive/%{commit}/NuML-%{version}.tar.gz
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+

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

Patch0: %{name}-porting_to_python310.patch
Patch1: %{name}-fix_for_swig.patch

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
%autosetup -n NuML-%{version} -N

%if 0%{?with_python}
%if 0%{?python3_version_nodots} > 39
%patch -P 0 -p1 -b .porting_to_python310
%endif
%endif
%patch -P 1 -p1 -b .fix_for_swig

%build
mkdir -p libnuml/build
%cmake3 -B libnuml/build -S libnuml -Wno-dev \
 -DEXTRA_INCLUDE_DIRS:STRING=%{_includedir}/minizip \
%if 0%{?with_python}
 -DWITH_PYTHON:BOOL=ON \
 -DWITH_SWIG:BOOL=ON \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python%{python3_version}$(python3-config --abiflags) \
 -DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{python3_version}$(python3-config --abiflags).so \
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

%make_build -C libnuml/build

%if 0%{?with_doc}
pushd libnuml
doxygen
popd
%endif

####################################################################################################

%install
%make_install -C libnuml/build

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
make test -C libnuml/build
%endif

%files
%doc libnuml/*.md
%license libnuml/LICENSE.txt
%{_libdir}/libnuml.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/cmake/numl-config*.cmake
%{_includedir}/numl/

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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.4-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.4-17
- Rebuilt for Python 3.13

* Sun Feb 04 2024 Antonio Trande <sagitter@fedoraproject.org> - 1.1.4-16
- Exclude ix86 architectures

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 1.1.4-13
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.4-11
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Sandro Mani <manisandro@gmail.com> - 1.1.4-9
- Rebuild (minizip-ng)

* Thu Oct 27 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.1.4-8
- Switch to minizip-ng

* Thu Sep 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.1.4-7
- Patched for Swig-4.1.0 (rhbz#2127978)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.4-5
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.4-2
- Rebuilt for Python 3.10

* Thu May 13 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.1.4-1
- Release 1.1.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2.20201214git50815eb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.1.3-1.20201214git50815eb
- Release 1.1.3

* Fri Jan 15 2021 Than Ngo <than@redhat.com> - 1.1.1-25.20190327gite61f6d5
- Workaround for doxygen crash

* Wed Nov 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.1.1-24.20190327gite61f6d5
- Patched for using Python-3.10 (rhbz#1900660)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-23.20190327gite61f6d5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-22.20190327gite61f6d5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-21.20190327gite61f6d5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20.20190327gite61f6d5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-19.20190327gite61f6d5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-18.20190327gite61f6d5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17.20190327gite61f6d5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-16.20190327gite61f6d5
- Don't hard-code python's abi flags

* Sun May 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.1.1-15.20190327gite61f6d5
- Build commit #e61f6d5
- Obsolete Python2-libnuml

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.1.1-13
- Bundle minizip on fedora 30+ (rhbz#1632187) (upstream bug #466)

* Tue Sep 04 2018 Patrik Novotný <panovotn@redhat.com> - 1.1.1-12
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Sat Sep 01 2018 Antonio Trande <sagitterATfedoraproject.org> - 1.1.1-11
- Deprecate Python2 on fedora 30+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-9
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Antonio Trande <sagitterATfedoraproject.org> - 1.1.1-8
- Rebuild for libsbml-5.17.0
- Add javapackages-tools

* Thu Feb 22 2018 Antonio Trande <sagitterATfedoraproject.org> - 1.1.1-7
- Add gcc gcc-c++ BR

* Thu Feb 15 2018 Antonio Trande <sagitterATfedoraproject.org> - 1.1.1-6
- Fix %%ldconfig_scriptlets for sub-package

* Thu Feb 15 2018 Antonio Trande <sagitterATfedoraproject.org> - 1.1.1-5
- Rebuild for libsbml-5.16.0
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Antonio Trande <sagitterATfedoraproject.org> - 1.1.1-3
- Created a static sub-package

* Fri Sep 29 2017 Antonio Trande <sagitterATfedoraproject.org> - 1.1.1-2
- Created a documentation sub-package
- Java shared library moved into a private lib directory
- Java shared library symlinked from /usr/lib/java

* Thu Sep 28 2017 Antonio Trande <sagitterATfedoraproject.org> - 1.1.1-1
- First package
