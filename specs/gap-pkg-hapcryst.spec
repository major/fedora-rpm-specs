%global gap_pkgname hapcryst
%global giturl      https://github.com/gap-packages/hapcryst

Name:           gap-pkg-%{gap_pkgname}
Version:        0.2.0
Release:        %autorelease
Summary:        Integral cohomology computations of Bieberbach groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/hapcryst/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
# Fix documentation bugs
Patch:          %{name}-doc.patch
# Adapt to Carat -> CaratInterface name change
Patch:          %{name}-carat.patch

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): examples lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(aclib) >= 1.1
BuildRequires:  gap(autodoc)
BuildRequires:  gap(caratinterface) >= 1.1
BuildRequires:  gap(cryst) >= 4.1.5
BuildRequires:  gap(crystcat) >= 1.1.2
BuildRequires:  gap(gapdoc) >= 0.99
BuildRequires:  gap(hap) >= 1.8
BuildRequires:  gap(nq)
BuildRequires:  gap(polycyclic) >= 2.8.1
BuildRequires:  gap(polymaking) >= 0.8.6
BuildRequires:  gap-devel >= 4.12
BuildRequires:  gap-pkg-polymaking-doc >= 0.8.6

Requires:       gap(aclib) >= 1.1
Requires:       gap(cryst) >= 4.1.5
Requires:       gap(hap) >= 1.8
Requires:       gap(polycyclic) >= 2.8.1
Requires:       gap(polymaking) >= 0.8.6
Requires:       gap-core >= 4.12

Recommends:     gap(caratinterface) >= 1.1
Recommends:     gap(crystcat) >= 1.1.2

Provides:       gap(HAPcryst) = %{version}-%{release}
Provides:       gap(hapcryst) = %{version}-%{release}

%description
This package is an add-on for Graham Ellis' HAP package.  HAPcryst implements
some functions for crystallographic groups (namely OrbitStabilizer-type
methods).  It is also capable of calculating free resolutions for Bieberbach
groups.

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
Requires:       gap-pkg-polymaking-doc >= 0.8.6

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -p0 -n %{gap_upname}-%{version}

%build -a
# Fix up broken HTML links between the two books
sed -i 's,\./lib,.&,g' doc/*.html

%install -a
rm -fr %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/lib/datatypes/doc
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/lib/datatypes/doc
%gap_copy_docs -d lib/datatypes/doc

%check -p
# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%dir %{gap_libdir}/pkg/%{gap_upname}/lib/
%dir %{gap_libdir}/pkg/%{gap_upname}/lib/datatypes/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/*.gd
%{gap_libdir}/pkg/%{gap_upname}/lib/*.gi
%{gap_libdir}/pkg/%{gap_upname}/lib/datatypes/*.gd
%{gap_libdir}/pkg/%{gap_upname}/lib/datatypes/*.gi
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%docdir %{gap_libdir}/pkg/%{gap_upname}/lib/datatypes/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/lib/datatypes/doc/

%changelog
%autochangelog
