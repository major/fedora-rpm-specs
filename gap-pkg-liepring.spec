%global pkgname liepring

Name:           gap-pkg-%{pkgname}
Version:        2.8
Release:        %autorelease
Summary:        Database and algorithms for Lie p-rings

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/liepring/
VCS:            https://github.com/gap-packages/liepring
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-liering
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-singular
BuildRequires:  tth

Requires:       gap-pkg-liering
Requires:       gap-pkg-singular

%description
The main object of the LiePRing package is to provide access to the
nilpotent Lie rings of order p^n for p>2 and n<=7.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        LiePRing documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Fix paths
sed -i 's,\.\./\.\./\.\./,%{gap_libdir}/,' doc/make_doc

%build
export LC_ALL=C.UTF-8
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm ../../doc

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap htm lib tst VERSION %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};%{gap_libdir}" tst/testall.g

%files
%doc README.md
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/htm/
%exclude %{gap_libdir}/pkg/%{pkgname}/lib/notes/
%exclude %{gap_libdir}/pkg/%{pkgname}/lib/dim6/notes/
%exclude %{gap_libdir}/pkg/%{pkgname}/lib/dim7/2gen/notes/
%exclude %{gap_libdir}/pkg/%{pkgname}/lib/dim7/3gen/notes/
%exclude %{gap_libdir}/pkg/%{pkgname}/lib/dim7/4gen/notes/
%exclude %{gap_libdir}/pkg/%{pkgname}/lib/dim7/5gen/notes/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/lib/notes/
%docdir %{gap_libdir}/pkg/%{pkgname}/lib/dim6/notes/
%docdir %{gap_libdir}/pkg/%{pkgname}/lib/dim7/2gen/notes/
%docdir %{gap_libdir}/pkg/%{pkgname}/lib/dim7/3gen/notes/
%docdir %{gap_libdir}/pkg/%{pkgname}/lib/dim7/4gen/notes/
%docdir %{gap_libdir}/pkg/%{pkgname}/lib/dim7/5gen/notes/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/lib/notes/
%{gap_libdir}/pkg/%{pkgname}/lib/dim6/notes/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/2gen/notes/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/3gen/notes/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/4gen/notes/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/5gen/notes/

%changelog
%autochangelog
