# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Break a circular dependency on ocaml-ppx-jane
%bcond test 0

Name:           ocaml-ppx-expect
Version:        0.17.3
Release:        %autorelease
Summary:        Framework for writing tests in OCaml

License:        MIT
URL:            https://github.com/janestreet/ppx_expect
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_expect-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppx-here-devel >= 0.17
BuildRequires:  ocaml-ppx-inline-test-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0
BuildRequires:  ocaml-stdio-devel >= 0.17

%if %{with test}
BuildRequires:  ocaml-ppx-jane-devel
%endif

%description
Ppx_expect is a framework for writing tests in OCaml, similar to Cram
(https://bitheap.org/cram/).  Ppx_expect mimics the existing inline
tests framework with the `let%%expect_test` construct.  The body of an
expect-test can contain output-generating code, interleaved with
`%%expect` extension expressions to denote the expected output.

When run, these tests will pass iff the output matches what was
expected.  If a test fails, a corrected file with the suffix
".corrected" will be produced with the actual output, and the
`inline_tests_runner` will output a diff.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-here-devel%{?_isa}
Requires:       ocaml-ppx-inline-test-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-stdio-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_expect-%{version}

%build
%dune_build

%install
%dune_install

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.mdx
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
