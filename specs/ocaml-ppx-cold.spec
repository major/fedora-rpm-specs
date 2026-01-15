# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ppx-cold
Version:        0.17.0
Release:        %autorelease
Summary:        OCaml definition of [@@cold] attribute

License:        MIT
URL:            https://github.com/janestreet/ppx_cold
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_cold-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
Ppx_cold translates `[@@cold]` attributes to:

`[@@inline never] [@@local never] [@@specialise never]`

See the discussion in https://github.com/ocaml/ocaml/issues/8563.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_cold-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
