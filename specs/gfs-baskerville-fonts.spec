# SPDX-License-Identifier: MIT
Version: 20070327
Release: 47%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/18th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Baskerville
%global fontsummary       GFS Baskerville, an 18th century oblique Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
John Baskerville (1706-1775) got involved in typography late in his career but
his contribution was significant. He was a successful entrepreneur and
possessed an inquiring mind which he applied to produce many aesthetic and
technical innovations in printing. He invented a new ink formula, a new type
of smooth paper and made various improvements in the printing press. He was
also involved in type design which resulted in a Latin typeface which was used
for the edition of Virgil, in 1757. The quality of the type was admired
throughout of Europe and America and was revived with great success in the
early 20th century.

Baskerville was also involved in the design of a Greek typeface which he used
in an edition of the New Testament for Oxford University, in 1763. He adopted
the practice of avoiding the excessive number of ligatures which Alexander
Wilson had started a few years earlier but his Greek types were rather narrow
in proportion and did not win the sympathy of the philologists and other
scholars of his time. They did influence, however, the Greek types of
Giambattista Bodoni. and through him Didot’s Greek in Paris.

The typeface has been digitally revived as GFS Baskerville Classic by Sophia
Kalaitzidou and George D. Matthiopoulos and is now available as part of GFS’
type library.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%setup -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc *.pdf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20070327-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070327-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070327-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070327-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20070327-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20070327-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20070327-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 25 2022 Akira TAGOH <tagoh@redhat.com>
- 20070327-40
- Fix FTBFS

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

 Wed Apr 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070327-35
🐞 Workaround Fedora problems created by rpm commit 93604e

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070327-34
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070327-33
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070327-32
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070327-31
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070327-30
✅ Convert to fonts-rpm-macros use

* Sun Nov 25 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 20070327-2
✅ Initial packaging
