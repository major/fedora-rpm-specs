%global pkgname toric
%global upname  Toric
%global giturl  https://github.com/gap-packages/toric

Name:           gap-pkg-%{pkgname}
Version:        1.9.6
Release:        %autorelease
Summary:        Computations with toric varieties in GAP

License:        MIT
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/toric/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
Toric implements some computations related to toric varieties and
combinatorial geometry in GAP.  Affine toric varieties can be created
and related information about them can be calculated.

%package doc
# The content is MIT.  The remaining licenses cover the various fonts embedded
# in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        MIT AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Toric documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p1 -n %{upname}-%{version}

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{upname}/
%{gap_libdir}/pkg/%{upname}/*.g
%{gap_libdir}/pkg/%{upname}/lib/
%{gap_libdir}/pkg/%{upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
