%global pkgname qpa
%global giturl  https://github.com/gap-packages/qpa

Name:           gap-pkg-%{pkgname}
Version:        1.35
Release:        %autorelease
Summary:        GAP package for quivers and path algebras

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://folk.ntnu.no/oyvinso/QPA/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-gbnp
BuildRequires:  tex(beamer.cls)
BuildRequires:  tex(pcrr8t.tfm)
BuildRequires:  tex(textpos.sty)
BuildRequires:  tex(xy.sty)

Requires:       gap-pkg-gbnp

%description
This package carries out computations for finite dimensional quotients
of path algebras over the fields that are available in GAP.  QPA stands
for "Quivers and Path Algebras".

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
# XY: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        QPA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%conf
# Fix a broken reference
sed -i 's/Basic Construction/Constructing Quivers/' doc/chapter_path_algebras.xml

%build
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

cd doc/gap-days-lectures
pdflatex lecture1
pdflatex lecture1
pdflatex lecture2
pdflatex lecture2
pdflatex lecture3
pdflatex lecture3
pdflatex lecture4a
pdflatex lecture4a

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g examples lib tst version %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs
%gap_copy_docs -d doc/gap-days-lectures

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc CHANGES README
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/
%{gap_libdir}/pkg/%{pkgname}/version

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/

%changelog
%autochangelog
