# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %{ocaml_native_compiler}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# TESTING NOTE: The testsuite requires that gappalib-coq be installed already.
# Hence, we cannot run it on the koji builders.  The maintainer should always
# install the package and run "remake check" manually before committing.

%global gappadir %{ocamldir}/coq/user-contrib/Gappa
%global coqver  8.20.1
%global commit  ae99b9db1a8d4effbbb7965e99e43e697545d8a1
%global giturl  https://gitlab.inria.fr/gappa/coq

Name:           gappalib-coq
Version:        1.6.0
Release:        %autorelease
Summary:        Coq support library for gappa

License:        LGPL-3.0-or-later
URL:            https://gappa.gitlabpages.inria.fr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  coq = %{coqver}
BuildRequires:  flocq
BuildRequires:  gappa
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-zarith-devel
BuildRequires:  remake

Requires:       coq%{?_isa} = %{coqver}
Requires:       flocq
Requires:       gappa

%description
This support library provides vernacular files so that the certificates
Gappa generates can be imported by the Coq proof assistant.  It also
provides a "gappa" tactic that calls Gappa on the current Coq goal.

Gappa (Génération Automatique de Preuves de Propriétés Arithmétiques --
automatic proof generation of arithmetic properties) is a tool intended
to help verifying and formally proving properties on numerical programs
dealing with floating-point or fixed-point arithmetic.

%package source
Summary:        Source Coq files
Requires:       %{name} = %{version}-%{release}

%description source
This package contains the source Coq files for gappalib-coq.  These
files are not needed to use gappalib-coq.  They are made available for
informational purposes.

%prep
%autosetup -n coq-%{name}-%{version}-%{commit}

%conf
# Enable debuginfo
sed -i 's/-rectypes/-g &/' Remakefile.in

# Generate the configure script
autoconf -f

%build
# The %%configure macro specifies --libdir, which this configure script
# unfortunately uses to identify where the Coq files should go.  We want
# the default (i.e., ask coq itself where they go).
./configure --prefix=%{_prefix} --datadir=%{_datadir}

# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake

remake -d %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{gappadir}
DESTDIR=%{buildroot} remake install

# Also install the source files
cp -p src/*.v  %{buildroot}%{gappadir}

%check
remake check

%files
%doc AUTHORS NEWS.md README.md
%license COPYING
%{_libdir}/ocaml/coq-gappa/
%{gappadir}
%exclude %{gappadir}/*.v

%files source
%{gappadir}/*.v

%changelog
%autochangelog
