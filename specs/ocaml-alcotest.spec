# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# To build all parts of alcotest requires the async, js_of_ocaml, and lwt
# packages.  The async package in particular requires many packages that test
# with alcotest.  We build only the base alcotest package to break the circular
# dependency.
%bcond async 0

%global srcname alcotest
%global giturl  https://github.com/mirage/alcotest

Name:           ocaml-%{srcname}
Version:        1.9.1
Release:        %autorelease
Summary:        Lightweight and colorful test framework for OCaml

License:        ISC
URL:            https://mirage.github.io/alcotest/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/%{srcname}-%{version}.tar.gz
# We neither need nor want the stdlib-shims or ocaml-syntax-shims packages in
# Fedora.  They are forward compatibility packages for older OCaml
# installations.  Patch them out instead.  Upstream does not want this patch
# until stdlib-shims and ocaml-syntax-shims are obsolete.
Patch:          0001-Drop-the-stdlib-shims-subpackage.patch

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-cmdliner-devel >= 1.2.0
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-fmt-devel >= 0.8.7
BuildRequires:  ocaml-re-devel >= 1.7.2
BuildRequires:  ocaml-uutf-devel >= 1.0.1

%if %{with async}
BuildRequires:  js-of-ocaml-compiler-devel >= 3.11.0
BuildRequires:  ocaml-async-devel >= 0.16.0
BuildRequires:  ocaml-async-kernel-devel
BuildRequires:  ocaml-async-unix-devel >= 0.16.0
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-core-devel >= 0.16.0
BuildRequires:  ocaml-core-unix-devel >= 0.16.0
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-lwt-devel
%endif

%description
Alcotest is a lightweight and colorful test framework.

Alcotest exposes a simple interface to perform unit tests, including a
simple `TESTABLE` module type, a `check` function to assert test
predicates, and a `run` function to perform a list of `unit -> unit`
test callbacks.

Alcotest provides quiet and colorful output where only faulty runs are
fully displayed at the end of the run (with the full logs ready to
inspect), with a simple (yet expressive) query language to select the
tests to run.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-uutf-devel%{?_isa}

%if %{with async}
Requires:       ocaml-async-devel
Requires:       ocaml-lwt-devel
%endif

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%dune_build %{!?with_async:-p alcotest}

%install
%dune_install %{!?with_async:alcotest}

%check
%dune_check %{!?with_async:-p alcotest}

%files -f .ofiles
%doc CHANGES.md README.md alcotest-help.txt
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
