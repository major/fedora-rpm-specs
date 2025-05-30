# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hxt
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

Name:           ghc-%{pkg_name}
Version:        9.3.1.22
Release:        %autorelease
Summary:        A collection of tools for processing XML with Haskell

License:        MIT
URL:            https://hackage.haskell.org/package/hxt
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hxt-charproperties-devel
BuildRequires:  ghc-hxt-regex-xmlschema-devel
BuildRequires:  ghc-hxt-unicode-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-parsec-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hxt-charproperties-prof
BuildRequires:  ghc-hxt-regex-xmlschema-prof
BuildRequires:  ghc-hxt-unicode-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-parsec-prof
%endif
# End cabal-rpm deps

%description
The Haskell XML Toolbox bases on the ideas of HaXml and HXML, but introduces a
more general approach for processing XML with Haskell. The Haskell XML Toolbox
uses a generic data model for representing XML documents, including the DTD
subset and the document subset, in Haskell. It contains a validating XML
parser, a HTML parser, namespace support, an XPath expression evaluator, an
XSLT library, a RelaxNG schema validator and funtions for serialization and
deserialization of user defined data. The library makes extensive use of the
arrow approach for processing XML. Since version 9 the toolbox is partitioned
into various (sub-)packages. This package contains the core functionality,
hxt-curl, hxt-tagsoup, hxt-relaxng, hxt-xpath, hxt-xslt, hxt-regex-xmlschema
contain the extensions. hxt-unicode contains encoding and decoding functions,
hxt-charproperties char properties for unicode and XML. Changes from 9.3.1.21:
ghc-9.0 compatibility

Changes from 9.3.1.20: ghc 8.10 and 9.0 compatibility, tuple picker up to
24-tuples, Either instance for xpickle

Changes from 9.3.1.19: ghc-8.8.2 compatibility


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc examples


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
