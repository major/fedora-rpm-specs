%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-spdx-licenses
Version:        1.3.0
Release:        %autorelease
Summary:        SPDX License Expression parser in OCaml

License:        MIT
URL:            https://github.com/kit-ty-kate/spdx_licenses
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/spdx_licenses-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-alcotest-devel >= 1.4.0
BuildRequires:  ocaml-dune >= 2.3

%description
spdx_licenses is an OCaml library aiming to provide an up-to-date and
strict SPDX License Expression parser.

It implements the format described in
https://spdx.github.io/spdx-spec/appendix-IV-SPDX-license-expressions/.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n spdx_licenses-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.txt

%files devel -f .ofiles-devel

%changelog
%autochangelog
