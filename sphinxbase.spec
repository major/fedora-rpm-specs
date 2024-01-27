%global extraver prealpha

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:           sphinxbase
Version:        5
Release:        0.18.%{extraver}%{?dist}
Epoch:          1
Summary:        Common library for CMU Sphinx voice recognition products

License:        BSD
URL:            http://cmusphinx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}%{extraver}.tar.gz

# https://github.com/cmusphinx/sphinxbase/pull/72
Patch0:         sphinxbase-5prealpha-fix-doxy2swig.patch

# https://github.com/cmusphinx/sphinxbase/pull/90
Patch1:         sphinxbase-5prealpha-stdbool.patch

# Fix code for SWIG 4.2.0
Patch2:         sphinxbase-swig-4.2.0-array-typemap-fix.patch

BuildRequires: make
BuildRequires:  autoconf-archive
BuildRequires:  bison
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  libtool
BuildRequires:  %{blaslib}-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Pod::Usage)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig

%description
Sphinxbase is a common library for CMU Sphinx voice recognition products.
This package does not provide voice recognition by itself.

%package devel
Summary:        Header and other development files for sphinxbase
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pkgconfig(libpulse)
Provides:       bundled(jquery)

%description devel
Header files and other development files for sphinxbase.

%package libs
Summary:        Libraries for sphinxbase

%description libs
The libraries for sphinxbase.

%package -n python3-sphinxbase
%{?python_provide:%python_provide python3-sphinxbase}
Summary:        Python interface to sphinxbase
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-sphinxbase
Python 3 interface to sphinxbase.

%prep
%setup -q -n sphinxbase-%{version}%{extraver}

# Use blaslib instead of the blas reference implementation
sed -ri 's/blas|lapack/%{blaslib}/' configure.ac

# Use system-provided ax_python_devel.m4
rm -f m4/ax_python_devel.m4

# Regenerate configure files due to blaslib and m4 changes
autoreconf -fi

# Fix encoding
iconv -f ISO8859-1 -t UTF-8 -o AUTHORS.new AUTHORS
touch -r AUTHORS.new AUTHORS
mv -f AUTHORS.new AUTHORS

# Force code generation with newer versions of Cython and bison
rm -f python/sphinxbase.c src/libsphinxbase/lm/jsgf_parser.{c,h}

# Improve auto requires detection
for f in src/sphinx_jsgf2fsg/fsg2dot.pl; do
  sed -r 's|/usr/bin/env (.*)|/usr/bin/\1|' $f > $f.new
  touch -r $f $f.new
  mv -f $f.new $f
done

%patch0 -p1 -b .fix-doxy2swig
%patch1 -p1 -b .stdbool
%patch2 -p1 -b .swig420

%build
export CPPFLAGS="-I %{_includedir}/%{blaslib}"
export PYTHON="python3"
%configure --disable-static --with-python=%{__python3}

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g.*\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# Build the programs and libraries
make %{?_smp_mflags}

# Some private libs are marked as nonprivate in the pkgconfig file
extralibs=$(sed -n 's/^Libs:.*-lm \(.*\)/\1/p' sphinxbase.pc | sed 's/  / /g')
sed -e 's/^\(libs=".*-lm\).*/\1"/' \
    -e 's/^\(Libs:.*-lm\).*/\1/' \
    -e "s/^Libs\.private.*/& $extralibs/" \
    -i sphinxbase.pc

# Build the man pages
cd doc
export LD_LIBRARY_PATH=../src/libsphinxbase/.libs:../src/libsphinxad/.libs
for prog in sphinx_cepview sphinx_fe; do
  perl args2man.pl ../src/${prog}/${prog} < ${prog}.1.in > ${prog}.1
done
perl args2man.pl ../src/sphinx_adtools/sphinx_pitch < sphinx_pitch.1.in > sphinx_pitch.1

%install
# Install the binaries and libraries
mkdir -p %{buildroot}%{python3_sitearch}
%make_install

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/*.1 %{buildroot}%{_mandir}/man1

# Remove libtool archives
rm -f %{buildroot}%{python3_sitearch}/sphinxbase/*.la
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%doc doc/html
%{_includedir}/sphinxbase/
%{_libdir}/libsphinxad.so
%{_libdir}/libsphinxbase.so
%{_libdir}/pkgconfig/sphinxbase.pc
%{_datadir}/sphinxbase/

%files libs
%doc AUTHORS NEWS README
%license LICENSE
%{_libdir}/libsphinxad.so.3*
%{_libdir}/libsphinxbase.so.3*

%files -n python3-sphinxbase
%{python3_sitearch}/sphinxbase

%changelog
* Thu Jan 25 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1:5-0.18.prealpha
- Fix for SWIG 4.2.0 update (BZ #2260324)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.17.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1:5-0.16.prealpha
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.15.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.14.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:5-0.13.prealpha
- Rebuilt for Python 3.11

* Fri Feb 11 2022 W. Michael Petullo <mike@flyn.org> - 1:5-0.13.prealpha
- Patch to remove stdbool.h conflict (BZ #2049678)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.12.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.11.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:5-0.10.prealpha
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.9.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1:5-0.8.prealpha
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 W. Michael Petullo <mike@flyn.org> - 1:5-0.7.prealpha
- Fix errant use of python_sitearch macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.6.prealpha
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.5.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:5-0.4.prealpha
- Rebuilt for Python 3.9

* Thu Feb 13 2020 W. Michael Petullo <mike@flyn.org> - 1:5-0.3.prealpha
- Fix doxy2swig with Python 3.9, https://bugzilla.redhat.com/show_bug.cgi?id=1793503

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5-0.2.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 W. Michael Petullo <mike@flyn.org> - 1:5-0.1.prealpha
- More work to switch to Python 3
- Use %%make_install
- Remove %%ldconfig_scriptlets
- More specific glob in %%{python3_sitearch}
- Move prealpha and make use of epoch
- Use epoch in requires
- Remove remaining .la file
- More specific globbing of libraries

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5prealpha-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Miro Hrončok <mhroncok@redhat.com> - 5prealpha-4
- Switch to Python 3

* Thu Aug 09 2018 W. Michael Petullo <mike@flyn.org> - 5prealpha-3
- Remove --disable-rpath after noticing warning from ./configure
- Add autoconf-archive to BuildRequires

* Thu Aug 09 2018 W. Michael Petullo <mike@flyn.org> - 5prealpha-2
- Add swig to BuildRequires

* Sun Jul 22 2018 W. Michael Petullo <mike@flyn.org> - 5prealpha-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 0.8-20
- Build with /usr/bin/python2 instead of /usr/bin/python

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-18
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-17
- Python 2 binary package renamed to python2-sphinxbase
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 16 2017 Jerry James <loganjerry@gmail.com> - 0.8-16
- Link with openblas instead of atlas

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Jerry James <loganjerry@gmail.com> - 0.8-9
- Link with atlas instead of the reference blas implementation
- Add Provides: bundled(jquery)
- Fix private libs listed as nonprivate in the pkgconfig file
- Minor spec file cleanups

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.8-5
- Perl 5.18 rebuild

* Fri Mar 29 2013 Jerry James <loganjerry@gmail.com> - 0.8-4
- Different approach to the -largefile patch to fix problems with the original
- Drop -aarch64 patch since we now run autoreconf
- Add -uninit patch to fix bogus lm scores
- Add -doxygen patch to fix some broken doxygen comments

* Thu Mar 28 2013 Jerry James <loganjerry@gmail.com> - 0.8-3
- Add -largefile patch to get large file support
- Add -aarch64 patch (bz 926565)

* Mon Feb 18 2013 Jerry James <loganjerry@gmail.com> - 0.8-2
- Add perl(Pod::Usage) BR

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Jerry James <loganjerry@gmail.com> - 0.8-1
- New upstream release
- Drop patches; no longer necessary

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 0.7-4
- Rebuild for bz 772699

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.7-3
- Rebuild for GCC 4.7
- Fix a typo in the filter

* Fri Jul 15 2011 Jerry James <loganjerry@gmail.com> - 0.7-2
- Use RPM 4.9's new filter scheme to remove bogus provides
- Minor spec file cleanups

* Tue Apr 19 2011 Jerry James <loganjerry@gmail.com> - 0.7-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- New upstream release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Nov 20 2009 Jerry James <loganjerry@gmail.com> - 0.4.1-2
- Update python BRs for Rawhide

* Mon Jun  1 2009 Jerry James <loganjerry@gmail.com> - 0.4.1-1
- Initial RPM
