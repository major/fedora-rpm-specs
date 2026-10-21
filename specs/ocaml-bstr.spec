%global srcname bstr
%global giturl  https://github.com/robur-coop/bstr

Name:           ocaml-%{srcname}
Version:        0.1.1
Release:        %autorelease
Summary:        Synthetic library for OCaml bigstrings

License:        MIT
URL:            https://git.robur.coop/robur/bstr
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{srcname}-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-dune >= 3.5.0

# Test dependencies
# The ocaml-crowbar package is only available on x86_64
%ifarch %{x86_64}
BuildRequires:  ocaml-crowbar-devel >= 0.2.2
%endif

%description
This small set of libraries offers a homogeneous API between 2 types and their
derivations with the slice type, as well as a small DSL for decoding "packets"
(such as ARP or DNS) without too much difficulty.

The aim is to homogenize the 2 types bytes and bigstring and to derive them
with a slice type, giving the user all the levers needed to manipulate byte
sequences, whether in the form of a bigstring or bytes.  The slice view avoids
copying when it comes to decoding a packet and extracting a sub-part.  The
slice also applies to bigstrings, whose Bigarray.Array1.sub is more expensive.

This set of libraries is a synthesis of astring (which offers a range of
useful functions as well as slice), cstruct (which offers a similar API for
bigstrings), bigstringaf (which offers some other useful functions), the
standard OCaml library and repr for decoding/encoding these values into OCaml
records/variants.

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
