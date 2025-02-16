%global pkgname digraphs
%global giturl  https://github.com/digraphs/Digraphs

Name:           gap-pkg-%{pkgname}
Version:        1.10.0
Release:        %autorelease
Summary:        GAP package for digraphs and multidigraphs

# The project as a whole is GPL-3.0-or-later.
# The bundled copy of bliss is LGPL-3.0-only.
License:        GPL-3.0-or-later AND LGPL-3.0-only
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://digraphs.github.io/Digraphs/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-datastructures
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-nautytracesinterface
BuildRequires:  gap-pkg-orb
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  planarity-devel
BuildRequires:  tex(a4wide.sty)
BuildRequires:  xdg-utils

Requires:       gap-pkg-datastructures%{?_isa}
Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}

Recommends:     gap-pkg-grape%{?_isa}
Recommends:     gap-pkg-nautytracesinterface%{?_isa}
Recommends:     graphviz

# The bundled copy of bliss has been modified for better integration with GAP
Provides:       bundled(bliss) = 0.73

%description
The Digraphs package is a GAP package containing methods for graphs,
digraphs, and multidigraphs.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Digraphs documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

%conf
# Make sure the bundled planarity is not used
rm -fr extern/edge-addition-planarity-suite-Version_3.0.1.0

%build
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules \
  --with-external-planarity
%make_build

# Build the documentation
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a bin data gap notebooks tst VERSIONS *.g \
   %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
# The "extreme" tests take a long time, so just run the "standard" tests
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" tst/teststandard.g
rm -fr ../pkg

%files
%doc CHANGELOG.md README.md
%license GPL LICENSE
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/data/
%{gap_archdir}/pkg/%{pkgname}/gap/
%{gap_archdir}/pkg/%{pkgname}/notebooks/
%{gap_archdir}/pkg/%{pkgname}/tst/
%{gap_archdir}/pkg/%{pkgname}/VERSIONS

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
