%global giturl  https://github.com/mjambon/testo

Name:           ocaml-testo
Version:        0.4.0
Release:        %autorelease
Summary:        Test framework for OCaml

License:        ISC
URL:            https://testocaml.net/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/testo-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-dune >= 3.18
BuildRequires:  ocaml-fpath-devel
BuildRequires:  ocaml-lwt-devel >= 5.6.0
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-re-devel >= 1.10.0

%description
Testo is a test framework for OCaml that takes inspiration from its
predecessor alcotest and from pytest.  Features include:

- support for explicit XFAIL tests i.e. tests that are expected to fail,
  indicating that they should be fixed eventually;
- support for test snapshots i.e. persistent storage of captured stdout,
  stderr, or output files;
- reviewing and approving tests without rerunning them;
- nested test suites;
- various ways to select tests;
- parallel execution (using multiprocessing);
- supports OCaml >= 4.08.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fpath-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n testo-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
