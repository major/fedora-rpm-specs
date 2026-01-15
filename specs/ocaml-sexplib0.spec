# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-sexplib0
Version:        0.17.0
Release:        %autorelease
Summary:        Definition of S-expressions and some base converters

License:        MIT
URL:            https://github.com/janestreet/sexplib0
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/sexplib0-%{version}.tar.gz

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-dune >= 3.11.0

%description
This package contains a library with the definition of S-expressions and some
base converters.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n sexplib0-%{version}

%build
%dune_build

%install
%dune_install

%files -f .ofiles
%doc README.md CHANGES.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
