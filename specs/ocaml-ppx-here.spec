# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ppx-here
Version:        0.17.0
Release:        %autorelease
Summary:        Expands [@here] into its location

License:        MIT
URL:            https://github.com/janestreet/ppx_here
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_here-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
Ppx_here is a ppx rewriter that defines an extension node whose value is its
source position.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_here-%{version}

%build
%dune_build

%install
%dune_install

%check
# We do not run the tests from a directory named ppx containing ppx_here.
# Adapt the test to running inside of the ppx_here directory.
sed -e 's,dummy\.ml\.pp,dummy.pp.ml,g' \
    -e 's,\\"ppx/ppx_here/test/dummy\.mll\\",test/dummy.mll,' \
    -i test/dune

%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
