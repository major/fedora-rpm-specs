# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-base64
Version:        3.5.1
Release:        %autorelease
Summary:        Base64 library for OCaml

License:        ISC
URL:            https://github.com/mirage/ocaml-base64
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/v%{version}/base64-%{version}.tbz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune

# Test dependencies
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-rresult-devel


%description
Base64 is a group of similar binary-to-text encoding schemes that
represent binary data in an ASCII string format by translating it into
a radix-64 representation. It is specified in RFC 4648.


%package devel
Summary:        Development files for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for %{name}.


%prep
%autosetup -n base64-%{version}


%build
# Only build the source and test directories since the other directories
# require packages that we don't have or need.
rm -r bench fuzz
%dune_build


%install
%dune_install


%check
%dune_check


%files -f .ofiles
%doc README.md
%license LICENSE.md


%files devel -f .ofiles-devel
%doc CHANGES.md


%changelog
%autochangelog
