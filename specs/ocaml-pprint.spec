Name:           ocaml-pprint
Version:        20230830
Release:        %autorelease
Summary:        A pretty-printing combinator library for OCaml

License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/fpottier/pprint
Source0:        https://github.com/fpottier/pprint/archive/%{version}/pprint-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 1.3

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%description
PPrint is an OCaml library for pretty-printing textual documents.
It takes care of indentation and line breaks,
and is typically used to pretty-print code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n pprint-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
dune exec test/PPrintTest.exe

%files -f .ofiles
%license LICENSE
%doc README.md CHANGES.md AUTHORS.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
