# When bootstrapping a new architecture, there is no gap-pkg-io package yet,
# since it requires this package to build.  We only need it for testing this
# package, not for building it, so use the following procedure:
# 1. Do a bootstrap build of this package.
# 2. Build gap-pkg-io.
# 3. Do a normal build of this packages, which includes running the tests.
%bcond bootstrap 0

%global gap_pkgname    autodoc
%global gap_upname     AutoDoc
%global gap_skip_check %{?with_bootstrap}
%global giturl         https://github.com/gap-packages/AutoDoc

Name:           gap-pkg-%{gap_pkgname}
Version:        2025.05.09
Release:        %autorelease
Summary:        Generate documentation from GAP source code

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/AutoDoc/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs .. --bare -c 'LoadPackage("GAPDoc");'
BuildOption(install): gap makefile tst
BuildOption(check): --bare -c 'LoadPackage("GAPDoc");' tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
%if %{without bootstrap}
BuildRequires:  gap-pkg-io
%endif
BuildRequires:  tex(a4wide.sty)

# AUTODOC_CurrentDirectory invokes pwd
Requires:       coreutils
Requires:       gap-core
Requires:       GAPDoc-latex

%description
This package is an add-on to GAPDoc that enables generating documentation from
GAP source code.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        AutoDoc documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%install -a
cp -p doc/*.xml %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/doc

%files
%doc CHANGES.md README.md
%license COPYRIGHT LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/makefile
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
