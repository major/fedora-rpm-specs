# NOTE: There is no %%check section, because the tests require administrator
# privileges so that non-default values can be written to:
# - /proc/sys/kernel/core_pattern
# - /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

Name:           ocaml-monolith
Version:        20250922
Release:        %autorelease
Summary:        Framework for strong random testing of OCaml libraries

License:        LGPL-3.0-or-later
URL:            https://gitlab.inria.fr/fpottier/monolith
VCS:            git:%{url}.git
Source:         %{url}/-/archive/%{version}/monolith-%{version}.tar.bz2

# The ocaml-afl-persistent package is currently only built for x86_64
ExclusiveArch:  %{x86_64}

BuildRequires:  ocaml >= 4.12
BuildRequires:  ocaml-afl-persistent-devel >= 1.3
BuildRequires:  ocaml-dune >= 3.11
BuildRequires:  ocaml-pprint-devel >= 20200410

%description
Monolith offers facilities for testing an OCaml library (for instance, a data
structure implementation) by comparing it against a reference implementation.
It can be used to perform either random testing or fuzz testing.  Fuzz testing
relies on the external tool afl-fuzz.

The user must describe what types and operations the library provides.  Under
the best circumstances, this requires 2-3 lines of code per type or operation.
The user must also provide a reference implementation and a candidate
implementation of the library.

Then, like a monkey typing on a keyboard, Monolith attempts to exercise the
library in every possible way, in the hope of discovering a sequence of
operations that leads to an unexpected behavior (that is, a situation where
the library either raises an unexpected exception or returns an incorrect
result).  If such a scenario is discovered, it is printed in the form of an
OCaml program, so as to help the user reproduce the problem.

Monolith assumes that the candidate implementation behaves in a deterministic
way.  (Without this assumption, one cannot hope to reliably produce a
problematic scenario.)  It does however allow nondeterministic specifications,
that is, situations where the candidate implementation is allowed to behave in
several possible ways.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-afl-persistent-devel%{?_isa}
Requires:       ocaml-pprint-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n monolith-%{version}

%build
%dune_build

%install
%dune_install

%files -f .ofiles
%doc AUTHORS.md CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
%autochangelog
