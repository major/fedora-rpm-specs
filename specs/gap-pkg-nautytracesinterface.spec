# There have been no official releases yet, so we pull from git
%global date     20250620
%global commit   75cf4e55feaff7d3b3bce0624d7290bc8b0ec56b
%global user     gap-packages
%global pkgname  nautytracesinterface
%global forgeurl https://github.com/gap-packages/NautyTracesInterface

# When bootstrapping a new architecture, there is no gap-pkg-digraphs package
# yet.  It is only needed for testing this package, but it requires this package
# to function at all.  Therefore, do the following:
# 1. Build this package in boostrap mode.
# 2. Build gap-pkg-digraphs.
# 3. Build this package in non-boostrap mode.
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        0.3
Summary:        GAP interface to nauty and Traces

%forgemeta

Release:        %autorelease
License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/NautyTracesInterface/
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}
# Fedora-only patch: use the system nauty library
Patch:          %{name}-nauty.patch
# Fix a broken documentation reference
Patch:          %{forgeurl}/pull/53.patch

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
This package contains documentation for gap-pkg-%{pkgname}.

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

%install
# make install doesn't put ANYTHING where it is supposed to go, so...
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a bin examples gap tst *.g %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g
%endif

%files
%doc README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/gap/
%{gap_archdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/examples/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/examples/

%changelog
%autochangelog
