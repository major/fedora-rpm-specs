Name:           ocaml-omd
Version:        1.3.2
Release:        %autorelease
Summary:        Extensible Markdown library and tool in "pure OCaml"

License:        ISC
URL:            https://github.com/ocaml/omd
Source0:        https://github.com/ocaml/omd/archive/%{version}/omd-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  help2man
BuildRequires:  ocaml >= 4.04
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-findlib

%description
Omd is an OCaml library designed to parse, manipulate, and print
Markdown into different formats.  In addition to the library, a
command-line tool omd is included to easily convert markdown into HTML.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n omd-%{version} -p1

%build
%dune_build

%install
%dune_install

mkdir -p %{buildroot}%{_mandir}/man1
help2man -N --version-string=%{version} -o %{buildroot}%{_mandir}/man1/omd.1 \
  -n 'Convert markdown to HTML' %{buildroot}%{_bindir}/omd

%check
%dune_check

%files -f .ofiles
%doc README.md CHANGES.md
%{_mandir}/man1/omd.1*

%files devel -f .ofiles-devel

%changelog
%autochangelog
