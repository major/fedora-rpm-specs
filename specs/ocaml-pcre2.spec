Name:           ocaml-pcre2
Version:        8.0.2
Release:        %autorelease
Summary:        OCaml bindings to the pcre2 library

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/camlp5/pcre2-ocaml
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/pcre2-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  pkgconfig(libpcre2-8)

%description
This packages offers library functions for string pattern matching and
substitution, similar to the functionality offered by the Perl language.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pcre2-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n pcre2-ocaml-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md CHANGES.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
