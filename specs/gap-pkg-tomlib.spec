%global gap_pkgname tomlib
%global giturl      https://github.com/gap-packages/tomlib

Name:           gap-pkg-%{gap_pkgname}
Version:        1.2.11
Release:        %autorelease
Summary:        GAP Table of Marks package

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/tomlib/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): data gap htm tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(atlasrep) >= 1.5
BuildRequires:  gap(autodoc) >= 2016.01.21
BuildRequires:  gap-devel >= 4.4
BuildRequires:  parallel

Requires:       gap(atlasrep) >= 1.5
Requires:       gap-core >= 4.4

Recommends:     gap(ctbllib) >= 1.1

Provides:       gap(TomLib) = %{version}-%{release}
Provides:       gap(tomlib) = %{version}-%{release}

%description
This package provides access to several hundred tables of marks of almost
simple groups and their maximal subgroups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Table of Marks documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%build -a
# Compress large tables of marks
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/*.tom

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/data/
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/htm/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
