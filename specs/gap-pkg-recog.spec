%global gap_pkgname recog
%global giturl      https://github.com/gap-packages/recog

Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.1
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

BuildRequires:  gap(atlasrep) >= 2.1.0
BuildRequires:  gap(autodoc) >= 2019.07.03
BuildRequires:  gap(factint) >= 1.6.3
BuildRequires:  gap(forms) >= 1.2.11
BuildRequires:  gap(genss) >= 1.6.8
BuildRequires:  gap(orb) >= 4.9.0
BuildRequires:  gap-devel >= 4.13

Requires:       gap(atlasrep) >= 2.1.0
Requires:       gap(factint) >= 1.6.3
Requires:       gap(forms) >= 1.2.11
Requires:       gap(genss) >= 1.6.8
Requires:       gap(orb) >= 4.9.0
Requires:       gap-core >= 4.13

Provides:       gap(recog) = %{version}-%{release}

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
rm -fr %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/tst/working/veryslow
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g
cp -a tst/working/veryslow %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/tst/working

%files
%doc CHANGES NOTES README.md TODO
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
