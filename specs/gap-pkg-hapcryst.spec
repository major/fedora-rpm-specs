%global pkgname hapcryst
%global giturl  https://github.com/gap-packages/hapcryst

Name:           gap-pkg-%{pkgname}
Version:        0.1.15
Release:        %autorelease
Summary:        Integral cohomology computations of Bieberbach groups

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/hapcryst/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Fix documentation bugs
Patch:          %{name}-doc.patch
# Adapt to Carat -> CaratInterface name change
Patch:          %{name}-carat.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-caratinterface
BuildRequires:  gap-pkg-cryst
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-hap
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-polymaking-doc

Requires:       gap-pkg-aclib
Requires:       gap-pkg-cryst
Requires:       gap-pkg-hap
Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-polymaking

Recommends:     gap-pkg-caratinterface
Recommends:     gap-pkg-crystcat

%description
This package is an add-on for Graham Ellis' HAP package.  HAPcryst
implements some functions for crystallographic groups (namely
OrbitStabilizer-type methods).  It is also capable of calculating free
resolutions for Bieberbach groups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        HAPcryst documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
# Build the documentation
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

# Fix up broken HTML links between the two books
sed -i 's,\./lib,.&,g' doc/*.html

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g examples lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
rm -fr %{buildroot}%{gap_libdir}/pkg/%{pkgname}/lib/datatypes/doc
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/lib/datatypes/doc
%gap_copy_docs
%gap_copy_docs -d lib/datatypes/doc

%check
# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

# Run the actual tests
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc CHANGES README
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%dir %{gap_libdir}/pkg/%{pkgname}/lib/
%dir %{gap_libdir}/pkg/%{pkgname}/lib/datatypes/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/lib/*.gd
%{gap_libdir}/pkg/%{pkgname}/lib/*.gi
%{gap_libdir}/pkg/%{pkgname}/lib/datatypes/*.gd
%{gap_libdir}/pkg/%{pkgname}/lib/datatypes/*.gi
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%docdir %{gap_libdir}/pkg/%{pkgname}/lib/datatypes/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/lib/datatypes/doc/

%changelog
%autochangelog
