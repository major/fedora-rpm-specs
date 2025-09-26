%global gap_pkgname cohomolo
%global giturl      https://github.com/gap-packages/cohomolo

Name:           gap-pkg-%{gap_pkgname}
Version:        1.6.11
Release:        %autorelease
Summary:        Cohomology groups of finite groups on finite modules

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/cohomolo/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
# Add missing shebangs
Patch:          %{name}-shebang.patch
# Fix all -Wlto-type-mismatch warnings
Patch:          %{name}-lto.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap htm testdata tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tth

Requires:       gap-core%{?_isa}

%description
This package may be used to perform certain cohomological calculations on a
finite permutation group G.  The following properties of G can be computed:

1. The p-part Mul_p of the Schur multiplier Mul of G, and a presentation of a
   covering extension of Mul_p by G, for a specified prime p;

2. The dimensions of the first and second cohomology groups of G acting on a
   finite dimensional KG-module M, where K is a field of prime order; and

3. Presentations of split and nonsplit extensions of M by G.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Cohomolo documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -p1 -n %{gap_upname}-%{version}

%conf
# Fix paths
sed -i 's,\.\./\.\./\.\./,%{gap_libdir}/,' doc/make_doc

%build
# There are lot of type safety violations in the C code.  It also
# relies on implicit function declarations, a C89-only language
# feature.
%global build_type_safety_c 0
%set_build_flags
export CC='gcc -std=gnu89'

# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{gap_archdir}

# Build the binaries
%make_build

# Build the documentation
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm ../../doc

%install -a
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/standalone
cp -a standalone/{data.d,info.d} \
   %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/standalone

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/gap/
%{gap_archdir}/pkg/%{gap_upname}/standalone/
%{gap_archdir}/pkg/%{gap_upname}/testdata/
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_archdir}/pkg/%{gap_upname}/htm/
%{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
