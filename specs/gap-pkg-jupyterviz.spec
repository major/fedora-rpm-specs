%global pkgname jupyterviz
%global giturl  https://github.com/nathancarter/jupyterviz

Name:           gap-pkg-%{pkgname}
Version:        1.5.6
Release:        %autorelease
Summary:        Jupyter notebook visualization tools for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://nathancarter.github.io/jupyterviz/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Update the python scripts for python 3
# https://github.com/nathancarter/jupyterviz/pull/21
Patch:          %{name}-python3.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-json
BuildRequires:  gap-pkg-jupyterkernel
BuildRequires:  python3-devel

Requires:       gap-pkg-json
Requires:       gap-pkg-jupyterkernel

%description
This package adds visualization tools to GAP for use in Jupyter
notebooks.  These include standard line and bar graphs, pie charts,
scatter plots, and graphs in the vertices-and-edges sense.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Jupyter visualization tools for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
python3 extract_examples.py
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g *.ipynb examples lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc CHANGES README.md
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/*.ipynb
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/

%changelog
%autochangelog
