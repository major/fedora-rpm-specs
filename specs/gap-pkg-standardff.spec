%global gap_pkgname standardff
%global gap_upname  StandardFF
%global gap_makedoc makedocrel.g
%global giturl      https://github.com/frankluebeck/StandardFF

Name:           gap-pkg-%{gap_pkgname}
Version:        1.0
Release:        %autorelease
Summary:        Standardized generation of finite fields and cyclic subgroups

License:        GPL-3.0-or-later
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/gap/StandardFF/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs .. -r pathtoroot
BuildOption(install): data lib tst VERSION
BuildOption(check): tst/testall.g

BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-factint
BuildRequires:  gap-pkg-spinsym
BuildRequires:  gap-pkg-io
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(ntl)

Requires:       gap-core%{?_isa}

Recommends:     gap-pkg-ctbllib
Recommends:     gap-pkg-factint

%description
The StandardFF package contains an implementation of *standard* generators of
finite fields and of cyclic subgroups in the multiplicative groups of finite
fields, as described in https://arxiv.org/abs/2107.02257.

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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%build -p
# Build the NTL interfaces
cd ntl
for fil in *.cc; do
  g++ %{build_cxxflags} $fil -o $(basename $fil .cc) %{build_ldflags} -lntl
done
cd -

# Help the documentation building step find the GAP root
cat > pathtoroot << EOF
pathtoroot := "%{gap_libdir}";
EOF

%install -a
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/ntl
cp -p ntl/{factors,findirr,findstdirrGF{2,p},isirrGF{p,q}} \
   %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/ntl

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/data/
%{gap_archdir}/pkg/%{gap_upname}/lib/
%{gap_archdir}/pkg/%{gap_upname}/ntl/
%{gap_archdir}/pkg/%{gap_upname}/tst/
%{gap_archdir}/pkg/%{gap_upname}/VERSION

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
