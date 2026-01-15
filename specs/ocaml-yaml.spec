# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Fedora does not have crowbar, ezjsonm, or junit_alcotest
%global run_tests 0

%global giturl  https://github.com/avsm/ocaml-yaml

Name:           ocaml-yaml
Version:        3.2.0
Release:        %autorelease
Summary:        Parse and generate YAML 1.1/1.2 files

License:        ISC
URL:            https://avsm.github.io/ocaml-yaml/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/yaml-%{version}.tbz

# Unbundle libyaml.  See:
# - https://github.com/yaml/libyaml/pull/235
# - https://github.com/avsm/ocaml-yaml/issues/51
Patch:          %{name}-unbundle-libyaml.patch

BuildRequires:  libyaml-devel
BuildRequires:  ocaml >= 4.13.0
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-ctypes-devel >= 0.14.0
BuildRequires:  ocaml-dune >= 2.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ppx-sexp-conv-devel >= 0.9.0
BuildRequires:  ocaml-sexplib-devel

# Test dependencies
%if %{run_tests}
BuildRequires:  ocaml-alcotest-devel >= 1.5.0
BuildRequires:  ocaml-crowbar-devel
BuildRequires:  ocaml-ezjsonm-devel
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-junit-alcotest-devel
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-mdx-devel >= 2.1.0
%endif

%description
This is an OCaml library to parse and generate the YAML file format.  It is
intended to be interoperable with the Ezjsonm [1] JSON handling library, if
the simple common subset of Yaml is used.  Anchors and other advanced Yaml
features are not implemented in the JSON compatibility layer.

[1] https://github.com/mirage/ezjsonm

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libyaml-devel%{?_isa}
Requires:       ocaml-bos-devel%{?_isa}
Requires:       ocaml-ctypes-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        sexp
Summary:        Parse and generate YAML 1.1/1.2 files with sexp support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    sexp
This package adds sexp support to the functionality of ocaml-yaml.

%package        sexp-devel
Summary:        Development files for %{name}-sexp
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-sexp%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-sexplib-devel%{?_isa}

%description    sexp-devel
The %{name}-sexp-devel package contains libraries and signature files for
developing applications that use %{name}-sexp.

%prep
%autosetup -N -n yaml-%{version}

# Unbundle the included copy of libyaml.
# https://bugzilla.redhat.com/show_bug.cgi?id=2217729#c4
rm vendor/{*.c,yaml.h,yaml_private.h}
cp -p %{_includedir}/yaml.h vendor/yaml.h
%patch -P0 -p1
touch vendor/dummy.c
ln -s %{_libdir}/libyaml.so ffi/lib/dllyaml.so

%build
%dune_build

%install
%dune_install -s

%if %{run_tests}
%check
%dune_check
%endif

%files -f .ofiles-yaml
%license LICENSE.md
%doc README.md CHANGES.md

%files devel -f .ofiles-yaml-devel

%files sexp -f .ofiles-yaml-sexp
%license LICENSE.md
%doc README.md CHANGES.md

%files sexp-devel -f .ofiles-yaml-sexp-devel

%changelog
%autochangelog
