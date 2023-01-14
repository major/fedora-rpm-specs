%global pkgname digraphs

Name:           gap-pkg-%{pkgname}
Version:        1.6.1
Release:        2%{?dist}
Summary:        GAP package for digraphs and multidigraphs

# The project as a whole is GPL-3.0-or-later.
# The bundled copy of bliss is LGPL-3.0-only.
License:        GPL-3.0-or-later AND LGPL-3.0-only
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://digraphs.github.io/Digraphs/
Source0:        https://github.com/digraphs/Digraphs/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-datastructures
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-nautytracesinterface
BuildRequires:  gap-pkg-orb
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  planarity-devel
BuildRequires:  xdg-utils

Requires:       gap-pkg-datastructures%{?_isa}
Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}

Recommends:     gap-pkg-grape%{?_isa}
Recommends:     gap-pkg-nautytracesinterface%{?_isa}

# The bundled copy of bliss has been modified for better integration with GAP
Provides:       bundled(bliss) = 0.73

%description
The Digraphs package is a GAP package containing methods for graphs,
digraphs, and multidigraphs.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Digraphs documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Make sure the bundled planarity is not used
rm -fr extern/edge-addition-planarity-suite-Version_3.0.1.0

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules \
  --with-external-planarity
%make_build

# Build the documentation
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

# Remove a useless empty directory
rmdir bin/lib

%install
# make install doesn't put ANYTHING where it is supposed to go, so...
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a bin data gap notebooks tst VERSION* *.g \
   %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
# The "extreme" tests take a long time, so just run the "standard" tests
export LC_ALL=C.UTF-8
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" tst/teststandard.g
rm -fr ../pkg

%files
%doc CHANGELOG.md README.md
%license GPL LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.6.1-2
- Update for split GAP directories

* Wed Dec  7 2022 Jerry James <loganjerry@gmail.com> - 1.6.1-1
- Version 1.6.1

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.6.0-1
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.6.0-1
- Version 1.6.0
- Update for gap 4.12.0

* Wed Aug 17 2022 Jerry James <loganjerry@gmail.com> - 1.5.3-3
- Convert License tag to SPDX

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 1.5.3-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 21 2022 Jerry James <loganjerry@gmail.com> - 1.5.3-1
- Version 1.5.3

* Wed Mar 30 2022 Jerry James <loganjerry@gmail.com> - 1.5.2-1
- Version 1.5.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- Version 1.5.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 15 2021 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Version 1.4.1

* Thu Jan 28 2021 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Version 1.4.0
- Disable tests on 32-bit ARM due to memory exhaustion

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Version 1.3.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Version 1.3.0

* Wed May 27 2020 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- Version 1.2.1

* Sat Mar 21 2020 Jerry James <loganjerry@gmail.com> - 1.1.2-1
- Version 1.1.2

* Sat Feb  8 2020 Jerry James <loganjerry@gmail.com> - 1.1.1-1
- Version 1.1.1
- Drop upstreamed -overflow patch
- Bundle modified bliss

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3

* Sat Oct  5 2019 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- New upstream version
- Drop upstreamed -bliss and -planarity patches

* Mon Aug 12 2019 Jerry James <loganjerry@gmail.com> - 0.15.4-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 0.15.3-1
- New upstream version

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 0.15.2-1
- New upstream version
- Unbundle planarity
- Drop -popcount patch, no longer needed
- Add -overflow patch

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 28 2018 Jerry James <loganjerry@gmail.com> - 0.12.1-1
- New upstream version

* Sat Mar 17 2018 Jerry James <loganjerry@gmail.com> - 0.12.0-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  9 2018 Jerry James <loganjerry@gmail.com> - 0.11.0-2
- Recommend gap-pkg-nautytracesinterface

* Sat Nov 25 2017 Jerry James <loganjerry@gmail.com> - 0.11.0-1
- New upstream version

* Thu Aug  3 2017 Jerry James <loganjerry@gmail.com> - 0.10.0-1
- Initial RPM
