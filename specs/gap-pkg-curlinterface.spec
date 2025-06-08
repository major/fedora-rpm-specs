%global pkgname curlinterface
%global upname  curlInterface
%global giturl  https://github.com/gap-packages/curlInterface

# TESTING NOTE: the tests, unsurprisingly, require network access.  Since the
# koji builders have no network access, the tests always fail.  The maintainer
# should run the tests in an environment where testing is possible prior to
# each koji build.
%bcond tests 0

Name:           gap-pkg-%{pkgname}
Version:        2.4.1
Release:        %autorelease
Summary:        Simple web access for GAP

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/curlInterface/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{upname}-%{version}.tar.gz
# Avoid a type warning from curl
Patch:          %{name}-callback.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)

Requires:       gap-core%{?_isa}

%description
This package provides a simple GAP wrapper around libcurl, to allow
downloading files over http, ftp and https.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Curl interface for GAP documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version} -p1

%build
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules

# Build the binary interface
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{upname}/doc
cp -a *.g bin gap tst %{buildroot}%{gap_archdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%if %{with tests}
%check
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g
%endif

%files
%doc CHANGES README.md
%license GPL LICENSE
%dir %{gap_archdir}/pkg/%{upname}/
%{gap_archdir}/pkg/%{upname}/*.g
%{gap_archdir}/pkg/%{upname}/bin/
%{gap_archdir}/pkg/%{upname}/gap/
%{gap_archdir}/pkg/%{upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{upname}/doc/
%{gap_archdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
