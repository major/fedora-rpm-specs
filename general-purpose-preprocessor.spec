Summary: Customizable language-agnostic preprocessor
Name: general-purpose-preprocessor
Version: 2.27
Release: 7%{?dist}
License: LGPLv2+
URL: https://logological.org/gpp
Source0: https://files.nothingisreal.com/software/gpp/gpp-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: make
Provides: gpp

%description
GPP is a general-purpose preprocessor with customizable syntax,
suitable for a wide range of preprocessing tasks. Its independence
from any one programming language makes it much more versatile than
the C preprocessor (cpp), while its syntax is lighter and more
flexible than that of GNU m4. There are built-in macros for use with
C/C++, LaTeX, HTML, XHTML, and Prolog files.

%prep
%setup -q -n gpp-%{version}

%build
%configure
make

%install
%make_install

%files
%{_bindir}/gpp
%license COPYING THANKS
%doc ChangeLog AUTHORS NEWS README THANKS
%doc %{_mandir}/man1/gpp.1.*
%exclude /usr/share/doc/gpp/gpp.1
%exclude /usr/share/doc/gpp/gpp.html
%exclude /usr/share/doc/gpp/gpp.pp

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.24-16
- Add Provides:gpp (#1669483)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.24-3
- Rename to general-purpose-preprocessor because of gnome printing panel

* Sat Oct 19 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.24-2
- Fedora-ifification.

* Fri Dec  3 2004 Tristan Miller <psychonaut@nothingisreal.com> - 2.24-1
- Initial build.
