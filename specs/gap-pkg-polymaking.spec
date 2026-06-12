%global gap_pkgname polymaking
%global giturl      https://github.com/gap-packages/polymaking

Name:           gap-pkg-%{gap_pkgname}
Version:        0.8.9
Release:        %autorelease
Summary:        GAP interface to polymake

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/polymaking/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2016.01.21
BuildRequires:  gap-devel >= 4.8
BuildRequires:  polymake

Requires:       gap-core >= 4.8
Requires:       polymake

Provides:       gap(polymaking) = %{version}-%{release}

%description
This package provides a very basic GAP interface to polymake.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Polymaking documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%check -p
# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
