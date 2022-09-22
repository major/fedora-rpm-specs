%undefine _package_note_flags
%global srcname camlimages

Name:           ocaml-%{srcname}
Version:        5.0.4
Release:        8%{?dist}
Summary:        OCaml image processing library
License:        LGPLv2 with exceptions

URL:            https://gitlab.com/camlspotter/camlimages
Source0:        https://gitlab.com/camlspotter/camlimages/-/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  ghostscript
BuildRequires:  giflib-devel
BuildRequires:  ocaml >= 4.06.0
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune-devel >= 1.11
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-graphics-devel
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-stdio-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  rgb

Requires:       ghostscript
Requires:       rgb

%description
This is an image processing library, which provides some basic
functions of image processing and loading/saving various image file
formats. In addition the library can handle huge images that cannot be
(or can hardly be) stored into the memory (the library automatically
creates swap files and escapes them to reduce the memory usage).

%package        devel
Summary:        Development files for camlimages
Requires:       %{name}%{?_isa} = %{version}-%{release} 
Requires:       ocaml-graphics-devel%{?_isa}
Requires:       ocaml-lablgtk-devel%{?_isa}
Requires:       ocaml-stdio-devel%{?_isa}

%description    devel
The camlimages-devel package provides libraries and headers for 
developing applications using camlimages.

Includes documentation provided by odoc.

%prep
%autosetup -n %{srcname}-%{version}

%build
dune build %{?_smp_mflags} --display=verbose
dune build %{?_smp_mflags} @doc

# Relink the stublibs with $RPM_LD_FLAGS.
for lib in exif freetype gif jpeg png tiff xpm; do
  cd _build/default/$lib
  ocamlmklib -g -ldopt '%{build_ldflags}' -o camlimages_${lib}_stubs \
    $(ar t libcamlimages_${lib}_stubs.a)
  cd -
done

%install
dune install --destdir=%{buildroot}

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%check
dune runtest

%files
%doc README.md Changes.txt
%license License.txt
%dir %{_libdir}/ocaml/%{srcname}/
%dir %{_libdir}/ocaml/%{srcname}/core/
%dir %{_libdir}/ocaml/%{srcname}/exif/
%dir %{_libdir}/ocaml/%{srcname}/freetype/
%dir %{_libdir}/ocaml/%{srcname}/gif/
%dir %{_libdir}/ocaml/%{srcname}/graphics/
%dir %{_libdir}/ocaml/%{srcname}/jpeg/
%dir %{_libdir}/ocaml/%{srcname}/lablgtk2/
%dir %{_libdir}/ocaml/%{srcname}/png/
%dir %{_libdir}/ocaml/%{srcname}/tiff/
%dir %{_libdir}/ocaml/%{srcname}/xpm/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/*/*.cma
%{_libdir}/ocaml/%{srcname}/*/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/*.so

%files devel
%doc _build/default/_doc/_html/*
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*/*.a
%{_libdir}/ocaml/%{srcname}/*/*.cmx
%{_libdir}/ocaml/%{srcname}/*/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/*/*.cmt
%{_libdir}/ocaml/%{srcname}/*/*.cmti
%{_libdir}/ocaml/%{srcname}/*/*.mli

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 5.0.4-7
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 5.0.4-6
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 5.0.4-4
- Rebuild for ocaml-lablgtk 2.18.12

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 5.0.4-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 5.0.4-1
- Version 5.0.4
- New URLs
- Drop all patches
- Drop the out of date reference manual
- Build with dune and odoc instead of ocamlbuild and ocamldoc

* Mon Mar  1 19:41:31 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-28
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-26
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-25
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 4.2.5-24
- {Build,}Require rgb not xorg-x11-server-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-22
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-21
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-20
- OCaml 4.11.0 pre-release

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-19
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-18
- OCaml 4.10.0 final.

* Thu Feb 06 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-17
- Remove bogus "lablgtk" dependency.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-15
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-14
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-13
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-12
- OCaml 4.08.1 (final) rebuild.

* Sat Aug 10 2019 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-11
- Rebuild against new ocaml-lablgtk.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-10
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-6
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-5
- OCaml 4.07.0-rc1 rebuild.

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 4.2.5-4
- Rebuild (giflib)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.2.5-3
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-1
- New upstream version 4.2.5.
- New version fixes compatibility with latest lablgtk.

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.4-2
- OCaml 4.06.0 rebuild.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.4-1
- New upstream version 4.2.4.
- Replace opt test with ocaml_native_compiler.
- Pass -g option to ocamlopt so debuginfo is generated correctly.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.2-7
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.2-4
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.2-3
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 4.2.2-1
- New upstream version 4.2.2.
- Drop patch for exif handling which is included upstream.
- Drop patch for warn-error since this is fixed upstream.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 16 2015 Bruno Wolff III <bruno@wolff.to> - 4.1.0-18
- devel shouldn't cover all doc files

* Tue Aug 11 2015 Bruno Wolff III <bruno@wolff.to> - 4.1.0-17
- Don't use %%doc to copy over htmlref for -devel package

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-16
- Bump release and rebuild.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-15
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-14
- Enable bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-13
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-12
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-10
- ocaml-4.02.1 rebuild.

* Fri Oct 31 2014 Bruno Wolff III <bruno@wolff.to> - 4.1.0-9
- Rebuild to link with updated dependencies

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-8
- ocaml-4.02.0 final rebuild.

* Tue Aug 19 2014 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-7
- Kill -warn-error A so we can build on OCaml 4.02.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Bruno Wolff III <bruno@wolff.to> - 4.1.0-5
- Rebuild for ocaml update

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 25 2013 Ville Skyttä <ville.skytta@iki.fi> - 4.1.0-3
- Fix -debuginfo, enable exif and rgb.txt support (#1009155).

* Fri Sep 27 2013 Bruno Wolff III <bruno@wolff.to> - 4.1.0-2
- Try to get actual debug output

* Sun Sep 15 2013 Bruno Wolff III <bruno@wolff.to> - 4.1.0-1
- Update to 4.1.0
- Enable debug output
- Patch for recent libpng is no longer needed

* Sat Sep 14 2013 Bruno Wolff III <bruno@wolff.to> - 4.0.1-13
- Rebuild for OCaml 4.01.0

* Sun Aug 11 2013 Bruno Wolff III <bruno@wolff.to> - 4.0.1-12
- Move to unversioned doc directory
- Fixes FTBFS bug 992390

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 4.0.1-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 4.0.1-8
- rebuild against new libjpeg

* Wed Oct 17 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-7
- Rebuild for ocaml 4.0.1

* Sun Jul 29 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-6
- Rebuild for ocaml 4.0.0 final

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-4
- Rebuild for new ocaml

* Fri May 11 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-3
- Rebuild for new libtiff

* Sat Mar 10 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-2
- Fixup "should fixes" from review

* Sun Jan 29 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-1
- Resurrect ocaml-camlimages
