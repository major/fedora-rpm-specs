# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

%global pkgname jupyterkernel
%global upname  JupyterKernel
%global giturl  https://github.com/gap-packages/JupyterKernel

Name:           gap-pkg-%{pkgname}
Version:        1.5.1
Release:        %autorelease
Summary:        Jupyter kernel written in GAP

License:        BSD-3-Clause
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/JupyterKernel/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-crypting
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-json
BuildRequires:  gap-pkg-uuid
BuildRequires:  gap-pkg-zeromqinterface
BuildRequires:  %{py3_dist jupyter-client}
BuildRequires:  %{py3_dist notebook}

Requires:       gap-pkg-crypting
Requires:       gap-pkg-io
Requires:       gap-pkg-json
Requires:       gap-pkg-uuid
Requires:       gap-pkg-zeromqinterface
Requires:       python-jupyter-filesystem

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{_bindir}
cp -p bin/jupyter-kernel-gap %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a *.g demos gap tst %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

mkdir -p %{buildroot}%{_datadir}/jupyter/kernels
cp -a etc/jupyter %{buildroot}%{_datadir}/jupyter/kernels/gap-4

mkdir -p %{buildroot}%{_datadir}/jupyter/nbextensions
cp -a etc/gap-mode %{buildroot}%{_datadir}/jupyter/nbextensions

mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d
cp -p etc/gap-mode.json %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README.md
%license COPYRIGHT.md LICENSE
%{_bindir}/jupyter-kernel-gap
%{_datadir}/jupyter/nbextensions/gap-mode/
%{_datadir}/jupyter/kernels/gap-4/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/gap-mode.json
%dir %{gap_libdir}/pkg/%{upname}/
%{gap_libdir}/pkg/%{upname}/*.g
%{gap_libdir}/pkg/%{upname}/gap/
%{gap_libdir}/pkg/%{upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{upname}/demos/
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/demos/
%{gap_libdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
