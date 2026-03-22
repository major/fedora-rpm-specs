# This package is installed into an archful location, but contains no ELF
# objects.
%global debug_package %{nil}

%global flocqdir %{ocamldir}/coq/user-contrib/Flocq
%global rocqver 9.1.1
%global commit  7aab8f55bceec0cfafc3b3bc0e77e0dbb5a70c5f
%global giturl  https://gitlab.inria.fr/flocq/flocq

Name:           flocq
Version:        4.2.2
Release:        %autorelease
Summary:        Formalization of floating point numbers for Coq

License:        LGPL-3.0-or-later
URL:            https://flocq.gitlabpages.inria.fr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

# Rocq's plugin architecture requires cmxs files
ExclusiveArch:  %{ocaml_native_compiler}

BuildRequires:  autoconf
BuildRequires:  coq-core-compat
BuildRequires:  gcc-c++
BuildRequires:  remake
BuildRequires:  rocq = %{rocqver}
BuildRequires:  rocq-stdlib
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

Requires:       rocq%{?_isa} = %{rocqver}
Requires:       rocq-stdlib%{?_isa}

%description
Flocq (Floats for Rocq) is a floating-point formalization for the Rocq system.
It provides a comprehensive library of theorems on a multi-radix
multi-precision arithmetic.  It also supports efficient numerical computations
inside Rocq.

%package source
Summary:        Source Rocq files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description source
This package contains the source Rocq files for flocq.  These files are not
needed to use flocq.  They are made available for informational purposes.

%prep
%autosetup -n %{name}-%{name}-%{version}-%{commit}

%conf
# Point to the local coqdoc files
sed -i 's,\(--coqlib \)[^[:blank:]]*,\1%{ocamldir}/coq,' Remakefile.in

# Generate the configure script
autoconf -f

%build
# We do NOT want to specify --libdir, and we don't need CFLAGS, etc.
./configure

# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake

remake -d %{?_smp_mflags} all doc

%install
sed -i 's,%{_libdir},%{buildroot}%{_libdir},' Remakefile
remake install

# Also install the source files
cp -p src/*.v %{buildroot}%{flocqdir}
cp -p src/Calc/*.v %{buildroot}%{flocqdir}/Calc
cp -p src/Core/*.v %{buildroot}%{flocqdir}/Core
cp -p src/IEEE754/*.v %{buildroot}%{flocqdir}/IEEE754
cp -p src/Pff/*.v %{buildroot}%{flocqdir}/Pff
cp -p src/Prop/*.v %{buildroot}%{flocqdir}/Prop

%files
%doc AUTHORS NEWS.md README.md html
%license COPYING
%{flocqdir}
%exclude %{flocqdir}/*.v
%exclude %{flocqdir}/*/*.v

%files source
%{flocqdir}/*.v
%{flocqdir}/Calc/*.v
%{flocqdir}/Core/*.v
%{flocqdir}/IEEE754/*.v
%{flocqdir}/Pff/*.v
%{flocqdir}/Prop/*.v

%changelog
%autochangelog
