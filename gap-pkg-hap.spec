# TODO: This package wants homology, if the Pascal issues can be resolved:
# http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Homology/

%global pkgname hap

# When bootstrapping a new architecture, the hapcryst package is not yet
# available.  Therefore:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-hapcryst.
# 3. Build this package in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        1.55
Release:        1%{?dist}
Summary:        Homological Algebra Programming for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://gap-packages.github.io/hap/
Source0:        https://github.com/gap-packages/hap/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  asymptote
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-congruence
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-edim
BuildRequires:  gap-pkg-fga
%if %{without bootstrap}
BuildRequires:  gap-pkg-hapcryst
%endif
BuildRequires:  gap-pkg-laguna
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-polymaking
BuildRequires:  gap-pkg-singular
BuildRequires:  graphviz
BuildRequires:  ImageMagick
BuildRequires:  perl-generators
BuildRequires:  xdg-utils

Requires:       coreutils
Requires:       gap-pkg-aclib
Requires:       gap-pkg-crystcat
Requires:       gap-pkg-fga
Requires:       gap-pkg-nq
Requires:       gap-pkg-polycyclic
Requires:       xdg-utils

Recommends:     asymptote
Recommends:     gap-pkg-congruence
Recommends:     gap-pkg-edim
Recommends:     gap-pkg-laguna
Recommends:     gap-pkg-polymaking
Recommends:     gap-pkg-singular

Suggests:       gap-pkg-hapcryst
Suggests:       gap-pkg-xmod
Suggests:       graphviz
Suggests:       ImageMagick
Suggests:       openssh-clients

# This can be removed when F40 reaches EOL
Obsoletes:      gap-pkg-happrime < 0.6-8

%description
HAP is a homological algebra library for use with the GAP computer
algebra system, and is still under development.  Its initial focus is on
computations related to the cohomology of groups.  Both finite and
infinite groups are handled, with emphasis on integral coefficients.

Recent additions include some functions for computing homology of
crossed modules and simplicial groups, and also some functions for
handling simplicial complexes, cubical complexes and regular
CW-complexes in the context of topological data analysis.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        HAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

# This can be removed when F40 reaches EOL
Obsoletes:      gap-pkg-happrime-doc < 0.6-8

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Don't force the web browser to be firefox
sed -i.orig 's/"firefox"/"xdg-open"/' lib/externalSoftware.gap
fixtimestamp lib/externalSoftware.gap

# Remove obsolete files
find . \( -name \*keep\* -o -name \*working\* -o -name \*.swp \) -delete
rm -fr lib/*/*.old lib/Functors/*.ancient lib/GOuterGroups/*.trial

# Clean up documentation to force complete rebuild
cd doc
./clean
cd -
cd tutorial
./clean
cd -

# Fix end of line encoding
sed -i.orig 's/\r//' www/SideLinks/HAPpagestyles.css
fixtimestamp www/SideLinks/HAPpagestyles.css

# Remove incorrect executable bits
chmod a-x lib/Kelvin/{*.xml,kelvin.gd,*.gi,init.g,tutex/*.txt} \
          lib/Perturbations/Gcomplexes/*.gz \
          www/SideLinks/About/*.g

%build
# Build the documentation
export LC_ALL=C.UTF-8
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g boolean date lib tst tutorial version www \
   %{buildroot}%{gap_libdir}/pkg/%{pkgname}
rm -f %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tutorial/clean
rm -fr %{buildroot}%{gap_libdir}/pkg/%{pkgname}/lib/CompiledGAP
%gap_copy_docs

%if %{without bootstrap}
%check
export LC_ALL=C.UTF-8

# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

# Now we can run the actual test; the 2G default is not enough on s390x
# Do not run the very slow tests
gap -l "%{buildroot}%{gap_libdir};" -o 3G tst/testquick.g
%endif

%files
%doc README.md
%license www/copyright/*.html
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/tutorial/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/tutorial/

%changelog
* Mon Apr 17 2023 Jerry James <loganjerry@gmail.com> - 1.55-1
- Version 1.55

* Mon Mar 20 2023 Jerry James <loganjerry@gmail.com> - 1.54-1
- Version 1.54

* Tue Feb 28 2023 Jerry James <loganjerry@gmail.com> - 1.53-1
- Version 1.53

* Mon Feb 13 2023 Jerry James <loganjerry@gmail.com> - 1.52-1
- Version 1.52

* Fri Feb  3 2023 Jerry James <loganjerry@gmail.com> - 1.50-1
- Version 1.50

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.49-2
- Update for split GAP directories

* Mon Jan  9 2023 Jerry James <loganjerry@gmail.com> - 1.49-1
- Version 1.49

* Sat Jan  7 2023 Jerry James <loganjerry@gmail.com> - 1.48-1
- Version 1.48

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.47-2
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.47-2
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.47-1
- Convert License tag to SPDX

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 1.47-1
- Version 1.47

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 1.46-1
- Version 1.46

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 1.45-1
- Version 1.45

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 1.44-1
- Do not build on i386 due to unavailability of polymake

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 1.44-1
- Version 1.44
- Drop -happrime patch now that gap-pkg-happrime has been retired

* Thu Jun 30 2022 Jerry James <loganjerry@gmail.com> - 1.43-1
- Version 1.43
- Drop now irrelevant -lpres patch

* Fri Jun  3 2022 Jerry James <loganjerry@gmail.com> - 1.41-1
- Version 1.41

* Thu Jun  2 2022 Jerry James <loganjerry@gmail.com> - 1.40-1
- Version 1.40

* Thu Apr 21 2022 Jerry James <loganjerry@gmail.com> - 1.39-1
- Version 1.39

* Wed Mar  9 2022 Jerry James <loganjerry@gmail.com> - 1.38-1
- Version 1.38

* Mon Feb 21 2022 Jerry James <loganjerry@gmail.com> - 1.37-1
- Version 1.37

* Thu Feb 10 2022 Jerry James <loganjerry@gmail.com> - 1.35-1
- Version 1.35

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jul 31 2021 Jerry James <loganjerry@gmail.com> - 1.34-1
- Version 1.34

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul  1 2021 Jerry James <loganjerry@gmail.com> - 1.33-1
- Version 1.33

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 1.32-1
- Version 1.32

* Tue Apr 13 2021 Jerry James <loganjerry@gmail.com> - 1.30-1
- Version 1.30
- Drop the upstreamed -polymake4 patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Jerry James <loganjerry@gmail.com> - 1.29-1
- Version 1.29

* Tue Jan  5 2021 Jerry James <loganjerry@gmail.com> - 1.28-1
- Version 1.28
- Give the tests access to more memory

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May  5 2020 Jerry James <loganjerry@gmail.com> - 1.26-1
- Version 1.26

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 1.25-1
- Version 1.25
- New URLs
- Drop upstreamed -doc patch

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 1.24-3
- Add -polymake4 patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Jerry James <loganjerry@gmail.com> - 1.24-1
- Version 1.24

* Tue Aug 13 2019 Jerry James <loganjerry@gmail.com> - 1.21-1
- New upstream release
- Drop -dims patch; upstream fixed it another way

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Jerry James <loganjerry@gmail.com> - 1.19-2
- Changes due to gap-pkg-singular becoming available

* Wed Feb  6 2019 Jerry James <loganjerry@gmail.com> - 1.19-1
- New upstream release
- Add -dims and -lpres patches
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb  3 2018 Jerry James <loganjerry@gmail.com> - 1.12.5-1
- New upstream release

* Wed Sep  6 2017 Jerry James <loganjerry@gmail.com> - 1.12.0-1
- New upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Jerry James <loganjerry@gmail.com> - 1.11.14-1
- New upstream release
- Use upstream's 3-part version scheme
- Suggest the hapcryst and xmod packages

* Tue Aug 16 2016 Jerry James <loganjerry@gmail.com> - 1.11-2
- Switch crystcat from Recommends to Requires

* Fri Aug  5 2016 Jerry James <loganjerry@gmail.com> - 1.11-1
- Initial RPM
