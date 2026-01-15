# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifarch %{ocaml_native_compiler}
# The only source file for this package consists of a single "include" line.
# It exports some private functions from the library in ocaml-base.  Although
# debuginfo is generated, it is tagged with the file names from ocaml-base,
# rather than the single 1-line source file in this project.  That leads to
# this error:
#
# Processing files: ocaml-variantslib-debugsource-0.13.0-1.fc32.x86_64
# error: Empty %%files file /builddir/build/BUILD/variantslib-0.13.0/debugsourcefiles.list
#
# Do not try to gather debug sources to workaround the problem.
%undefine _debugsource_packages
%else
%global debug_package %{nil}
%endif

Name:           ocaml-variantslib
Version:        0.17.0
Release:        %autorelease
Summary:        OCaml variants as first class values

License:        MIT
URL:            https://github.com/janestreet/variantslib
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/variantslib-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0

%description
This package contains an OCaml syntax extension to define first class values
representing variants.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n variantslib-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
