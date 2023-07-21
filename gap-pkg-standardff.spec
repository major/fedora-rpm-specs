%global pkgname standardff
%global upname  StandardFF

Name:           gap-pkg-%{pkgname}
Version:        0.9.4
Release:        4%{?dist}
Summary:        Standardized generation of finite fields and cyclic subgroups

License:        GPL-3.0-or-later
ExclusiveArch:  %{gap_arches}
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/gap/StandardFF/
Source0:        https://github.com/frankluebeck/StandardFF/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-factint
BuildRequires:  gap-pkg-spinsym
BuildRequires:  gap-pkg-io
BuildRequires:  gcc-c++
BuildRequires:  ntl-devel

Requires:       gap-core

Recommends:     gap-pkg-ctbllib
Recommends:     gap-pkg-factint

%description
The StandardFF package contains an implementation of *standard*
generators of finite fields and of cyclic subgroups in the
multiplicative groups of finite fields, as described in
https://arxiv.org/abs/2107.02257.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
BuildArch:      noarch
Summary:        StandardFF documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version} -p0

%build
export LC_ALL=C.UTF-8

# Build the NTL interfaces
cd ntl
for fil in *.cc; do
  g++ %{build_cxxflags} $fil -o $(basename $fil .cc) %{build_ldflags} -lntl
done
cd -

# Build the documentation
mkdir ../pkg
ln -s ../%{upname}-%{version} ../pkg
cat > pathtoroot << EOF
pathtoroot := "%{gap_libdir}";
EOF
gap -l "$PWD/..;" -r pathtoroot makedocrel.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{upname}/{doc,ntl}
cp -a *.g data lib tst VERSION %{buildroot}%{gap_archdir}/pkg/%{upname}
cp -p ntl/{factors,findirr,findstdirrGF{2,p},isirrGF{p,q}} \
   %{buildroot}%{gap_archdir}/pkg/%{upname}/ntl
%gap_copy_docs -n %{upname}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%{gap_archdir}/pkg/%{upname}/
%exclude %{gap_archdir}/pkg/%{upname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{upname}/doc/
%{gap_archdir}/pkg/%{upname}/doc/

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 0.9.4-2
- Update for split GAP directories

* Tue Sep 13 2022 Jerry James <loganjerry@gmail.com> - 0.9.4-1
- Initial RPM
