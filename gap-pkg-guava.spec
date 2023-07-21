%global pkgname guava

Name:           gap-pkg-%{pkgname}
Version:        3.18
Release:        3%{?dist}
Summary:        Computing with error-correcting codes

License:        GPL-2.0-or-later
ExclusiveArch:  %{gap_arches}
URL:            https://gap-packages.github.io/guava/
Source0:        https://github.com/gap-packages/guava/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Enable the optional Sonata code.  Upstream says to uncomment this code if
# Sonata is available, and that is all this patch does.
Patch0:         %{name}-sonata.patch
# Patch to fix C compiler warnings that indicate possible runtime problems.
Patch1:         %{name}-warning.patch
# Use popcount instructions where available.
Patch2:         %{name}-popcount.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-sonata
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  parallel

Requires:       gap-core%{?_isa}
Requires:       gap-pkg-sonata

%global _docdir_fmt %{name}

%description
GUAVA is a package that implements coding theory algorithms in GAP.
Codes can be created and manipulated and information about codes can be
calculated.

GUAVA consists of various files written in the GAP language, and an
external program from J. S. Leon for dealing with automorphism groups of
codes and isomorphism testing functions.  Several algorithms that need
the speed are integrated in the GAP kernel.

The functions within GUAVA can be divided into four categories:
- Construction of codes.  GUAVA can construct non-linear, linear and
  cyclic codes over an arbitrary finite field.  Examples are
  HadamardCode, ReedMullerCode, BestKnownLinearCode, QRCode and
  GoppaCode.
- Manipulation of codes.  These functions allow the user to transform
  one code into another or to construct a new code from two codes.
  Examples are PuncturedCode, DualCode, DirectProductCode and UUVCode.
- Computation of information about codes.  This information is stored in
  the code record.  Examples are MinimumDistance, OuterDistribution,
  IsSelfDualCode and AutomorphismGroup.
- Generation of bounds on linear codes.  The table by Brouwer and
  Verhoeff (as it existed in the mid-1990s) is incorporated into GUAVA.
  For example, BoundsMinimumDistance.

%package doc
# The content is GFDL-1.2-no-invariants-or-later.  The remaining licenses cover
# the various fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GFDL-1.2-no-invariants-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        GUAVA documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

# Avoid name collisions in the documentation
cp -p src/ctjhai/README README.ctjhai

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated script.  Do not use %%configure.
./configure %{gap_archdir}

# Building with %%{?_smp_mflags} fails
make CFLAGS="%{build_cflags} -DLONG_EXTERNAL_NAMES"

# Compress large tables
parallel %{?_smp_mflags} --no-notice gzip --best ::: tbl/*.g

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg/%{pkgname}
gap -l "$PWD/..;" makedoc.g
rm -fr ../../doc ../pkg
pushd src/leon/doc
pdftex manual.tex
popd

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin lib tbl tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
# The documentation tests cannot be run, as they require breaking out of
# infinite loops.  See comments about a user interrupt.
export LC_ALL=C.UTF-8
cd tst
gap -l "%{buildroot}%{gap_archdir};" << EOF
LoadPackage("guava");
if Test("guava.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("decoding.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("hadamard.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("external.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
EOF

%files
%doc CHANGES HISTORY README.md README.ctjhai
%license COPYING
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%doc src/leon/doc/manual.pdf
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 3.18-1
- Version 3.18
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 3.17-1
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 3.17-1
- Version 3.17
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 3.16-3
- Convert License tags to SPDX

* Mon Jul 25 2022 Jerry James <loganjerry@gmail.com> - 3.16-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 25 2022 Jerry James <loganjerry@gmail.com> - 3.16-1
- Version 3.16

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 3.15-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Jerry James <loganjerry@gmail.com> - 3.15-1
- New upstream version
- License change to GPLv3+

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 3.14-5
- Rebuild for changed bin dir name in gap 4.10.1

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 3.14-4
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Jerry James <loganjerry@gmail.com> - 3.14-1
- New upstream version
- Drop upstreamed -bibtex patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan  6 2017 Jerry James <loganjerry@gmail.com> - 3.13.1-3
- Fix a broken submake command

* Fri Aug 19 2016 Jerry James <loganjerry@gmail.com> - 3.13.1-2
- More compiler warnings fixed

* Tue Aug 16 2016 Jerry James <loganjerry@gmail.com> - 3.13.1-1
- Initial RPM
