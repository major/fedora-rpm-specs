Name:		vim-latex
Version:	1.10.0
Release:	16%{?dist}
Summary:	Tools to view, edit and compile LaTeX documents in Vim
# According to doc/latex-suite license is Vim charityware license
License:	Vim
URL:		http://vim-latex.sourceforge.net/
Source0:	http://downloads.sourceforge.net/vim-latex/vim-latex-%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/vim-latex/vim-latex-%{version}.tar.gz.asc
Source2:	vim-latex-gpgkeys.gpg
# Use Python 3, bug #1676189
Patch0:		vim-latex-1.10.0-Interpret-outline.py-by-Python-3.patch
BuildArch:	noarch

# We need vim-filesystem for dir ownership
Requires:	vim-filesystem
# Needed for compilation
Requires:	tex(latex)
# Needed for display
Requires:	xdvi

# Needed for vim macros
BuildRequires: vim-filesystem

# Needed to build documentation
BuildRequires:	make
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtds

# For source verification with gpgv
BuildRequires:	gnupg2

%description
A comprehensive set of tools to view, edit and compile LaTeX documents without
needing to ever quit Vim. Together, they provide tools starting from macros to
speed up editing LaTeX documents to compiling TeX files to forward searching
.dvi documents.

%package doc
Summary:	Documentation for vim-latex

%description doc
Documentation for vim-latex.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# build documentation
%make_build -C doc

%install
# Install files
%make_install VIMDIR=%{vimfiles_root} BINDIR=%{_bindir} PREFIX=%{_prefix}


%files
%doc %{vimfiles_root}/doc/imaps.txt
%doc %{vimfiles_root}/doc/latex*.txt
%{_bindir}/latextags
%{_bindir}/ltags
%{_datadir}/appdata/vim-latex.metainfo.xml
%{vimfiles_root}/compiler/*
%{vimfiles_root}/ftplugin/*
%{vimfiles_root}/indent/*
%{vimfiles_root}/plugin/*


%files doc
%doc doc/latex-suite doc/latex-suite-quickstart


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Arthur Bols <arthur@bols.dev> - 1.10.0-11
- Spec file cleanup

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Petr Pisar <ppisar@redhat.com> - 1.10.0-3
- Use Python 3 (bug #1676189)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Jeremiah Mahler <jmmahler@gmail.com> - 1.10.0-1
- Update to release 1.10.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Till Maas <opensource@till.name> - 1.9.0-1
- Update to new release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.23-16.20141116.812.gitd0f31c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.23-15.20141116.812.gitd0f31c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Till Maas <opensource@till.name> - 1.8.23-14.20141116.812.gitd0f31c9
- Update to new release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.23-13.20130116.788.git2ef9956
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.23-12.20130116.788.git2ef9956
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.23-11.20130116.788.git2ef9956
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Till Maas <opensource@till.name> - 1.8.23-10
- Update to new release

* Fri Nov 16 2012 Till Maas <opensource@till.name> - 1.8.23-9
- Update to new release

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.23-8.20120125.768.git8b62284
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 25 2012 Till Maas <opensource@till.name> - 1.8.23-7.20120125.768-git8b62284
- Update to new snaphot

* Sun Jan 15 2012 Mario Santagiuliana <mario@marionline.it> - 1.8.23-6.20110214.1049-git089726a
- Fix my changelog: date error reporting

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.23-5.20110214.1049.git089726a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011 Mario Santagiuliana <mario@marionline.it> - 1.8.23-5.20110214.1049-git089726a
- Review spec file
- Fix changelog error

* Fri Oct 28 2011 Mario Santagiuliana <mario@marionline.it> - 1.8.23-4.20110214.1049-git089726a
- Review spec file

* Mon Feb 14 2011 Till Maas <opensource@till.name> - 1.8.23-3.20110214.1049.git089726a
- Update to new release
- Adjust to new upstream snapshot schema
- build documentation, that is not included in upstream snapshot anymore

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.23-2.20101027.r1112
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 01 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.8.23-1.20101027.r1112
- Update to 20101027-r1112.

* Sat Jan 30 2010 Till Maas <opensource@till.name> - 1.8.23-1.20100129.r1104
- Update to new release

* Thu Dec 31 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.8.23-1.20091230.r1079
- Update to 20091230-r1079.

* Fri Oct 09 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.5-3.20091002.r1074
- Use make install instead of manual install.

* Thu Oct 08 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.5-2.20091002.r1074
- Update to 20091002-r1074.

* Thu Oct 08 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.5-2.20090901.r1069
- Added missing Requires: tex(latex) and xdvi.

* Mon Sep 28 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.5-1.20090901.r1069
- First release.
