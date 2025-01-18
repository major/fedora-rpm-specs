# Do we generate the data-files?
%bcond_without mathinit

# Are licenses packaged using %%license?
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%bcond_without	license_dir
%else
%bcond_with	license_dir
%endif

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           arprec
Version:        2.2.19
Release:        24%{?dist}
Summary:        Software package for performing arbitrary precision arithmetic

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://crd.lbl.gov/~dhbailey/mpdist
Source0:        %{url}/%{name}-%{version}.tar.gz
Source1:        %{url}/BSD-LBNL-License.doc

Patch0:         arprec-2.2.19-fix_istream_logic.patch

BuildRequires:  gcc-c++
BuildRequires:  catdoc
BuildRequires:  chrpath
BuildRequires:  gcc-gfortran
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  qd-devel

%description
ARPREC is a software package for performing arbitrary precision
arithmetic.  It consists of a revision and extension of Bailey's
earlier MPFUN package, enhanced with special IEEE numerical
techniques.  Features include:

  * Written in C++ for broad portability and fast execution.

  * Includes C++ and Fortran 90/95 interfaces based on custom data-types
    and operator/function overloading, which permit the library to be
    used with only minor modifications for many conventional C++ and
    Fortran-90 programs.

  * Includes all of the usual arithmetic operations, as well as many
    transcendental functions, including cos, sin, tan, arccos, arcsin,
    arctan, exp, log, log10, erf, gamma and Bessel functions.

  * Supports three arbitrary precision data-types: mp_real, mp_int
    and mp_complex.

  * Supports many mixed-mode operations between arbitrary precision
    variables or constants and conventional variables or constants.

  * Includes special library routines, incorporating advanced
    algorithms for extra-high precision (above 1000 digits) computation.

  * Includes a number of sample application programs, including programs
    for quadrature (numerical definite integrals), PLSQ (integer relation
    finding) and polynomial root finding.

  * Includes the "Experimental Mathematician's Toolkit".  This is a
    self-contained interactive program that performs many operations
    typical of modern experimental mathematics, including arithmetic
    expressions, common transcendental functions, infinite series
    evaluation, definite integrals, polynomial roots, user-defined
    functions, all evaluated to a user-defined level of numeric
    precision, up to 1000 decimal digits.


%package data
Summary:        Data files for %{name}-tools
BuildArch:      noarch

%description data
This package contains data-files used with %{name}-tools.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files and headers for %{name}.


%package doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description doc
This package contains the documentation and some brief examples.


%package tools
Summary:        Interactive high-precision arithmetic computing environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-data    = %{version}-%{release}

%description tools
This is a complete interactive high-precision arithmetic computing
environment.  One enters expressions in a Mathematica-style syntax,
and the operations are performed using the ARPREC package, with a
level of precision that can be set from 100 to 1000 decimal digit
accuracy.  Variables and vector arrays can be defined and referenced.
This program supports all basic arithmetic operations, common
transcendental and combinatorial functions, multi-pair PSLQ (one-,
two- or three-level versions), high-precision quadrature, i.e. numeric
integration (Gaussian, error function or tanh-sinh), and summation of
series.


%prep
%autosetup -cp 1

pushd %{name}

# Pull-in upstream's .doc-license.
%{__cp} -a %{SOURCE1} .

# Create an user-friendly ascii-text from original .doc-license.
%{_bindir}/catdoc -d utf-8 %{SOURCE1} | \
  %{__sed} -e 's!\f!!g' > BSD-LBNL-License.txt && \
  /bin/touch -r %{SOURCE1} BSD-LBNL-License.txt

# Remove some unneeded and obsoleted files.
%{_bindir}/find . -depth -name '._*' -print0 | %{_bindir}/xargs -0 %{__rm} -rf
%{_bindir}/find . -depth -name '.[dD][sS]_[sS]tore' -print0 | \
  %{_bindir}/xargs -0 %{__rm} -rf

# The testsuite is a good example for using this lib.  So let's store it's
# files in another location before they get cluttered with intermediate stuff.
%{__cp} -a tests examples
%{__rm} -rf examples/Makefile*

# Get all pre-build quads-data from mathinit.
%{__sed} -i -e 's!nquadopt = 1!nquadopt = 3!g' toolkit/mathinit.f

# Use the pre-build data-files in mathtool.
%{__sed} -i -e 's!const\.dat!%{_datadir}/%{name}/&!g' \
  -e 's!quad.*\.dat!%{_datadir}/%{name}/&!g' toolkit/mathtool.f

# Make arprec-config multilib-friendly.  Substitute original script
# with a wrapper-script for pkg-config.
%{__cat} << EOS > arprec-config.rpmbuild
#!/bin/sh
# arprec-config.  Generated during rpmbuild.
pc=\`which pkg-config\`

usage()
{
  %{__cat} << EOF
Usage: arprec-config [OPTIONS]
Options:
    [--prefix]
    [--exec-prefix]
    [--version]
    [--libs]
    [--fc]
    [--fclibs]
    [--fcflags]
    [--fmainlib]
    [--cxx]
    [--cxxflags]
    [--configure-args]
EOF
  exit $1
}

while test \$# -gt 0; do
  case "\$1" in
  -*=*) optarg=\`echo "\$1" | sed 's/[-_a-zA-Z0-9]*=//'\` ;;
  *) optarg= ;;
  esac

  case \$1 in
    --prefix)
      \$pc --variable=prefix %{name}
      ;;
    --exec-prefix)
      \$pc --variable=exec_prefix %{name}
      ;;
    --version)
      \$pc --modversion %{name}
      ;;
    --libs)
      \$pc --libs %{name}
      ;;
    --cxx)
      \$pc --variable=cxx %{name}
      ;;
    --configure-args)
      \$pc --variable=configure_args %{name}
      ;;
    --fclibs)
      \$pc --variable=fclibs %{name}
      ;;
    --fcflags)
      \$pc --variable=fcflags %{name}
      ;;
    --fmainlib)
      \$pc --variable=fmainlib %{name}
      ;;
    --cxxflags)
      \$pc --variable=cxxflags %{name}
      ;;
    --fc)
      \$pc --variable=fc %{name}
      ;;
    *)
      usage 1 1>&2
      ;;
  esac
  shift
done
EOS

# Create a template for pkg-config.  This will be used by the modified
# arprec-config as well.
%{__cat} << EOF > %{name}.pc
############################
# Pkg-Config file for @name@
############################

prefix=@prefix@
exec_prefix=\${prefix}

bindir=@bindir@
datarootdir=@datadir@
datadir=\${datarootdir}/@name@
includedir=@includedir@
libdir=@libdir@
mandir=@mandir@
sharedstatedir=@sharedstatedir@
sysconfdir=@sysconfdir@

configure_args=@configure_args@
cxx=@cxx@
cxxflags=@cxxflags@
fc=@fc@
fcflags=-I${includedir}/@name@ @fcflags@
fclibs=@fclibs@
fmainlib=@fmainlib@

Name:           @name@
Version:        @version@
Description:    @name@ - @summary@

Libs:           @libs@
Cflags:         -I\${includedir}
EOF

popd


%build
pushd %{name}

# Remove obsoleted autotools-macros from configure.ac for el6+.  Running
# `autoupdate` and `autoreconf -fiv` is the recommended procedure to do so.
# For further reference have a look at libtool's manual on gnu.org:
# http://www.gnu.org/software/libtool/manual/html_node/LT_005fINIT.html
#
# During the el5-build we need to correct some timestamps, because they are
# broken in upstream's pristine tarballs.  This is not needed for el6+,
# because this will be taken care of by `autoupdate` and `autoreconf -fiv`.
%{_bindir}/autoupdate
%{_bindir}/autoreconf -fiv

# Invoke the `regular` build-procedure.
%configure \
  --disable-static \
  --enable-qd \
  --enable-shared
%make_build
# Toolkit target needs single-threaded build.
make toolkit

# Substitute @var@ in .pc-template from %%prep
%{__chmod} +x %{name}-config
%{__sed} -i -e 's!@prefix@!%{_prefix}!g' \
  -e 's!@bindir@!%{_bindir}!g' \
  -e 's!@datadir@!%{_datadir}!g' \
  -e 's!@name@!%{name}!g' \
  -e 's!@includedir@!%{_includedir}!g' \
  -e 's!@libdir@!%{_libdir}!g' \
  -e 's!@mandir@!%{_mandir}!g' \
  -e 's!@sharedstatedir@!%{_sharedstatedir}!g' \
  -e 's!@sysconfdir@!%{_sysconfdir}!g' \
  -e 's!@version@!%{version}!g' \
  -e 's!@summary@!Software package for performing arbitrary precision arithmetic!g' \
  -e "s~@libs@~$(./%{name}-config --libs)~g" \
  -e "s~@configure_args@~$(./%{name}-config --configure-args)~g" \
  -e "s~@cxx@~$(./%{name}-config --cxx)~g" \
  -e "s~@cxxflags@~$(./%{name}-config --cxxflags)~g" \
  -e "s~@fc@~$(./%{name}-config --fc)~g" \
  -e "s~@fcflags@~$(./%{name}-config --fcflags)~g" \
  -e "s~@fclibs@~$(./%{name}-config --fclibs)~g" \
  -e "s~@fmainlib@~$(./%{name}-config --fmainlib)~g" \
  %{name}.pc
%{__chmod} -x %{name}-config

# Pre-build the data-files for `mathtool`.
pushd toolkit
%if %{with mathinit}
./mathinit
%else
/bin/touch const.dat quadgs.dat quaderf.dat quadts.dat
%endif
popd

popd


%install
pushd %{name}

%make_install

# Remove unneeded and obsolete stuff.  %%{name}-config will be replaced by the
# new wrapper later.  The pre-installed docs will be picked as %%doc within
# %%files.  The .la-dumpings from libtool are obsolete and not useful.
%{__rm} -rf %{buildroot}%{_bindir}/%{name}-config \
  %{buildroot}%{_datadir}/* %{buildroot}%{_libdir}/*.la

# Create needed dirs.
%{__mkdir} -p %{buildroot}%{_datadir}/%{name} %{buildroot}%{_libdir}/pkgconfig

# There's no install-target for `mathtool`, so it must be install `by hand`.
for tool in toolkit/.libs/math*
do
  %{__install} -pm 0755 ${tool} \
    %{buildroot}%{_bindir}/%{name}-`basename ${tool}`
done

# Install the custom arprec-config wrapper-script and the needed .pc-file.
%{__install} -pm 0755 %{name}-config.rpmbuild %{buildroot}%{_bindir}/%{name}-config
%{__install} -pm 0644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig

# Install the pre-build data-files for `mathtool`.
%{__install} -pm 0644 toolkit/*.dat %{buildroot}%{_datadir}/%{name}

# Kill rpath on all binaries within %%{_bindir}.
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/%{name}-math*

# Install documentation and license.
%{__mkdir} -p %{buildroot}%{_pkgdocdir}/{examples,toolkit}
%{__install} -pm 0644 AUTHORS* BSD-LBNL-License* ChangeLog* \
  COPYING* NEWS* README* doc/* \
  %{buildroot}%{_pkgdocdir}
%{__install} -pm 0644 examples/* %{buildroot}%{_pkgdocdir}/examples
%{__install} -pm 0644 toolkit/README* %{buildroot}%{_pkgdocdir}/toolkit
%if %{with license}
%{__rm} -rf BSD-LBNL-License* COPYING*
%endif

popd


%check
# On Fedora the IO-read test failes for some unknown reason.  On RHEL all
# tests run fine.  The comment from upstream on bugreport with build.log:
#
# It looks like everything is working fine.  I don't know why it is failing
# that one test.  Let me know if you have any problems in running your codes
# -- I don't think you will.
# DHB
%make_build -C %{name} check


%ldconfig_scriptlets


%files
%if %{with license}
%license %{name}/BSD-LBNL-License* %{name}/COPYING*
%else
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/BSD-LBNL-License*
%doc %{_pkgdocdir}/COPYING*
%endif
%{_libdir}/lib%{name}*.so.*


%files data
%if %{with license}
%license %{_datadir}/licenses/%{name}
%else
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/BSD-LBNL-License*
%doc %{_pkgdocdir}/COPYING*
%endif
%{_datadir}/%{name}


%files devel
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%if %{with license}
%license %{_datadir}/licenses/%{name}
%endif
%doc %{_pkgdocdir}


%files tools
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/toolkit
%{_bindir}/%{name}-math*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.19-23
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Björn Esser <besser82@fedoraproject.org> - 2.2.19-14
- Fix build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Björn Esser <besser82@fedoraproject.org> - 2.2.19-5
- Rebuilt for GCC8

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.19-2
- Add patch to fix fix istream error logic

* Tue Jul 18 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.19-1
- New upstream release (rhbz#1472013)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.18-4
- Rebuilt for GCC-7

* Wed Feb 24 2016 Björn Esser <fedora@besser82.io> - 2.2.18-3
- fix build with gcc 6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Björn Esser <fedora@besser82.io> - 2.2.18-1
- new upstream release (#1290979)
- use %%license if applicable
- use unified %%_pkgdocdir
- general improvements to specfile

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.17-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 Björn Esser <bjoern.esser@gmail.com> - 2.2.17-2
- set timestamp for BSD-LBNL-License.txt from %%{SOURCE1}
- added conditional for %%check-target to be present on el5, only
- whitespace cleanup

* Fri Dec 20 2013 Björn Esser <bjoern.esser@gmail.com> - 2.2.17-1
- new upstream release: v2.2.17 (#1045344)
- fixed `macro-in-comment %%{_bindir}`
- fixed `macro-in-%%changelog %%{name}`

* Thu Sep 19 2013 Björn Esser <bjoern.esser@gmail.com> - 2.2.16-5
- fix Group-tag for devel-pkg

* Thu Sep 19 2013 Björn Esser <bjoern.esser@gmail.com> - 2.2.16-4
- fix "Variable 'datarootdir' not defined in '%%{_libdir}/pkgconfig/arprec.pc'"

* Fri Sep 13 2013 Björn Esser <bjoern.esser@gmail.com> - 2.2.16-3
- added needed bits for el5
- created an ascii-txt license from the license.doc provided by upstream
- nuked rpath from %%{_bindir}/%%{name}-math*
- added .pc-file to solve the multiarch-problematic and aged %%{name}-config
- fix some broken timestamps when building for el5 (not needed for el6+)
- run `autoupdate` and `autoreconf -fiv` to fix-up obsolete autotools-macros
  for el6+

* Fri Sep 13 2013 Björn Esser <bjoern.esser@gmail.com> - 2.2.16-2
- renamed tools-common pkg to data
- merged common-devel pkg with devel, because it can't be noarch
- removed calling autoreconf during %%build
- some minor improvements in %%prep, mostly comments
- as suggested in rhbz# 1007577 c#2

* Thu Sep 12 2013 Björn Esser <bjoern.esser@gmail.com> - 2.2.16-1
- Initial rpm release (#1007577)
