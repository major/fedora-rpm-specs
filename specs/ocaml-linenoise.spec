Name:           ocaml-linenoise
Version:        1.5.1
Release:        %autorelease
Summary:        OCaml bindings to linenoise

License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/%{name}
Source0:        https://github.com/ocaml-community/%{name}/archive/v%{version}/linenoise-v%{version}.tar.gz

# Unbundle linenoise
Patch0:          unbundle-linenoise.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 1.1
BuildRequires:  linenoise-devel

%description
Self-contained OCaml bindings to linenoise.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ocaml-linenoise-%{version} -p1

# Ensure the bundled linenoise sources are not used in the build
rm src/linenoise_src.*

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
