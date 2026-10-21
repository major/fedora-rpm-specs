%global srcname optint
%global giturl  https://github.com/mirage/optint

Name:           ocaml-%{srcname}
Version:        0.3.0
Release:        %autorelease
Summary:        Efficient integer types on 64-bit architectures

License:        MIT
URL:            https://mirage.github.io/optint/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{srcname}-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildRequires:  ocaml >= 4.07.0
BuildRequires:  ocaml-dune

# Test dependencies
# The ocaml-crowbar package is only available on x86_64
%ifarch %{x86_64}
BuildRequires:  ocaml-crowbar-devel >= 0.2
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-monolith-devel
%endif

%description
This library provides two new integer types, Optint.t and Optint.Int63.t,
which guarantee efficient representation on 64-bit architectures and provide a
best-effort boxed representation on 32-bit architectures.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%check
%ifarch %{x86_64}
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
