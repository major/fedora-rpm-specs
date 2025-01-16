%global pkgname zeromqinterface
%global upname  ZeroMQInterface
%global giturl  https://github.com/gap-packages/ZeroMQInterface

Name:           gap-pkg-%{pkgname}
Version:        0.16
Release:        %autorelease
Summary:        ZeroMQ bindings for GAP

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/ZeroMQInterface/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  python3-devel

Requires:       gap-core%{?_isa}

%description
This package provides both low-level bindings as well as some higher
level interfaces for the ZeroMQ message passing library for GAP and
HPC-GAP, enabling lightweight distributed computation.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Documentation for ZeroMQ bindings for GAP
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%conf
# Fix python shebang
sed -i.orig 's,%{_bindir}/env python,%{python3},' zgap
touch -r zgap.orig zgap
rm zgap.orig

%build
%configure --with-gaproot=%{gap_archdir}
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{upname}/doc
cp -a bin gap tst *.g %{buildroot}%{gap_archdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

mkdir -p %{buildroot}%{gap_archdir}/bin
cp -p zgap %{buildroot}%{gap_archdir}/bin

%check
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g

%files
%doc CHANGES.md README.md
%license COPYRIGHT.md LICENSE
%{gap_archdir}/bin/zgap
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
