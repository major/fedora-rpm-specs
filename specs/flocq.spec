# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %{ocaml_native_compiler}

# This package is installed into an archful location, but contains no ELF
# objects.
%global debug_package %{nil}

%global flocqdir %{ocamldir}/coq/user-contrib/Flocq
%global coqver  8.20.1
%global commit  e1443068c65f644989e1f4eefecd72084de4e13d
%global giturl  https://gitlab.inria.fr/flocq/flocq

Name:           flocq
Version:        4.2.1
Release:        %autorelease
Summary:        Formalization of floating point numbers for Coq

License:        LGPL-3.0-or-later
URL:            https://flocq.gitlabpages.inria.fr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  remake
BuildRequires:  coq = %{coqver}
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
Requires:       coq%{?_isa} = %{coqver}

%description
Flocq (Floats for Coq) is a floating-point formalization for the Coq
system.  It provides a comprehensive library of theorems on a
multi-radix multi-precision arithmetic.  It also supports efficient
numerical computations inside Coq.

%package source
Summary:        Source Coq files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description source
This package contains the source Coq files for flocq.  These files are
not needed to use flocq.  They are made available for informational
purposes.

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

# Workaround for a stack overflow compiling one file on ppc64le when
# using OCaml 5.2.  I observed this only happens with coqc, not with
# coqc.byte, so use coqc.byte for this one file.
#
# File "./src/Core/Digits.v", line 948, characters 0-4:
# Error: Stack overflow.
# Failed to build src/Core/Digits.vo
%ifarch %{power64}
remake -d %{?_smp_mflags} all ||: ;# expected to fail
coqc.byte -q -R src Flocq src/Core/Digits.v
%endif

remake -d %{?_smp_mflags} all doc

%install
sed -i "s,%{_libdir},$RPM_BUILD_ROOT%{_libdir}," Remakefile
remake install

# Also install the source files
cp -p src/*.v $RPM_BUILD_ROOT%{flocqdir}
cp -p src/Calc/*.v $RPM_BUILD_ROOT%{flocqdir}/Calc
cp -p src/Core/*.v $RPM_BUILD_ROOT%{flocqdir}/Core
cp -p src/IEEE754/*.v $RPM_BUILD_ROOT%{flocqdir}/IEEE754
cp -p src/Pff/*.v $RPM_BUILD_ROOT%{flocqdir}/Pff
cp -p src/Prop/*.v $RPM_BUILD_ROOT%{flocqdir}/Prop

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
