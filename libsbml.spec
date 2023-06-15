%bcond_without perl
%bcond_without ruby
%bcond_with    octave
%bcond_without r
%bcond_with    java
%bcond_without python
%bcond_without check

# The build result of docs is different between architectures.
# Also, something is wrong with javascript, and the page is unusable anywa.
# Let's not build the subpackage until the issue is fixed upstream.
%bcond_with doc

# Exclude sharp binding (Error CS0246)
Obsoletes:      libsbml-sharp < 0:5.18.0-20
%ifarch %{mono_arches}
%bcond_with mono
%else
%bcond_with mono
%endif

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
Version:        5.19.0
Release:        26%{?dist}
Summary:        Systems Biology Markup Language library
License:        LGPLv2+
URL:            http://sbml.org/Software/libSBML
Source0:        https://sourceforge.net/projects/sbml/files/%{name}/%{version}/stable/libSBML-%{version}-core-plus-packages-src.tar.gz
Source1:        https://sourceforge.net/projects/sbml/files/%{name}/%{version}/stable/libSBML-%{version}-render-src.zip

# https://bugzilla.redhat.com/show_bug.cgi?id=1632190
Patch0:         %{name}-use-system-minizip-cmake.patch
Patch1:         %{name}-fix_install_libpaths.patch
Patch2:         time-clock.diff
Patch3:         %{name}-fix-jsfile-globs.diff

# formatter was dropped in python3.10. It appears the imported code was just a noop.
Patch4:         %{name}-drop-formatter-import.diff
# Do not use private unittest.TestCase.assert_() method
# (fixes Python 3.11 compatibility, RHBZ#2019426)
#
# https://github.com/sbmlteam/libsbml/pull/178
#
# We need, and can use, only one of the three commits in that PR; the others
# affect files in dev/ that are not present in the PyPI source distribution.
Patch5:         https://github.com/sbmlteam/%{name}/pull/178/commits/b12b7f9372424f5271a838c95605d9946c7ea1fb.patch

Patch6:         %{name}-rhbz_2128592.patch

BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  libxml2-devel
BuildRequires:  expat-devel
BuildRequires:  check-devel
BuildRequires:  minizip-ng-devel
BuildRequires:  swig
BuildRequires:  hostname

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
%autosetup -n libSBML-%{version}-Source -p1
unzip -n %{SOURCE1}

sed -r -i s/DOXYGEN_MAX_VERSION=1.8.11/DOXYGEN_MAX_VERSION=2.0.0/ configure

%if %{with python}
find . -type f -name '*.py' -exec %{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}"  {} \;
python3 -m lib2to3 -f print -w docs/src/filters/
python3 -m lib2to3 -f next -w docs
%endif

grep -e 'This file was automatically generated by SWIG' -r . -l|xargs rm

%if %{with doc}
mkdir build-docs
cp -a $(ls -1|grep -v build-docs) build-docs/
%endif

%build
mkdir -p build
%{set_build_flags}
%cmake3 -B build -DENABLE_{LAYOUT,QUAL,COMP,FBC,RENDER,GROUPS,MULTI}=ON \
       -DCSHARP_COMPILER:FILEPATH=%{_bindir}/mcs \
%if %{with python}
       -DWITH_PYTHON:BOOL=ON \
       -DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python%{python3_version}$(python3-config --abiflags) \
       -DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{python3_version}$(python3-config --abiflags).so \
       -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
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

%make_build -C build
%make_build -C build libsbml.pc

%if %{with doc}
pushd build-docs
%configure --disable-static \
           --with-expat=no \
           --with-libxml=yes \
%if %{with doc}
           --with-doxygen \
%endif
%if %{with python}
           --with-python --with-python-interpreter=%{__python3} \
%endif
           --enable-layout --enable-comp --enable-fbc --enable-qual

cp ../build/src/bindings/python/libsbml-doxygen.py src/bindings/python/
# build is parallelized internally
make docs
%endif

%install
%make_install -C build

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
R CMD INSTALL -l %{buildroot}%{_libdir}/R/library build/src/bindings/r/%{rpkg}_%{version}_R_*.tar.gz
rm -rf %{buildroot}%{_libdir}/R/library/%{rpkg}/R.css
%endif

%if %{with doc}
make -C build-docs install-docs DESTDIR=%{buildroot}
mv %{buildroot}%{_pkgdocdir}-%{version} %{buildroot}%{_pkgdocdir}
%endif

%if %{with ruby}
install -Dm0644 src/bindings/ruby/README.txt %{buildroot}%{_pkgdocdir}/README-ruby.txt
%endif

%if %{with check}
%check
pushd build
# See https://github.com/sbmlteam/libsbml/issues/234
ctest --force-new-ctest-process -VV \
        -E "test_ruby_binding|test_perl_binding"
popd
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
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.19.0-26
- Rebuilt for Python 3.12

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 5.19.0-25
- R-maint-sig mass rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.19.0-23
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Tue Nov 15 2022 Sandro Mani <manisandro@gmail.com> - 5.19.0-22
- Rebuild (minizip-ng)

* Thu Oct 27 2022 Antonio Trande <sagitter@fedoraproject.org> - 5.19.0-21
- Switch to minizip-ng rhbz#2138146

* Thu Sep 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 5.19.0-20
- Patched for rhbz#2128592

* Mon Sep 05 2022 Iñaki Úcar <iucar@fedoraproject.org> - 5.19.0-19
- Rebuild for R 4.2.1

* Wed Aug 03 2022 Antonio Trande <sagitter@fedoraproject.org> - 5.19.0-18
- Disable Java support

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.19.0-16
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Antonio Trande <sagitter@fedoraproject.org> - 5.19.0-15
- Skip Perl binding test

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.19.0-14
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.19.0-13
- Perl 5.36 rebuild

* Tue Feb 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 5.19.0-12
- Fix Java compatibility (rhbz#2056614)

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.19.0-11
- F-36: rebuild against ruby31

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 5.19.0-9
- Fix Python 3.11 with upstream PR#178 (fix RHBZ#2019426)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Antonio Trande <sagitter@fedoraproject.org> - 5.19.0-7
- Rebuilt for R-4.0 (rhbz#1973622)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.19.0-6
- Rebuilt for Python 3.10

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.19.0-5
- Perl 5.34 rebuild

* Tue Feb 09 2021 Miro Hrončok <mhroncok@redhat.com> - 5.19.0-4
- Rebuilt for minizip 3.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.19.0-2
- Fix build under Python 3.10 (#1913346)

* Thu Jan  7 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.19.0-1
- Update to latest version

* Wed Jan 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 5.18.0-21
- Disable documentation build with Python-3.10 (rhbz#1913346)

* Sat Nov 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.18.0-20
- Modify patch #3 (rhbz#1897107)

* Fri Nov 13 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.18.0-19
- Porting to Python-3.10 (rhbz#1897107)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.18.0-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.18.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.18.0-16
- Enable cmake_in_source_build (rhbz#1859845)

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.18.0-15
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.18.0-14
- Rebuilt for Python 3.9

* Sat May 16 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.18.0-13
- Do not link to libpython

* Sat May 16 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.18.0-12
- Some adjustments

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.18.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.18.0-10
- F-32: rebuild against ruby27

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.18.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.18.0-8
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 5.18.0-7
- Remove obsolete requirements for %%post/%%postun scriptlets

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.18.0-5
- Fix build under python3.8 (#1718374)
- Make Obsoletes versioned

* Tue Jun 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.18.0-4
- Perl 5.30 re-rebuild updated packages

* Mon Jun 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 5.18.0-3
- Use abiflags

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.18.0-2
- Perl 5.30 rebuild

* Tue Apr 30 2019 Antonio Trande <sagitter@fedoraproject.org> - 5.18.0-1
- Update to 5.18.0
- Drop python2-libsbml

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Vít Ondruch <vondruch@redhat.com> - 5.17.0-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Thu Nov 15 2018 Orion Poplawski <orion@cora.nwra.com> - 5.17.0-11
- Rebuild for octave 4.4

* Mon Sep 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.17.0-10
- Bundle minizip on fedora 30+ (rhbz#1632190) (upstream bug #466)

* Tue Sep 04 2018 Pavel Raiskup <praiskup@redhat.com> - 5.17.0-9
- rebuild against minizip-compat-devel, rhbz#1609830, rhbz#1615381

* Sun Sep 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.17.0-8
- Deprecate python2 on fedora 30+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 5.17.0-6
- Perl 5.28 rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.17.0-5
- Perl 5.28 rebuild

* Thu Jun 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.17.0-4
- Fix upstream bug #463

* Wed Jun 27 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.17.0-3
- Fix Python37 compiling error (upstream bug #461) (bz#1594498)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.17.0-2
- Rebuilt for Python 3.7

* Fri Jun 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.17.0-1
- Update to 5.17.0

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 5.16.0-9
- explicitly BR: javapackages-tools so that we have java macros

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 5.16.0-8
- rebuild for R 3.5.0

* Fri Apr 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.16.0-7
- Minor fix

* Fri Apr 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.16.0-6
- Provide the static library (required by other packages)
- Add Provides tag

* Wed Mar 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.16.0-5
- Obsoletes octave-SBML < 5.15.0

* Sat Feb 10 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.16.0-4
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.16.0-2
- F-28: rebuild for ruby25

* Fri Dec 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 5.16.0-1
- Update to 5.16.0

* Thu Oct 26 2017 Vít Ondruch <vondruch@redhat.com> - 5.15.0-7
- Drop the explicit dependnecy on rubypick.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.15.0-4
- Perl 5.26 rebuild

* Sat Apr 15 2017 Antonio Trande <sagitter@fedoraproject.org> - 5.15.0-3
- Undo latest change
- Does not provide static library files

* Fri Apr 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 5.15.0-2
- Provide static library files

* Tue Apr 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 5.15.0-1
- Update to 5.15.0 (stable)
- Disable Octave binding (bugged)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Vít Ondruch <vondruch@redhat.com> - 5.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.14.0-2
- Rebuild for Python 3.6

* Thu Dec  8 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.14.0-1
- Update to latest (experimental) release
- Disable test_csharp_bindings_full on i686 (#1402549)

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com>
- Rebuild for octave 4.2

* Tue Aug 16 2016 Antonio Trande <sagitter@fedoraproject.org> - 5.13.0-5
- Rebuild for Python 3.5.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.13.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.13.0-3
- Perl 5.24 rebuild

* Mon Apr 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 5.13.0-2
- Fixed BR packages for Perl

* Mon Apr 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 5.13.0-1
- Update to 5.13.0 (stable)
- Removed _hardened_build definition for F <23
- Old patch dropped

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Antonio Trande <sagitter@fedoraproject.org> - 5.12.0-6
- Python2 sub-package renamed

* Thu Jan 21 2016 Antonio Trande <sagitter@fedoraproject.org> - 5.12.0-5
- Defined rubypick as BuildRequires for ruby-SBML
- Defined Ruby paths

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 5.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Sat Dec 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.12.0-3
- Tests enabled

* Fri Dec 11 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.12.0-2
- Try to build without clang

* Sat Nov 14 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.12.0-1
- Update to 5.12.0
- Added patch(#2) for the formatter with Python3.5

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.6-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.6-9
- Rebuilt again

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.6-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Nov 01 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.6-7
- Tests enabled except for Ruby
- clang compiler not used on s390 s390x ppc64 ppc64le
- Hardened builds on <F23

* Thu Oct 29 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.6-6
- perl-Test required on F24

* Wed Oct 28 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.6-5
- Rebuild for cmake upgrade
- Disabled Perl and Ruby bindings test

* Mon Jul 27 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.6-4
- Disabled 'parallel make' for language bindings

* Mon Jul 27 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.6-3
- Compiled the core-plus source archive

* Thu Jul 23 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.6-2
- Some tests disabled

* Thu Jul 23 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.6-1
- Bump to the release 5.11.6 (experimental)

* Wed Jul 22 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.13.20150528svn22272
- Tests disabled on PPC s390x arches

* Sat Jul 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.12.20150528svn22272
- Tests disabled on ARM aarch64

* Tue Jul  7 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@laptop> - 5.11.5-0.11.20150528svn22272
- Rebuild for octave 4.0.0

* Sat Jun 20 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.10.20150528svn22272
- Enabled tests of binding libraries

* Thu Jun 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.9.20150528svn22272
- All tests enabled

* Thu Jun 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.8.20150528svn22272
- Excluded failed tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.5-0.7.20150528svn22272
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.11.5-0.6.20150528svn22272
- Perl 5.22 rebuild

* Thu Jun 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.5.20150528svn22272
- Rebuild again

* Thu Jun 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.4.20150528svn22272
- Performed all tests in F23

* Wed Jun 03 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.3.20150528svn22272
- Exclude 'test_csharp_bindings_full' and 'test_ruby_binding' test in <F23

* Wed Jun 03 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.2.20150528svn22272
- Exclude 'test_csharp_bindings_full' test in ARM
- Use clang++ in >F22

* Thu May 28 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.5-0.1.20150528svn22272
- Update to svn pre-release #22272
- clang++ set as compiler on >F22
- Set C# compiler on >F22

* Thu May 28 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.11.4-1
- Update to 5.11.4
- clang++ set as compiler

* Sat Feb 21 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-11
- Disable -java and -mono on arch: they crash in tests

* Fri Feb 06 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-10
- Rename -docs to -doc, run make unparallelized

* Wed Feb 04 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-9
- Apply upstream patch for arm test failures

* Tue Feb 03 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-8
- Fix things found in review (macro in comment, R:mono-core, %%doc
  duplication, macro usage)

* Mon Jan 26 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-7
- Allow newer doxygen

* Fri Jan 09 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-6
- Enable many many subpackages

* Tue Jan 06 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-5
- Unbundle minizip

* Wed Dec 17 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-4
- Do not build on arm

* Sat Dec 13 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-3
- Convert to hybrid cmake (main part) / make (docs).

* Fri Dec 12 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-2
- docs subpackage is no arch, remove %%{_isa} from dependency.

* Tue Dec 09 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.11.0-1
- Initial packaging.

