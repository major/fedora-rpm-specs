%global _docdir_fmt %{name}

Name:		gappa
Version:	1.5.0
Release:	%autorelease
Summary:	Prove programs with floating-point or fixed-point arithmetic

License:	GPL-3.0-only OR CECILL-2.1
URL:		https://gappa.gitlabpages.inria.fr/
VCS:		git:https://gitlab.inria.fr/gappa/gappa.git
Source:		%{url}/releases/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:	bison
BuildRequires:	boost-devel
BuildRequires:	flex
BuildRequires:	gcc-c++
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
BuildRequires:	%{py3_dist sphinx}
BuildRequires:	remake

%description
Gappa is a tool intended to help verifying and formally prove
properties on numerical programs and circuits handling floating-point
or fixed-point arithmetic.  This tool manipulates logical formulas
stating the enclosures of expressions in some intervals.  Through the
use of rounding operators as part of the expressions, Gappa is specially
designed to deal with formulas that could appear when certifying numerical
codes. In particular, Gappa makes it simple to bound computational errors
due to floating-point arithmetic.  The tool and its documentation were
written by Guillaume Melquiond.

%package doc
Summary:	Documentation for gappa
BuildArch:	noarch
# In addition to the project license, the Javascript and CSS bundled with the
# documentation has the following licenses:
# - searchindex.js: BSD-2-Clause
# - _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# - _static/alabaster.css: BSD-3-Clause
# - _static/basic.css: BSD-2-Clause
# - _static/custom.css: BSD-3-Clause
# - _static/doctools.js: BSD-2-Clause
# - _static/documentation_options.js: BSD-2-Clause
# - _static/file.png: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/minus.png: BSD-2-Clause
# - _static/plus.png: BSD-2-Clause
# - _static/searchtools.js: BSD-2-Clause
# - _static/underscore*.js: MIT
License:	(GPL-3.0-only OR CECILL-2.1) AND MIT AND BSD-2-Clause AND BSD-3-Clause

%description doc
Documentation for gappa.

%prep
%autosetup

%conf
# Increase the test timeout for ARM
sed -i 's/timeout 5/&0/' Remakefile.in

%build
%configure
# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake
remake -d %{?_smp_mflags}
remake -d doc/html/index.html
rm doc/html/.buildinfo

%install
DESTDIR=%{buildroot} remake install

%check
remake check

%files
%{_bindir}/gappa
%doc README.md NEWS.md
%license COPYING COPYING.GPL

%files doc
%doc AUTHORS doc/html

%changelog
%autochangelog
