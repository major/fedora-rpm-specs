%global gap_pkgname francy
%global giturl      https://github.com/gap-packages/francy

Name:           gap-pkg-%{gap_pkgname}
Version:        2.0.3
Release:        %autorelease
Summary:        Framework for interactive discrete mathematics

License:        MIT
URL:            https://gap-packages.github.io/francy/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples gap notebooks schema tst
BuildOption(check): tst/testall.g

BuildRequires:  elinks
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-json
BuildRequires:  gap-pkg-jupyterkernel
BuildRequires:  gap-pkg-uuid
BuildRequires:  xdg-utils

Requires:       gap-pkg-json
Requires:       gap-pkg-jupyterkernel
Requires:       gap-pkg-uuid
Requires:       xdg-utils

%description
Francy is a package for GAP and provides a framework for Interactive Discrete
Mathematics.

Unlike xgap, Francy is not linked with any GUI framework and instead, this
package generates a semantic model that can be used to produce a graphical
representation using any other framework / language.

There is a JavaScript implementation of the graphical representation that
works on Jupyter, embedded in a Web page or as a Desktop Application (e.g.
using electron).

%package doc
# The content is MIT.  The remaining licenses cover the various fonts embedded
# in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MIT AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Francy documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%conf
# Call xdg-open instead of open
sed -i.orig 's/"open "/"xdg-open "/' gap/canvas.gi
touch -r gap/canvas.gi.orig gap/canvas.gi
rm gap/canvas.gi.orig

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/schema/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%docdir %{gap_libdir}/pkg/%{gap_upname}/notebooks/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/notebooks/

%changelog
%autochangelog
