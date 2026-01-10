# When bootstrapping a new architecture, there is no gap-pkg-digraphs package
# yet.  It is only needed for testing this package, but it requires this package
# to function at all.  Therefore, do the following:
# 1. Build this package in boostrap mode.
# 2. Build gap-pkg-digraphs.
# 3. Build this package in non-boostrap mode.
%bcond bootstrap 0

# There have been no official releases yet, so we pull from git
%global date           20251125
%global commit         530c14844dc789d6c6af026758451482c4bfc684
%global user           gap-packages
%global gap_pkgname    nautytracesinterface
%global gap_skip_check %{?with_bootstrap}
%global forgeurl       https://github.com/gap-packages/NautyTracesInterface

Name:           gap-pkg-%{gap_pkgname}
Version:        0.3
Summary:        GAP interface to nauty and Traces

%forgemeta

Release:        %autorelease
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/NautyTracesInterface/
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}
# Fedora-only patch: use the system nauty library
Patch:          %{name}-nauty.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin examples gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
%if %{without bootstrap}
BuildRequires:  gap-pkg-digraphs
BuildRequires:  gap-pkg-grape
%endif
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libnauty)

Requires:       gap-core%{?_isa}

%description
This GAP package provides an interface to nauty and Traces.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        NautyTracesInterface documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%forgeautosetup -p1

%conf
# Make sure the bundled nauty is not used
rm -fr nauty*

# Generate the configure script
autoreconf -fi

%build
%configure --with-gaproot=%{gap_archdir} --with-nauty=%{_includedir}/nauty \
  --disable-silent-rules
%make_build
%make_build doc

%files
%doc README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/gap/
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_archdir}/pkg/%{gap_upname}/examples/
%{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
