%global gap_pkgname recog
%global giturl      https://github.com/gap-packages/recog

Name:           gap-pkg-%{gap_pkgname}
Version:        1.4.4
Release:        %autorelease
Summary:        Group recognition methods

License:        GPL-3.0-or-later
URL:            https://gap-packages.github.io/recog/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): contrib examples gap tst

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-factint
BuildRequires:  gap-pkg-forms
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-orb
BuildRequires:  gap-pkg-tomlib

Requires:       gap-pkg-atlasrep
Requires:       gap-pkg-factint
Requires:       gap-pkg-forms
Requires:       gap-pkg-genss
Requires:       gap-pkg-orb

%description
This is a GAP package for group recognition.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Recog documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -b 1

%check
# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

# Do not run the very slow tests
gap -l '%{buildroot}%{gap_libdir};' tst/testquick.g
gap -l '%{buildroot}%{gap_libdir};' tst/testslow.g

%files
%doc CHANGES NOTES README.md TODO WISHLIST
%license COPYRIGHT LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/contrib/
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
