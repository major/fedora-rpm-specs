%global pkgname AutoDoc
%global giturl  https://github.com/gap-packages/AutoDoc

# When bootstrapping a new architecture, there is no gap-pkg-io package yet,
# since it requires this package to build.  We only need it for testing this
# package, not for building it, so use the following procedure:
# 1. Do a bootstrap build of this package.
# 2. Build gap-pkg-io.
# 3. Do a normal build of this packages, which includes running the tests.
%bcond bootstrap 0

Name:           gap-pkg-autodoc
Version:        2023.06.19
Release:        %autorelease
Summary:        Generate documentation from GAP source code

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/AutoDoc/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

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
This package is an add-on to GAPDoc that enables generating
documentation from GAP source code.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
mkdir ../pkg
ln -s ../AutoDoc-%{version} ../pkg
gap -l "$PWD/..;" --bare -c 'LoadPackage("GAPDoc");' makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap makefile tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs
cp -p doc/*.xml %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc

%if %{without bootstrap}
%check
gap -l '%{buildroot}%{gap_libdir};' --bare -c 'LoadPackage("GAPDoc");' tst/testall.g
%endif

%files
%doc CHANGES README.md
%license COPYRIGHT LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/makefile
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
