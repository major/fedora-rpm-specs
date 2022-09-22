%global pkgname digraphs

Name:           gap-pkg-%{pkgname}
Version:        1.5.3
Release:        3%{?dist}
Summary:        GAP package for digraphs and multidigraphs

# The project as a whole is GPL-3.0-or-later.
# The bundled copy of bliss is LGPL-3.0-only.
License:        GPL-3.0-or-later AND LGPL-3.0-only
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
%configure --with-gaproot=%{_gap_dir} --disable-silent-rules \
  --with-external-planarity --without-intrinsics
%make_build

# Build the documentation
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

# Remove a useless empty directory
rmdir bin/lib

%install
# make install doesn't put ANYTHING where it is supposed to go, so...
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc
cp -a bin data gap notebooks tst VERSION* *.g \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
cp -p doc/*.{bib,css,html,js,lab,pdf,six,txt,xml} \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc

# The 32-bit ARM builders frequently run out of memory while running tests
%ifnarch %{arm}
%check
export LC_ALL=C.UTF-8
cd tst

# The digraph test erases all variables, so do this in two parts.
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" << EOF
LoadPackage("digraphs");
r1 := Test("testinstall.tst", rec( compareFunction := "uptowhitespace" ));
r2 := Test("standard/attr.tst", rec( compareFunction := "uptowhitespace" ));
r3 := Test("standard/cliques.tst", rec( compareFunction := "uptowhitespace" ));
r4 := Test("standard/constructors.tst", rec( compareFunction := "uptowhitespace" ));
r5 := Test("standard/display.tst", rec( compareFunction := "uptowhitespace" ));
r6 := Test("standard/examples.tst", rec( compareFunction := "uptowhitespace" ));
r7 := Test("standard/grahom.tst", rec( compareFunction := "uptowhitespace" ));
r8 := Test("standard/grape.tst", rec( compareFunction := "uptowhitespace" ));
r9 := Test("standard/io.tst", rec( compareFunction := "uptowhitespace" ));
rA := Test("standard/isomorph.tst", rec( compareFunction := "uptowhitespace" ));
rB := Test("standard/labels.tst", rec( compareFunction := "uptowhitespace" ));
rC := Test("standard/oper.tst", rec( compareFunction := "uptowhitespace" ));
rD := Test("standard/orbits.tst", rec( compareFunction := "uptowhitespace" ));
rE := Test("standard/planar.tst", rec( compareFunction := "uptowhitespace" ));
rF := Test("standard/prop.tst", rec( compareFunction := "uptowhitespace" ));
GAP_EXIT_CODE(r1 and r2 and r3 and r4 and r5 and r6 and r7 and r8 and r9 and rA and rB and rC and rD and rE and rF);
EOF

gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" << EOF
LoadPackage("digraphs");
GAP_EXIT_CODE(Test("standard/digraph.tst", rec( compareFunction := "uptowhitespace" )));
EOF

find %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version} -size 0 -delete
%endif

%files
%doc CHANGELOG.md README.md
%license GPL LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
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
