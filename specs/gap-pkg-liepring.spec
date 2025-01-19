%global pkgname liepring
%global giturl  https://github.com/gap-packages/liepring

Name:           gap-pkg-%{pkgname}
Version:        2.9.1
Release:        %autorelease
Summary:        Database and algorithms for Lie p-rings

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/liepring/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-liering
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-singular
BuildRequires:  tth

Requires:       gap-pkg-liering

Recommends:     gap-pkg-singular

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

%conf
# Fix paths
sed -i 's,\.\./\.\./\.\./,%{gap_libdir}/,' doc/make_doc

%build
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
gap -l '%{buildroot}%{gap_libdir};%{gap_libdir}' tst/testall.g

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%dir %{gap_libdir}/pkg/%{pkgname}/lib/
%dir %{gap_libdir}/pkg/%{pkgname}/lib/dim6/
%dir %{gap_libdir}/pkg/%{pkgname}/lib/dim7/
%dir %{gap_libdir}/pkg/%{pkgname}/lib/dim7/2gen/
%dir %{gap_libdir}/pkg/%{pkgname}/lib/dim7/3gen/
%dir %{gap_libdir}/pkg/%{pkgname}/lib/dim7/4gen/
%dir %{gap_libdir}/pkg/%{pkgname}/lib/dim7/5gen/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/lib/*.gi
%{gap_libdir}/pkg/%{pkgname}/lib/dim6/gap*
%{gap_libdir}/pkg/%{pkgname}/lib/dim6/stuff/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/2gen/gap*
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/2gen/group*
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/2gen/stuff/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/3gen/gap*
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/3gen/stuff/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/4gen/gap*
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/4gen/stuff/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/5gen/gap*
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/5gen/stuff/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/6gen/
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/gap*
%{gap_libdir}/pkg/%{pkgname}/lib/dim7/stuff/
%{gap_libdir}/pkg/%{pkgname}/lib/dim8/
%{gap_libdir}/pkg/%{pkgname}/tst/
%{gap_libdir}/pkg/%{pkgname}/VERSION

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
