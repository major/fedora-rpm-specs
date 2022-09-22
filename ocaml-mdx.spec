%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-mdx
Version:        2.1.0
Release:        7%{?dist}
Summary:        Executable code blocks inside markdown files

License:        ISC
URL:            https://realworldocaml.github.io/mdx/
Source0:        https://github.com/realworldocaml/mdx/releases/download/%{version}/mdx-%{version}.tbz
# Update to cmdliner 1.1.0.  See:
# https://github.com/realworldocaml/mdx/commit/18481d8a48204b95ce66c0ce88cec416530fc6f5
# https://github.com/realworldocaml/mdx/commit/85654df98e3a1f5821a22f12836555b47ea2ed93
# https://github.com/realworldocaml/mdx/commit/b714cb6a9357d119185753bc59108e169d8bf246
Patch0:         %{name}-cmdliner.patch

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-cppo >= 1.1.0
BuildRequires:  ocaml-csexp-devel >= 1.3.2
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-fmt-devel >= 0.8.7
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-logs-devel >= 0.7.0
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-odoc-parser-devel >= 1.0.0
BuildRequires:  ocaml-re-devel >= 1.7.2
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-version-devel >= 2.3.0

%description
mdx enables execution of code blocks inside markdown files.  There are
(currently) two sub-commands, corresponding to two modes of operation:
preprocessing (`ocaml-mdx pp`) and tests (`ocaml-mdx test`).

The preprocessor mode enables mixing documentation and code, and the
practice of "literate programming" using markdown and OCaml.

The test mode enables ensuring that shell scripts and OCaml fragments in
the documentation always stay up-to-date.

The blocks in markdown files can be parameterized by `mdx`-specific
labels, that will change the way `mdx` interprets the block.  The syntax
is: `<!-- $MDX labels -->`, where `labels` is a list of valid labels
separated by a comma.  This line must immediately precede the block it
is attached to.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-csexp-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-odoc-parser-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-version-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n mdx-%{version} -p1

# Adapt to grep 3.8
sed -i 's/egrep/grep -E/' test/bin/mdx-test/expect/padding/test-case.md

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 20 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-7
- Add patch to adapt tests to cmdliner 1.1.0

* Tue Aug  2 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-6
- Rebuild for ocaml-odoc-parser 2.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  8 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-4
- Rebuild for ocaml-version 3.5.0
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 2.1.0-3
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 2.1.0-2
- OCaml 4.13.1 rebuild to remove package notes

* Thu Feb  3 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- Version 2.1.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Initial RPM
