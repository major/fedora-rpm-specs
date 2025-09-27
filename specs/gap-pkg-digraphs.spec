%global gap_pkgname digraphs
%global giturl      https://github.com/digraphs/Digraphs

Name:           gap-pkg-%{gap_pkgname}
Version:        1.12.2
Release:        %autorelease
Summary:        GAP package for digraphs and multidigraphs

# The project as a whole is GPL-3.0-or-later.
# The bundled copy of bliss is LGPL-3.0-only.
License:        GPL-3.0-or-later AND LGPL-3.0-only
URL:            https://digraphs.github.io/Digraphs/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
# Compatibility with planarity 4.x
Patch:          %{name}-planarity4.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): bin data gap notebooks tst VERSIONS
BuildOption(check): tst/teststandard.g

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
BuildRequires:  pkgconfig(libplanarity)
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
The Digraphs package is a GAP package containing methods for graphs, digraphs,
and multidigraphs.

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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%conf
# Make sure the bundled planarity is not used
rm -fr extern/edge-addition-planarity-suite-Version_3.0.1.0

%build -p
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules \
  --with-external-planarity
%make_build

%check -p
cp -p doc/*.xml %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/doc

%check -a
rm %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/doc/*.xml

%files
%doc CHANGELOG.md README.md
%license GPL LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/data/
%{gap_archdir}/pkg/%{gap_upname}/gap/
%{gap_archdir}/pkg/%{gap_upname}/notebooks/
%{gap_archdir}/pkg/%{gap_upname}/tst/
%{gap_archdir}/pkg/%{gap_upname}/VERSIONS

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
