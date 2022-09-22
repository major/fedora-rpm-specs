%undefine _package_note_flags

Name:           ocaml-stdint
Version:        0.7.0
Release:        9%{?dist}
Summary:        Various signed and unsigned integers for OCaml

License:        MIT
URL:            https://github.com/andrenth/%{name}
Source0:        %{url}/releases/download/%{version}/stdint-%{version}.tbz
# Fix lognot and logxor for Int40, Int48, Int56, and Int128
# https://github.com/andrenth/ocaml-stdint/pull/60
Patch0:         %{name}-lognot.patch
# Fix or disable broken tests
# https://github.com/andrenth/ocaml-stdint/issues/59
Patch1:         %{name}-test.patch

BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 1.10
BuildRequires:  ocaml-qcheck-devel

# This can be removed when F40 reaches EOL
Obsoletes:      ocaml-stdint-doc < 0.7.0-9

%description
The stdint library provides signed and unsigned integer types of various
fixed widths: 8, 16, 24, 32, 40, 48, 56, 64 and 128 bits.

This interface is similar to Int32 and Int64 from the base library but
provides more functions and constants like arithmetic and bit-wise
operations, constants like maximum and minimum values, infix operators
converting to and from every other integer type (including int, float and
nativeint), parsing from and conversion to readable strings (binary,
octal, decimal, hexadecimal), and conversion to and from buffers in both
big endian and little endian byte order.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
%autosetup -n stdint-%{version} -p1

# Skip 128-bit tests on 32-bit platforms.  The necessary functions are not
# fully implemented.
%if 0%{?__isa_bits} == 32
sed -i '/"Int128.*"/d;/"Uint128.*"/d' tests/stdint_test.ml
%endif

%build
%dune_build

# Relink the stublib with RPM_LD_FLAGS
cd _build/default/lib
ocamlmklib -g -ldopt '%{build_ldflags}' -o stdint_stubs $(ar t libstdint_stubs.a)
cd -

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.7.0-8
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-8
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-7
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-5
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 23:32:56 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-3
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- Version 0.7.0
- Add -lognot and -test patches

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-9
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-8
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-4
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 0.6.0-2
- OCaml 4.10.0 final

* Thu Feb  6 2020 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- Initial RPM
