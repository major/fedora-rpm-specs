# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

%global gap_pkgname jupyterkernel
%global gap_upname  JupyterKernel
%global giturl      https://github.com/gap-packages/JupyterKernel

Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.1
Release:        %autorelease
Summary:        Jupyter kernel written in GAP

License:        BSD-3-Clause
URL:            https://gap-packages.github.io/JupyterKernel/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): demos gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2014.03.27
BuildRequires:  gap(crypting) >= 0.9
BuildRequires:  gap(gapdoc) >= 1.6.1
BuildRequires:  gap(io) >= 4.5.4
BuildRequires:  gap(json) >= 2.0.0
BuildRequires:  gap(uuid) >= 0.6
BuildRequires:  gap(zeromqinterface) >= 0.10
BuildRequires:  gap-devel >= 4.10

Requires:       gap(crypting) >= 0.9
Requires:       gap(io) >= 4.5.4
Requires:       gap(json) >= 2.0.0
Requires:       gap(uuid) >= 0.6
Requires:       gap(zeromqinterface) >= 0.10
Requires:       gap-core >= 4.10
Requires:       python-jupyter-filesystem
Requires:       %{py3_dist notebook} >= 5.3

Provides:       gap(jupyterkernel) = %{version}-%{release}
Provides:       gap(JupyterKernel) = %{version}-%{release}

%description
This package implements the Jupyter protocol in GAP.

%package doc
# The content is BSD-3-Clause.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        BSD-3-Clause AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Jupyter kernel for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%install -a
mkdir -p %{buildroot}%{_bindir}
cp -p bin/jupyter-kernel-gap %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/jupyter/kernels
cp -a etc/jupyter %{buildroot}%{_datadir}/jupyter/kernels/gap-4

mkdir -p %{buildroot}%{_datadir}/jupyter/nbextensions
cp -a etc/gap-mode %{buildroot}%{_datadir}/jupyter/nbextensions

mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d
cp -p etc/gap-mode.json %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d

%files
%doc README.md
%license COPYRIGHT.md LICENSE
%{_bindir}/jupyter-kernel-gap
%{_datadir}/jupyter/nbextensions/gap-mode/
%{_datadir}/jupyter/kernels/gap-4/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/gap-mode.json
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/demos/
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/demos/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
