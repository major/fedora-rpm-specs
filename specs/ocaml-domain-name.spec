# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif


Name:           ocaml-domain-name
Version:        0.5.0
Release:        %autorelease
Summary:        RFC 1035 Internet domain names


License:        ISC
URL:            https://github.com//hannesm/domain-name
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/domain-name-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# Tests
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-uutf-devel

%description
A domain name is a sequence of labels separated by dots, such as `foo.example`.
Each label may contain any bytes. The length of each label may not exceed 63
charactes.  The total length of a domain name is limited to 253 (byte
representation is 255), but other protocols (such as SMTP) may apply even
smaller limits.  A domain name label is case preserving, comparison is done in a
case insensitive manner.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains files for developing applications that use
%{name}.


%prep
%autosetup -n domain-name-%{version}


%build
%dune_build

%install
%dune_install -s

%check
%dune_check


%files -f .ofiles-domain-name
%doc README.md
%license LICENSE.md
%dir %{ocamldir}/domain-name/
%{ocamldir}/domain-name/META

%files devel -f .ofiles-domain-name-devel
%{ocamldir}/domain-name/dune-package
%{ocamldir}/domain-name/opam

%changelog
%autochangelog
