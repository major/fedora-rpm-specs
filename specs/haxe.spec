# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global commit_haxelib f17fffa97554b1bdba37750e3418051f017a5bc2
%global commit_hx3compat f1f18201e5c0479cb5adf5f6028788b37f37b730

Name:           haxe
Version:        4.3.4
Release:        8%{?dist}
Summary:        Multi-target universal programming language

# As described in https://haxe.org/foundation/open-source.html:
#   * The Haxe Compiler - GPLv2+
#   * The Haxe Standard Library - MIT
#
# The source files:
#   * All files in the std folder is MIT licensed.
#   * Ocamllibs in the libs folder:
#     * extc, ilib, javalib, neko, swflib - GPLv2+
#     * pcre - LGPLv2+
#     * everything else - LGPLv2.1+
# Automatically converted from old format: GPLv2+ and MIT and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-LGPLv2+

URL:            https://haxe.org/

Source0:        https://github.com/HaxeFoundation/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/HaxeFoundation/haxelib/archive/%{commit_haxelib}.tar.gz#/haxelib-%{commit_haxelib}.tar.gz
Source2:        https://github.com/HaxeFoundation/hx3compat/archive/%{commit_hx3compat}.tar.gz#/hx3compat-%{commit_hx3compat}.tar.gz
# Updates needed for OCaml 5.3.0
Patch:          %{name}-ocaml5.3.patch

BuildRequires:  make
BuildRequires:  nekovm-devel >= 2.3.0
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-camlp5-devel
BuildRequires:  ocaml-camlp-streams
BuildRequires:  ocaml-sedlex-devel >= 2.0
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-extlib-devel >= 1.7.8
BuildRequires:  ocaml-ptmap-devel
BuildRequires:  ocaml-sha-devel
BuildRequires:  ocaml-luv-devel >= 0.5.12
BuildRequires:  zlib-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(libuv)
BuildRequires:  mbedtls-devel
BuildRequires:  cmake
BuildRequires:  help2man
Requires:       nekovm >= 2.3.0
Requires:       %{name}-stdlib = %{version}

%description
Haxe is an open source toolkit based on a modern,
high level, strictly typed programming language, a cross-compiler,
a complete cross-platform standard library and ways to access each
platform's native capabilities.

%package        stdlib
Summary:        The Haxe standard library
BuildArch:      noarch

%description    stdlib
The %{name}-stdlib package contains the standard library used
by the Haxe compiler.

%prep
%setup -q
pushd extra/haxelib_src && tar -xf %{SOURCE1} --strip-components=1 && popd
pushd extra/haxelib_src/hx3compat && tar -xf %{SOURCE2} --strip-components=1 && popd
%autopatch -p1

%build
# note that the Makefile does not support parallel building
make

# Recompile haxelib.
#
# In the default Makefile, haxelib is built using `nekotools boot ...`.
# It produces haxelib by concatenating the neko binary with haxelib neko bytecode.
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/FFE3B3TGLXMVPDIZGAOJYHFOJMBGUQUL/
#
# Instead, use the haxelib CMake, which use `nekotools boot -c ...`
# to produce a C source code and build it with standard C toolchain.
rm ./haxelib
%cmake -S extra/haxelib_src -DHAXE_COMPILER="$(realpath haxe)"
%cmake_build
mv %__cmake_builddir/haxelib .

chmod 755 haxe haxelib

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

cp -p haxe %{buildroot}%{_bindir}
cp -p haxelib %{buildroot}%{_bindir}
cp -rfp std %{buildroot}%{_datadir}/%{name}

# Generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
help2man ./haxe --version-option=-version --no-discard-stderr --no-info --output=%{buildroot}%{_mandir}/man1/haxe.1
help2man ./haxelib --help-option=help --version-option=version --no-info --output=%{buildroot}%{_mandir}/man1/haxelib.1

%check
%{buildroot}%{_bindir}/haxe -version
%{buildroot}%{_bindir}/haxelib version

# should not call haxe from the source dir or it will get confused about the std lib
pushd %{buildroot}
%{buildroot}%{_bindir}/haxe -v Std
popd

%files
%doc README.md
%license extra/LICENSE.txt
%{_bindir}/haxe
%{_bindir}/haxelib
%{_mandir}/man1/haxe.1*
%{_mandir}/man1/haxelib.1*

%files stdlib
%doc README.md
%license extra/LICENSE.txt
%{_datadir}/%{name}/

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 4.3.4-7
- OCaml 5.3.0 rebuild for Fedora 42
- Add patch for OCaml 5.3.0 compatibility

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> - 4.3.4-6
- Rebuilt for mbedTLS 3.6.1

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.4-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 4.3.4-3
- OCaml 5.2.0 ppc64le fix

* Thu May 30 2024 Richard W.M. Jones <rjones@redhat.com> - 4.3.4-2
- OCaml 5.2.0 for Fedora 41

* Tue Mar 05 2024 Andy Li <andy@onthewings.net> - 4.3.4-1
- New upstream version 4.3.4. (RHBZ#2267830)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 4.3.3-3
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.3.3-2
- OCaml 5.1.1 rebuild for Fedora 40

* Sun Nov 19 2023 Andy Li <andy@onthewings.net> - 4.3.3-1
- New upstream version 4.3.3. (RHBZ#2250370)
- Drop haxe-ocaml5.patch which is no longer needed.

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-2
- OCaml 5.1 rebuild for Fedora 40

* Fri Sep 15 2023 Andy Li <andy@onthewings.net> - 4.3.2-1
- New upstream version 4.3.2. (RHBZ#2237112)
- Use the properly built haxelib. (RHBZ#2129517)
- Add haxe-ocaml5.patch from upstream for OCaml 5 compat. (RHBZ#2218692)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.3.1-2
- OCaml 5.0 rebuild for Fedora 39

* Sun Apr 30 2023 Andy Li <andy@onthewings.net> - 4.3.1-1
- New upstream version 4.3.1. (RHBZ#2185083, RHBZ#2128307)
- Update haxelib to 4.1.0.

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-5
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-2
- OCaml 4.14.0 rebuild

* Mon May 23 2022 Andy Li <andy@onthewings.net> - 4.2.5-1
- New upstream version 4.2.5. (RHBZ#2063455)

* Sat Jan 22 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.2.4-3
- Rebuilt for mbedTLS 2.28.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Andy Li <andy@onthewings.net> - 4.2.4-1
- New upstream version 4.2.4. (RHBZ#2018499)

* Sun Oct 24 2021 Andy Li <andy@onthewings.net> - 4.2.3-1
- New upstream version 4.2.3. (RHBZ#1960768)

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 4.2.1-6
- OCaml 4.13.1 build

* Fri Aug  6 2021 Jerry James <loganjerry@gmail.com> - 4.2.1-5
- Rebuild for ocaml-luv 0.5.10

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 4.2.1-4
- Rebuild for ocaml-luv 0.5.9

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 10 2021 Jerry James <loganjerry@gmail.com> - 4.2.1-2
- Rebuild for ocaml-luv 0.5.8

* Thu Mar 04 2021 Andy Li <andy@onthewings.net> - 4.2.1-1
- New upstream version 4.2.1. (RHBZ#1926782)

* Tue Mar  2 00:02:04 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 4.1.5-3
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Andy Li <andy@onthewings.net> - 4.1.5-1
- New upstream version 4.1.5. (RHBZ#1911805)

* Sat Nov 14 2020 Andy Li <andy@onthewings.net> - 4.1.4-1
- New upstream version 4.1.4. (RHBZ#1896901)

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-6
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-5
- OCaml 4.11.0 rebuild

* Thu Jul 30 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-4
- Enable debuginfo again.

* Thu Jul 30 2020 Andy Li <andy@onthewings.net> - 4.1.3-3
- Disable debug package. (Empty debugsourcefiles.list)
- Do not strip since haxelib fails to run after stripping.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Andy Li <andy@onthewings.net> - 4.1.3-1
- New upstream version 4.1.3. (RHBZ#1859658)

* Sat Jun 20 2020 Andy Li <andy@onthewings.net> - 4.1.2-1
- New upstream version 4.1.2. (RHBZ#1849186)

* Thu Jun 04 2020 Andy Li <andy@onthewings.net> - 4.1.1-1
- New upstream version 4.1.1. (RHBZ#1835307)

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.5-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Sun Apr 05 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.5-6
- Update all OCaml dependencies for RPM 4.16.

* Tue Mar 31 2020 Andy Li <andy@onthewings.net> - 4.0.5-5
- Fix build command to avoid accidentially building to OCaml bytecode.
- Add test that runs the Haxe compiler.
- Add missing BuildRequires: ocaml-gen-devel.

* Sun Mar 08 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.5-4
- Bump and rebuild for camlp5 7.11.

* Sun Mar 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.5-3
- Rebuild for OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Andy Li <andy@onthewings.net> - 4.0.5-1
- New upstream version 4.0.5. (RHBZ#1784429)

* Sat Nov 30 2019 Andy Li <andy@onthewings.net> - 4.0.3-1
- New upstream version 4.0.3. (RHBZ#1778263)

* Tue Nov 12 2019 Andy Li <andy@onthewings.net> - 4.0.2-1
- New upstream version 4.0.2. (RHBZ#1771192)

* Sun Nov 10 2019 Andy Li <andy@onthewings.net> - 4.0.1-1
- New upstream version 4.0.1. (RHBZ#1765817)
- Remove camlp5.diff, which is no longer needed.

* Fri Jul 26 2019 Andy Li <andy@onthewings.net> - 3.4.7-5
- Add camlp5.diff patch to use camlp5 instead of camlp4.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Andy Li <andy@onthewings.net> - 3.4.7-1
- New upstream version 3.4.7. (RHBZ#1544583)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Andy Li <andy@onthewings.net> - 3.4.5-1
- New upstream version 3.4.5. (RHBZ#1540771)

* Sat Oct 14 2017 Andy Li <andy@onthewings.net> - 3.4.4-1
- New upstream version 3.4.4.
- Compile haxelib as a proper binary instead of `nekotools boot`.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 23 2017 Andy Li <andy@onthewings.net> - 3.4.2-1
- New upstream version 3.4.2.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Andy Li <andy@onthewings.net> - 3.4.0-1
- New upstream version 3.4.0.
- Fixed license info.

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 3.2.1-4
- Rebuild for OCaml 4.04.0.

* Thu Jun 09 2016 Andy Li <andy@onthewings.net> - 3.2.1-3
- Rebuilt against nekovm 2.1.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 07 2015 Andy Li <andy@onthewings.net> - 3.2.1-1
- Initial RPM release

