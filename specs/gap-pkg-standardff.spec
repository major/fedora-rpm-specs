%global pkgname standardff
%global upname  StandardFF
%global giturl  https://github.com/frankluebeck/StandardFF

Name:           gap-pkg-%{pkgname}
Version:        1.0
Release:        %autorelease
Summary:        Standardized generation of finite fields and cyclic subgroups

License:        GPL-3.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/gap/StandardFF/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-factint
BuildRequires:  gap-pkg-spinsym
BuildRequires:  gap-pkg-io
BuildRequires:  gcc-c++
BuildRequires:  ntl-devel

Requires:       gap-core%{?_isa}

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
%autosetup -n %{upname}-%{version}

%build
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
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{upname}/
%{gap_archdir}/pkg/%{upname}/*.g
%{gap_archdir}/pkg/%{upname}/data/
%{gap_archdir}/pkg/%{upname}/lib/
%{gap_archdir}/pkg/%{upname}/ntl/
%{gap_archdir}/pkg/%{upname}/tst/
%{gap_archdir}/pkg/%{upname}/VERSION

%files doc
%docdir %{gap_archdir}/pkg/%{upname}/doc/
%{gap_archdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
