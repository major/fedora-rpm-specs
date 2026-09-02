%global gap_pkgname orbitalgraphs
%global gap_upname  OrbitalGraphs
%global giturl      https://github.com/gap-packages/OrbitalGraphs

# Upstream has not tagged a commit since version 0.1.1 in 2021, but we need
# subsequent commits for gap-pkg-vole
%global commit      0255d714b5bb8d8e7a3e3f8332df9bbd11f35b8a
%global shortcommit %{sub %{commit} 1 7}
%global gitdate     20260711

Name:           gap-pkg-%{gap_pkgname}
Version:        0.1.2^%{gitdate}.%{shortcommit}
Release:        %autorelease
Summary:        Computations with orbital graphs in GAP

License:        MPL-2.0
URL:            https://gap-packages.github.io/OrbitalGraphs/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{commit}/%{gap_upname}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap notebooks tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2016.02.16
BuildRequires:  gap(gapdoc) >= 1.6.3
BuildRequires:  gap(digraphs) >= 1.1.1
BuildRequires:  gap-devel >= 4.11.0
BuildRequires:  gap-pkg-digraphs-doc >= 1.1.1

Requires:       gap(digraphs) >= 1.1.1
Requires:       gap-core >= 4.11.0

Provides:       gap(OrbitalGraphs) = %{version}-%{release}
Provides:       gap(orbitalgraphs) = %{version}-%{release}

%description
This package contains some utilities to compute with and research orbital
graphs in GAP.

%package doc
# The content is MPL-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        OrbitalGraphs documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       gap-pkg-digraphs-doc >= 1.1.1

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{commit}

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/notebooks/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/notebooks/

%changelog
%autochangelog
