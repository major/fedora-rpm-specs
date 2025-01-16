%global pkgname francy
%global giturl  https://github.com/gap-packages/francy

Name:           gap-pkg-%{pkgname}
Version:        2.0.3
Release:        %autorelease
Summary:        Framework for interactive discrete mathematics

License:        MIT
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/francy/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

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
Francy is a package for GAP and provides a framework for Interactive
Discrete Mathematics.

Unlike xgap, Francy is not linked with any GUI framework and instead,
this package generates a semantic model that can be used to produce a
graphical representation using any other framework / language.

There is a JavaScript implementation of the graphical representation
that works on Jupyter, embedded in a Web page or as a Desktop Application
(e.g. using electron).

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

%conf
# Call xdg-open instead of open
sed -i.orig 's/"open "/"xdg-open "/' gap/canvas.gi
touch -r gap/canvas.gi.orig gap/canvas.gi
rm gap/canvas.gi.orig

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g examples gap notebooks schema tst \
   %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/schema/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%docdir %{gap_libdir}/pkg/%{pkgname}/notebooks/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/notebooks/

%changelog
%autochangelog
