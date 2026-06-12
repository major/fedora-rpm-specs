%global gap_pkgname jupyterviz
%global giturl      https://github.com/nathancarter/jupyterviz

Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.6
Release:        %autorelease
Summary:        Jupyter notebook visualization tools for GAP

License:        GPL-2.0-or-later
URL:            https://nathancarter.github.io/jupyterviz/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
# Update the python scripts for python 3
# https://github.com/nathancarter/jupyterviz/pull/21
Patch:          %{name}-python3.patch

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): *.ipynb examples lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc)
BuildRequires:  gap(gapdoc) >= 1.3
BuildRequires:  gap(json) >= 2.0.0
BuildRequires:  gap(jupyterkernel)
BuildRequires:  gap-devel >= 4.9
BuildRequires:  python3-devel

Requires:       gap(json) >= 2.0.0
Requires:       gap(jupyterkernel)
Requires:       gap-core >= 4.9
Requires:       xdg-utils

Provides:       gap(JupyterViz) = %{version}-%{release}
Provides:       gap(jupyterviz) = %{version}-%{release}

%description
This package adds visualization tools to GAP for use in Jupyter notebooks.
These include standard line and bar graphs, pie charts, scatter plots, and
graphs in the vertices-and-edges sense.

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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -p0 -n %{gap_upname}-%{version}

%build -p
python3 extract_examples.py

%files
%doc CHANGES README.md
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/*.ipynb
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
