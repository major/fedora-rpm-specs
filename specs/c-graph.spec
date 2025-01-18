Name:		c-graph
Version:	2.0.1
Release:	14%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Summary:	Convolution Graph
URL:		http://www.gnu.org/software/%{name}
Source0:	http://ftp.gnu.org/gnu/c-graph/%{name}-%{version}.tar.gz
BuildRequires:	gcc-gfortran
BuildRequires:	help2man
BuildRequires: make
Requires:	coreutils
Requires:	gnuplot
Requires:	ImageMagick
Requires:	less
Requires:	ncurses

%description
Convolution Theorem Visualization

Convolution is a core concept in today's cutting-edge technologies of
deep learning and computer vision. Singularly cogent in application to
digital signal processing, the convolution theorem is regarded as the
most powerful tool in modern scientific analysis. Long utilised for
accelerating the application of filters to images, fast training of
convolutional neural networks exploit the convolution theorem to accelerate
training and inference in the ubiquitous applications of computer vision
that, today, are at the vanguard of the evolving artificially intelligent
world in which we are becoming increasingly immersed.

Coded in modern Fortran, GNU C-Graph is the de facto tool for visualizing
convolution in university courses worldwide. "C-Graph" stands for
"Convolution Graph" - Free Software that makes learning about convolution
easy!

%prep
%setup -q

%build
%configure
# remove \r\n line endings
sed -e 's|\r||' README > README.new
touch -r README.new README
mv README.new README
make %{?_smp_mflags} FCFLAGS="$FFLAGS"

%install
make install DESTDIR=%{buildroot}

# must be created when installing info
rm -f %{buildroot}%{_infodir}/dir

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc %{_docdir}/%{name}
%doc %{_infodir}/%{name}*
%doc %{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.1-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.1-1
- New upstream release

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2.0-16
- Remove obsolete requirements for %%post/%%preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 2.0-10
- Rebuilt for libgfortran soname bump

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0-3
- Do not modify README timestamp (#881794)
- Use proper fortran compile flags (#881794)

* Tue Jan 15 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0-2
- Correct summary as per package author suggestion (#881794)
- Add missing requires for called binaries (#881794)
- Correct description to use American English per the guidelines (#881794)
- Move documentation to docdir (#881794)

* Mon Nov 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0-1
- Initial c-graph spec
