%global gap_pkgname qpa
%global giturl      https://github.com/gap-packages/qpa

Name:           gap-pkg-%{gap_pkgname}
Version:        1.37
Release:        %autorelease
Summary:        GAP package for quivers and path algebras

License:        GPL-2.0-or-later
URL:            https://folk.ntnu.no/oyvinso/QPA/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): examples lib tst version
BuildOption(check): tst/testall.g

BuildRequires:  GAPDoc-latex
BuildRequires:  gap(gbnp) >= 0.9.5
BuildRequires:  gap-devel >= 4.11
BuildRequires:  tex(beamer.cls)
BuildRequires:  tex(pcrr8t.tfm)
BuildRequires:  tex(textpos.sty)
BuildRequires:  tex(xy.sty)

Requires:       gap(gbnp) >= 0.9.5
Requires:       gap-core >= 4.11

Provides:       gap(qpa) = %{version}-%{release}

%description
This package carries out computations for finite dimensional quotients of path
algebras over the fields that are available in GAP.  QPA stands for "Quivers
 and Path Algebras".

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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%build -a
cd doc/gap-days-lectures
pdflatex -interaction=nonstopmode lecture1
pdflatex -interaction=nonstopmode lecture1
pdflatex -interaction=nonstopmode lecture2
pdflatex -interaction=nonstopmode lecture2
pdflatex -interaction=nonstopmode lecture3
pdflatex -interaction=nonstopmode lecture3
pdflatex -interaction=nonstopmode lecture4a
pdflatex -interaction=nonstopmode lecture4a

%install -a
%gap_copy_docs -d doc/gap-days-lectures

%files
%doc CHANGES README
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/
%{gap_libdir}/pkg/%{gap_upname}/version

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
