%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
# Debuginfo is not useful for OCaml programs since gdb doesn't know about OCaml
%global debug_package %{nil}

Name:           bibtex2html
Version:        1.99
Release:        11%{?dist}
Summary:        Collection of tools for translating from BibTeX to HTML

License:        GPLv2
URL:            http://www.lri.fr/~filliatr/bibtex2html/index.en.html
Source0:        http://www.lri.fr/~filliatr/ftp/bibtex2html/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  perl-interpreter
BuildRequires:  tex(latex)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  hevea
BuildRequires: make


%description
bibtex2html is a collection of tools for translating from BibTeX to HTML. 
They allow to produce, from a set of bibliography files in BibTeX format, 
a bibliography in HTML format.

%prep
%setup -q
sed -i 's/-cclib -lstr//' Makefile.in
for file in CHANGES README ; do
   mv $file timestamp && \
   iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp && \
   touch -r timestamp $file && \
   rm timestamp
done

%build
%configure 
make %{?_smp_mflags}

%install
%{__perl} -pi -e 's|^BINDIR=.*|BINDIR=%{buildroot}%{_bindir}|g;' Makefile
%{__perl} -pi -e 's|^MANDIR =.*|MANDIR=%{buildroot}%{_mandir}|g;' Makefile
make install 

%files
%doc CHANGES README GPL COPYING manual.pdf manual.html 
%{_mandir}/man1/*.1.gz
%{_bindir}/*


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.99-1
- Update to 1.99
- Replace BR: texlive-preprint by tex(fullpage.sty)
- Remove ocaml version constraint

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.97-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.97-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.97-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.97-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.97-11
- remove ExcludeArch

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 1.97-10
- Rebuild for OCaml 4.04.0.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.97-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Guido Grazioli <guido.grazioli@gmail.com> - 1.97-4
- Fix FTBFS

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Guido Grazioli <guido.grazioli@gmail.com> - 1.97-1
- Update to 1.97
- Adapt to current packaging guidelines

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Guido Grazioli <guido.grazioli@gmail.com> - 1.96-1
- Upstream 1.96
- Fix FTBFS

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 02 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.95-1
- Upstream 1.95

* Fri Oct 02 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.94-1
- Upstream 1.94

* Tue Sep 22 2009 Dennis Gilmore <dennis@ausil.us> - 1.93-5
- ExcludeArch sparc64 s390 s390x

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 19 2009 Guido Grazioli <guido.grazioli@gmail.com> 1.93-3
- added manual (no html on ppc64 until hevea available)

* Wed Mar 18 2009 Guido Grazioli <guido.grazioli@gmail.com> 1.93-2
- sanitized charset conversion
- added smp make flags

* Tue Mar 17 2009 Guido Grazioli <guido.grazioli@gmail.com> 1.93-1
- initial packaging
